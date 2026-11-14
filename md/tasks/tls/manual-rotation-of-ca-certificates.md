---
title: چرخش دستی گواهی‌های CA
content_type: task
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه گواهی‌های مرجع صدور گواهی (certificate authority یا CA) را به‌صورت دستی بچرخانید (rotate).

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}


- برای اطلاعات بیشتر دربارهٔ احراز هویت در کوبرنتیز، به
  [احراز هویت](/docs/reference/access-authn-authz/authentication) مراجعه کنید.
- برای اطلاعات بیشتر دربارهٔ بهترین شیوه‌های مربوط به گواهی‌های CA، به
  [CA ریشهٔ واحد](/docs/setup/best-practices/certificates/#single-root-ca) مراجعه کنید.

<!-- steps -->

## چرخش دستی گواهی‌های CA

{{< caution >}}
حتماً از دایرکتوری گواهی‌ها، همراه با فایل‌های پیکربندی و هر فایل لازم دیگری، نسخهٔ پشتیبان تهیه کنید.

این روش فرض می‌کند که control plane کوبرنتیز در یک پیکربندی با دسترس‌پذیری بالا (HA) و با چند API server اجرا می‌شود.
همچنین فرض بر این است که API server به‌صورت تدریجی و بی‌خطر (graceful) خاتمه می‌یابد تا کلاینت‌ها بتوانند به‌طور تمیز از یک API server قطع شوند و
به API server دیگری متصل شوند.

در پیکربندی‌هایی که تنها یک API server دارند، هنگام راه‌اندازی مجدد API server، کلاستر در دسترس نخواهد بود.
{{< /caution >}}

1. گواهی‌ها و کلیدهای خصوصی CA جدید (برای نمونه `ca.crt`، `ca.key`، `front-proxy-ca.crt`
   و `front-proxy-ca.key`) را در دایرکتوری گواهی‌های کوبرنتیز روی همهٔ نودهای control plane توزیع کنید.

1. فلگ `--root-ca-file` مربوط به {{< glossary_tooltip term_id="kube-controller-manager" >}} را به‌روزرسانی کنید تا
   هر دو CA قدیمی و جدید را در بر بگیرد، سپس kube-controller-manager را مجدداً راه‌اندازی کنید.

   هر {{< glossary_tooltip text="ServiceAccount" term_id="service-account" >}} که از این مرحله به بعد ایجاد شود،
   Secretهایی دریافت می‌کند که هر دو CA قدیمی و جدید را در بر دارند.

   {{< note >}}
   فایل‌هایی که با فلگ‌های `--client-ca-file` و `--cluster-signing-cert-file` در kube-controller-manager مشخص می‌شوند،
   نمی‌توانند بستهٔ CA (CA bundle) باشند. اگر این فلگ‌ها و `--root-ca-file` به یک فایل `ca.crt` اشاره کنند که اکنون یک
   بسته است (یعنی هر دو CA قدیمی و جدید را در بر دارد)، با خطا مواجه خواهید شد. برای دور زدن این مشکل، می‌توانید CA جدید را
   در فایلی جداگانه کپی کنید و فلگ‌های `--client-ca-file` و `--cluster-signing-cert-file` را به این نسخهٔ کپی ارجاع دهید.
   پس از آنکه `ca.crt` دیگر یک بسته نبود، می‌توانید فلگ‌های مشکل‌دار را دوباره به `ca.crt` ارجاع دهید و نسخهٔ کپی را حذف کنید.

   [مسئلهٔ ۱۳۵۰](https://github.com/kubernetes/kubeadm/issues/1350) در kubeadm، باگی را پیگیری می‌کند که به‌دلیل آن
   kube-controller-manager نمی‌تواند بستهٔ CA را بپذیرد.
   {{< /note >}}

1. صبر کنید تا controller manager مقدار `ca.crt` را در Secretهای حساب‌های سرویس به‌روزرسانی کند تا هر دو گواهی CA قدیمی و جدید را در بر بگیرد.

    اگر Podهایی پیش از آنکه API serverها از CA جدید استفاده کنند راه‌اندازی شوند، این Podهای جدید این به‌روزرسانی را دریافت می‌کنند و به هر دو
    CA قدیمی و جدید اعتماد خواهند کرد.

1. همهٔ Podهایی را که از پیکربندی درون‌کلاستری (in-cluster) استفاده می‌کنند (برای نمونه kube-proxy، CoreDNS و غیره) مجدداً راه‌اندازی کنید تا بتوانند از
   داده‌های به‌روزشدهٔ مرجع صدور گواهی در Secretهای مرتبط با ServiceAccountها استفاده کنند.

   * مطمئن شوید که CoreDNS، kube-proxy و سایر Podهایی که از پیکربندی درون‌کلاستری استفاده می‌کنند، مطابق انتظار کار می‌کنند.

1. هر دو CA قدیمی و جدید را به فایلی که فلگ‌های `--client-ca-file` و `--kubelet-certificate-authority`
   در پیکربندی `kube-apiserver` به آن اشاره می‌کنند، اضافه کنید.

1. هر دو CA قدیمی و جدید را به فایلی که فلگ `--client-ca-file` در پیکربندی `kube-scheduler` به آن اشاره می‌کند، اضافه کنید.

1. گواهی‌های حساب‌های کاربری را با جایگزین کردن محتوای `client-certificate-data` و `client-key-data`
   به‌ترتیب به‌روزرسانی کنید.

   برای اطلاعات دربارهٔ ایجاد گواهی برای حساب‌های کاربری مجزا، به
   [پیکربندی گواهی‌ها برای حساب‌های کاربری](/docs/setup/best-practices/certificates/#configure-certificates-for-user-accounts) مراجعه کنید.

   افزون بر این، بخش `certificate-authority-data` را در فایل‌های kubeconfig،
   به‌ترتیب با داده‌های مرجع صدور گواهی قدیمی و جدید که با Base64 کدگذاری شده‌اند، به‌روزرسانی کنید.

1. فلگ `--root-ca-file` مربوط به {{< glossary_tooltip term_id="cloud-controller-manager" >}} را به‌روزرسانی کنید تا
   هر دو CA قدیمی و جدید را در بر بگیرد، سپس cloud-controller-manager را مجدداً راه‌اندازی کنید.

   {{< note >}}
   اگر کلاستر شما cloud-controller-manager ندارد، می‌توانید از این مرحله صرف‌نظر کنید.
   {{< /note >}}

1. مراحل زیر را به‌صورت تدریجی (rolling) دنبال کنید.

   1. هر
      [API server تجمیعی](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) دیگر یا
      هر کنترل‌کنندهٔ webhook را مجدداً راه‌اندازی کنید تا به گواهی‌های CA جدید اعتماد کنند.

   1. با به‌روزرسانی فایلی که `clientCAFile` در پیکربندی kubelet به آن اشاره می‌کند و همچنین
      `certificate-authority-data` در `kubelet.conf`، kubelet را روی همهٔ نودها مجدداً راه‌اندازی کنید تا از هر دو CA قدیمی و جدید استفاده کند.

      اگر kubelet شما از چرخش گواهی کلاینت استفاده نمی‌کند، `client-certificate-data` و
      `client-key-data` را در `kubelet.conf` روی همهٔ نودها به‌روزرسانی کنید؛ همچنین فایل گواهی کلاینت kubelet را
      که معمولاً در `/var/lib/kubelet/pki` قرار دارد نیز به‌روزرسانی کنید.

   1. API serverها را با گواهی‌هایی (`apiserver.crt`، `apiserver-kubelet-client.crt` و
      `front-proxy-client.crt`) که با CA جدید امضا شده‌اند، مجدداً راه‌اندازی کنید.
      می‌توانید از کلیدهای خصوصی موجود یا کلیدهای خصوصی جدید استفاده کنید.
      اگر کلیدهای خصوصی را تغییر داده‌اید، آن‌ها را نیز در دایرکتوری گواهی‌های کوبرنتیز به‌روزرسانی کنید.

      از آنجا که Podهای کلاستر شما به هر دو CA قدیمی و جدید اعتماد دارند، قطع اتصال کوتاهی رخ می‌دهد
      و پس از آن، کلاینت‌های کوبرنتیز درون Podها دوباره به API server جدید متصل می‌شوند.
      API server جدید از گواهی‌ای استفاده می‌کند که با CA جدید امضا شده است.

      * {{< glossary_tooltip term_id="kube-scheduler" text="kube-scheduler" >}} را مجدداً راه‌اندازی کنید تا از CAهای جدید
        استفاده کند و به آن‌ها اعتماد کند.
      * مطمئن شوید که لاگ‌های مؤلفه‌های control plane هیچ خطای TLS نشان نمی‌دهند.

      {{< note >}}
      برای تولید گواهی‌ها و کلیدهای خصوصی برای کلاستر خود با ابزار خط فرمان `openssl`،
      به [گواهی‌ها (`openssl`)](/docs/tasks/administer-cluster/certificates/#openssl) مراجعه کنید.
      همچنین می‌توانید از [`cfssl`](/docs/tasks/administer-cluster/certificates/#cfssl) استفاده کنید.
      {{< /note >}}

    1. به همهٔ DaemonSetها و Deploymentها حاشیه‌نویسی (annotation) اضافه کنید تا جایگزینی Podها به‌شکلی تدریجی و امن‌تر آغاز شود.

      ```shell
      for namespace in $(kubectl get namespace -o jsonpath='{.items[*].metadata.name}'); do
          for name in $(kubectl get deployments -n $namespace -o jsonpath='{.items[*].metadata.name}'); do
              kubectl patch deployment -n ${namespace} ${name} -p '{"spec":{"template":{"metadata":{"annotations":{"ca-rotation": "1"}}}}}';
          done
          for name in $(kubectl get daemonset -n $namespace -o jsonpath='{.items[*].metadata.name}'); do
              kubectl patch daemonset -n ${namespace} ${name} -p '{"spec":{"template":{"metadata":{"annotations":{"ca-rotation": "1"}}}}}';
          done
      done
      ```

      {{< note >}}
      برای محدود کردن تعداد اختلال‌های هم‌زمانی که برنامهٔ شما تجربه می‌کند،
      به [پیکربندی بودجهٔ اختلال Pod](/docs/tasks/run-application/configure-pdb/) مراجعه کنید.
      {{< /note >}}

        بسته به نحوهٔ استفادهٔ شما از StatefulSetها، ممکن است لازم باشد جایگزینی تدریجی مشابهی را برای آن‌ها نیز انجام دهید.

1. اگر کلاستر شما برای پیوستن نودها از توکن‌های bootstrap استفاده می‌کند، ConfigMap `cluster-info` را در فضای نام (namespace)
   `kube-public` با CA جدید به‌روزرسانی کنید.

   ```shell
   base64_encoded_ca="$(base64 -w0 /etc/kubernetes/pki/ca.crt)"

   kubectl get cm/cluster-info --namespace kube-public -o yaml | \
       /bin/sed "s/\(certificate-authority-data:\).*/\1 ${base64_encoded_ca}/" | \
       kubectl apply -f -
   ```

1. عملکرد کلاستر را بررسی کنید.

    1. لاگ‌های مؤلفه‌های control plane را همراه با لاگ‌های kubelet و kube-proxy بررسی کنید.
       مطمئن شوید که این مؤلفه‌ها هیچ خطای TLS گزارش نمی‌کنند؛ برای جزئیات بیشتر به
       [بررسی لاگ‌ها](/docs/tasks/debug/debug-cluster/#looking-at-logs) مراجعه کنید.

    1. لاگ‌های همهٔ API serverهای تجمیعی و Podهایی را که از پیکربندی درون‌کلاستری استفاده می‌کنند، بررسی کنید.

1. پس از آنکه عملکرد کلاستر با موفقیت تأیید شد:

   1. همهٔ توکن‌های حساب سرویس را به‌روزرسانی کنید تا فقط گواهی CA جدید را در بر بگیرند.

      * همهٔ Podهایی که از kubeconfig درون‌کلاستری استفاده می‌کنند، در نهایت باید مجدداً راه‌اندازی شوند تا Secret جدید را دریافت کنند
        و هیچ Podای به CA قدیمی کلاستر وابسته نماند.

   1. مؤلفه‌های control plane را با حذف CA قدیمی از فایل‌های kubeconfig و از فایل‌هایی که به‌ترتیب فلگ‌های
      `--client-ca-file` و `--root-ca-file` به آن‌ها اشاره می‌کنند، مجدداً راه‌اندازی کنید.

   1. روی هر نود، kubelet را با حذف CA قدیمی از فایلی که فلگ `clientCAFile` به آن اشاره می‌کند
      و از فایل kubeconfig مربوط به kubelet، مجدداً راه‌اندازی کنید. این کار را باید به‌صورت به‌روزرسانی تدریجی انجام دهید.

      اگر کلاستر شما امکان این تغییر را فراهم می‌کند، می‌توانید آن را به‌جای پیکربندی مجدد نودها،
      با جایگزین کردن آن‌ها نیز به‌صورت تدریجی اعمال کنید.
