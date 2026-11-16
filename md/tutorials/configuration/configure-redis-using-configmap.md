---
reviewers:
- eparis
- pmorie
title: پیکربندی Redis با استفاده از یک ConfigMap
content_type: tutorial
weight: 30
---

<!-- overview -->

این صفحه نمونه‌ای واقعی از پیکربندی Redis با استفاده از یک ConfigMap ارائه می‌دهد و بر پایهٔ وظیفهٔ [پیکربندی یک Pod برای استفاده از ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/) بنا شده است.



## {{% heading "objectives" %}}


* یک ConfigMap حاوی مقادیر پیکربندی Redis ایجاد کنید.
* یک Pod مربوط به Redis ایجاد کنید که ConfigMap ایجادشده را mount کند و از آن استفاده کند.
* بررسی کنید که پیکربندی به‌درستی اعمال شده باشد.



## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

* مثالی که در این صفحه نشان داده شده است با `kubectl` نسخهٔ 1.14 و بالاتر کار می‌کند.
* با [پیکربندی یک Pod برای استفاده از ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/) آشنا باشید.



<!-- lessoncontent -->


## مثال واقعی: پیکربندی Redis با استفاده از یک ConfigMap

برای پیکربندی یک حافظهٔ نهان (cache) مربوط به Redis با استفاده از داده‌های ذخیره‌شده در یک ConfigMap، مراحل زیر را دنبال کنید.

ابتدا یک ConfigMap با یک بلوک پیکربندی خالی ایجاد کنید:

```shell
cat <<EOF >./example-redis-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: example-redis-config
data:
  redis-config: ""
EOF
```

ConfigMap ایجادشده در بالا را به همراه مانیفست یک Pod مربوط به Redis اعمال کنید:

```shell
kubectl apply -f example-redis-config.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/config/redis-pod.yaml
```

محتوای مانیفست Pod مربوط به Redis را بررسی کنید و به نکات زیر توجه کنید:

* یک حجم (volume) با نام `config` به‌وسیلهٔ `spec.volumes[1]` ایجاد می‌شود.
* فیلدهای `key` و `path` در زیر `spec.volumes[1].configMap.items[0]`، کلید `redis-config` از
  ConfigMap با نام `example-redis-config` را به‌صورت فایلی با نام `redis.conf` روی حجم `config` در دسترس قرار می‌دهند.
* سپس حجم `config` به‌وسیلهٔ `spec.containers[0].volumeMounts[1]` در مسیر `/redis-master` mount می‌شود.

نتیجهٔ نهایی این است که داده‌های موجود در `data.redis-config` از ConfigMap با نام `example-redis-config`
در بالا، به‌صورت `/redis-master/redis.conf` درون Pod در دسترس قرار می‌گیرند.

{{% code_sample file="pods/config/redis-pod.yaml" %}}

آبجکت‌های ایجادشده را بررسی کنید:

```shell
kubectl get pod/redis configmap/example-redis-config 
```

باید خروجی زیر را ببینید:

```
NAME        READY   STATUS    RESTARTS   AGE
pod/redis   1/1     Running   0          8s

NAME                             DATA   AGE
configmap/example-redis-config   1      14s
```

به یاد داشته باشید که کلید `redis-config` را در ConfigMap با نام `example-redis-config` خالی گذاشتیم:

```shell
kubectl describe configmap/example-redis-config
```

باید یک کلید `redis-config` خالی ببینید:

```shell
Name:         example-redis-config
Namespace:    default
Labels:       <none>
Annotations:  <none>

Data
====
redis-config:
```

با استفاده از `kubectl exec` وارد Pod شوید و ابزار `redis-cli` را اجرا کنید تا پیکربندی فعلی را بررسی کنید:

```shell
kubectl exec -it pod/redis -- redis-cli
```

مقدار `maxmemory` را بررسی کنید:

```shell
127.0.0.1:6379> CONFIG GET maxmemory
```

خروجی باید مقدار پیش‌فرض 0 را نشان دهد:

```shell
1) "maxmemory"
2) "0"
```

به همین ترتیب، مقدار `maxmemory-policy` را بررسی کنید:

```shell
127.0.0.1:6379> CONFIG GET maxmemory-policy
```

این دستور نیز باید مقدار پیش‌فرض آن، یعنی `noeviction`، را برگرداند:

```shell
1) "maxmemory-policy"
2) "noeviction"
```

اکنون چند مقدار پیکربندی به ConfigMap با نام `example-redis-config` اضافه می‌کنیم:

{{% code_sample file="pods/config/example-redis-config.yaml" %}}

ConfigMap به‌روزشده را اعمال کنید:

```shell
kubectl apply -f example-redis-config.yaml
```

تأیید کنید که ConfigMap به‌روز شده است:

```shell
kubectl describe configmap/example-redis-config
```

باید مقادیر پیکربندی‌ای را که همین حالا اضافه کردیم ببینید:

```shell
Name:         example-redis-config
Namespace:    default
Labels:       <none>
Annotations:  <none>

Data
====
redis-config:
----
maxmemory 2mb
maxmemory-policy allkeys-lru
```

دوباره با استفاده از `redis-cli` از طریق `kubectl exec`، Pod مربوط به Redis را بررسی کنید تا ببینید آیا پیکربندی اعمال شده است یا نه:

```shell
kubectl exec -it pod/redis -- redis-cli
```

مقدار `maxmemory` را بررسی کنید:

```shell
127.0.0.1:6379> CONFIG GET maxmemory
```

این مقدار همچنان روی مقدار پیش‌فرض 0 باقی مانده است:

```shell
1) "maxmemory"
2) "0"
```

به همین ترتیب، `maxmemory-policy` نیز همچنان روی تنظیم پیش‌فرض `noeviction` باقی مانده است:

```shell
127.0.0.1:6379> CONFIG GET maxmemory-policy
```

خروجی:

```shell
1) "maxmemory-policy"
2) "noeviction"
```

مقادیر پیکربندی تغییر نکرده‌اند، زیرا Pod برای دریافت مقادیر به‌روزشده از ConfigMapهای مرتبط باید
دوباره راه‌اندازی شود. Pod را حذف و دوباره ایجاد می‌کنیم:

```shell
kubectl delete pod redis
kubectl apply -f https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/config/redis-pod.yaml
```

اکنون برای آخرین بار مقادیر پیکربندی را دوباره بررسی کنید:

```shell
kubectl exec -it pod/redis -- redis-cli
```

مقدار `maxmemory` را بررسی کنید:

```shell
127.0.0.1:6379> CONFIG GET maxmemory
```

اکنون باید مقدار به‌روزشدهٔ 2097152 برگردانده شود:

```shell
1) "maxmemory"
2) "2097152"
```

به همین ترتیب، `maxmemory-policy` نیز به‌روز شده است:

```shell
127.0.0.1:6379> CONFIG GET maxmemory-policy
```

اکنون مقدار مطلوب، یعنی `allkeys-lru`، را نشان می‌دهد:

```shell
1) "maxmemory-policy"
2) "allkeys-lru"
```

با حذف منابع ایجادشده، محیط کار خود را پاک‌سازی کنید:

```shell
kubectl delete pod/redis configmap/example-redis-config
```

## {{% heading "whatsnext" %}}


* دربارهٔ [ConfigMapها](/docs/tasks/configure-pod-container/configure-pod-configmap/) بیشتر بیاموزید.
* مثالی از [به‌روزرسانی پیکربندی از طریق یک ConfigMap](/docs/tutorials/configuration/updating-configuration-via-a-configmap/) را دنبال کنید.
