---
reviewers:
  - liggitt
  - enj
title: مدیریت حساب‌های سرویس
content_type: concept
weight: 50
---

<!-- overview -->

هر _ServiceAccount_ هویتی برای فرایندهایی فراهم می‌کند که در یک Pod اجرا می‌شوند.

فرایندی که درون یک Pod اجرا می‌شود می‌تواند با استفاده از هویت حساب سرویس (service account) مرتبط با خود، در برابر API server کلاستر احراز هویت کند.

برای آشنایی مقدماتی با حساب‌های سرویس، مطلب [پیکربندی حساب‌های سرویس](/docs/tasks/configure-pod-container/configure-service-account/) را بخوانید.

این راهنما برخی از مفاهیم پشت ServiceAccountها را توضیح می‌دهد. همچنین در این راهنما توضیح داده می‌شود که چگونه می‌توان توکن‌هایی را که نماینده‌ی ServiceAccountها هستند دریافت یا باطل کرد، و چگونه می‌توان (به‌صورت اختیاری) اعتبار یک ServiceAccount را به طول عمر یک آبجکت API گره زد.

<!-- body -->

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

برای اینکه بتوانید این مراحل را دقیقاً دنبال کنید، مطمئن شوید که یک فضای نام (namespace) با نام `examplens` دارید. اگر چنین فضای نامی ندارید، با اجرای دستور زیر آن را ایجاد کنید:

```shell
kubectl create namespace examplens
```

## حساب‌های کاربری در مقابل حساب‌های سرویس

کوبرنتیز به چند دلیل میان مفهوم حساب کاربری و حساب سرویس تمایز قائل می‌شود:

- حساب‌های کاربری برای انسان‌ها هستند. حساب‌های سرویس برای فرایندهای برنامه‌ها هستند که (در کوبرنتیز) درون کانتینرهایی اجرا می‌شوند که بخشی از Podها هستند.
- حساب‌های کاربری قرار است سراسری باشند: نام‌ها باید در همه‌ی فضاهای نام یک کلاستر یکتا باشند. فارغ از اینکه به کدام فضای نام نگاه کنید، یک نام کاربری مشخص همواره نماینده‌ی همان کاربر است. در کوبرنتیز، حساب‌های سرویس به فضای نام وابسته‌اند: دو فضای نام متفاوت می‌توانند ServiceAccountهایی با نام‌های یکسان داشته باشند.
- معمولاً حساب‌های کاربری یک کلاستر ممکن است از یک پایگاه داده‌ی سازمانی همگام‌سازی شوند؛ در چنین پایگاهی، ایجاد حساب کاربری جدید به امتیازهای ویژه نیاز دارد و به فرایندهای پیچیده‌ی کسب‌وکار گره خورده است. در مقابل، ایجاد حساب سرویس قرار است سبک‌تر باشد تا کاربران کلاستر بتوانند در صورت نیاز، برای وظایف مشخص حساب سرویس بسازند. جدا کردن ایجاد ServiceAccount از مراحل پذیرش کاربران انسانی، پیروی بارهای کاری از اصل کمترین امتیاز (least privilege) را آسان‌تر می‌کند.
- ملاحظات ممیزی (auditing) برای انسان‌ها و حساب‌های سرویس ممکن است متفاوت باشد؛ این جداسازی دستیابی به آن را آسان‌تر می‌کند.
- بسته‌ی پیکربندی یک سامانه‌ی پیچیده ممکن است شامل تعریف حساب‌های سرویس گوناگون برای مؤلفه‌های آن سامانه باشد. از آنجا که حساب‌های سرویس را می‌توان بدون محدودیت‌های زیاد ایجاد کرد و نام آن‌ها به فضای نام وابسته است، چنین پیکربندی‌ای معمولاً قابل‌حمل است.

## توکن‌های حساب سرویس مقید

توکن‌های ServiceAccount را می‌توان به آبجکت‌های APIای مقید کرد که در kube-apiserver وجود دارند. با این کار می‌توان اعتبار یک توکن را به وجود یک آبجکت API دیگر گره زد. انواع آبجکت‌های پشتیبانی‌شده عبارت‌اند از:

* Pod (برای اتصال حجم‌های (volume) projected استفاده می‌شود؛ پایین‌تر را ببینید)
* Secret (می‌توان از آن برای امکان باطل کردن توکن با حذف Secret استفاده کرد)
* Node (می‌توان از آن برای باطل شدن خودکار توکن هنگام حذف Node آن استفاده کرد؛ ایجاد توکن‌های جدید مقید به نود از نسخه‌ی v1.33 به بعد در وضعیت GA است)
* ValidatingWebhookConfiguration یا MutatingWebhookConfiguration (برای [احراز هویت در برابر admission webhookها](/docs/reference/access-authn-authz/extensible-admission-controllers/#authenticating-to-admission-webhooks) استفاده می‌شود؛ در نسخه‌ی v1.37 آلفا است و به [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `APIServerWebhookAuthenticationToken` نیاز دارد)

وقتی یک توکن به یک آبجکت مقید می‌شود، مقادیر `metadata.name` و `metadata.uid` آن آبجکت به‌عنوان «ادعاهای خصوصی» (private claims) اضافی در JWT صادرشده ذخیره می‌شوند.

وقتی یک توکن مقید به kube-apiserver ارائه می‌شود، احرازکننده‌ی هویت حساب سرویس این ادعاها را استخراج و راستی‌آزمایی می‌کند. اگر آبجکت ارجاع‌شده یا ServiceAccount در انتظار حذف باشد (برای مثال به دلیل finalizerها)، احراز هویت با آن توکن در هر لحظه‌ای که ۶۰ ثانیه (یا بیشتر) پس از تاریخ `.metadata.deletionTimestamp` باشد، ناموفق خواهد بود. اگر آبجکت ارجاع‌شده دیگر وجود نداشته باشد (یا `metadata.uid` آن مطابقت نداشته باشد)، درخواست احراز هویت نخواهد شد.

### فراداده‌ی اضافی در توکن‌های مقید به Pod

{{< feature-state feature_gate_name="ServiceAccountTokenPodNodeInfo" >}}

وقتی یک توکن حساب سرویس به یک آبجکت Pod مقید می‌شود، فراداده‌ی اضافی‌ای نیز درون توکن جای داده می‌شود که مقدار فیلد `spec.nodeName` پاد مقیدشده و در صورت وجود، uid آن Node را نشان می‌دهد.

این اطلاعات نود هنگام استفاده از توکن برای احراز هویت، از سوی kube-apiserver راستی‌آزمایی **نمی‌شود**. این اطلاعات گنجانده می‌شود تا یکپارچه‌سازان هنگام بررسی یک JWT، برای اطلاع از نام و uid نود مرتبط مجبور به دریافت آبجکت‌های API از نوع Pod یا Node نباشند.

### راستی‌آزمایی و بررسی ادعاهای خصوصی

با استفاده از TokenReview API می‌توان ادعاهای خصوصی یک توکن را راستی‌آزمایی و استخراج کرد:

1. ابتدا فرض کنید یک پاد با نام `test-pod` و یک حساب سرویس با نام `my-sa` دارید.
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

1. این منبع را برای بازبینی به apiserver ارسال کنید:

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
   با اینکه برای ایجاد این منبع از `kubectl create -f` استفاده می‌شود و تعریف آن شبیه سایر انواع منابع در کوبرنتیز است، TokenReview نوع ویژه‌ای است و kube-apiserver در واقع آبجکت TokenReview را در etcd ذخیره نمی‌کند. از این رو، `kubectl get tokenreview` دستور معتبری نیست.
   {{< /note >}}

#### طرح‌واره‌ی ادعاهای خصوصی حساب سرویس

طرح‌واره‌ی (schema) ادعاهای مختص کوبرنتیز در توکن‌های JWT در حال حاضر مستند نشده است، اما بخش مربوط در کد را می‌توانید در [بسته‌ی serviceaccount](https://github.com/kubernetes/kubernetes/blob/d8919343526597e0788a1efe133c70d9a0c07f69/pkg/serviceaccount/claims.go#L56-L68) در مخزن کد کوبرنتیز پیدا کنید.

می‌توانید یک JWT را با ابزارهای استاندارد رمزگشایی JWT بررسی کنید. در ادامه نمونه‌ای از یک JWT برای ServiceAccount با نام `my-serviceaccount` آمده است که به یک آبجکت Pod با نام `my-pod` مقید است؛ این پاد در فضای نام `my-namespace` قرار دارد و روی Node با نام `my-node` زمان‌بندی شده است:

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
فیلدهای `aud` و `iss` در این JWT ممکن است بسته به پیکربندی شما، در کلاسترهای مختلف کوبرنتیز متفاوت باشند.

وجود هم‌زمان ادعاهای `pod` و `node` نشان می‌دهد که این توکن به یک آبجکت *Pod* مقید است. API server هنگام راستی‌آزمایی توکن‌های ServiceAccount مقید به Pod، وجود آبجکت Node ارجاع‌شده را راستی‌آزمایی **نمی‌کند**.
{{< /note >}}

سرویس‌هایی که بیرون از کوبرنتیز اجرا می‌شوند و می‌خواهند JWTها را به‌صورت آفلاین اعتبارسنجی کنند، می‌توانند از این طرح‌واره همراه با یک اعتبارسنج JWT سازگار که با اطلاعات OpenID Discovery دریافت‌شده از API server پیکربندی شده است استفاده کنند تا JWTهای ارائه‌شده را بدون نیاز به TokenReview API راستی‌آزمایی کنند.

سرویس‌هایی که JWTها را به این روش راستی‌آزمایی می‌کنند، جاری و همچنان معتبر بودن ادعاهای جای‌داده‌شده در توکن JWT را راستی‌آزمایی **نمی‌کنند**. یعنی اگر توکن به آبجکتی مقید باشد و آن آبجکت دیگر وجود نداشته باشد، توکن همچنان (تا زمان انقضای پیکربندی‌شده‌ی آن) معتبر در نظر گرفته می‌شود.

کلاینت‌هایی که باید از معتبر بودن ادعاهای مقید یک توکن اطمینان داشته باشند، **باید** از TokenReview API استفاده کنند و توکن را به `kube-apiserver` ارائه دهند تا ادعاهای جای‌داده‌شده را راستی‌آزمایی و گسترش دهد؛ مراحل این کار مشابه بخش [راستی‌آزمایی و بررسی ادعاهای خصوصی](#verifying-and-inspecting-private-claims) در بالا است، با این تفاوت که از یک [کتابخانه‌ی کلاینت پشتیبانی‌شده](/docs/reference/using-api/client-libraries/) استفاده می‌شود. برای اطلاعات بیشتر درباره‌ی JWTها و ساختار آن‌ها، [JSON Web Token RFC](https://datatracker.ietf.org/doc/html/rfc7519) را ببینید.

## سازوکار حجم توکن حساب سرویس مقید {#bound-service-account-token-volume}

{{< feature-state feature_gate_name="BoundServiceAccountTokenVolume" >}}

به‌طور پیش‌فرض، control plane کوبرنتیز (به‌طور مشخص، [کنترل‌کننده‌ی پذیرش ServiceAccount](#serviceaccount-admission-controller)) یک [حجم projected](/docs/concepts/storage/projected-volumes/) به Podها اضافه می‌کند و این حجم شامل توکنی برای دسترسی به API کوبرنتیز است.

در ادامه نمونه‌ای از شکل این حجم برای یک Pod راه‌اندازی‌شده آمده است:

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

این تکه از مانیفست یک حجم projected تعریف می‌کند که از سه منبع تشکیل شده است. در این مثال، هر منبع نماینده‌ی یک مسیر واحد درون آن حجم نیز هست. این سه منبع عبارت‌اند از:

1. یک منبع `serviceAccountToken` که شامل توکنی است که kubelet از kube-apiserver دریافت می‌کند. kubelet توکن‌های دارای محدودیت زمانی را با استفاده از TokenRequest API دریافت می‌کند. توکنی که برای یک TokenRequest صادر می‌شود، یا با حذف پاد یا پس از طول عمر تعیین‌شده (به‌طور پیش‌فرض یک ساعت) منقضی می‌شود. kubelet همچنین پیش از انقضای توکن، آن را تازه‌سازی می‌کند. این توکن به Pod مشخصی مقید است و مخاطب (audience) آن kube-apiserver است. این سازوکار جایگزین سازوکار قدیمی‌تری شد که حجمی مبتنی بر یک Secret اضافه می‌کرد؛ در آن سازوکار، Secret نماینده‌ی ServiceAccount پاد بود اما منقضی نمی‌شد.
1. یک منبع `configMap`. این ConfigMap شامل بسته‌ای از داده‌های مرجع صدور گواهی (certificate authority) است. Podها می‌توانند از این گواهی‌ها استفاده کنند تا مطمئن شوند به kube-apiserver کلاستر شما متصل می‌شوند (و نه به یک middlebox یا همتایی که به‌اشتباه پیکربندی شده است).
1. یک منبع `downwardAPI` که نام فضای نام دربرگیرنده‌ی Pod را پیدا می‌کند و این اطلاعات نام را در اختیار کد برنامه‌ای قرار می‌دهد که درون Pod اجرا می‌شود.

هر کانتینری درون Pod که این حجم مشخص را متصل (mount) کند، می‌تواند به اطلاعات بالا دسترسی داشته باشد.

{{< note >}}
هیچ سازوکار مشخصی برای باطل کردن توکنی که از طریق TokenRequest صادر شده است وجود ندارد. اگر دیگر به توکن حساب سرویس مقید یک Pod اعتماد ندارید، می‌توانید آن Pod را حذف کنید. حذف یک Pod باعث منقضی شدن توکن‌های حساب سرویس مقید به آن می‌شود.
{{< /note >}}

## مدیریت دستی Secret برای ServiceAccountها

نسخه‌های کوبرنتیز پیش از v1.22 به‌طور خودکار اعتبارنامه‌هایی برای دسترسی به API کوبرنتیز ایجاد می‌کردند. این سازوکار قدیمی‌تر بر پایه‌ی ایجاد Secretهای توکن بود که سپس می‌شد آن‌ها را در Podهای در حال اجرا متصل کرد.

در نسخه‌های جدیدتر، از جمله کوبرنتیز v{{< skew currentVersion >}}، اعتبارنامه‌های API با استفاده از [TokenRequest](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/) API [مستقیماً دریافت می‌شوند](#bound-service-account-token-volume) و با استفاده از یک حجم projected در Podها متصل می‌شوند. توکن‌هایی که با این روش دریافت می‌شوند طول عمر محدودی دارند و با حذف Podای که در آن متصل شده‌اند، به‌طور خودکار باطل می‌شوند.

همچنان می‌توانید برای نگهداری یک توکن حساب سرویس، یک Secret را [به‌صورت دستی ایجاد کنید](/docs/tasks/configure-pod-container/configure-service-account/#manually-create-an-api-token-for-a-serviceaccount)؛ برای مثال، اگر به توکنی نیاز دارید که هرگز منقضی نشود.

پس از اینکه یک Secret را به‌صورت دستی ایجاد کردید و آن را به یک ServiceAccount پیوند دادید، control plane کوبرنتیز به‌طور خودکار توکن را در آن Secret قرار می‌دهد.

{{< note >}}
با اینکه سازوکار دستی برای ایجاد توکن ServiceAccount بلندمدت وجود دارد، توصیه می‌شود به‌جای آن از [TokenRequest](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/) برای دریافت توکن‌های کوتاه‌مدت دسترسی به API استفاده کنید.
{{< /note >}}

## پاک‌سازی توکن‌های قدیمی ServiceAccount که به‌طور خودکار تولید شده‌اند {#auto-generated-legacy-serviceaccount-token-clean-up}

پیش از نسخه‌ی 1.24، کوبرنتیز به‌طور خودکار توکن‌های مبتنی بر Secret برای ServiceAccountها تولید می‌کرد. کوبرنتیز برای تمایز میان توکن‌های تولیدشده‌ی خودکار و توکن‌های ایجادشده‌ی دستی، وجود ارجاعی از فیلد secrets در ServiceAccount را بررسی می‌کند. اگر Secret در فیلد `secrets` ارجاع داده شده باشد، توکن قدیمیِ تولیدشده‌ی خودکار در نظر گرفته می‌شود؛ در غیر این صورت، توکن قدیمیِ ایجادشده‌ی دستی در نظر گرفته می‌شود. برای مثال:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: build-robot
  namespace: default
secrets:
  - name: build-robot-secret # usually NOT present for a manually generated token
```

از نسخه‌ی 1.29 به بعد، توکن‌های قدیمی ServiceAccount که به‌طور خودکار تولید شده‌اند، اگر برای مدت مشخصی (به‌طور پیش‌فرض یک سال) استفاده نشوند، نامعتبر علامت‌گذاری می‌شوند. توکن‌هایی که پس از آن نیز برای همین مدت تعیین‌شده (باز هم به‌طور پیش‌فرض یک سال) بدون استفاده بمانند، سپس از سوی control plane پاک‌سازی می‌شوند.

اگر کاربران از یک توکن تولیدشده‌ی خودکارِ نامعتبرشده استفاده کنند، اعتبارسنج توکن کارهای زیر را انجام می‌دهد:

1. یک حاشیه‌نویسی (annotation) ممیزی برای جفت کلید-مقدار `authentication.k8s.io/legacy-token-invalidated: <secret name>/<namespace>` اضافه می‌کند،
1. شمارنده‌ی متریک `invalid_legacy_auto_token_uses_total` را افزایش می‌دهد،
1. برچسب `kubernetes.io/legacy-token-last-used` روی Secret را با تاریخ جدید به‌روزرسانی می‌کند،
1. خطایی برمی‌گرداند که نشان می‌دهد توکن نامعتبر شده است.

کاربران با دریافت این خطای اعتبارسنجی می‌توانند Secret را به‌روزرسانی کنند و برچسب `kubernetes.io/legacy-token-invalid-since` را حذف کنند تا استفاده از این توکن به‌طور موقت مجاز شود.

در ادامه نمونه‌ای از یک توکن قدیمیِ تولیدشده‌ی خودکار آمده است که با برچسب‌های `kubernetes.io/legacy-token-last-used` و `kubernetes.io/legacy-token-invalid-since` علامت‌گذاری شده است:

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

### کنترل‌کننده‌ی ServiceAccount

کنترل‌کننده‌ی ServiceAccount، ServiceAccountهای درون فضاهای نام را مدیریت می‌کند و اطمینان می‌دهد که در هر فضای نام فعال، یک ServiceAccount با نام "default" وجود داشته باشد.

### کنترل‌کننده‌ی توکن

کنترل‌کننده‌ی توکن حساب سرویس به‌عنوان بخشی از `kube-controller-manager` اجرا می‌شود. این کنترل‌کننده به‌صورت ناهمگام عمل می‌کند و کارهای زیر را انجام می‌دهد:

- حذف ServiceAccountها را زیر نظر می‌گیرد و همه‌ی Secretهای توکن ServiceAccount مربوط را حذف می‌کند.
- افزوده شدن Secretهای توکن ServiceAccount را زیر نظر می‌گیرد، از وجود ServiceAccount ارجاع‌شده اطمینان حاصل می‌کند و در صورت نیاز، توکنی به Secret اضافه می‌کند.
- حذف Secretها را زیر نظر می‌گیرد و در صورت نیاز، ارجاع به آن را از ServiceAccount مربوط حذف می‌کند.

باید با استفاده از فلگ `--service-account-private-key-file`، یک فایل کلید خصوصی حساب سرویس را به کنترل‌کننده‌ی توکن در `kube-controller-manager` بدهید. از این کلید خصوصی برای امضای توکن‌های حساب سرویس تولیدشده استفاده می‌شود. به همین ترتیب، باید کلید عمومی متناظر را با استفاده از فلگ `--service-account-key-file` به `kube-apiserver` بدهید. از این کلید عمومی برای راستی‌آزمایی توکن‌ها در هنگام احراز هویت استفاده می‌شود.

{{< feature-state feature_gate_name="ExternalServiceAccountTokenSigner" >}}

به‌عنوان راه‌اندازی جایگزین برای تنظیم فلگ‌های `--service-account-private-key-file` و `--service-account-key-file`، می‌توانید یک امضاکننده‌ی JWT خارجی را برای [امضای توکن ServiceAccount و مدیریت کلید به‌صورت خارجی](#external-serviceaccount-token-signing-and-key-management) پیکربندی کنید. توجه کنید که این دو روش راه‌اندازی مانعه‌الجمع هستند و نمی‌توان آن‌ها را با هم پیکربندی کرد.

### کنترل‌کنندهٔ پذیرش ServiceAccount

تغییر Podها از طریق افزونه‌ای به نام [کنترل‌کنندهٔ پذیرش](/docs/reference/access-authn-authz/admission-controllers/) (Admission Controller) انجام می‌شود که بخشی از API server است. این کنترل‌کنندهٔ پذیرش به‌صورت همگام عمل می‌کند و Podها را هنگام ایجاد تغییر می‌دهد. وقتی این افزونه فعال باشد (که در بیشتر توزیع‌ها به‌طور پیش‌فرض فعال است)، هنگام ایجاد یک Pod کارهای زیر را انجام می‌دهد:

1. اگر فیلد `.spec.serviceAccountName` در Pod تنظیم نشده باشد، کنترل‌کنندهٔ پذیرش نام ServiceAccount این Pod ورودی را `default` قرار می‌دهد.
1. کنترل‌کنندهٔ پذیرش اطمینان حاصل می‌کند که ServiceAccount ارجاع‌شده در Pod ورودی وجود دارد. اگر هیچ ServiceAccount با نام منطبق وجود نداشته باشد، کنترل‌کنندهٔ پذیرش Pod ورودی را رد می‌کند. این بررسی حتی برای ServiceAccount با نام `default` نیز اعمال می‌شود.
1. به شرط آنکه نه فیلد `automountServiceAccountToken` در ServiceAccount و نه فیلد `automountServiceAccountToken` در Pod روی `false` تنظیم شده باشد:
   - کنترل‌کنندهٔ پذیرش Pod ورودی را تغییر می‌دهد و یک {{< glossary_tooltip text="حجم" term_id="volume" >}} اضافی به آن می‌افزاید که حاوی توکنی برای دسترسی به API است.
   - کنترل‌کنندهٔ پذیرش به هر کانتینر در Pod یک `volumeMount` اضافه می‌کند و از کانتینرهایی که از قبل برای مسیر `/var/run/secrets/kubernetes.io/serviceaccount` اتصال حجم تعریف‌شده دارند، صرف‌نظر می‌کند. در کانتینرهای لینوکسی، این حجم در مسیر `/var/run/secrets/kubernetes.io/serviceaccount` متصل می‌شود؛ در نودهای ویندوزی، اتصال در مسیر معادل انجام می‌شود.
1. اگر مشخصات Pod ورودی از قبل هیچ `imagePullSecrets` نداشته باشد، کنترل‌کنندهٔ پذیرش `imagePullSecrets` را از `ServiceAccount` کپی می‌کند و به Pod می‌افزاید.

### کنترل‌کنندهٔ ردیابی توکن‌های قدیمی ServiceAccount

{{< feature-state feature_gate_name="LegacyServiceAccountTokenTracking" >}}

این کنترل‌کننده یک ConfigMap به نام `kube-system/kube-apiserver-legacy-service-account-token-tracking` در فضای نام `kube-system` ایجاد می‌کند. این ConfigMap زمانی را ثبت می‌کند که سیستم پایش توکن‌های قدیمی حساب سرویس را آغاز کرده است.

### پاک‌کنندهٔ توکن‌های قدیمی ServiceAccount

{{< feature-state feature_gate_name="LegacyServiceAccountTokenCleanUp" >}}

پاک‌کنندهٔ توکن‌های قدیمی ServiceAccount به‌عنوان بخشی از `kube-controller-manager` اجرا می‌شود و هر ۲۴ ساعت یک بار بررسی می‌کند که آیا توکن قدیمی و خودکار ایجادشده‌ای از ServiceAccount وجود دارد که در *مدت زمان مشخص‌شده* استفاده نشده باشد. در این صورت، پاک‌کننده آن توکن‌ها را نامعتبر علامت‌گذاری می‌کند.

پاک‌کننده ابتدا ConfigMap ایجادشده توسط control plane را بررسی می‌کند (به شرط آنکه `LegacyServiceAccountTokenTracking` فعال باشد). اگر زمان کنونی به اندازهٔ *مدت زمان مشخص‌شده* از تاریخ ثبت‌شده در ConfigMap گذشته باشد، پاک‌کننده فهرست Secretهای کلاستر را پیمایش می‌کند و هر Secret از نوع `kubernetes.io/service-account-token` را ارزیابی می‌کند.

اگر یک Secret همهٔ شرایط زیر را داشته باشد، پاک‌کننده آن را نامعتبر علامت‌گذاری می‌کند:

- این Secret به‌صورت خودکار ایجاد شده باشد؛ یعنی میان آن و یک ServiceAccount ارجاع دوطرفه وجود داشته باشد.
- این Secret در حال حاضر توسط هیچ Podی متصل نشده باشد.
- این Secret از زمان ایجاد یا از آخرین باری که استفاده شده، در *مدت زمان مشخص‌شده* استفاده نشده باشد.

پاک‌کننده با افزودن برچسبی به نام `kubernetes.io/legacy-token-invalid-since` به Secret، با مقداری برابر تاریخ کنونی، آن را نامعتبر علامت‌گذاری می‌کند. اگر یک Secret نامعتبر در *مدت زمان مشخص‌شده* استفاده نشود، پاک‌کننده آن را حذف خواهد کرد.

{{< note >}}
مقدار پیش‌فرض همهٔ *مدت‌های زمان مشخص‌شده* در بالا یک سال است. مدیر کلاستر می‌تواند این مقدار را از طریق آرگومان خط فرمان `--legacy-service-account-token-clean-up-period` در مؤلفهٔ `kube-controller-manager` پیکربندی کند.
{{< /note >}}

### رابط TokenRequest API

{{< feature-state for_k8s_version="v1.22" state="stable" >}}

برای دریافت توکنی با زمان محدود برای یک ServiceAccount، از زیرمنبع [TokenRequest](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/) آن ServiceAccount استفاده می‌کنید. برای دریافت توکن API جهت استفاده درون کانتینر نیازی به فراخوانی آن ندارید، زیرا kubelet این کار را با استفاده از یک _حجم projected_ برای شما انجام می‌دهد.

اگر می‌خواهید از TokenRequest API از طریق `kubectl` استفاده کنید، به [ایجاد دستی توکن API برای یک ServiceAccount](/docs/tasks/configure-pod-container/configure-service-account/#manually-create-an-api-token-for-a-serviceaccount) مراجعه کنید.

control plane کوبرنتیز (به‌طور مشخص، کنترل‌کنندهٔ پذیرش ServiceAccount) یک حجم projected به Podها اضافه می‌کند و kubelet اطمینان حاصل می‌کند که این حجم حاوی توکنی است که به کانتینرها امکان می‌دهد با هویت ServiceAccount درست احراز هویت شوند.

(این سازوکار جایگزین سازوکار پیشین شد که حجمی مبتنی بر یک Secret اضافه می‌کرد؛ در آن سازوکار، Secret نمایندهٔ ServiceAccount مربوط به Pod بود اما منقضی نمی‌شد.)

در ادامه نمونه‌ای از ظاهر این حجم در یک Pod اجراشده آمده است:

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

این بخش از مانیفست یک حجم projected تعریف می‌کند که اطلاعات سه منبع را با هم ترکیب می‌کند:

1. یک منبع `serviceAccountToken` که حاوی توکنی است که kubelet از kube-apiserver دریافت می‌کند. kubelet توکن‌های دارای زمان محدود را با استفاده از TokenRequest API دریافت می‌کند. توکنی که برای یک TokenRequest صادر می‌شود، یا با حذف Pod یا پس از گذشت طول عمر تعریف‌شده (به‌طور پیش‌فرض ۱ ساعت) منقضی می‌شود. این توکن به Pod مشخصی وابسته است و مخاطب (audience) آن kube-apiserver است.
1. یک منبع `configMap`. این ConfigMap حاوی مجموعه‌ای از داده‌های مرجع صدور گواهی است. Podها می‌توانند با این گواهی‌ها اطمینان حاصل کنند که به kube-apiserver کلاستر شما متصل می‌شوند (و نه به یک واسط میانی یا همتایی که به‌اشتباه پیکربندی شده است).
1. یک منبع `downwardAPI`. این حجم `downwardAPI` نام فضای نامی را که Pod در آن قرار دارد، در اختیار کد برنامهٔ در حال اجرا درون Pod قرار می‌دهد.

هر کانتینری درون Pod که این حجم را متصل کند، به اطلاعات بالا دسترسی دارد.

## ایجاد توکن‌های API اضافی {#create-token}

{{< caution >}}
فقط در صورتی توکن‌های API بلندمدت ایجاد کنید که سازوکار [درخواست توکن](#tokenrequest-api) مناسب نباشد. سازوکار درخواست توکن، توکن‌هایی با زمان محدود فراهم می‌کند؛ از آنجا که این توکن‌ها منقضی می‌شوند، خطر کمتری برای امنیت اطلاعات دارند.
{{< /caution >}}

برای ایجاد یک توکن API ماندگار و بدون انقضا برای یک ServiceAccount، یک Secret از نوع `kubernetes.io/service-account-token` با حاشیه‌نویسی‌ای ایجاد کنید که به آن ServiceAccount ارجاع دهد. سپس control plane یک توکن بلندمدت تولید می‌کند و آن Secret را با دادهٔ توکن تولیدشده به‌روزرسانی می‌کند.

در ادامه یک مانیفست نمونه برای چنین Secretی آمده است:

{{% code_sample file="secret/serviceaccount/mysecretname.yaml" %}}

برای ایجاد یک Secret بر اساس این نمونه، دستور زیر را اجرا کنید:

```shell
kubectl -n examplens create -f https://k8s.io/examples/secret/serviceaccount/mysecretname.yaml
```

برای مشاهدهٔ جزئیات آن Secret، دستور زیر را اجرا کنید:

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

اگر یک Pod جدید را در فضای نام `examplens` اجرا کنید، آن Pod می‌تواند از Secret از نوع service-account-token مربوط به `myserviceaccount` که هم‌اکنون ایجاد کردید، استفاده کند.

{{< caution >}}
در فیلد `secrets` یک ServiceAccount به Secretهای دستی ایجادشده ارجاع ندهید؛ در غیر این صورت، اگر این Secretها مدت طولانی استفاده نشوند، پاک‌سازی خواهند شد. لطفاً به [پاک‌سازی توکن‌های قدیمی و خودکار ایجادشدهٔ ServiceAccount](#auto-generated-legacy-serviceaccount-token-clean-up) مراجعه کنید.
{{< /caution >}}

## حذف یا نامعتبرسازی توکن ServiceAccount {#delete-token}

### حذف یا نامعتبرسازی توکن بلندمدت یا قدیمی ServiceAccount {#delete-legacy-token}

اگر نام Secretی را که حاوی توکن مورد نظر برای حذف است می‌دانید:

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

سپس Secretی را که اکنون نامش را می‌دانید حذف کنید:

```shell
kubectl -n examplens delete secret/example-automated-thing-token-zyxwv
```

### حذف یا نامعتبرسازی توکن کوتاه‌مدت ServiceAccount {#delete-short-lived}

توکن‌های کوتاه‌مدت ServiceAccount پس از گذشت محدودیت زمانی‌ای که هنگام ایجادشان تعیین شده است، به‌طور خودکار منقضی می‌شوند. هیچ سابقهٔ مرکزی از توکن‌های صادرشده وجود ندارد؛ بنابراین راهی برای ابطال تک‌تک توکن‌ها وجود ندارد.

اگر ناچارید یک توکن کوتاه‌مدت را پیش از انقضایش باطل کنید، می‌توانید ServiceAccount مرتبط با آن را حذف و دوباره ایجاد کنید. با این کار UID آن تغییر می‌کند و در نتیجه **همهٔ** توکن‌های ServiceAccount که برای آن ایجاد شده بودند، نامعتبر می‌شوند.

## امضای خارجی توکن ServiceAccount و مدیریت کلید

{{< feature-state feature_gate_name="ExternalServiceAccountTokenSigner" >}}

می‌توان kube-apiserver را طوری پیکربندی کرد که برای امضای توکن و مدیریت کلیدهای تأیید توکن از یک امضاکنندهٔ خارجی استفاده کند. این قابلیت به توزیع‌های کوبرنتیز امکان می‌دهد برای امضا و تأیید اعتبارنامه‌های حساب سرویس، با راهکارهای مدیریت کلید دلخواه خود (برای مثال HSMها یا سرویس‌های KMS ابری) یکپارچه شوند. برای پیکربندی kube-apiserver جهت استفاده از external-jwt-signer، فلگ `--service-account-signing-endpoint` را برابر مسیر یک سوکت دامنهٔ یونیکس (UDS) روی سیستم فایل قرار دهید، یا آن را با نماد @ آغاز کنید تا به یک UDS در فضای نام سوکت‌های انتزاعی (abstract socket namespace) اشاره کند. در UDS پیکربندی‌شده باید یک سرور RPC وجود داشته باشد که سرویس gRPC با نام `ExternalJWTSigner` را پیاده‌سازی کند.

برای آنکه kube-apiserver راه‌اندازی شود، external-jwt-signer باید سالم و آمادهٔ ارائهٔ کلیدهای پشتیبانی‌شدهٔ حساب سرویس باشد.

{{< note >}}
فلگ‌های `--service-account-key-file` و `--service-account-signing-key-file` در kube-apiserver همچنان برای خواندن از فایل‌ها استفاده می‌شوند، مگر آنکه `--service-account-signing-endpoint` تنظیم شده باشد؛ این دو روش برای پشتیبانی از امضا و احراز هویت JWT، ناسازگار با یکدیگرند و نمی‌توان هم‌زمان از هر دو استفاده کرد.
{{< /note >}}

هر امضاکنندهٔ خارجی یک سرویس gRPC با نام `v1.ExternalJWTSigner` ارائه می‌کند که ۳ متد را پیاده‌سازی می‌کند:

### متد Metadata

قرار است `kube-apiserver` متد Metadata را یک بار هنگام راه‌اندازی فراخوانی کند. با این کار امضاکنندهٔ خارجی می‌تواند فراداده‌هایی مانند حداکثر طول عمر توکنی که پشتیبانی می‌کند را با kube-apiserver به اشتراک بگذارد.

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

### متد FetchKeys

متد FetchKeys مجموعهٔ کلیدهای عمومی‌ای را برمی‌گرداند که برای امضای توکن‌های حساب سرویس کوبرنتیز مورد اعتماد هستند. kube-apiserver این RPC را در موارد زیر فراخوانی می‌کند:
* هر بار که تلاش می‌کند یک JWT صادرشده از صادرکنندهٔ حساب سرویس را با شناسهٔ کلیدی ناشناخته اعتبارسنجی کند، و
* به‌صورت دوره‌ای، تا بتواند کلیدهای نسبتاً به‌روزی را از نقطهٔ پایانی OIDC JWKs ارائه دهد.

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

### متد Sign

متد Sign یک payload سریال‌شدهٔ JWT را دریافت می‌کند و سرآیند و امضای سریال‌شده را برمی‌گرداند. سپس `kube-apiserver` توکن JWT را از سرآیند، payload و امضا سرهم می‌کند.

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

اگر برای آزمایش، فضای نام `examplens` را ایجاد کرده‌اید، می‌توانید آن را حذف کنید:

```shell
kubectl delete namespace examplens
```

## {{% heading "whatsnext" %}}

- دربارهٔ [حجم‌های projected](/docs/concepts/storage/projected-volumes/) جزئیات بیشتری بخوانید.
