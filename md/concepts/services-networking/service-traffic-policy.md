---
reviewers:
- maplain
title: سیاست ترافیک داخلی Service
content_type: concept
weight: 120
description: >-
  اگر دو Pod در کلاستر شما بخواهند با یکدیگر ارتباط برقرار کنند و هر دو Pod در واقع روی
  یک نود اجرا شوند، از _سیاست ترافیک داخلی Service_ استفاده کنید تا ترافیک شبکه درون همان نود باقی بماند.
  پرهیز از رفت‌وبرگشت از طریق شبکهٔ کلاستر می‌تواند به قابلیت اطمینان، کارایی
  (تأخیر و توان عملیاتی شبکه) یا کاهش هزینه کمک کند.
---


<!-- overview -->

{{< feature-state for_k8s_version="v1.26" state="stable" >}}

_سیاست ترافیک داخلی Service_ محدودیت‌هایی بر ترافیک داخلی اعمال می‌کند تا ترافیک داخلی
تنها به endpointهایی درون نودی هدایت شود که ترافیک از آن سرچشمه گرفته است. منظور از
ترافیک «داخلی» در اینجا، ترافیکی است که از Podهای کلاستر فعلی سرچشمه می‌گیرد.
این کار می‌تواند به کاهش هزینه‌ها و بهبود کارایی کمک کند.

<!-- body -->

## استفاده از سیاست ترافیک داخلی Service

می‌توانید سیاست ترافیکِ فقط‌داخلی را برای یک
{{< glossary_tooltip text="Service" term_id="service" >}} با تنظیم
`.spec.internalTrafficPolicy` آن روی `Local` فعال کنید. این کار به kube-proxy می‌گوید که برای ترافیک داخلی کلاستر
تنها از endpointهای محلیِ نود استفاده کند.

{{< note >}}
برای Podهایی که روی نودهای بدون endpoint برای یک Service مشخص قرار دارند، آن Service
طوری رفتار می‌کند که گویی هیچ endpointی ندارد (برای Podهای این نود)، حتی اگر سرویس
روی نودهای دیگر endpoint داشته باشد.
{{< /note >}}

نمونهٔ زیر نشان می‌دهد که یک Service هنگامی که
`.spec.internalTrafficPolicy` آن را روی `Local` تنظیم می‌کنید، چگونه به نظر می‌رسد:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
  internalTrafficPolicy: Local
```

## نحوهٔ کارکرد

kube-proxy، endpointهایی را که ترافیک را به آن‌ها هدایت می‌کند، بر اساس
تنظیم `spec.internalTrafficPolicy` فیلتر می‌کند. هنگامی که این تنظیم روی `Local` باشد، تنها endpointهای
محلیِ نود در نظر گرفته می‌شوند. هنگامی که روی `Cluster` (مقدار پیش‌فرض) باشد یا تنظیم نشده باشد،
کوبرنتیز همهٔ endpointها را در نظر می‌گیرد.

## {{% heading "whatsnext" %}}

* دربارهٔ [مسیریابی آگاه از توپولوژی](/docs/concepts/services-networking/topology-aware-routing) بخوانید
* دربارهٔ [سیاست ترافیک خارجی Service](/docs/tasks/access-application-cluster/create-external-load-balancer/#preserving-the-client-source-ip) بخوانید
* آموزش [اتصال برنامه‌ها با Serviceها](/docs/tutorials/services/connect-applications-service/) را دنبال کنید
