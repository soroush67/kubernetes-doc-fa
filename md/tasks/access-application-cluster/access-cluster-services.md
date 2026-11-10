---
title: دسترسی به سرویس‌های در حال اجرا روی کلاسترها
content_type: task
weight: 140
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه به سرویس‌های در حال اجرا روی کلاستر کوبرنتیز متصل شوید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

## دسترسی به سرویس‌های در حال اجرا روی کلاستر

در کوبرنتیز، [نودها](/docs/concepts/architecture/nodes/)،
[پادها](/docs/concepts/workloads/pods/) و [سرویس‌ها](/docs/concepts/services-networking/service/) همگی
IP مخصوص به خود را دارند. در بسیاری از موارد، IPهای نودها، IPهای پادها و برخی از IPهای سرویس‌ها در یک کلاستر
قابل مسیریابی (routable) نیستند؛ بنابراین از ماشینی خارج از کلاستر، مانند رایانهٔ رومیزی شما، نمی‌توان به آن‌ها دسترسی داشت.

### روش‌های اتصال

برای اتصال به نودها، پادها و سرویس‌ها از بیرون کلاستر چند گزینه در اختیار دارید:

- دسترسی به سرویس‌ها از طریق IPهای عمومی.
  - از سرویسی با نوع `NodePort` یا `LoadBalancer` استفاده کنید تا سرویس از بیرون کلاستر
    در دسترس باشد. مستندات [سرویس‌ها](/docs/concepts/services-networking/service/) و
    [kubectl expose](/docs/reference/generated/kubectl/kubectl-commands/#expose) را ببینید.
  - بسته به محیط کلاستر شما، ممکن است این کار سرویس را فقط در معرض شبکهٔ سازمانی شما قرار دهد
    یا آن را در اینترنت در دسترس کند. بررسی کنید که آیا سرویسی که در معرض دسترسی قرار می‌گیرد امن است یا نه.
    آیا این سرویس احراز هویت را خودش انجام می‌دهد؟
  - پادها را پشت سرویس‌ها قرار دهید. برای دسترسی به یک پاد مشخص از میان مجموعه‌ای از رونوشت‌ها (replicas)، مثلاً برای اشکال‌زدایی،
    یک برچسب یکتا روی آن پاد قرار دهید و سرویس جدیدی بسازید که این برچسب را انتخاب کند.
  - در بیشتر موارد، لازم نیست توسعه‌دهندهٔ برنامه مستقیماً از طریق
    IP نودها (nodeIP) به نودها دسترسی داشته باشد.
- دسترسی به سرویس‌ها، نودها یا پادها با استفاده از Proxy Verb.
  - پیش از دسترسی به سرویس راه دور، احراز هویت و مجوزدهی را از طریق apiserver انجام می‌دهد.
    اگر سرویس‌ها برای قرار گرفتن در معرض اینترنت به‌اندازهٔ کافی امن نیستند، یا برای دسترسی به
    پورت‌های روی IP نود، یا برای اشکال‌زدایی، از این روش استفاده کنید.
  - پراکسی‌ها ممکن است برای برخی از برنامه‌های وب مشکل ایجاد کنند.
  - فقط برای HTTP/HTTPS کار می‌کند.
  - [اینجا](#manually-constructing-apiserver-proxy-urls) توضیح داده شده است.
- دسترسی از یک نود یا پاد درون کلاستر.
  - یک پاد را اجرا کنید و سپس با استفاده از [kubectl exec](/docs/reference/generated/kubectl/kubectl-commands/#exec) به یک پوسته (shell) درون آن متصل شوید.
    از همان پوسته به نودها، پادها و سرویس‌های دیگر متصل شوید.
  - برخی از کلاسترها ممکن است اجازه دهند با ssh به یکی از نودهای کلاستر وارد شوید. از آنجا ممکن است بتوانید
    به سرویس‌های کلاستر دسترسی داشته باشید. این روش غیراستاندارد است و روی برخی کلاسترها کار می‌کند،
    اما روی برخی دیگر نه. ممکن است مرورگرها و ابزارهای دیگر نصب باشند یا نباشند. ممکن است DNS کلاستر کار نکند.

### کشف سرویس‌های داخلی

معمولاً چند سرویس وجود دارند که kube-system آن‌ها را روی کلاستر راه‌اندازی می‌کند. فهرست این سرویس‌ها را
با دستور `kubectl cluster-info` دریافت کنید:

```shell
kubectl cluster-info
```

خروجی مشابه زیر است:

```
Kubernetes master is running at https://192.0.2.1
elasticsearch-logging is running at https://192.0.2.1/api/v1/namespaces/kube-system/services/elasticsearch-logging/proxy
kibana-logging is running at https://192.0.2.1/api/v1/namespaces/kube-system/services/kibana-logging/proxy
coredns is running at https://192.0.2.1/api/v1/namespaces/kube-system/services/kube-dns/proxy
grafana is running at https://192.0.2.1/api/v1/namespaces/kube-system/services/monitoring-grafana/proxy
heapster is running at https://192.0.2.1/api/v1/namespaces/kube-system/services/monitoring-heapster/proxy
```

این خروجی، URL مربوط به proxy-verb را برای دسترسی به هر سرویس نشان می‌دهد.
برای مثال، در این کلاستر ثبت لاگ در سطح کلاستر (با استفاده از Elasticsearch) فعال است. در صورت ارسال اعتبارنامه‌های مناسب،
می‌توان از نشانی `https://192.0.2.1/api/v1/namespaces/kube-system/services/elasticsearch-logging/proxy/`
به آن دسترسی داشت؛ همچنین می‌توان از طریق kubectl proxy به آن دسترسی پیدا کرد، برای مثال در نشانی
`http://localhost:8080/api/v1/namespaces/kube-system/services/elasticsearch-logging/proxy/`.

{{< note >}}
برای آشنایی با نحوهٔ ارسال اعتبارنامه‌ها یا استفاده از kubectl proxy، صفحهٔ [دسترسی به کلاسترها با استفاده از API کوبرنتیز](/docs/tasks/administer-cluster/access-cluster-api/#accessing-the-kubernetes-api)
را ببینید.
{{< /note >}}

#### ساختن دستی URLهای پراکسی apiserver

همان‌طور که در بالا اشاره شد، برای دریافت URL پراکسی سرویس از دستور `kubectl cluster-info` استفاده می‌کنید. برای ساختن
URLهای پراکسی‌ای که شامل اندپوینت‌ها، پسوندها و پارامترهای سرویس باشند، آن‌ها را به انتهای URL پراکسی سرویس اضافه می‌کنید:
`http://`*`kubernetes_master_address`*`/api/v1/namespaces/`*`namespace_name`*`/services/`*`[https:]service_name[:port_name]`*`/proxy`

اگر برای پورت خود نامی تعیین نکرده‌اید، لازم نیست *port_name* را در URL مشخص کنید. همچنین می‌توانید
برای پورت‌های نام‌دار و بی‌نام، به‌جای *port_name* از شمارهٔ پورت استفاده کنید.

به‌طور پیش‌فرض، سرور API با استفاده از HTTP به سرویس شما پراکسی می‌کند. برای استفاده از HTTPS، پیشوند `https:` را به ابتدای نام سرویس اضافه کنید:
`http://<kubernetes_master_address>/api/v1/namespaces/<namespace_name>/services/<service_name>/proxy`

قالب‌های پشتیبانی‌شده برای بخش `<service_name>` در URL عبارت‌اند از:

* قالب `<service_name>`: با استفاده از http به پورت پیش‌فرض یا پورت بی‌نام پراکسی می‌کند
* قالب `<service_name>:<port_name>`: با استفاده از http به نام پورت یا شمارهٔ پورت مشخص‌شده پراکسی می‌کند
* قالب `https:<service_name>:`: با استفاده از https به پورت پیش‌فرض یا پورت بی‌نام پراکسی می‌کند (به دونقطهٔ انتهایی توجه کنید)
* قالب `https:<service_name>:<port_name>`: با استفاده از https به نام پورت یا شمارهٔ پورت مشخص‌شده پراکسی می‌کند

##### مثال‌ها

* برای دسترسی به اندپوینت `_search?q=user:kimchy` در سرویس Elasticsearch، از نشانی زیر استفاده می‌کنید:

  ```
  http://192.0.2.1/api/v1/namespaces/kube-system/services/elasticsearch-logging/proxy/_search?q=user:kimchy
  ```

* برای دسترسی به اطلاعات سلامت کلاستر Elasticsearch با `_cluster/health?pretty=true`، از نشانی زیر استفاده می‌کنید:

  ```
  https://192.0.2.1/api/v1/namespaces/kube-system/services/elasticsearch-logging/proxy/_cluster/health?pretty=true
  ```

  اطلاعات سلامت مشابه زیر است:

  ```json
  {
    "cluster_name" : "kubernetes_logging",
    "status" : "yellow",
    "timed_out" : false,
    "number_of_nodes" : 1,
    "number_of_data_nodes" : 1,
    "active_primary_shards" : 5,
    "active_shards" : 5,
    "relocating_shards" : 0,
    "initializing_shards" : 0,
    "unassigned_shards" : 5
  }
  ```

* برای دسترسی به اطلاعات سلامت سرویس *https* در Elasticsearch با `_cluster/health?pretty=true`، از نشانی زیر استفاده می‌کنید:

  ```
  https://192.0.2.1/api/v1/namespaces/kube-system/services/https:elasticsearch-logging:/proxy/_cluster/health?pretty=true
  ```

#### استفاده از مرورگرهای وب برای دسترسی به سرویس‌های در حال اجرا روی کلاستر

ممکن است بتوانید URL پراکسی apiserver را در نوار نشانی مرورگر وارد کنید. با این حال:

- مرورگرهای وب معمولاً نمی‌توانند توکن ارسال کنند؛ بنابراین ممکن است لازم باشد از احراز هویت پایه (با گذرواژه) استفاده کنید.
  می‌توان apiserver را طوری پیکربندی کرد که احراز هویت پایه را بپذیرد،
  اما ممکن است کلاستر شما برای پذیرش احراز هویت پایه پیکربندی نشده باشد.
- ممکن است برخی از برنامه‌های وب کار نکنند؛ به‌ویژه برنامه‌هایی که جاوااسکریپت سمت کلاینت دارند و URLها را
  بدون آگاهی از پیشوند مسیر پراکسی می‌سازند.
