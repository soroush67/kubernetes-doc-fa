---
reviewers:
  - liggitt
  - enj
title: مدیریت Service Accountها
content_type: concept
weight: 50
---

<!-- overview -->

یک _ServiceAccount_ هویتی برای فرایندهایی فراهم می‌کند که در یک Pod اجرا می‌شوند.

یک فرایند درون یک Pod می‌تواند از هویت service account مرتبط با خود برای احراز هویت در برابر API server کلاستر استفاده کند.

برای آشنایی مقدماتی با service accountها، [پیکربندی service accountها](/docs/tasks/configure-pod-container/configure-service-account/) را بخوانید.

این راهنمای کار برخی از مفاهیم پشت ServiceAccountها را توضیح می‌دهد. همچنین این راهنما شرح می‌دهد که چگونه توکن‌هایی را که نماینده ServiceAccountها هستند دریافت یا ابطال کنید، و چگونه (به‌صورت اختیاری) اعتبار یک ServiceAccount را به طول عمر یک آبجکت API وابسته کنید.

<!-- body -->

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

برای اینکه بتوانید این مراحل را دقیقاً دنبال کنید، مطمئن شوید که فضای نامی (namespace) با نام `examplens` دارید.
اگر ندارید، با اجرای دستور زیر آن را ایجاد کنید:

```shell
kubectl create namespace examplens
```

## حساب‌های کاربری در برابر service accountها

کوبرنتیز به چند دلیل میان مفهوم حساب کاربری (user account) و service account تمایز قائل می‌شود:

- حساب‌های کاربری برای انسان‌ها هستند. service accountها برای فرایندهای برنامه‌اند که (از دید کوبرنتیز) در کانتینرهایی اجرا می‌شوند که بخشی از podها هستند.
- حساب‌های کاربری قرار است سراسری باشند: نام‌ها باید در میان همه فضاهای نام (namespace) یک کلاستر یکتا باشند. فرقی نمی‌کند به کدام فضای نام نگاه کنید، یک نام کاربری مشخص که نماینده یک کاربر است، همواره همان کاربر را نشان می‌دهد.
  در کوبرنتیز، service accountها در سطح فضای نام تعریف می‌شوند: دو فضای نام متفاوت می‌توانند ServiceAccountهایی با نام‌های یکسان داشته باشند.
- معمولاً حساب‌های کاربری یک کلاستر ممکن است از یک پایگاه داده سازمانی همگام‌سازی شوند، جایی که ایجاد حساب کاربری جدید نیازمند سطح دسترسی ویژه است و به فرایندهای پیچیده کسب‌وکاری گره خورده است. در مقابل، ایجاد service account قرار است سبک‌تر باشد و به کاربران کلاستر اجازه دهد در صورت نیاز service accountهایی برای وظایف مشخص ایجاد کنند. جدا بودن ایجاد ServiceAccount از مراحل پذیرش کاربران انسانی، پیروی بارهای کاری از اصل حداقل دسترسی (principle of least privilege) را آسان‌تر می‌کند.
- ملاحظات ممیزی (auditing) برای انسان‌ها و service accountها ممکن است متفاوت باشد؛ این تفکیک دستیابی به آن را آسان‌تر می‌کند.
- یک بسته پیکربندی برای یک سامانه پیچیده ممکن است شامل تعریف service accountهای مختلف برای اجزای آن سامانه باشد. از آنجا که service accountها بدون محدودیت‌های زیاد قابل ایجاد هستند و نام‌هایشان در سطح فضای نام تعریف می‌شود، چنین پیکربندی‌ای معمولاً قابل جابه‌جایی (portable) است.

## توکن‌های service account مقید (Bound)

توکن‌های ServiceAccount را می‌توان به آبجکت‌های API که در kube-apiserver وجود دارند مقید کرد.
این کار می‌تواند برای وابسته کردن اعتبار یک توکن به وجود یک آبجکت API دیگر به کار رود.
انواع آبجکت پشتیبانی‌شده به شرح زیر است:

* Pod (برای mountهای حجم projected استفاده می‌شود؛ در ادامه ببینید)
* Secret (می‌تواند برای امکان ابطال یک توکن از طریق حذف Secret استفاده شود)
* Node (می‌تواند برای ابطال خودکار یک توکن هنگام حذف Node آن استفاده شود؛ ایجاد توکن‌های جدید مقید به node از نسخه v1.33 به بعد GA است)
* ValidatingWebhookConfiguration یا MutatingWebhookConfiguration (برای
  [احراز هویت در webhookهای admission](/docs/reference/access-authn-authz/extensible-admission-controllers/#authenticating-to-admission-webhooks)
  استفاده می‌شود؛ در نسخه v1.37 آلفا است و به
  [feature gate](/docs/reference/command-line-tools-reference/feature-gates/)
  با نام `APIServerWebhookAuthenticationToken` نیاز دارد)

هنگامی که یک توکن به یک آبجکت مقید می‌شود، مقادیر `metadata.name` و `metadata.uid` آن آبجکت به‌عنوان «claimهای خصوصی» (private claims) اضافی در JWT صادرشده ذخیره می‌شوند.

وقتی یک توکن مقید به kube-apiserver ارائه می‌شود، احراز‌کننده هویت service account این claimها را استخراج و بررسی می‌کند.
اگر آبجکت ارجاع‌شده یا ServiceAccount در انتظار حذف باشد (برای مثال به دلیل finalizerها)، آنگاه در هر لحظه‌ای که ۶۰ ثانیه (یا بیشتر) پس از زمان `.metadata.deletionTimestamp` باشد، احراز هویت با آن توکن شکست خواهد خورد.
اگر آبجکت ارجاع‌شده دیگر وجود نداشته باشد (یا `metadata.uid` آن مطابقت نداشته باشد)، درخواست احراز هویت نخواهد شد.

### فراداده اضافی در توکن‌های مقید به Pod

{{< feature-state feature_gate_name="ServiceAccountTokenPodNodeInfo" >}}

هنگامی که یک توکن service account به یک آبجکت Pod مقید می‌شود، فراداده اضافی نیز در توکن درج می‌شود که مقدار فیلد `spec.nodeName` از pod مقید‌شده و در صورت وجود، uid آن Node را نشان می‌دهد.

این اطلاعات node هنگام استفاده از توکن برای احراز هویت، توسط kube-apiserver **بررسی نمی‌شود**.
این اطلاعات درج می‌شود تا یکپارچه‌سازان هنگام بررسی یک JWT مجبور نباشند آبجکت‌های API مربوط به Pod یا Node را برای بررسی نام و uid مربوط به Node واکشی کنند.

### بررسی و وارسی claimهای خصوصی {#verifying-and-inspecting-private-claims}

از API با نام TokenReview می‌توان برای بررسی و استخراج claimهای خصوصی از یک توکن استفاده کرد:

1. ابتدا فرض کنید یک pod با نام `test-pod` و یک service account با نام `my-sa` دارید.
1. توکنی ایجاد کنید که به این Pod مقید باشد:

   ```shell
   kubectl create token my-sa --bound-object-kind="Pod" --bound-object-name="test-pod"
   ```

1. این توکن را در فایل جدیدی با نام `tokenreview.yaml` کپی کنید:

   ```yaml
   apiVersion: authentication.k8s.io/v1
   kind: TokenReview
   spec:
     token: <token from step 2>
   ```

1. این منبع را برای بررسی به apiserver ارسال کنید:

   ```shell
   # use '-o yaml' to inspect the output
   kubectl create -o yaml -f tokenreview.yaml
   ```

   باید خروجی‌ای مانند زیر ببینید:

   ```yaml
   apiVersion: authentication.k8s.io/v1
   kind: TokenReview
   metadata:
     creationTimestamp: null
   spec:
     token: <token>
   status:
     audiences:
     - https://kubernetes.default.svc.cluster.local
     authenticated: true
     user:
       extra:
         authentication.kubernetes.io/credential-id:
         - JTI=7ee52be0-9045-4653-aa5e-0da57b8dccdc
         authentication.kubernetes.io/node-name:
         - kind-control-plane
         authentication.kubernetes.io/node-uid:
         - 497e9d9a-47aa-4930-b0f6-9f2fb574c8c6
         authentication.kubernetes.io/pod-name:
         - test-pod
         authentication.kubernetes.io/pod-uid:
         - e87dbbd6-3d7e-45db-aafb-72b24627dff5
       groups:
       - system:serviceaccounts
       - system:serviceaccounts:default
       - system:authenticated
       uid: f8b4161b-2e2b-11e9-86b7-2afc33b31a7e
       username: system:serviceaccount:default:my-sa
   ```

   {{< note >}}
   با وجود استفاده از `kubectl create -f` برای ایجاد این منبع، و تعریف آن به شکلی مشابه سایر انواع منبع در کوبرنتیز، TokenReview یک نوع ویژه است و kube-apiserver در واقع آبجکت TokenReview را در etcd ذخیره نمی‌کند.
   بنابراین `kubectl get tokenreview` یک دستور معتبر نیست.
   {{< /note >}}

#### طرحواره (Schema) claimهای خصوصی service account

طرحواره claimهای مختص کوبرنتیز در توکن‌های JWT در حال حاضر مستند نشده است، اما بخش مربوط در کد را می‌توانید در
[بسته serviceaccount](https://github.com/kubernetes/kubernetes/blob/d8919343526597e0788a1efe133c70d9a0c07f69/pkg/serviceaccount/claims.go#L56-L68)
در کدبیس کوبرنتیز بیابید.

می‌توانید یک JWT را با ابزار استاندارد رمزگشایی JWT بررسی کنید. در ادامه نمونه‌ای از یک JWT برای ServiceAccount با نام `my-serviceaccount` آمده است که به یک آبجکت Pod با نام `my-pod` مقید شده است، این Pod روی Node با نام `my-node` زمان‌بندی شده و در فضای نام `my-namespace` قرار دارد:

```json
{
  "aud": [
    "https://my-audience.example.com"
  ],
  "exp": 1729605240,
  "iat": 1729601640,
  "iss": "https://my-cluster.example.com",
  "jti": "aed34954-b33a-4142-b1ec-389d6bbb4936",
  "kubernetes.io": {
    "namespace": "my-namespace",
    "node": {
      "name": "my-node",
      "uid": "646e7c5e-32d6-4d42-9dbd-e504e6cbe6b1"
    },
    "pod": {
      "name": "my-pod",
      "uid": "5e0bd49b-f040-43b0-99b7-22765a53f7f3"
    },
    "serviceaccount": {
      "name": "my-serviceaccount",
      "uid": "14ee3fa4-a7e2-420f-9f9a-dbc4507c3798"
    }
  },
  "nbf": 1729601640,
  "sub": "system:serviceaccount:my-namespace:my-serviceaccount"
}
```

{{< note >}}
فیلدهای `aud` و `iss` در این JWT ممکن است بسته به پیکربندی شما در کلاسترهای مختلف کوبرنتیز متفاوت باشند.

وجود هر دو claim با نام‌های `pod` و `node` نشان می‌دهد که این توکن به یک آبجکت *Pod* مقید شده است. هنگام بررسی توکن‌های ServiceAccount مقید به Pod، API server وجود آبجکت Node ارجاع‌شده را **بررسی نمی‌کند**.
{{< /note >}}

سرویس‌هایی که خارج از کوبرنتیز اجرا می‌شوند و می‌خواهند اعتبارسنجی آفلاین JWTها را انجام دهند، می‌توانند از این طرحواره، همراه با یک اعتبارسنج JWT سازگار که با اطلاعات OpenID Discovery از API server پیکربندی شده است، برای بررسی JWTهای ارائه‌شده بدون نیاز به استفاده از API با نام TokenReview بهره ببرند.

سرویس‌هایی که JWTها را به این روش بررسی می‌کنند، **بررسی نمی‌کنند** که claimهای درج‌شده در توکن JWT همچنان جاری و معتبر باشند.
این بدان معناست که اگر توکن به یک آبجکت مقید شده باشد و آن آبجکت دیگر وجود نداشته باشد، توکن همچنان معتبر در نظر گرفته می‌شود (تا زمانی که توکن بر اساس پیکربندی منقضی شود).

کلاینت‌هایی که به اطمینان از معتبر بودن claimهای مقید یک توکن نیاز دارند، **باید** از API با نام TokenReview استفاده کنند تا توکن را به `kube-apiserver` ارائه دهند و آن claimهای درج‌شده را بررسی و بسط دهد؛ مراحل این کار مشابه بخش [بررسی و وارسی claimهای خصوصی](#verifying-and-inspecting-private-claims) در بالا است، اما با یک [کتابخانه کلاینت پشتیبانی‌شده](/docs/reference/using-api/client-libraries/).
برای اطلاعات بیشتر درباره JWTها و ساختار آن‌ها، [RFC مربوط به JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) را ببینید.

## سازوکار حجم توکن service account مقید {#bound-service-account-token-volume}

{{< feature-state feature_gate_name="BoundServiceAccountTokenVolume" >}}

به‌طور پیش‌فرض، control plane کوبرنتیز (به‌طور مشخص
[admission controller مربوط به ServiceAccount](#serviceaccount-admission-controller))
یک [حجم projected](/docs/concepts/storage/projected-volumes/) به Podها اضافه می‌کند،
و این حجم شامل یک توکن برای دسترسی به API کوبرنتیز است.

در اینجا نمونه‌ای از شکل این بخش برای یک Pod راه‌اندازی‌شده آمده است:

```yaml
...
  - name: kube-api-access-<random-suffix>
    projected:
      sources:
        - serviceAccountToken:
            path: token # must match the path the app expects
        - configMap:
            items:
              - key: ca.crt
                path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
              - fieldRef:
                  apiVersion: v1
                  fieldPath: metadata.namespace
                path: namespace
```

این قطعه مانیفست یک حجم projected تعریف می‌کند که از سه منبع (source) تشکیل شده است. در این مورد، هر منبع نمایانگر یک مسیر واحد درون آن حجم نیز هست. سه منبع عبارت‌اند از:

1. یک منبع `serviceAccountToken` که شامل توکنی است که kubelet از kube-apiserver دریافت می‌کند.
   kubelet توکن‌های دارای محدودیت زمانی را با استفاده از API با نام TokenRequest واکشی می‌کند. توکنی که برای یک TokenRequest صادر می‌شود، یا هنگام حذف pod منقضی می‌شود یا پس از یک مدت زمان تعریف‌شده (به‌طور پیش‌فرض ۱ ساعت).
   kubelet همچنین این توکن را پیش از انقضای آن تازه‌سازی می‌کند.
   این توکن به Pod مشخص مقید است و kube-apiserver مخاطب (audience) آن است.
   این سازوکار جایگزین سازوکار قدیمی‌تری شد که حجمی مبتنی بر Secret اضافه می‌کرد، که در آن Secret نمایانگر ServiceAccount مربوط به Pod بود، اما منقضی نمی‌شد.
1. یک منبع `configMap`. این ConfigMap شامل مجموعه‌ای از داده‌های مرجع صدور گواهی (certificate authority) است. Podها می‌توانند از این گواهی‌ها استفاده کنند تا مطمئن شوند به kube-apiserver کلاستر شما متصل می‌شوند (و نه به یک middlebox یا یک طرف مقابل که به‌طور تصادفی نادرست پیکربندی شده است).
1. یک منبع `downwardAPI` که نام فضای نامی را که Pod در آن قرار دارد جست‌وجو می‌کند و این اطلاعات نام را در دسترس کد برنامه‌ای که درون Pod اجرا می‌شود قرار می‌دهد.

هر کانتینر درون Pod که این حجم مشخص را mount کند، می‌تواند به اطلاعات بالا دسترسی داشته باشد.

{{< note >}}
سازوکار خاصی برای باطل کردن توکنی که از طریق TokenRequest صادر شده است وجود ندارد. اگر دیگر به یک توکن service account مقید برای یک Pod اعتماد ندارید، می‌توانید آن Pod را حذف کنید. حذف یک Pod باعث انقضای توکن‌های service account مقید آن می‌شود.
{{< /note >}}

## مدیریت دستی Secret برای ServiceAccountها

نسخه‌های کوبرنتیز پیش از v1.22 به‌طور خودکار اعتبارنامه‌هایی برای دسترسی به API کوبرنتیز ایجاد می‌کردند. این سازوکار قدیمی‌تر مبتنی بر ایجاد Secretهای توکن بود که سپس می‌توانستند در Podهای در حال اجرا mount شوند.

در نسخه‌های جدیدتر، از جمله کوبرنتیز v{{< skew currentVersion >}}، اعتبارنامه‌های API با استفاده از API با نام
[TokenRequest](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
[مستقیماً دریافت](#bound-service-account-token-volume) می‌شوند
و با استفاده از یک حجم projected در Podها mount می‌شوند.
توکن‌هایی که با این روش دریافت می‌شوند طول عمر محدود دارند و هنگامی که Podای که در آن mount شده‌اند حذف شود، به‌طور خودکار باطل می‌شوند.

همچنان می‌توانید یک Secret را برای نگهداری توکن service account
[به‌صورت دستی ایجاد کنید](/docs/tasks/configure-pod-container/configure-service-account/#manually-create-an-api-token-for-a-serviceaccount)؛ برای مثال، اگر به توکنی نیاز دارید که هرگز منقضی نشود.

پس از اینکه یک Secret را به‌صورت دستی ایجاد کنید و آن را به یک ServiceAccount پیوند دهید،
control plane کوبرنتیز به‌طور خودکار توکن را در آن Secret درج می‌کند.

{{< note >}}
اگرچه سازوکار دستی برای ایجاد توکن ServiceAccount با عمر طولانی وجود دارد،
توصیه می‌شود به‌جای آن از [TokenRequest](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
برای دریافت توکن‌های دسترسی API با عمر کوتاه استفاده کنید.
{{< /note >}}

## پاک‌سازی توکن‌های قدیمی ServiceAccount که به‌طور خودکار تولید شده‌اند {#auto-generated-legacy-serviceaccount-token-clean-up}

پیش از نسخه 1.24، کوبرنتیز به‌طور خودکار توکن‌های مبتنی بر Secret را برای ServiceAccountها تولید می‌کرد. برای تمایز میان توکن‌هایی که به‌طور خودکار تولید شده‌اند و توکن‌هایی که به‌صورت دستی ایجاد شده‌اند، کوبرنتیز وجود یک ارجاع را از فیلد secrets مربوط به ServiceAccount بررسی می‌کند. اگر Secret در فیلد `secrets` ارجاع داده شده باشد، یک توکن قدیمی تولیدشده‌ی خودکار در نظر گرفته می‌شود. در غیر این صورت، یک توکن قدیمی ایجادشده به‌صورت دستی در نظر گرفته می‌شود. برای مثال:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: build-robot
  namespace: default
secrets:
  - name: build-robot-secret # usually NOT present for a manually generated token
```

از نسخه 1.29 به بعد، توکن‌های قدیمی ServiceAccount که به‌طور خودکار تولید شده‌اند، در صورتی که برای یک مدت زمان مشخص (به‌طور پیش‌فرض یک سال) استفاده نشوند، نامعتبر علامت‌گذاری می‌شوند. توکن‌هایی که برای این مدت تعریف‌شده (باز هم به‌طور پیش‌فرض، یک سال) همچنان استفاده نشده باقی بمانند، پس از آن توسط control plane پاک‌سازی (purge) خواهند شد.

اگر کاربران از یک توکن خودکار نامعتبرشده استفاده کنند، اعتبارسنج توکن

1. یک حاشیه‌نویسی (annotation) ممیزی برای جفت کلید-مقدار
   `authentication.k8s.io/legacy-token-invalidated: <secret name>/<namespace>` اضافه می‌کند،
1. شمارنده متریک `invalid_legacy_auto_token_uses_total` را افزایش می‌دهد،
1. برچسب `kubernetes.io/legacy-token-last-used` در Secret را با تاریخ جدید به‌روزرسانی می‌کند،
1. خطایی بازمی‌گرداند که نشان می‌دهد توکن نامعتبر شده است.

هنگام دریافت این خطای اعتبارسنجی، کاربران می‌توانند Secret را به‌روزرسانی کنند و برچسب `kubernetes.io/legacy-token-invalid-since` را حذف کنند تا استفاده از این توکن به‌طور موقت مجاز شود.

در اینجا نمونه‌ای از یک توکن قدیمی تولیدشده‌ی خودکار آمده است که با برچسب‌های `kubernetes.io/legacy-token-last-used` و `kubernetes.io/legacy-token-invalid-since` علامت‌گذاری شده است:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: build-robot-secret
  namespace: default
  labels:
    kubernetes.io/legacy-token-last-used: 2022-10-24
    kubernetes.io/legacy-token-invalid-since: 2023-10-25
  annotations:
    kubernetes.io/service-account.name: build-robot
type: kubernetes.io/service-account-token
```

## جزئیات control plane

### کنترل‌کننده ServiceAccount

یک کنترل‌کننده ServiceAccount، ServiceAccountها را درون فضاهای نام مدیریت می‌کند و اطمینان حاصل می‌کند که یک ServiceAccount با نام «default» در هر فضای نام فعال وجود دارد.

### کنترل‌کننده توکن

کنترل‌کننده توکن service account به‌عنوان بخشی از `kube-controller-manager` اجرا می‌شود.
این کنترل‌کننده به‌صورت ناهمگام (asynchronous) عمل می‌کند. این کنترل‌کننده:

- حذف ServiceAccount را زیر نظر می‌گیرد و همه Secretهای توکن ServiceAccount متناظر را حذف می‌کند.
- افزودن Secret توکن ServiceAccount را زیر نظر می‌گیرد، اطمینان حاصل می‌کند که ServiceAccount ارجاع‌شده وجود دارد و در صورت نیاز یک توکن به Secret اضافه می‌کند.
- حذف Secret را زیر نظر می‌گیرد و در صورت نیاز ارجاع را از ServiceAccount متناظر حذف می‌کند.

شما باید یک فایل کلید خصوصی service account را با استفاده از پرچم `--service-account-private-key-file` در `kube-controller-manager` به کنترل‌کننده توکن بدهید. از کلید خصوصی برای امضای توکن‌های service account تولیدشده استفاده می‌شود.
به‌طور مشابه، باید کلید عمومی متناظر را با استفاده از پرچم `--service-account-key-file` به `kube-apiserver` بدهید. از کلید عمومی برای بررسی توکن‌ها در حین احراز هویت استفاده خواهد شد.

{{< feature-state feature_gate_name="ExternalServiceAccountTokenSigner" >}}

یک راه‌اندازی جایگزین برای تنظیم پرچم‌های `--service-account-private-key-file` و `--service-account-key-file` این است که یک امضاکننده JWT خارجی برای [امضای توکن ServiceAccount و مدیریت کلید به‌صورت خارجی](#external-serviceaccount-token-signing-and-key-management) پیکربندی شود.
توجه داشته باشید که این دو راه‌اندازی متقابلاً ناسازگارند و نمی‌توان آن‌ها را با هم پیکربندی کرد.

### کنترل‌کننده پذیرش ServiceAccount

تغییر Podها از طریق افزونه‌ای به نام [کنترل‌کننده پذیرش (Admission Controller)](/docs/reference/access-authn-authz/admission-controllers/) پیاده‌سازی شده است.
این افزونه بخشی از API server است.
این کنترل‌کننده پذیرش به‌صورت همگام (synchronous) عمل می‌کند و Podها را هنگام ایجاد شدن تغییر می‌دهد.
زمانی که این افزونه فعال باشد (و در بیشتر توزیع‌ها به‌طور پیش‌فرض فعال است)، هنگام ایجاد یک Pod کارهای زیر را انجام می‌دهد:

1. اگر برای Pod مقدار `.spec.serviceAccountName` تنظیم نشده باشد، کنترل‌کننده پذیرش نام ServiceAccount این Pod ورودی را برابر `default` قرار می‌دهد.
1. کنترل‌کننده پذیرش اطمینان حاصل می‌کند که ServiceAccount ارجاع‌شده توسط Pod ورودی وجود دارد. اگر ServiceAccount‌ای با نام مطابق وجود نداشته باشد، کنترل‌کننده پذیرش Pod ورودی را رد می‌کند. این بررسی حتی برای ServiceAccount با نام `default` نیز اعمال می‌شود.
1. به شرطی که نه فیلد `automountServiceAccountToken` در ServiceAccount و نه فیلد `automountServiceAccountToken` در Pod روی `false` تنظیم شده باشد:
   - کنترل‌کننده پذیرش، Pod ورودی را تغییر می‌دهد و یک {{< glossary_tooltip text="حجم (volume)" term_id="volume" >}} اضافی که حاوی توکن دسترسی به API است به آن اضافه می‌کند.
   - کنترل‌کننده پذیرش یک `volumeMount` به هر کانتینر در Pod اضافه می‌کند و کانتینرهایی را که از قبل برای مسیر `/var/run/secrets/kubernetes.io/serviceaccount` یک volume mount تعریف‌شده دارند، نادیده می‌گیرد.
     برای کانتینرهای لینوکسی، این حجم در مسیر `/var/run/secrets/kubernetes.io/serviceaccount` مانت می‌شود؛
     در نودهای ویندوزی، مانت در مسیر معادل آن انجام می‌شود.
1. اگر مشخصات (spec) Pod ورودی از قبل شامل هیچ `imagePullSecrets` نباشد، کنترل‌کننده پذیرش مقادیر `imagePullSecrets` را از `ServiceAccount` کپی کرده و به آن اضافه می‌کند.

### کنترل‌کننده ردیابی توکن‌های قدیمی ServiceAccount

{{< feature-state feature_gate_name="LegacyServiceAccountTokenTracking" >}}

این کنترل‌کننده یک ConfigMap با نام
`kube-system/kube-apiserver-legacy-service-account-token-tracking` در فضای نام
`kube-system` ایجاد می‌کند. این ConfigMap زمانی را ثبت می‌کند که سیستم شروع به پایش توکن‌های قدیمی
service account کرده است.

### پاک‌کننده توکن‌های قدیمی ServiceAccount

{{< feature-state feature_gate_name="LegacyServiceAccountTokenCleanUp" >}}

پاک‌کننده توکن‌های قدیمی ServiceAccount به‌عنوان بخشی از
`kube-controller-manager` اجرا می‌شود و هر ۲۴ ساعت بررسی می‌کند که آیا توکن قدیمی ServiceAccount که به‌صورت خودکار ایجاد شده است، در یک *بازه زمانی مشخص* استفاده نشده است یا خیر.
در صورت استفاده‌نشدن، پاک‌کننده آن توکن‌ها را نامعتبر علامت‌گذاری می‌کند.

پاک‌کننده ابتدا ConfigMap ایجادشده توسط control plane را بررسی می‌کند
(مشروط بر اینکه `LegacyServiceAccountTokenTracking` فعال باشد). اگر زمان فعلی به اندازه یک *بازه زمانی مشخص* پس از تاریخ ثبت‌شده در ConfigMap باشد،
پاک‌کننده سپس فهرست Secretهای کلاستر را پیمایش می‌کند و هر Secret با نوع `kubernetes.io/service-account-token` را ارزیابی می‌کند.

اگر یک Secret همه شرایط زیر را داشته باشد، پاک‌کننده آن را نامعتبر علامت‌گذاری می‌کند:

- Secret به‌صورت خودکار ایجاد شده باشد، یعنی به‌صورت دوطرفه توسط یک ServiceAccount ارجاع داده شده باشد.
- Secret در حال حاضر توسط هیچ Podی مانت نشده باشد.
- Secret از زمان ایجاد یا از آخرین استفاده، در یک *بازه زمانی مشخص* استفاده نشده باشد.

پاک‌کننده یک Secret را با افزودن برچسبی به نام
`kubernetes.io/legacy-token-invalid-since` به آن، با تاریخ جاری به‌عنوان مقدار، نامعتبر علامت‌گذاری می‌کند. اگر یک Secret نامعتبر در یک *بازه زمانی مشخص* استفاده نشود،
پاک‌کننده آن را حذف می‌کند.

{{< note >}}
همه *بازه‌های زمانی مشخص* بالا به‌طور پیش‌فرض برابر یک سال هستند. مدیر کلاستر می‌تواند این مقدار را از طریق آرگومان خط فرمان
`--legacy-service-account-token-clean-up-period` برای مؤلفه
`kube-controller-manager` پیکربندی کند.
{{< /note >}}

### TokenRequest API

{{< feature-state for_k8s_version="v1.22" state="stable" >}}

شما از زیرمنبع (subresource) [TokenRequest](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
مربوط به یک ServiceAccount برای دریافت توکن زمان‌دار برای آن ServiceAccount استفاده می‌کنید.
برای دریافت توکن API جهت استفاده درون یک کانتینر نیازی به فراخوانی این مورد ندارید، زیرا
kubelet این کار را با استفاده از یک _projected volume_ برای شما انجام می‌دهد.

اگر می‌خواهید از TokenRequest API در `kubectl` استفاده کنید، به
[ایجاد دستی توکن API برای یک ServiceAccount](/docs/tasks/configure-pod-container/configure-service-account/#manually-create-an-api-token-for-a-serviceaccount) مراجعه کنید.

control plane در کوبرنتیز (به‌طور مشخص، کنترل‌کننده پذیرش ServiceAccount)
یک projected volume به Podها اضافه می‌کند و kubelet اطمینان حاصل می‌کند که این حجم حاوی توکنی است
که به کانتینرها اجازه می‌دهد به‌عنوان ServiceAccount صحیح احراز هویت شوند.

(این سازوکار جایگزین سازوکار قبلی شده است که حجمی مبتنی بر Secret اضافه می‌کرد،
که در آن Secret نماینده ServiceAccount برای Pod بود اما منقضی نمی‌شد.)

در اینجا نمونه‌ای از ظاهر آن برای یک Pod اجراشده آمده است:

```yaml
...
  - name: kube-api-access-<random-suffix>
    projected:
      defaultMode: 420 # decimal equivalent of octal 0644
      sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
              - key: ca.crt
                path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
              - fieldRef:
                  apiVersion: v1
                  fieldPath: metadata.namespace
                path: namespace
```

این قطعه مانیفست یک projected volume تعریف می‌کند که اطلاعات سه منبع را ترکیب می‌کند:

1. یک منبع `serviceAccountToken` که حاوی توکنی است که kubelet از kube-apiserver دریافت می‌کند.
   kubelet توکن‌های زمان‌دار را با استفاده از TokenRequest API دریافت می‌کند. توکنی که برای یک TokenRequest صادر می‌شود، یا هنگام حذف Pod یا پس از یک مدت عمر مشخص (به‌طور پیش‌فرض ۱ ساعت) منقضی می‌شود.
   این توکن به Pod مشخصی متصل (bound) است و مخاطب (audience) آن kube-apiserver است.
1. یک منبع `configMap`. این ConfigMap حاوی مجموعه‌ای از داده‌های مرجع گواهی (certificate authority) است. Podها می‌توانند از این گواهی‌ها استفاده کنند تا مطمئن شوند به kube-apiserver کلاستر شما متصل می‌شوند (و نه به یک middlebox یا یک همتای اشتباه پیکربندی‌شده).
1. یک منبع `downwardAPI`. این حجم `downwardAPI` نام فضای نامی را که Pod در آن قرار دارد، در اختیار کد برنامه‌ای که درون Pod اجرا می‌شود قرار می‌دهد.

هر کانتینر درون Pod که این حجم را مانت کند می‌تواند به اطلاعات بالا دسترسی داشته باشد.

## ایجاد توکن‌های API اضافی {#create-token}

{{< caution >}}
فقط در صورتی توکن‌های API بلندمدت ایجاد کنید که سازوکار [token request](#tokenrequest-api)
مناسب نباشد. سازوکار token request توکن‌های با محدودیت زمانی ارائه می‌دهد؛ از آنجا که این توکن‌ها
منقضی می‌شوند، ریسک کمتری برای امنیت اطلاعات دارند.
{{< /caution >}}

برای ایجاد یک توکن API پایدار و بدون انقضا برای یک ServiceAccount، یک
Secret از نوع `kubernetes.io/service-account-token` با یک حاشیه‌نویسی (annotation)
که به ServiceAccount ارجاع می‌دهد ایجاد کنید. سپس control plane یک توکن بلندمدت تولید می‌کند و
آن Secret را با داده‌های توکن تولیدشده به‌روزرسانی می‌کند.

در اینجا یک مانیفست نمونه برای چنین Secret ای آمده است:

{{% code_sample file="secret/serviceaccount/mysecretname.yaml" %}}

برای ایجاد یک Secret بر اساس این مثال، دستور زیر را اجرا کنید:

```shell
kubectl -n examplens create -f https://k8s.io/examples/secret/serviceaccount/mysecretname.yaml
```

برای مشاهده جزئیات آن Secret، دستور زیر را اجرا کنید:

```shell
kubectl -n examplens describe secret mysecretname
```

خروجی مشابه زیر است:

```
Name:           mysecretname
Namespace:      examplens
Labels:         <none>
Annotations:    kubernetes.io/service-account.name=myserviceaccount
                kubernetes.io/service-account.uid=8a85c4c4-8483-11e9-bc42-526af7764f64

Type:   kubernetes.io/service-account-token

Data
====
ca.crt:         1362 bytes
namespace:      9 bytes
token:          ...
```

اگر یک Pod جدید را در فضای نام `examplens` اجرا کنید، می‌تواند از Secret با نوع service-account-token به نام `myserviceaccount` که هم‌اکنون ایجاد کرده‌اید استفاده کند.

{{< caution >}}
Secretهایی را که به‌صورت دستی ایجاد شده‌اند در فیلد `secrets` یک
ServiceAccount ارجاع ندهید. در غیر این صورت، Secretهای ایجادشده به‌صورت دستی در صورت عدم استفاده برای مدت طولانی پاک خواهند شد.
لطفاً به [پاک‌سازی توکن‌های قدیمی ServiceAccount که به‌صورت خودکار ایجاد شده‌اند](#auto-generated-legacy-serviceaccount-token-clean-up) مراجعه کنید.
{{< /caution >}}

## حذف/نامعتبرسازی یک توکن ServiceAccount {#delete-token}

### حذف/نامعتبرسازی یک توکن ServiceAccount بلندمدت/قدیمی {#delete-legacy-token}

اگر نام Secret حاوی توکنی را که می‌خواهید حذف کنید می‌دانید:

```shell
kubectl delete secret name-of-secret
```

در غیر این صورت، ابتدا Secret مربوط به ServiceAccount را پیدا کنید.

```shell
# This assumes that you already have a namespace named 'examplens'
kubectl -n examplens get serviceaccount/example-automated-thing -o yaml
```

خروجی مشابه زیر است:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","kind":"ServiceAccount","metadata":{"annotations":{},"name":"example-automated-thing","namespace":"examplens"}}
  creationTimestamp: "2019-07-21T07:07:07Z"
  name: example-automated-thing
  namespace: examplens
  resourceVersion: "777"
  selfLink: /api/v1/namespaces/examplens/serviceaccounts/example-automated-thing
  uid: f23fd170-66f2-4697-b049-e1e266b7f835
secrets:
  - name: example-automated-thing-token-zyxwv
```

سپس Secret را که اکنون نام آن را می‌دانید حذف کنید:

```shell
kubectl -n examplens delete secret/example-automated-thing-token-zyxwv
```

### حذف/نامعتبرسازی یک توکن ServiceAccount کوتاه‌مدت {#delete-short-lived}

توکن‌های کوتاه‌مدت ServiceAccount پس از گذشت مدت زمانی که هنگام ایجاد آن‌ها مشخص شده است به‌طور خودکار منقضی می‌شوند. هیچ سابقه مرکزی از توکن‌های صادرشده وجود ندارد،
بنابراین راهی برای ابطال توکن‌های جداگانه وجود ندارد.

اگر مجبورید یک توکن کوتاه‌مدت را پیش از انقضای آن ابطال کنید، می‌توانید ServiceAccount مرتبط با آن را حذف و دوباره ایجاد کنید. این کار
UID آن را تغییر می‌دهد و در نتیجه **همه** توکن‌های ServiceAccount را که برای آن ایجاد شده بودند نامعتبر می‌کند.

## امضای توکن ServiceAccount و مدیریت کلید به‌صورت خارجی

{{< feature-state feature_gate_name="ExternalServiceAccountTokenSigner" >}}

kube-apiserver را می‌توان طوری پیکربندی کرد که از یک امضاکننده خارجی برای امضای توکن و مدیریت کلیدهای تأیید توکن استفاده کند.
این قابلیت به توزیع‌های کوبرنتیز امکان می‌دهد برای امضا و تأیید اعتبارنامه‌های service account با راهکارهای مدیریت کلید مورد نظر خود
(برای مثال HSMها و KMSهای ابری) یکپارچه شوند.
برای پیکربندی kube-apiserver جهت استفاده از external-jwt-signer، فلگ `--service-account-signing-endpoint` را
روی مکان یک Unix domain socket (UDS) در یک فایل‌سیستم تنظیم کنید، یا آن را با نماد @ شروع کنید و نام
یک UDS در فضای نام socket انتزاعی (abstract) را بیاورید. در UDS پیکربندی‌شده باید یک سرور RPC وجود داشته باشد که
سرویس gRPC با نام `ExternalJWTSigner` را پیاده‌سازی می‌کند.

برای راه‌اندازی kube-apiserver، external-jwt-signer باید سالم باشد و آماده ارائه کلیدهای پشتیبانی‌شده service account باشد.

{{< note >}}
فلگ‌های kube-apiserver یعنی `--service-account-key-file` و `--service-account-signing-key-file` همچنان
برای خواندن از فایل‌ها استفاده خواهند شد، مگر اینکه `--service-account-signing-endpoint` تنظیم شده باشد؛ این‌ها
روش‌های متقابلاً ناسازگار (mutually exclusive) برای پشتیبانی از امضای JWT و احراز هویت هستند.
{{< /note >}}

یک امضاکننده خارجی سرویس gRPC با نام `v1.ExternalJWTSigner` را ارائه می‌دهد که ۳ متد را پیاده‌سازی می‌کند:

### Metadata

Metadata قرار است هنگام راه‌اندازی یک بار توسط `kube-apiserver` فراخوانی شود.
این متد به امضاکننده خارجی امکان می‌دهد فراداده‌ها را با kube-apiserver به اشتراک بگذارد، مانند حداکثر عمر توکنی که امضاکننده پشتیبانی می‌کند.

```proto
rpc Metadata(MetadataRequest) returns (MetadataResponse) {}

message MetadataRequest {}

message MetadataResponse {
  // used by kube-apiserver for defaulting/validation of JWT lifetime while accounting for configuration flag values:
  // 1. `--service-account-max-token-expiration`
  // 2. `--service-account-extend-token-expiration`
  //
  // * If `--service-account-max-token-expiration` is greater than `max_token_expiration_seconds`, kube-apiserver treats that as misconfiguration and exits.
  // * If `--service-account-max-token-expiration` is not explicitly set, kube-apiserver defaults to `max_token_expiration_seconds`.
  // * If `--service-account-extend-token-expiration` is true, the extended expiration is `min(1 year, max_token_expiration_seconds)`.
  //
  // `max_token_expiration_seconds` must be at least 600s.
  int64 max_token_expiration_seconds = 1;
}
```

### FetchKeys

FetchKeys مجموعه کلیدهای عمومی را برمی‌گرداند که برای امضای
توکن‌های service account در کوبرنتیز مورد اعتماد هستند. Kube-apiserver این RPC را در موارد زیر فراخوانی می‌کند:
* هر بار که تلاش می‌کند یک JWT از صادرکننده service account را با شناسه کلید ناشناخته اعتبارسنجی کند، و
* به‌صورت دوره‌ای، تا بتواند کلیدهای نسبتاً به‌روز را از نقطه پایانی OIDC JWKs ارائه دهد.

```proto
rpc FetchKeys(FetchKeysRequest) returns (FetchKeysResponse) {}

message FetchKeysRequest {}

message FetchKeysResponse {
  repeated Key keys = 1;

  // The timestamp when this data was pulled from the authoritative source of
  // truth for verification keys.
  // kube-apiserver can export this from metrics, to enable end-to-end SLOs.
  google.protobuf.Timestamp data_timestamp = 2;

  // refresh interval for verification keys to pick changes if any.
  // any value <= 0 is considered a misconfiguration.
  int64 refresh_hint_seconds = 3;
}

message Key {
  // A unique identifier for this key.
  // Length must be <=1024.
  string key_id = 1;

  // The public key, PKIX-serialized.
  // must be a public key supported by kube-apiserver (currently RSA 256 or ECDSA 256/384/521)
  bytes key = 2;

  // Set only for keys that are not used to sign bound tokens.
  // eg: supported keys for legacy tokens.
  // If set, key is used for verification but excluded from OIDC discovery docs.
  // if set, external signer should not use this key to sign a JWT.
  bool exclude_from_oidc_discovery = 3;
}
```

### Sign

Sign یک payload سریال‌شده JWT را دریافت می‌کند و هدر و امضای سریال‌شده را برمی‌گرداند.
سپس `kube-apiserver` JWT را از روی هدر، payload و امضا مونتاژ می‌کند.

```proto
rpc Sign(SignJWTRequest) returns (SignJWTResponse) {}

message SignJWTRequest {
  // URL-safe base64 wrapped payload to be signed.
  // Exactly as it appears in the second segment of the JWT
  string claims = 1;
}

message SignJWTResponse {
  // header must contain only alg, kid, typ claims.
  // typ must be “JWT”.
  // kid must be non-empty, <=1024 characters, and its corresponding public key should not be excluded from OIDC discovery.
  // alg must be one of the algorithms supported by kube-apiserver (currently RS256, ES256, ES384, ES512).
  // header cannot have any additional data that kube-apiserver does not recognize.
  // Already wrapped in URL-safe base64, exactly as it appears in the first segment of the JWT.
  string header = 1;

  // The signature for the JWT.
  // Already wrapped in URL-safe base64, exactly as it appears in the final segment of the JWT.
  string signature = 2;
}
```

## پاک‌سازی

اگر برای آزمایش یک فضای نام `examplens` ایجاد کرده‌اید، می‌توانید آن را حذف کنید:

```shell
kubectl delete namespace examplens
```

## {{% heading "whatsnext" %}}

- درباره [projected volumeها](/docs/concepts/storage/projected-volumes/) بیشتر بخوانید.
