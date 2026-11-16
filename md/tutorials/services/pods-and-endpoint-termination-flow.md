---
title: بررسی رفتار خاتمه‌یافتن Podها و endpointهای آن‌ها
content_type: tutorial
weight: 60
---


<!-- overview -->

پس از آنکه برنامهٔ خود را با دنبال‌کردن مراحلی مانند آنچه در [اتصال برنامه‌ها به Serviceها](/docs/tutorials/services/connect-applications-service/) آمده است به یک Service متصل کردید، برنامه‌ای تکثیرشده دارید که پیوسته در حال اجراست و روی شبکه در دسترس قرار گرفته است. این آموزش به شما کمک می‌کند روند خاتمه‌یافتن Podها را بررسی کنید و روش‌هایی را برای پیاده‌سازی تخلیهٔ تدریجی و آرام اتصال‌ها (graceful connection draining) بشناسید.

<!-- body -->

## فرایند خاتمه‌یافتن Podها و endpointهای آن‌ها

اغلب موقعیت‌هایی پیش می‌آید که باید یک Pod را خاتمه دهید؛ چه برای ارتقا و چه برای کاهش مقیاس. برای بهبود دسترس‌پذیری برنامه، ممکن است پیاده‌سازی یک سازوکار مناسب برای تخلیهٔ اتصال‌های فعال اهمیت داشته باشد.

این آموزش روند خاتمه‌یافتن Pod را در ارتباط با وضعیت endpoint متناظر با آن و حذف آن توضیح می‌دهد و برای نمایش این مفهوم از یک وب‌سرور ساده nginx استفاده می‌کند.

<!-- body -->

## نمونه‌ای از روند خاتمه‌یافتن endpoint

آنچه در ادامه می‌آید نمونه‌ای از روندی است که در سند [خاتمه‌یافتن Podها](/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) شرح داده شده است.

فرض کنید یک Deployment با تنها یک رونوشت `nginx` (صرفاً برای اهداف نمایشی) و یک Service دارید:

{{% code_sample file="service/pod-with-graceful-termination.yaml" %}}

{{% code_sample file="service/explore-graceful-termination-nginx.yaml" %}}

اکنون با استفاده از فایل‌های بالا، Pod مربوط به Deployment و Service را ایجاد کنید:

```shell
kubectl apply -f pod-with-graceful-termination.yaml
kubectl apply -f explore-graceful-termination-nginx.yaml
```

پس از آنکه Pod و Service در حال اجرا قرار گرفتند، می‌توانید نام EndpointSliceهای مرتبط را به دست آورید:

```shell
kubectl get endpointslice
```

خروجی مشابه زیر است:

```none
NAME                  ADDRESSTYPE   PORTS   ENDPOINTS                 AGE
nginx-service-6tjbr   IPv4          80      10.12.1.199,10.12.1.201   22m
```

می‌توانید وضعیت آن را ببینید و تأیید کنید که یک endpoint ثبت شده است:

```shell
kubectl get endpointslices -o json -l kubernetes.io/service-name=nginx-service
```

خروجی مشابه زیر است:

```none
{
    "addressType": "IPv4",
    "apiVersion": "discovery.k8s.io/v1",
    "endpoints": [
        {
            "addresses": [
                "10.12.1.201"
            ],
            "conditions": {
                "ready": true,
                "serving": true,
                "terminating": false
```

اکنون Pod را خاتمه دهید و تأیید کنید که خاتمه‌یافتن آن با رعایت پیکربندی دورهٔ خاتمهٔ آرام (graceful termination period) انجام می‌شود:

```shell
kubectl delete pod nginx-deployment-7768647bf9-b4b9s
```

همهٔ Podها:

```shell
kubectl get pods
```

خروجی مشابه زیر است:

```none
NAME                                READY   STATUS        RESTARTS      AGE
nginx-deployment-7768647bf9-b4b9s   1/1     Terminating   0             4m1s
nginx-deployment-7768647bf9-rkxlw   1/1     Running       0             8s
```

می‌بینید که Pod جدید زمان‌بندی شده است.

در حالی که endpoint جدید برای Pod جدید در حال ایجاد است، endpoint قدیمی همچنان در وضعیت خاتمه‌یافتن باقی می‌ماند:

```shell
kubectl get endpointslice -o json nginx-service-6tjbr
```

خروجی مشابه زیر است:

```none
{
    "addressType": "IPv4",
    "apiVersion": "discovery.k8s.io/v1",
    "endpoints": [
        {
            "addresses": [
                "10.12.1.201"
            ],
            "conditions": {
                "ready": false,
                "serving": true,
                "terminating": true
            },
            "nodeName": "gke-main-default-pool-dca1511c-d17b",
            "targetRef": {
                "kind": "Pod",
                "name": "nginx-deployment-7768647bf9-b4b9s",
                "namespace": "default",
                "uid": "66fa831c-7eb2-407f-bd2c-f96dfe841478"
            },
            "zone": "us-central1-c"
        },
        {
            "addresses": [
                "10.12.1.202"
            ],
            "conditions": {
                "ready": true,
                "serving": true,
                "terminating": false
            },
            "nodeName": "gke-main-default-pool-dca1511c-d17b",
            "targetRef": {
                "kind": "Pod",
                "name": "nginx-deployment-7768647bf9-rkxlw",
                "namespace": "default",
                "uid": "722b1cbe-dcd7-4ed4-8928-4a4d0e2bbe35"
            },
            "zone": "us-central1-c"
```

به این ترتیب، برنامه‌ها می‌توانند وضعیت خود را در هنگام خاتمه‌یافتن اعلام کنند و کلاینت‌ها (مانند متعادل‌کننده‌های بار) می‌توانند قابلیت تخلیهٔ اتصال‌ها را پیاده‌سازی کنند. این کلاینت‌ها می‌توانند endpointهای در حال خاتمه را تشخیص دهند و منطق ویژه‌ای برای آن‌ها به کار ببرند.

در کوبرنتیز، وضعیت `ready` برای endpointهای در حال خاتمه همیشه `false` تنظیم می‌شود. این کار برای حفظ سازگاری با نسخه‌های پیشین لازم است تا متعادل‌کننده‌های بار موجود از این endpointها برای ترافیک عادی استفاده نکنند. اگر به تخلیهٔ ترافیک از Pod در حال خاتمه نیاز باشد، آمادگی واقعی را می‌توان از طریق وضعیت `serving` بررسی کرد.

با حذف Pod، endpoint قدیمی نیز حذف می‌شود.


## {{% heading "whatsnext" %}}


* با نحوهٔ [اتصال برنامه‌ها به Serviceها](/docs/tutorials/services/connect-applications-service/) آشنا شوید
* دربارهٔ [استفاده از یک Service برای دسترسی به برنامه در کلاستر](/docs/tasks/access-application-cluster/service-access-application-cluster/) بیشتر بیاموزید
* دربارهٔ [اتصال یک فرانت‌اند به یک بک‌اند با استفاده از Service](/docs/tasks/access-application-cluster/connecting-frontend-backend/) بیشتر بیاموزید
* دربارهٔ [ایجاد یک متعادل‌کنندهٔ بار خارجی](/docs/tasks/access-application-cluster/create-external-load-balancer/) بیشتر بیاموزید
