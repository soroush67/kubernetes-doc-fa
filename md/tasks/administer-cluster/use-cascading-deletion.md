---
title: استفاده از حذف آبشاری در کلاستر
content_type: task
weight: 360
---

<!--overview-->

این صفحه نشان می‌دهد که چگونه می‌توانید نوع
[حذف آبشاری](/docs/concepts/architecture/garbage-collection/#cascading-deletion) (cascading deletion)
را که کلاستر شما هنگام {{<glossary_tooltip text="جمع‌آوری زباله" term_id="garbage-collection">}} به کار می‌برد، مشخص کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

همچنین برای آزمودن انواع مختلف حذف آبشاری، باید [یک Deployment نمونه ایجاد کنید](/docs/tasks/run-application/run-stateless-application-deployment/#creating-and-exploring-an-nginx-deployment).
برای هر نوع حذف باید این Deployment را دوباره ایجاد کنید.

## بررسی ارجاع‌های مالک در پادها

بررسی کنید که فیلد `ownerReferences` در پادهای شما وجود داشته باشد:

```shell 
kubectl get pods -l app=nginx --output=yaml
```

خروجی، فیلد `ownerReferences` را به شکلی مشابه زیر دارد:

```yaml
apiVersion: v1
    ...
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: nginx-deployment-6b474476c4
      uid: 4fdcd81c-bd5d-41f7-97af-3a3b759af9a7
    ...
```

## استفاده از حذف آبشاری پیش‌زمینه {#use-foreground-cascading-deletion}

کوبرنتیز به‌طور پیش‌فرض برای حذف وابسته‌های یک آبجکت از [حذف آبشاری پس‌زمینه](/docs/concepts/architecture/garbage-collection/#background-deletion)
استفاده می‌کند. بسته به نسخه‌ای از کوبرنتیز که کلاستر شما اجرا می‌کند، می‌توانید با `kubectl` یا API کوبرنتیز
به حذف آبشاری پیش‌زمینه (foreground) تغییر وضعیت دهید. {{<version-check>}}


می‌توانید آبجکت‌ها را با استفاده از `kubectl` یا API کوبرنتیز و به روش حذف آبشاری پیش‌زمینه حذف کنید.

**با استفاده از kubectl**

دستور زیر را اجرا کنید:
<!--TODO: verify release after which the --cascade flag is switched to a string in https://github.com/kubernetes/kubectl/commit/fd930e3995957b0093ecc4b9fd8b0525d94d3b4e-->

```shell
kubectl delete deployment nginx-deployment --cascade=foreground
```

**با استفاده از API کوبرنتیز**

1. یک نشست پراکسی محلی را آغاز کنید:

   ```shell
   kubectl proxy --port=8080
   ```

1. با استفاده از `curl` عملیات حذف را آغاز کنید:

   ```shell
   curl -X DELETE localhost:8080/apis/apps/v1/namespaces/default/deployments/nginx-deployment \
       -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Foreground"}' \
       -H "Content-Type: application/json"
   ```

   خروجی، یک {{<glossary_tooltip text="نهایی‌ساز" term_id="finalizer">}} با نام `foregroundDeletion`
   به شکل زیر دارد:

   ```
   "kind": "Deployment",
   "apiVersion": "apps/v1",
   "metadata": {
       "name": "nginx-deployment",
       "namespace": "default",
       "uid": "d1ce1b02-cae8-4288-8a53-30e84d8fa505",
       "resourceVersion": "1363097",
       "creationTimestamp": "2021-07-08T20:24:37Z",
       "deletionTimestamp": "2021-07-08T20:27:39Z",
       "finalizers": [
         "foregroundDeletion"
       ]
       ...
   ```


## استفاده از حذف آبشاری پس‌زمینه {#use-background-cascading-deletion}

1. [یک Deployment نمونه ایجاد کنید](/docs/tasks/run-application/run-stateless-application-deployment/#creating-and-exploring-an-nginx-deployment).
1. بسته به نسخه‌ای از کوبرنتیز که کلاستر شما اجرا می‌کند، با `kubectl` یا API کوبرنتیز
   این Deployment را حذف کنید. {{<version-check>}}


می‌توانید آبجکت‌ها را با استفاده از `kubectl` یا API کوبرنتیز و به روش حذف آبشاری پس‌زمینه حذف کنید.

کوبرنتیز به‌طور پیش‌فرض از حذف آبشاری پس‌زمینه استفاده می‌کند؛ بنابراین حتی اگر دستورهای زیر را
بدون فلگ `--cascade` یا آرگومان `propagationPolicy` اجرا کنید، همین روش به کار می‌رود.

**با استفاده از kubectl**

دستور زیر را اجرا کنید:

```shell
kubectl delete deployment nginx-deployment --cascade=background
```

**با استفاده از API کوبرنتیز**

1. یک نشست پراکسی محلی را آغاز کنید:

   ```shell
   kubectl proxy --port=8080
   ```

1. با استفاده از `curl` عملیات حذف را آغاز کنید:

   ```shell
   curl -X DELETE localhost:8080/apis/apps/v1/namespaces/default/deployments/nginx-deployment \
       -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Background"}' \
       -H "Content-Type: application/json"
   ```

   خروجی مشابه زیر است:

   ```
   "kind": "Status",
   "apiVersion": "v1",
   ...
   "status": "Success",
   "details": {
       "name": "nginx-deployment",
       "group": "apps",
       "kind": "deployments",
       "uid": "cc9eefb9-2d49-4445-b1c1-d261c9396456"
   }
   ```


## حذف آبجکت‌های مالک و یتیم‌کردن وابسته‌ها {#set-orphan-deletion-policy}

به‌طور پیش‌فرض، وقتی از کوبرنتیز می‌خواهید آبجکتی را حذف کند،
{{<glossary_tooltip text="کنترل‌کننده" term_id="controller">}} آبجکت‌های وابسته را نیز حذف می‌کند.
بسته به نسخه‌ای از کوبرنتیز که کلاستر شما اجرا می‌کند، می‌توانید با `kubectl` یا API کوبرنتیز
کاری کنید که کوبرنتیز این وابسته‌ها را *یتیم* (orphan) کند. {{<version-check>}}


**با استفاده از kubectl**

دستور زیر را اجرا کنید:

```shell
kubectl delete deployment nginx-deployment --cascade=orphan
```

**با استفاده از API کوبرنتیز**

1. یک نشست پراکسی محلی را آغاز کنید:

   ```shell
   kubectl proxy --port=8080
   ```

1. با استفاده از `curl` عملیات حذف را آغاز کنید:

   ```shell
   curl -X DELETE localhost:8080/apis/apps/v1/namespaces/default/deployments/nginx-deployment \
       -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Orphan"}' \
       -H "Content-Type: application/json"
   ```

   در خروجی، مقدار `orphan` در فیلد `finalizers` دیده می‌شود؛ مشابه زیر:

   ```
   "kind": "Deployment",
   "apiVersion": "apps/v1",
   "namespace": "default",
   "uid": "6f577034-42a0-479d-be21-78018c466f1f",
   "creationTimestamp": "2021-07-09T16:46:37Z",
   "deletionTimestamp": "2021-07-09T16:47:08Z",
   "deletionGracePeriodSeconds": 0,
   "finalizers": [
     "orphan"
   ],
   ...
   ```


می‌توانید بررسی کنید که Podهایی که این Deployment مدیریت می‌کرد، همچنان در حال اجرا هستند:

```shell
kubectl get pods -l app=nginx
```

## {{% heading "whatsnext" %}}

* دربارهٔ [مالک‌ها و وابسته‌ها](/docs/concepts/overview/working-with-objects/owners-dependents/) در کوبرنتیز بیشتر بدانید.
* دربارهٔ [نهایی‌سازها](/docs/concepts/overview/working-with-objects/finalizers/) در کوبرنتیز بیشتر بدانید.
* دربارهٔ [جمع‌آوری زباله](/docs/concepts/architecture/garbage-collection/) بیشتر بدانید.
