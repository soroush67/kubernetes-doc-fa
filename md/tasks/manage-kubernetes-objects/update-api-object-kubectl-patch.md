---
title: به‌روزرسانی درجای آبجکت‌های API با استفاده از kubectl patch
description: با kubectl patch آبجکت‌های API کوبرنتیز را درجا به‌روزرسانی کنید. یک وصلهٔ ادغام راهبردی یا یک وصلهٔ ادغام JSON اعمال کنید.
content_type: task
weight: 50
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه با `kubectl patch` یک آبجکت API را درجا به‌روزرسانی کنید. تمرین‌های این صفحه نحوهٔ اعمال یک وصلهٔ ادغام راهبردی (strategic merge patch) و یک وصلهٔ ادغام JSON (JSON merge patch) را نشان می‌دهند.



## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}




<!-- steps -->

## استفاده از وصلهٔ ادغام راهبردی برای به‌روزرسانی یک Deployment

در ادامه فایل پیکربندی یک Deployment با دو رونوشت (replica) آمده است. هر رونوشت یک Pod است که یک کانتینر دارد:

{{% code_sample file="application/deployment-patch.yaml" %}}

این Deployment را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/deployment-patch.yaml
```

فهرست Podهای مرتبط با Deployment خود را ببینید:

```shell
kubectl get pods
```

خروجی نشان می‌دهد که Deployment دو Pod دارد. مقدار `1/1` نشان می‌دهد که هر Pod یک کانتینر دارد:


```
NAME                        READY     STATUS    RESTARTS   AGE
patch-demo-28633765-670qr   1/1       Running   0          23s
patch-demo-28633765-j5qs3   1/1       Running   0          23s
```

نام Podهای در حال اجرا را یادداشت کنید. بعداً خواهید دید که این Podها خاتمه می‌یابند و Podهای جدیدی جای آن‌ها را می‌گیرند.

در این مرحله، هر Pod یک کانتینر دارد که ایمیج nginx را اجرا می‌کند. اکنون فرض کنید می‌خواهید هر Pod دو کانتینر داشته باشد: یکی برای اجرای nginx و دیگری برای اجرای redis.

فایلی با نام `patch-file.yaml` و محتوای زیر ایجاد کنید:

```yaml
spec:
  template:
    spec:
      containers:
      - name: patch-demo-ctr-2
        image: redis
```

وصله را روی Deployment خود اعمال کنید:

```shell
kubectl patch deployment patch-demo --patch-file patch-file.yaml
```

وضعیت Deployment وصله‌شده را مشاهده کنید:

```shell
kubectl get deployment patch-demo --output yaml
```

خروجی نشان می‌دهد که PodSpec در این Deployment دو کانتینر دارد:

```yaml
containers:
- image: redis
  imagePullPolicy: Always
  name: patch-demo-ctr-2
  ...
- image: nginx
  imagePullPolicy: Always
  name: patch-demo-ctr
  ...
```

فهرست Podهای مرتبط با Deployment وصله‌شده را ببینید:

```shell
kubectl get pods
```

خروجی نشان می‌دهد که نام Podهای در حال اجرا با نام Podهایی که پیش‌تر اجرا می‌شدند متفاوت است. این Deployment، Podهای قدیمی را خاتمه داده و دو Pod جدید مطابق با مشخصات (spec) به‌روزشدهٔ Deployment ایجاد کرده است. مقدار `2/2` نشان می‌دهد که هر Pod دو کانتینر دارد:

```
NAME                          READY     STATUS    RESTARTS   AGE
patch-demo-1081991389-2wrn5   2/2       Running   0          1m
patch-demo-1081991389-jmg7b   2/2       Running   0          1m
```

یکی از Podهای patch-demo را دقیق‌تر بررسی کنید:

```shell
kubectl get pod <your-pod-name> --output yaml
```

خروجی نشان می‌دهد که این Pod دو کانتینر دارد: یکی nginx و دیگری redis را اجرا می‌کند:

```
containers:
- image: redis
  ...
- image: nginx
  ...
```

### نکاتی دربارهٔ وصلهٔ ادغام راهبردی

وصله‌ای که در تمرین قبل اعمال کردید *وصلهٔ ادغام راهبردی* نام دارد. توجه کنید که این وصله فهرست `containers` را جایگزین نکرد، بلکه یک کانتینر جدید به آن افزود. به بیان دیگر، فهرست موجود در وصله با فهرست فعلی ادغام شد. اما هنگام اعمال وصلهٔ ادغام راهبردی روی یک فهرست، همیشه چنین اتفاقی نمی‌افتد. در برخی موارد، فهرست جایگزین می‌شود، نه ادغام.

در وصلهٔ ادغام راهبردی، هر فهرست بسته به راهبرد وصلهٔ (patch strategy) خود یا جایگزین می‌شود یا ادغام. راهبرد وصله با مقدار کلید `patchStrategy` در تگ فیلد (field tag) در کد منبع کوبرنتیز تعیین می‌شود. برای مثال، فیلد `Containers` در ساختار (struct) `PodSpec` دارای `patchStrategy` با مقدار `merge` است:

```go
type PodSpec struct {
  ...
  Containers []Container `json:"containers" patchStrategy:"merge" patchMergeKey:"name" ...`
  ...
}
```

راهبرد وصله را در
[مشخصات OpenApi](https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json) نیز می‌توانید ببینید:

```yaml
"io.k8s.api.core.v1.PodSpec": {
    ...,
    "containers": {
        "description": "List of containers belonging to the pod.  ...."
    },
    "x-kubernetes-patch-merge-key": "name",
    "x-kubernetes-patch-strategy": "merge"
}
```
<!-- for editors: intentionally use yaml instead of json here, to prevent syntax highlight error. -->

همچنین می‌توانید راهبرد وصله را در
[مستندات API کوبرنتیز](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podspec-v1-core) ببینید.

فایلی با نام `patch-file-tolerations.yaml` و محتوای زیر ایجاد کنید:

```yaml
spec:
  template:
    spec:
      tolerations:
      - effect: NoSchedule
        key: disktype
        value: ssd
```

وصله را روی Deployment خود اعمال کنید:

```shell
kubectl patch deployment patch-demo --patch-file patch-file-tolerations.yaml
```

وضعیت Deployment وصله‌شده را مشاهده کنید:

```shell
kubectl get deployment patch-demo --output yaml
```

خروجی نشان می‌دهد که PodSpec در این Deployment فقط یک تحمل (toleration) دارد:

```yaml
tolerations:
- effect: NoSchedule
  key: disktype
  value: ssd
```

توجه کنید که فهرست `tolerations` در PodSpec جایگزین شد، نه ادغام. دلیل این است که فیلد Tolerations در PodSpec، در تگ فیلد خود کلید `patchStrategy` ندارد. بنابراین وصلهٔ ادغام راهبردی از راهبرد وصلهٔ پیش‌فرض، یعنی `replace`، استفاده می‌کند.

```go
type PodSpec struct {
  ...
  Tolerations []Toleration `json:"tolerations,omitempty" protobuf:"bytes,22,opt,name=tolerations"`
  ...
}
```

## استفاده از وصلهٔ ادغام JSON برای به‌روزرسانی یک Deployment

وصلهٔ ادغام راهبردی با
[وصلهٔ ادغام JSON](https://tools.ietf.org/html/rfc7386) تفاوت دارد.
در وصلهٔ ادغام JSON، اگر بخواهید فهرستی را به‌روزرسانی کنید، باید کل فهرست جدید را مشخص کنید. فهرست جدید نیز به‌طور کامل جایگزین فهرست موجود می‌شود.

فرمان `kubectl patch` پارامتری به نام `type` دارد که می‌توانید آن را روی یکی از مقادیر زیر تنظیم کنید:

<table>
  <tr><th>مقدار پارامتر</th><th>نوع ادغام</th></tr>
  <tr><td>json</td><td><a href="https://tools.ietf.org/html/rfc6902">JSON Patch, RFC 6902</a></td></tr>
  <tr><td>merge</td><td><a href="https://tools.ietf.org/html/rfc7386">JSON Merge Patch, RFC 7386</a></td></tr>
  <tr><td>strategic</td><td>وصلهٔ ادغام راهبردی</td></tr>
</table>

برای مقایسهٔ وصلهٔ JSON و وصلهٔ ادغام JSON، به
[JSON Patch and JSON Merge Patch](https://erosb.github.io/post/json-patch-vs-merge-patch/) مراجعه کنید.

مقدار پیش‌فرض پارامتر `type` برابر با `strategic` است. بنابراین در تمرین قبل، یک وصلهٔ ادغام راهبردی اعمال کردید.

اکنون یک وصلهٔ ادغام JSON روی همان Deployment اعمال کنید. فایلی با نام `patch-file-2.yaml` و محتوای زیر ایجاد کنید:

```yaml
spec:
  template:
    spec:
      containers:
      - name: patch-demo-ctr-3
        image: gcr.io/google-samples/hello-app:2.0
```

در فرمان وصله، مقدار `type` را برابر با `merge` قرار دهید:

```shell
kubectl patch deployment patch-demo --type merge --patch-file patch-file-2.yaml
```

وضعیت Deployment وصله‌شده را مشاهده کنید:

```shell
kubectl get deployment patch-demo --output yaml
```

فهرست `containers` که در وصله مشخص کردید فقط یک کانتینر دارد. خروجی نشان می‌دهد که این فهرست تک‌کانتینری جایگزین فهرست `containers` موجود شده است.

```yaml
spec:
  containers:
  - image: gcr.io/google-samples/hello-app:2.0
    ...
    name: patch-demo-ctr-3
```

فهرست Podهای در حال اجرا را ببینید:

```shell
kubectl get pods
```

در خروجی می‌بینید که Podهای قبلی خاتمه یافته‌اند و Podهای جدیدی ایجاد شده‌اند. مقدار `1/1` نشان می‌دهد که هر Pod جدید فقط یک کانتینر را اجرا می‌کند.

```shell
NAME                          READY     STATUS    RESTARTS   AGE
patch-demo-1307768864-69308   1/1       Running   0          1m
patch-demo-1307768864-c86dc   1/1       Running   0          1m
```

## استفاده از وصلهٔ ادغام راهبردی با راهبرد retainKeys برای به‌روزرسانی یک Deployment

در ادامه فایل پیکربندی یک Deployment آمده است که از راهبرد `RollingUpdate` استفاده می‌کند:

{{% code_sample file="application/deployment-retainkeys.yaml" %}}

این Deployment را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/deployment-retainkeys.yaml
```

در این مرحله، Deployment ایجاد شده است و از راهبرد `RollingUpdate` استفاده می‌کند.

فایلی با نام `patch-file-no-retainkeys.yaml` و محتوای زیر ایجاد کنید:

```yaml
spec:
  strategy:
    type: Recreate
```

وصله را روی Deployment خود اعمال کنید:

```shell
kubectl patch deployment retainkeys-demo --type strategic --patch-file patch-file-no-retainkeys.yaml
```

در خروجی می‌بینید که وقتی برای `spec.strategy.rollingUpdate` مقداری تعریف شده باشد، نمی‌توان `type` را روی `Recreate` تنظیم کرد:

```
The Deployment "retainkeys-demo" is invalid: spec.strategy.rollingUpdate: Forbidden: may not be specified when strategy `type` is 'Recreate'
```

برای حذف مقدار `spec.strategy.rollingUpdate` هنگام به‌روزرسانی مقدار `type`، باید از راهبرد `retainKeys` در ادغام راهبردی استفاده کنید.

فایل دیگری با نام `patch-file-retainkeys.yaml` و محتوای زیر ایجاد کنید:

```yaml
spec:
  strategy:
    $retainKeys:
    - type
    type: Recreate
```

با این وصله مشخص می‌کنیم که می‌خواهیم فقط کلید `type` از آبجکت `strategy` حفظ شود. در نتیجه، `rollingUpdate` در طول عملیات وصله حذف می‌شود.

این وصلهٔ جدید را دوباره روی Deployment خود اعمال کنید:

```shell
kubectl patch deployment retainkeys-demo --type strategic --patch-file patch-file-retainkeys.yaml
```

محتوای Deployment را بررسی کنید:

```shell
kubectl get deployment retainkeys-demo --output yaml
```

خروجی نشان می‌دهد که آبجکت strategy در Deployment دیگر کلید `rollingUpdate` را ندارد:

```yaml
spec:
  strategy:
    type: Recreate
  template:
```

### نکاتی دربارهٔ وصلهٔ ادغام راهبردی با راهبرد retainKeys

وصله‌ای که در تمرین قبل اعمال کردید *وصلهٔ ادغام راهبردی با راهبرد retainKeys* نام دارد. این روش رهنمود (directive) جدیدی به نام `$retainKeys` معرفی می‌کند که از راهبردهای زیر پیروی می‌کند:

- شامل فهرستی از رشته‌ها است.
- همهٔ فیلدهایی که باید حفظ شوند، باید در فهرست `$retainKeys` حضور داشته باشند.
- فیلدهای حاضر در این فهرست با آبجکت زنده (live object) ادغام می‌شوند.
- همهٔ فیلدهای غایب هنگام اعمال وصله پاک می‌شوند.
- مجموعهٔ فیلدهای فهرست `$retainKeys` باید با فیلدهای موجود در وصله برابر یا ابرمجموعهٔ آن‌ها باشد.

راهبرد `retainKeys` برای همهٔ آبجکت‌ها کار نمی‌کند. این راهبرد فقط زمانی کار می‌کند که مقدار کلید `patchStrategy` در تگ فیلد در کد منبع کوبرنتیز شامل `retainKeys` باشد. برای مثال، فیلد `Strategy` در ساختار `DeploymentSpec` دارای `patchStrategy` با مقدار `retainKeys` است:

```go
type DeploymentSpec struct {
  ...
  // +patchStrategy=retainKeys
  Strategy DeploymentStrategy `json:"strategy,omitempty" patchStrategy:"retainKeys" ...`
  ...
}
```

راهبرد `retainKeys` را در [مشخصات OpenApi](https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json) نیز می‌توانید ببینید:

```yaml
"io.k8s.api.apps.v1.DeploymentSpec": {
    ...,
    "strategy": {
        "$ref": "#/definitions/io.k8s.api.apps.v1.DeploymentStrategy",
        "description": "The deployment strategy to use to replace existing pods with new ones.",
        "x-kubernetes-patch-strategy": "retainKeys"
    },
    ....
}
```
<!-- for editors: intentionally use yaml instead of json here, to prevent syntax highlight error. -->

همچنین می‌توانید راهبرد `retainKeys` را در
[مستندات API کوبرنتیز](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#deploymentspec-v1-apps) ببینید.

### شکل‌های دیگر فرمان kubectl patch

فرمان `kubectl patch` ورودی YAML یا JSON می‌پذیرد. این فرمان می‌تواند وصله را به‌صورت فایل یا مستقیماً در خط فرمان دریافت کند.

فایلی با نام `patch-file.json` و محتوای زیر ایجاد کنید:

```json
{
   "spec": {
      "template": {
         "spec": {
            "containers": [
               {
                  "name": "patch-demo-ctr-2",
                  "image": "redis"
               }
            ]
         }
      }
   }
}
```

فرمان‌های زیر معادل یکدیگرند:


```shell
kubectl patch deployment patch-demo --patch-file patch-file.yaml
kubectl patch deployment patch-demo --patch 'spec:\n template:\n  spec:\n   containers:\n   - name: patch-demo-ctr-2\n     image: redis'

kubectl patch deployment patch-demo --patch-file patch-file.json
kubectl patch deployment patch-demo --patch '{"spec": {"template": {"spec": {"containers": [{"name": "patch-demo-ctr-2","image": "redis"}]}}}}'
```

### به‌روزرسانی تعداد رونوشت‌های یک آبجکت با `kubectl patch` و `--subresource` {#scale-kubectl-patch}

فلگ `--subresource=[subresource-name]` همراه با فرمان‌های kubectl مانند get، patch، edit، apply و replace به کار می‌رود تا زیرمنبع‌های (subresource) `status`، `scale` و `resize` منابعی را که مشخص می‌کنید دریافت و به‌روزرسانی کند. برای هر یک از منابع API کوبرنتیز (منابع داخلی و CRها) که زیرمنبع `status`، `scale` یا `resize` دارند، می‌توانید یک زیرمنبع مشخص کنید.

برای مثال، Deployment یک زیرمنبع `status` و یک زیرمنبع `scale` دارد؛ بنابراین می‌توانید با `kubectl` فقط زیرمنبع `status` یک Deployment را دریافت یا تغییر دهید.

در ادامه مانیفست یک Deployment با دو رونوشت آمده است:

{{% code_sample file="application/deployment.yaml" %}}

این Deployment را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/deployment.yaml
```

فهرست Podهای مرتبط با Deployment خود را ببینید:

```shell
kubectl get pods -l app=nginx
```

در خروجی می‌بینید که Deployment دو Pod دارد. برای مثال:

```
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-7fb96c846b-22567   1/1     Running   0          47s
nginx-deployment-7fb96c846b-mlgns   1/1     Running   0          47s
```

اکنون آن Deployment را با فلگ `--subresource=[subresource-name]` وصله کنید:

```shell
kubectl patch deployment nginx-deployment --subresource='scale' --type='merge' -p '{"spec":{"replicas":3}}'
```

خروجی به این صورت است:

```shell
scale.autoscaling/nginx-deployment patched
```

فهرست Podهای مرتبط با Deployment وصله‌شده را ببینید:

```shell
kubectl get pods -l app=nginx
```

در خروجی می‌بینید که یک Pod جدید ایجاد شده است و اکنون ۳ Pod در حال اجرا دارید.

```
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-7fb96c846b-22567   1/1     Running   0          107s
nginx-deployment-7fb96c846b-lxfr2   1/1     Running   0          14s
nginx-deployment-7fb96c846b-mlgns   1/1     Running   0          107s
```

وضعیت Deployment وصله‌شده را مشاهده کنید:

```shell
kubectl get deployment nginx-deployment -o yaml
```

```yaml
...
spec:
  replicas: 3
  ...
status:
  ...
  availableReplicas: 3
  readyReplicas: 3
  replicas: 3
```

{{< note >}}
اگر `kubectl patch` را اجرا کنید و فلگ `--subresource` را برای منبعی مشخص کنید که از آن زیرمنبع خاص پشتیبانی نمی‌کند، سرور API خطای 404 Not Found برمی‌گرداند.
{{< /note >}}

## خلاصه

در این تمرین، با `kubectl patch` پیکربندی زندهٔ یک آبجکت Deployment را تغییر دادید. فایل پیکربندی‌ای را که در ابتدا برای ایجاد آبجکت Deployment استفاده کرده بودید تغییر ندادید. از دیگر فرمان‌های به‌روزرسانی آبجکت‌های API می‌توان به
[kubectl annotate](/docs/reference/generated/kubectl/kubectl-commands/#annotate)،
[kubectl edit](/docs/reference/generated/kubectl/kubectl-commands/#edit)،
[kubectl replace](/docs/reference/generated/kubectl/kubectl-commands/#replace)،
[kubectl scale](/docs/reference/generated/kubectl/kubectl-commands/#scale)
و
[kubectl apply](/docs/reference/generated/kubectl/kubectl-commands/#apply)
اشاره کرد.


{{< note >}}
وصلهٔ ادغام راهبردی برای منابع سفارشی (custom resources) پشتیبانی نمی‌شود.
{{< /note >}}


## {{% heading "whatsnext" %}}


* [مدیریت آبجکت‌های کوبرنتیز](/docs/concepts/overview/working-with-objects/object-management/)
* [مدیریت آبجکت‌های کوبرنتیز با فرمان‌های دستوری](/docs/tasks/manage-kubernetes-objects/imperative-command/)
* [مدیریت دستوری آبجکت‌های کوبرنتیز با فایل‌های پیکربندی](/docs/tasks/manage-kubernetes-objects/imperative-config/)
* [مدیریت اعلانی آبجکت‌های کوبرنتیز با فایل‌های پیکربندی](/docs/tasks/manage-kubernetes-objects/declarative-config/)
