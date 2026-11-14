---
reviewers:
- enj
- liggitt
- thockin
title: پیکربندی حساب‌های سرویس برای Podها
content_type: task
weight: 120
---

کوبرنتیز دو روش متمایز در اختیار کلاینت‌هایی قرار می‌دهد که درون کلاستر شما اجرا می‌شوند یا به هر نحو دیگری با
{{< glossary_tooltip text="control plane" term_id="control-plane" >}}
کلاستر شما ارتباط دارند، تا بتوانند خود را به
{{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}}
احراز هویت کنند.

یک _حساب سرویس_ (service account) برای فرایندهایی که در یک Pod اجرا می‌شوند هویتی فراهم می‌کند و به یک آبجکت ServiceAccount نگاشت می‌شود. هنگامی که خود را به سرور API احراز هویت می‌کنید، خود را به‌عنوان یک _کاربر_ مشخص معرفی می‌کنید. کوبرنتیز مفهوم کاربر را به رسمیت می‌شناسد، اما خودِ کوبرنتیز API ویژه‌ای برای User **ندارد**.

این راهنمای کار دربارهٔ ServiceAccountهاست که در API کوبرنتیز وجود دارند. در این راهنما چند روش برای پیکربندی ServiceAccountها برای Podها را خواهید دید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

<!-- steps -->

## استفاده از حساب سرویس پیش‌فرض برای دسترسی به سرور API

هنگامی که Podها با سرور API ارتباط برقرار می‌کنند، با یک ServiceAccount مشخص (برای مثال `default`) احراز هویت می‌شوند. در هر {{< glossary_tooltip text="فضای نام" term_id="namespace" >}} همیشه دست‌کم یک ServiceAccount وجود دارد.

هر فضای نام کوبرنتیز دست‌کم یک ServiceAccount دارد: ServiceAccount پیش‌فرض آن فضای نام که `default` نام دارد.
اگر هنگام ایجاد یک Pod، ServiceAccount را مشخص نکنید، کوبرنتیز به‌طور خودکار ServiceAccount با نام `default` در آن فضای نام را به آن اختصاص می‌دهد.

می‌توانید جزئیات Podی را که ایجاد کرده‌اید دریافت کنید. برای مثال:

```shell
kubectl get pods/<podname> -o yaml
```

در خروجی، فیلدی با نام `spec.serviceAccountName` می‌بینید.
اگر هنگام ایجاد Pod این مقدار را مشخص نکنید، کوبرنتیز آن را به‌طور خودکار تنظیم می‌کند.

برنامه‌ای که درون یک Pod اجرا می‌شود، می‌تواند با استفاده از اعتبارنامه‌های حساب سرویس که به‌طور خودکار مانت می‌شوند، به API کوبرنتیز دسترسی پیدا کند.
برای اطلاعات بیشتر، [دسترسی به کلاستر](/docs/tasks/access-application-cluster/access-cluster/) را ببینید.

هنگامی که یک Pod با یک ServiceAccount احراز هویت می‌شود، سطح دسترسی آن به
[افزونه و سیاست مجوزدهی](/docs/reference/access-authn-authz/authorization/#authorization-modules)
مورد استفاده بستگی دارد.

اعتبارنامه‌های API هنگام حذف Pod به‌طور خودکار باطل می‌شوند، حتی اگر finalizerهایی وجود داشته باشند. به‌طور مشخص، این اعتبارنامه‌ها ۶۰ ثانیه پس از مقدار `.metadata.deletionTimestamp` تنظیم‌شده روی Pod باطل می‌شوند (زمان حذف معمولاً برابر است با زمان پذیرفته‌شدن درخواست **delete** به‌علاوهٔ مهلت خاتمهٔ Pod).

### غیرفعال‌کردن مانت خودکار اعتبارنامه‌های API

اگر نمی‌خواهید {{< glossary_tooltip text="kubelet" term_id="kubelet" >}} اعتبارنامه‌های API یک ServiceAccount را به‌طور خودکار مانت کند، می‌توانید این رفتار پیش‌فرض را غیرفعال کنید.
برای غیرفعال‌کردن مانت خودکار اعتبارنامه‌های API در مسیر `/var/run/secrets/kubernetes.io/serviceaccount/token` برای یک حساب سرویس، مقدار `automountServiceAccountToken: false` را روی ServiceAccount تنظیم کنید:

برای مثال:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: build-robot
automountServiceAccountToken: false
...
```

همچنین می‌توانید مانت خودکار اعتبارنامه‌های API را برای یک Pod خاص غیرفعال کنید:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  serviceAccountName: build-robot
  automountServiceAccountToken: false
  ...
```

اگر هم در ServiceAccount و هم در `.spec` مربوط به Pod مقداری برای `automountServiceAccountToken` مشخص شده باشد، مشخصات Pod اولویت دارد.

## استفاده از بیش از یک ServiceAccount {#use-multiple-service-accounts}

هر فضای نام دست‌کم یک ServiceAccount دارد: منبع ServiceAccount پیش‌فرض که `default` نام دارد. با دستور زیر می‌توانید فهرست همهٔ منابع ServiceAccount را در
[فضای نام جاری](/docs/concepts/overview/working-with-objects/namespaces/#setting-the-namespace-preference)
خود ببینید:

```shell
kubectl get serviceaccounts
```

خروجی مشابه زیر است:

```
NAME      SECRETS    AGE
default   1          1d
```

می‌توانید آبجکت‌های ServiceAccount دیگری را به این شکل ایجاد کنید:

```shell
kubectl apply -f - <<EOF
apiVersion: v1
kind: ServiceAccount
metadata:
  name: build-robot
EOF
```

نام هر آبجکت ServiceAccount باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

اگر محتوای کامل آبجکت حساب سرویس را به این شکل دریافت کنید:

```shell
kubectl get serviceaccounts/build-robot -o yaml
```

خروجی مشابه زیر است:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: 2019-06-16T00:12:34Z
  name: build-robot
  namespace: default
  resourceVersion: "272500"
  uid: 721ab723-13bc-11e5-aec2-42010af0021e
```

با استفاده از افزونه‌های مجوزدهی می‌توانید
[مجوزهای حساب‌های سرویس را تنظیم کنید](/docs/reference/access-authn-authz/rbac/#service-account-permissions).

برای استفاده از یک حساب سرویس غیرپیش‌فرض، فیلد `spec.serviceAccountName` یک Pod را برابر نام ServiceAccount موردنظرتان قرار دهید.

فیلد `serviceAccountName` را فقط هنگام ایجاد Pod یا در الگوی یک Pod جدید می‌توان تنظیم کرد. نمی‌توانید فیلد `.spec.serviceAccountName` یک Pod موجود را به‌روزرسانی کنید.

{{< note >}}
فیلد `.spec.serviceAccount` نام مستعار منسوخ‌شده‌ای برای `.spec.serviceAccountName` است.
اگر می‌خواهید این فیلدها را از یک منبع بار کاری حذف کنید، هر دو فیلد را به‌صراحت در
[الگوی Pod](/docs/concepts/workloads/pods#pod-templates) خالی قرار دهید.
{{< /note >}}

### پاک‌سازی {#cleanup-use-multiple-service-accounts}

اگر ServiceAccount با نام `build-robot` را طبق مثال بالا ایجاد کرده‌اید، می‌توانید با اجرای دستور زیر آن را پاک کنید:

```shell
kubectl delete serviceaccount/build-robot
```

## ایجاد دستی توکن API برای یک ServiceAccount

فرض کنید همان‌طور که پیش‌تر گفته شد، یک حساب سرویس موجود با نام "build-robot" دارید.

می‌توانید با استفاده از `kubectl` یک توکن API با مدت اعتبار محدود برای آن ServiceAccount دریافت کنید:

```shell
kubectl create token build-robot
```

خروجی این دستور توکنی است که می‌توانید با آن به‌عنوان همان ServiceAccount احراز هویت کنید. با آرگومان خط فرمان `--duration` در دستور `kubectl create token` می‌توانید مدت اعتبار مشخصی برای توکن درخواست کنید (مدت اعتبار واقعی توکن صادرشده ممکن است کوتاه‌تر یا حتی طولانی‌تر باشد).

{{< feature-state feature_gate_name="ServiceAccountTokenNodeBinding" >}}

با استفاده از `kubectl` نسخهٔ v1.31 یا بالاتر، می‌توان توکن حساب سرویسی ایجاد کرد که مستقیماً به یک نود مقید شده باشد:

```shell
kubectl create token build-robot --bound-object-kind Node --bound-object-name node-001 --bound-object-uid 123...456
```

این توکن تا زمان انقضا، یا تا زمانی که نود یا حساب سرویس مرتبط با آن حذف شود، معتبر خواهد بود.

{{< note >}}
نسخه‌های کوبرنتیز پیش از v1.22 به‌طور خودکار اعتبارنامه‌های بلندمدتی برای دسترسی به API کوبرنتیز ایجاد می‌کردند. این سازوکار قدیمی‌تر بر پایهٔ ایجاد Secretهای توکن بود که سپس می‌توانستند در Podهای در حال اجرا مانت شوند. در نسخه‌های جدیدتر، از جمله کوبرنتیز v{{< skew currentVersion >}}، اعتبارنامه‌های API مستقیماً با استفاده از API
[TokenRequest](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
به دست می‌آیند و با استفاده از یک
[حجم projected](/docs/reference/access-authn-authz/service-accounts-admin/#bound-service-account-token-volume)
در Podها مانت می‌شوند.
توکن‌هایی که به این روش به دست می‌آیند طول عمر محدودی دارند و هنگامی که Podی که در آن مانت شده‌اند حذف شود، به‌طور خودکار نامعتبر می‌شوند.

همچنان می‌توانید یک Secret توکن حساب سرویس را به‌صورت دستی ایجاد کنید؛ برای مثال، اگر به توکنی نیاز دارید که هرگز منقضی نشود. با این حال، توصیه می‌شود به‌جای آن از زیرمنبع
[TokenRequest](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
برای دریافت توکن دسترسی به API استفاده کنید.
{{< /note >}}

### ایجاد دستی توکن API بلندمدت برای یک ServiceAccount

اگر می‌خواهید یک توکن API برای یک ServiceAccount به دست آورید، یک Secret جدید با حاشیه‌نویسی (annotation) ویژهٔ `kubernetes.io/service-account.name` ایجاد کنید.

```shell
kubectl apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: build-robot-secret
  annotations:
    kubernetes.io/service-account.name: build-robot
type: kubernetes.io/service-account-token
EOF
```

اگر Secret را با دستور زیر مشاهده کنید:

```shell
kubectl get secret/build-robot-secret -o yaml
```

می‌بینید که اکنون این Secret شامل یک توکن API برای ServiceAccount با نام "build-robot" است.

به دلیل حاشیه‌نویسی‌ای که تنظیم کرده‌اید، control plane به‌طور خودکار برای آن ServiceAccount توکن تولید می‌کند و آن را در Secret مرتبط ذخیره می‌کند. control plane همچنین توکن‌های ServiceAccountهای حذف‌شده را پاک می‌کند.

```shell
kubectl describe secrets/build-robot-secret
```

خروجی مشابه زیر است:

```
Name:           build-robot-secret
Namespace:      default
Labels:         <none>
Annotations:    kubernetes.io/service-account.name: build-robot
                kubernetes.io/service-account.uid: da68f9c6-9d26-11e7-b84e-002dc52800da

Type:   kubernetes.io/service-account-token

Data
====
ca.crt:         1338 bytes
namespace:      7 bytes
token:          ...
```

{{< note >}}
محتوای `token` در اینجا حذف شده است.

مراقب باشید محتوای یک Secret از نوع `kubernetes.io/service-account-token` را در جایی نمایش ندهید که ممکن است فرد دیگری صفحهٔ ترمینال یا رایانهٔ شما را ببیند.
{{< /note >}}

هنگامی که ServiceAccountی را که Secret مرتبطی دارد حذف می‌کنید، control plane کوبرنتیز به‌طور خودکار توکن بلندمدت را از آن Secret پاک می‌کند.

{{< note >}}
اگر ServiceAccount را با دستور زیر مشاهده کنید:

` kubectl get serviceaccount build-robot -o yaml`

نمی‌توانید Secret با نام `build-robot-secret` را در فیلد
[`.secrets`](/docs/reference/kubernetes-api/authentication-resources/service-account-v1/)
آبجکت‌های API مربوط به ServiceAccount ببینید، زیرا این فیلد فقط با Secretهای خودکار تولیدشده پر می‌شود.
{{< /note >}}

## افزودن ImagePullSecrets به یک حساب سرویس

ابتدا [یک imagePullSecret ایجاد کنید](/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod).
سپس بررسی کنید که ایجاد شده باشد. برای مثال:

- یک imagePullSecret ایجاد کنید، همان‌طور که در
  [مشخص‌کردن ImagePullSecrets روی یک Pod](/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod)
  توضیح داده شده است.

  ```shell
  kubectl create secret docker-registry myregistrykey --docker-server=<registry name> \
          --docker-username=DUMMY_USERNAME --docker-password=DUMMY_DOCKER_PASSWORD \
          --docker-email=DUMMY_DOCKER_EMAIL
  ```

- بررسی کنید که ایجاد شده باشد.

  ```shell
  kubectl get secrets myregistrykey
  ```

  خروجی مشابه زیر است:

  ```
  NAME             TYPE                              DATA    AGE
  myregistrykey    kubernetes.io/.dockerconfigjson   1       1d
  ```

### افزودن image pull secret به حساب سرویس

سپس حساب سرویس پیش‌فرض فضای نام را طوری تغییر دهید که از این Secret به‌عنوان imagePullSecret استفاده کند.

```shell
kubectl patch serviceaccount default -p '{"imagePullSecrets": [{"name": "myregistrykey"}]}'
```

می‌توانید با ویرایش دستی آبجکت نیز به همین نتیجه برسید:

```shell
kubectl edit serviceaccount/default
```

خروجی فایل `sa.yaml` مشابه زیر است:

ویرایشگر متنی انتخابی شما با پیکربندی‌ای شبیه به این باز می‌شود:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: 2021-07-07T22:02:39Z
  name: default
  namespace: default
  resourceVersion: "243024"
  uid: 052fb0f4-3d50-11e5-b066-42010af0d7b6
```

در ویرایشگر، خطی را که کلید `resourceVersion` دارد حذف کنید، خطوط مربوط به `imagePullSecrets:` را اضافه کنید و فایل را ذخیره کنید. مقدار `uid` را همان‌طور که بود باقی بگذارید.

پس از اعمال این تغییرات، ServiceAccount ویرایش‌شده تقریباً به این شکل خواهد بود:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: 2021-07-07T22:02:39Z
  name: default
  namespace: default
  uid: 052fb0f4-3d50-11e5-b066-42010af0d7b6
imagePullSecrets:
  - name: myregistrykey
```

### بررسی تنظیم‌شدن imagePullSecrets برای Podهای جدید

اکنون هنگامی که یک Pod جدید در فضای نام جاری و با استفاده از ServiceAccount پیش‌فرض ایجاد شود، فیلد `spec.imagePullSecrets` آن به‌طور خودکار تنظیم می‌شود:

```shell
kubectl run nginx --image=<registry name>/nginx --restart=Never
kubectl get pod nginx -o=jsonpath='{.spec.imagePullSecrets[0].name}{"\n"}'
```

خروجی به این صورت است:

```
myregistrykey
```

## پروجکشن حجم توکن ServiceAccount

{{< feature-state for_k8s_version="v1.20" state="stable" >}}

{{< note >}}
برای فعال‌سازی و استفاده از پروجکشن درخواست توکن، باید هر یک از آرگومان‌های خط فرمان زیر را برای `kube-apiserver` مشخص کنید:

`--service-account-issuer`
: شناسهٔ صادرکنندهٔ توکن حساب سرویس را تعریف می‌کند. آرگومان `--service-account-issuer` را می‌توانید چند بار مشخص کنید؛ این کار برای تغییر صادرکننده بدون ایجاد اختلال مفید است. هنگامی که این فلگ چند بار مشخص شود، اولین مقدار برای تولید توکن‌ها استفاده می‌شود و همهٔ مقادیر برای تعیین صادرکنندگان پذیرفته‌شده به کار می‌روند. برای اینکه بتوانید `--service-account-issuer` را چند بار مشخص کنید، باید کوبرنتیز v1.22 یا بالاتر را اجرا کنید.

`--service-account-key-file`
: مسیر فایلی را مشخص می‌کند که شامل کلیدهای خصوصی یا عمومی X.509 با کدگذاری PEM (از نوع RSA یا ECDSA) است و برای راستی‌آزمایی توکن‌های ServiceAccount استفاده می‌شود. فایل مشخص‌شده می‌تواند چند کلید داشته باشد و این فلگ را می‌توان چند بار با فایل‌های مختلف مشخص کرد. در صورت مشخص‌شدن چندباره، سرور API کوبرنتیز توکن‌هایی را که با هر یک از کلیدهای مشخص‌شده امضا شده باشند معتبر می‌داند.

`--service-account-signing-key-file`
: مسیر فایلی را مشخص می‌کند که کلید خصوصی جاری صادرکنندهٔ توکن حساب سرویس را در خود دارد. صادرکننده توکن‌های شناسهٔ صادرشده را با این کلید خصوصی امضا می‌کند.

`--api-audiences` (می‌توان آن را حذف کرد)
: مخاطبان (audiences) توکن‌های ServiceAccount را تعریف می‌کند. احرازکنندهٔ هویت توکن حساب سرویس بررسی می‌کند که توکن‌های استفاده‌شده در برابر API دست‌کم به یکی از این مخاطبان مقید باشند. اگر `api-audiences` چند بار مشخص شود، سرور API کوبرنتیز توکن‌های مربوط به هر یک از مخاطبان مشخص‌شده را معتبر می‌داند. اگر آرگومان خط فرمان `--service-account-issuer` را مشخص کنید اما `--api-audiences` را تنظیم نکنید، control plane به‌طور پیش‌فرض از فهرست مخاطبانی تک‌عضوی استفاده می‌کند که فقط شامل URL صادرکننده است.

{{< /note >}}

همچنین kubelet می‌تواند یک توکن ServiceAccount را به درون یک Pod پروجکت کند. می‌توانید ویژگی‌های موردنظر توکن، مانند مخاطب و مدت اعتبار، را مشخص کنید. این ویژگی‌ها برای توکن ServiceAccount پیش‌فرض قابل پیکربندی _نیستند_. همچنین هنگامی که Pod یا ServiceAccount حذف شود، این توکن در برابر API نامعتبر می‌شود.

می‌توانید این رفتار را در `spec` یک Pod با استفاده از نوعی از
[حجم projected](/docs/concepts/storage/volumes/#projected) به نام
`ServiceAccountToken` پیکربندی کنید.

توکن حاصل از این حجم projected یک {{<glossary_tooltip term_id="jwt" text="JSON Web Token">}} (JWT) است.
محتوای JSON این توکن از طرح‌واره‌ای کاملاً تعریف‌شده پیروی می‌کند. در ادامه نمونه‌ای از محتوای یک توکن مقید به Pod آمده است:

```yaml
{
  "aud": [  # matches the requested audiences, or the API server's default audiences when none are explicitly requested
    "https://kubernetes.default.svc"
  ],
  "exp": 1731613413,
  "iat": 1700077413,
  "iss": "https://kubernetes.default.svc",  # matches the first value passed to the --service-account-issuer flag
  "jti": "ea28ed49-2e11-4280-9ec5-bc3d1d84661a", 
  "kubernetes.io": {
    "namespace": "kube-system",
    "node": {
      "name": "127.0.0.1",
      "uid": "58456cb0-dd00-45ed-b797-5578fdceaced"
    },
    "pod": {
      "name": "coredns-69cbfb9798-jv9gn",
      "uid": "778a530c-b3f4-47c0-9cd5-ab018fb64f33"
    },
    "serviceaccount": {
      "name": "coredns",
      "uid": "a087d5a0-e1dd-43ec-93ac-f13d89cd13af"
    },
    "warnafter": 1700081020
  },
  "nbf": 1700077413,
  "sub": "system:serviceaccount:kube-system:coredns"
}
```

### اجرای یک Pod با استفاده از پروجکشن توکن حساب سرویس

برای اینکه به یک Pod توکنی با مخاطب `vault` و مدت اعتبار دو ساعت بدهید، می‌توانید مانیفست Podی مشابه زیر تعریف کنید:

{{% code_sample file="pods/pod-projected-svc-token.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl create -f https://k8s.io/examples/pods/pod-projected-svc-token.yaml
```

در این حالت kubelet توکن را از طرف Pod درخواست و ذخیره می‌کند، آن را در مسیر فایلی قابل پیکربندی در اختیار Pod قرار می‌دهد و با نزدیک‌شدن به زمان انقضا، توکن را تازه‌سازی می‌کند. اگر از عمر توکن بیش از ۸۰٪ کل طول عمر آن (TTL) یا بیش از ۲۴ ساعت گذشته باشد، kubelet پیشاپیش چرخش توکن را درخواست می‌کند.

بارگذاری مجدد توکن پس از چرخش آن بر عهدهٔ برنامه است. اغلب کافی است برنامه توکن را طبق یک زمان‌بندی (برای مثال هر ۵ دقیقه یک بار) بارگذاری کند، بدون اینکه زمان واقعی انقضا را دنبال کند.

### کشف صادرکنندهٔ ServiceAccount (Service account issuer discovery)

{{< feature-state for_k8s_version="v1.21" state="stable" >}}

اگر [نمایش توکن (token projection)](#serviceaccount-token-volume-projection) را برای ServiceAccountها در کلاستر خود فعال کرده باشید، از قابلیت کشف نیز می‌توانید استفاده کنید. کوبرنتیز روشی فراهم می‌کند که کلاینت‌ها بتوانند به‌عنوان یک _ارائه‌دهندهٔ هویت_ (identity provider) فدراسیون برقرار کنند. به این ترتیب، یک یا چند سامانهٔ خارجی می‌توانند در نقش _طرف اتکاکننده_ (relying party) عمل کنند.

{{< note >}}
نشانی URL صادرکننده باید با
[OIDC Discovery Spec](https://openid.net/specs/openid-connect-discovery-1_0.html) سازگار باشد. در عمل، این یعنی باید از طرح `https` استفاده کند و پیکربندی ارائه‌دهندهٔ OpenID را در `{service-account-issuer}/.well-known/openid-configuration` ارائه دهد.

اگر این نشانی سازگار نباشد، نقاط پایانی (endpoint) کشف صادرکنندهٔ ServiceAccount ثبت نمی‌شوند یا در دسترس نخواهند بود.
{{< /note >}}

وقتی این قابلیت فعال باشد، سرور API کوبرنتیز یک سند پیکربندی ارائه‌دهندهٔ OpenID را از طریق HTTP منتشر می‌کند. این سند پیکربندی در `/.well-known/openid-configuration` منتشر می‌شود. گاهی پیکربندی ارائه‌دهندهٔ OpenID را _سند کشف_ (discovery document) نیز می‌نامند. سرور API کوبرنتیز مجموعهٔ کلیدهای وب JSON مرتبط (JSON Web Key Set یا JWKS) را نیز از طریق HTTP در `/openid/v1/jwks` منتشر می‌کند.

{{< note >}}
پاسخ‌هایی که در `/.well-known/openid-configuration` و `/openid/v1/jwks` ارائه می‌شوند طوری طراحی شده‌اند که با OIDC سازگار باشند، اما به‌طور کامل از استاندارد OIDC پیروی نمی‌کنند. این اسناد فقط پارامترهایی را در بر دارند که برای اعتبارسنجی توکن‌های ServiceAccount کوبرنتیز لازم است.
{{< /note >}}

کلاسترهایی که از {{< glossary_tooltip text="RBAC" term_id="rbac">}} استفاده می‌کنند، یک ClusterRole پیش‌فرض به نام `system:service-account-issuer-discovery` دارند. یک ClusterRoleBinding پیش‌فرض این نقش را به گروه `system:serviceaccounts` اختصاص می‌دهد که همهٔ ServiceAccountها به‌طور ضمنی عضو آن هستند. به این ترتیب، پادهایی که روی کلاستر اجرا می‌شوند می‌توانند با توکن ServiceAccount سوارشدهٔ خود به سند کشف ServiceAccount دسترسی پیدا کنند. علاوه بر این، مدیران می‌توانند بسته به الزامات امنیتی خود و سامانه‌های خارجی‌ای که قصد فدراسیون با آن‌ها را دارند، این نقش را به `system:authenticated` یا `system:unauthenticated` نیز متصل کنند.

پاسخ JWKS شامل کلیدهای عمومی است که طرف اتکاکننده می‌تواند با آن‌ها توکن‌های ServiceAccount کوبرنتیز را اعتبارسنجی کند. طرف‌های اتکاکننده ابتدا پیکربندی ارائه‌دهندهٔ OpenID را درخواست می‌کنند و سپس با استفاده از فیلد `jwks_uri` در پاسخ، JWKS را پیدا می‌کنند.

در بسیاری از موارد، سرورهای API کوبرنتیز در اینترنت عمومی در دسترس نیستند، اما کاربران یا ارائه‌دهندگان خدمات می‌توانند نقاط پایانی عمومی‌ای فراهم کنند که پاسخ‌های ذخیره‌شده (cached) از سرور API را ارائه می‌دهند. در این موارد، می‌توان با دادن فلگ `--service-account-jwks-uri` به سرور API، مقدار `jwks_uri` را در پیکربندی ارائه‌دهندهٔ OpenID بازنویسی کرد تا به‌جای نشانی سرور API به آن نقطهٔ پایانی عمومی اشاره کند. نشانی URI مربوط به JWKS نیز، همانند نشانی URL صادرکننده، باید از طرح `https` استفاده کند.

## {{% heading "whatsnext" %}}

همچنین ببینید:

- [راهنمای مدیر کلاستر برای ServiceAccountها](/docs/reference/access-authn-authz/service-accounts-admin/) را بخوانید.
- دربارهٔ [مجوزدهی در کوبرنتیز](/docs/reference/access-authn-authz/authorization/) بخوانید.
- دربارهٔ [Secretها](/docs/concepts/configuration/secret/) بخوانید.
  - یا یاد بگیرید چگونه [اعتبارنامه‌ها را با استفاده از Secretها به‌صورت امن توزیع کنید](/docs/tasks/inject-data-application/distribute-credentials-secure/).
  - اما به خاطر داشته باشید که استفاده از Secretها برای احراز هویت به‌عنوان یک ServiceAccount منسوخ شده است. جایگزین توصیه‌شده،
    [نمایش توکن ServiceAccount در حجم (volume)](#serviceaccount-token-volume-projection) است.
- دربارهٔ [حجم‌های نمایشی (projected volumes)](/docs/tasks/configure-pod-container/configure-projected-volume-storage/) بخوانید.
- برای آشنایی با پیشینهٔ کشف OIDC، پیشنهاد بهبود کوبرنتیز (Kubernetes Enhancement Proposal) با عنوان
  [ServiceAccount signing key retrieval](https://github.com/kubernetes/enhancements/tree/master/keps/sig-auth/1393-oidc-discovery)
  را بخوانید.
- [OIDC Discovery Spec](https://openid.net/specs/openid-connect-discovery-1_0.html) را بخوانید.
