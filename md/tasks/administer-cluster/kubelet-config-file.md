---
reviewers:
- mtaufen
- dawnchen
title: تنظیم پارامترهای kubelet از طریق فایل پیکربندی
content_type: task
weight: 330
---

## {{% heading "prerequisites" %}}

در برخی از مراحل این صفحه از ابزار `jq` استفاده می‌شود. اگر `jq` را ندارید، می‌توانید
آن را از منابع نرم‌افزاری سیستم‌عامل خود نصب کنید یا از
[https://jqlang.github.io/jq/](https://jqlang.github.io/jq/) دریافت کنید.

برخی از مراحل نیز به نصب `curl` نیاز دارند که می‌توان آن را از منابع نرم‌افزاری
سیستم‌عامل نصب کرد.


<!-- overview -->

بخشی از پارامترهای پیکربندی kubelet را می‌توان به‌جای فلگ‌های خط فرمان، از طریق
یک فایل پیکربندی روی دیسک تنظیم کرد.

ارائهٔ پارامترها از طریق فایل پیکربندی روش توصیه‌شده است، زیرا استقرار نودها و
مدیریت پیکربندی را ساده‌تر می‌کند.

<!-- steps -->

## ایجاد فایل پیکربندی

بخشی از پیکربندی kubelet که می‌توان آن را از طریق فایل تنظیم کرد، در ساختار (struct)
[`KubeletConfiguration`](/docs/reference/config-api/kubelet-config.v1beta1/)
تعریف شده است.

فایل پیکربندی باید نمایشی از پارامترهای این ساختار در قالب JSON یا YAML باشد.
مطمئن شوید که kubelet مجوز خواندن این فایل را دارد.

نمونه‌ای از محتوای این فایل در ادامه آمده است:

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
address: "192.168.0.8"
port: 20250
serializeImagePulls: false
evictionHard:
    memory.available:  "100Mi"
    nodefs.available:  "10%"
    nodefs.inodesFree: "5%"
    imagefs.available: "15%"
    imagefs.inodesFree: "5%"
```

در این نمونه، kubelet با تنظیمات زیر پیکربندی شده است:

1. فیلد `address`: ‏kubelet روی نشانی IP ‏`192.168.0.8` سرویس‌دهی می‌کند.
1. فیلد `port`: ‏kubelet روی پورت `20250` سرویس‌دهی می‌کند.
1. فیلد `serializeImagePulls`: دریافت ایمیج‌ها به‌صورت موازی انجام می‌شود.
1. فیلد `evictionHard`: ‏kubelet در هر یک از شرایط زیر Podها را بیرون می‌راند (evict):

   - هنگامی که حافظهٔ در دسترس نود به کمتر از 100MiB برسد.
   - هنگامی که فضای در دسترس فایل‌سیستم اصلی نود کمتر از ۱۰٪ باشد.
   - هنگامی که فضای در دسترس فایل‌سیستم ایمیج‌ها کمتر از ۱۵٪ باشد.
   - هنگامی که بیش از ۹۵٪ از inodeهای فایل‌سیستم اصلی نود در حال استفاده باشند.

{{< note >}}
در این نمونه، اگر مقدار پیش‌فرض تنها یکی از پارامترهای evictionHard را تغییر دهید،
مقادیر پیش‌فرض سایر پارامترها به ارث نمی‌رسند و برابر با صفر قرار می‌گیرند. برای
ارائهٔ مقادیر سفارشی، باید همهٔ مقادیر آستانه را به‌ترتیب مشخص کنید.
به‌عنوان راه دیگر، می‌توانید MergeDefaultEvictionSettings را در فایل پیکربندی kubelet
برابر با true قرار دهید؛ در این صورت اگر پارامتری تغییر کند، سایر پارامترها به‌جای
صفر، مقادیر پیش‌فرض خود را به ارث می‌برند.
{{< /note >}}

فایل‌سیستم `imagefs` فایل‌سیستمی اختیاری است که محیط‌های اجرای کانتینر برای ذخیرهٔ
ایمیج‌های کانتینر و لایه‌های قابل‌نوشتن کانتینرها از آن استفاده می‌کنند.

## اجرای فرایند kubelet با پیکربندی از طریق فایل

{{< note >}}
اگر برای راه‌اندازی کلاستر خود از kubeadm استفاده می‌کنید، هنگام ایجاد کلاستر با `kubeadm init` از kubelet-config استفاده کنید.
برای جزئیات بیشتر، [پیکربندی kubelet با استفاده از kubeadm](/docs/setup/production-environment/tools/kubeadm/kubelet-integration/) را ببینید.
{{< /note >}}

kubelet را با فلگ `--config` اجرا کنید و مقدار آن را برابر با مسیر فایل پیکربندی kubelet قرار دهید.
در این صورت kubelet پیکربندی خود را از این فایل بارگذاری می‌کند.

توجه کنید که فلگ‌های خط فرمانی که همان مقدارِ فایل پیکربندی را هدف می‌گیرند، آن مقدار را بازنویسی می‌کنند.
این کار به حفظ سازگاری با نسخه‌های پیشین API خط فرمان کمک می‌کند.

همچنین مسیرهای نسبی در فایل پیکربندی kubelet نسبت به محل همان فایل پیکربندی
تفسیر می‌شوند، در حالی که مسیرهای نسبی در فلگ‌های خط فرمان نسبت به پوشهٔ کاری
فعلی kubelet تفسیر می‌شوند.

افزون بر این، برخی از مقادیر پیش‌فرض در فلگ‌های خط فرمان و فایل پیکربندی kubelet با هم متفاوت‌اند.
اگر `--config` ارائه شده باشد و مقادیر از طریق خط فرمان مشخص نشده باشند،
مقادیر پیش‌فرضِ نسخهٔ `KubeletConfiguration` اعمال می‌شوند.
در نمونهٔ بالا، این نسخه `kubelet.config.k8s.io/v1beta1` است.

## پوشهٔ drop-in برای فایل‌های پیکربندی kubelet {#kubelet-conf-d}

می‌توانید یک پوشهٔ پیکربندی drop-in برای kubelet مشخص کنید. به‌طور پیش‌فرض، kubelet
در هیچ مسیری به دنبال فایل‌های پیکربندی drop-in نمی‌گردد و شما باید مسیری را مشخص کنید.
برای مثال: `--config-dir=/etc/kubernetes/kubelet.conf.d`

در کوبرنتیز نسخهٔ v1.28 تا v1.29، تنها در صورتی می‌توانید `--config-dir` را مشخص کنید
که متغیر محیطی `KUBELET_CONFIG_DROPIN_DIR_ALPHA` را نیز برای فرایند kubelet تنظیم کرده باشید
(مقدار این متغیر اهمیتی ندارد).

{{< note >}}
پسوند یک فایل پیکربندی drop-in معتبر برای kubelet **باید** `.conf` باشد. برای نمونه: `99-kubelet-address.conf`
{{< /note >}}

kubelet فایل‌های موجود در پوشهٔ drop-in پیکربندی خود را با مرتب‌سازی الفبایی-عددی **کل نام فایل** پردازش می‌کند.
برای نمونه، ابتدا `00-kubelet.conf` پردازش می‌شود و سپس فایلی با نام `01-kubelet.conf` آن را بازنویسی می‌کند.

این فایل‌ها می‌توانند پیکربندی‌های ناقص داشته باشند، اما نباید نامعتبر باشند و باید فراداده‌های نوع، به‌ویژه `apiVersion` و `kind`، را در بر داشته باشند.
اعتبارسنجی تنها روی ساختار پیکربندی نهایی‌ای انجام می‌شود که به‌صورت داخلی در kubelet ذخیره شده است.
این رویکرد انعطاف‌پذیری لازم را برای مدیریت و ادغام پیکربندی‌های kubelet از منابع مختلف فراهم می‌کند و در عین حال از پیکربندی‌های نامطلوب جلوگیری می‌کند.
با این حال، باید توجه داشت که رفتار ادغام بسته به نوع دادهٔ فیلدهای پیکربندی متفاوت است.

انواع دادهٔ مختلف در ساختار پیکربندی kubelet به شکل‌های متفاوتی ادغام می‌شوند. برای اطلاعات بیشتر،
[سند مرجع](/docs/reference/node/kubelet-config-directory-merging/)
را ببینید.

### ترتیب ادغام پیکربندی kubelet

kubelet هنگام راه‌اندازی، پیکربندی را از منابع زیر ادغام می‌کند:

* feature gateهایی که از طریق خط فرمان مشخص شده‌اند (کمترین اولویت).
* پیکربندی kubelet.
* فایل‌های پیکربندی drop-in، به ترتیب مرتب‌سازی.
* آرگومان‌های خط فرمان به‌جز feature gateها (بیشترین اولویت).

{{< note >}}
سازوکار پوشهٔ drop-in پیکربندی kubelet شبیه روشی است که ابزار `kubeadm` برای وصله‌کردن (patch) پیکربندی فراهم می‌کند، اما با آن تفاوت دارد.
ابزار `kubeadm` برای پیکربندی خود از یک [راهبرد وصله‌گذاری](/docs/setup/production-environment/tools/kubeadm/control-plane-flags/#patches) مشخص
استفاده می‌کند، در حالی که تنها راهبرد وصله‌گذاری برای فایل‌های drop-in پیکربندی kubelet، راهبرد `replace` است.
kubelet ترتیب ادغام‌ها را بر اساس مرتب‌سازی الفبایی-عددی **پسوندها** تعیین می‌کند
و هر فیلدی را که در فایلی با اولویت بالاتر وجود داشته باشد، جایگزین می‌کند.
{{< /note >}}

## مشاهدهٔ پیکربندی kubelet

از آنجا که با این قابلیت ممکن است پیکربندی در چندین فایل پراکنده باشد، اگر کسی بخواهد
پیکربندی نهایی اعمال‌شده را بررسی کند، می‌تواند مراحل زیر را برای بررسی پیکربندی kubelet دنبال کند:

1. با استفاده از [`kubectl proxy`](/docs/reference/kubectl/generated/kubectl_proxy/) یک سرور پراکسی را در ترمینال خود اجرا کنید.

   ```bash
   kubectl proxy
   ```

   خروجی آن چیزی شبیه به این است:

   ```none
   Starting to serve on 127.0.0.1:8001
   ```

1. پنجرهٔ ترمینال دیگری باز کنید و با استفاده از `curl` پیکربندی kubelet را دریافت کنید.
   به‌جای `<node-name>` نام واقعی نود خود را قرار دهید:

   ```bash
   curl -X GET http://127.0.0.1:8001/api/v1/nodes/<node-name>/proxy/configz | jq .
   ```

   ```json
   {
     "kubeletconfig": {
       "enableServer": true,
       "staticPodPath": "/var/run/kubernetes/static-pods",
       "syncFrequency": "1m0s",
       "fileCheckFrequency": "20s",
       "httpCheckFrequency": "20s",
       "address": "192.168.1.16",
       "port": 10250,
       "readOnlyPort": 10255,
       "tlsCertFile": "/var/lib/kubelet/pki/kubelet.crt",
       "tlsPrivateKeyFile": "/var/lib/kubelet/pki/kubelet.key",
       "rotateCertificates": true,
       "authentication": {
         "x509": {
           "clientCAFile": "/var/run/kubernetes/client-ca.crt"
         },
         "webhook": {
           "enabled": true,
           "cacheTTL": "2m0s"
         },
         "anonymous": {
           "enabled": true
         }
       },
       "authorization": {
         "mode": "AlwaysAllow",
         "webhook": {
           "cacheAuthorizedTTL": "5m0s",
           "cacheUnauthorizedTTL": "30s"
         }
       },
       "registryPullQPS": 5,
       "registryBurst": 10,
       "eventRecordQPS": 50,
       "eventBurst": 100,
       "enableDebuggingHandlers": true,
       "healthzPort": 10248,
       "healthzBindAddress": "127.0.0.1",
       "oomScoreAdj": -999,
       "clusterDomain": "cluster.local",
       "clusterDNS": [
         "10.0.0.10"
       ],
       "streamingConnectionIdleTimeout": "4h0m0s",
       "nodeStatusUpdateFrequency": "10s",
       "nodeStatusReportFrequency": "5m0s",
       "nodeLeaseDurationSeconds": 40,
       "imageMinimumGCAge": "2m0s",
       "imageMaximumGCAge": "0s",
       "imageGCHighThresholdPercent": 85,
       "imageGCLowThresholdPercent": 80,
       "volumeStatsAggPeriod": "1m0s",
       "cgroupsPerQOS": true,
       "cgroupDriver": "systemd",
       "cpuManagerPolicy": "none",
       "cpuManagerReconcilePeriod": "10s",
       "memoryManagerPolicy": "None",
       "topologyManagerPolicy": "none",
       "topologyManagerScope": "container",
       "runtimeRequestTimeout": "2m0s",
       "hairpinMode": "promiscuous-bridge",
       "maxPods": 110,
       "podPidsLimit": -1,
       "resolvConf": "/run/systemd/resolve/resolv.conf",
       "cpuCFSQuota": true,
       "cpuCFSQuotaPeriod": "100ms",
       "nodeStatusMaxImages": 50,
       "maxOpenFiles": 1000000,
       "contentType": "application/vnd.kubernetes.protobuf",
       "kubeAPIQPS": 50,
       "kubeAPIBurst": 100,
       "serializeImagePulls": true,
       "evictionHard": {
         "imagefs.available": "15%",
         "memory.available": "100Mi",
         "nodefs.available": "10%",
         "nodefs.inodesFree": "5%",
         "imagefs.inodesFree": "5%"
       },
       "evictionPressureTransitionPeriod": "1m0s",
       "mergeDefaultEvictionSettings": false,
       "enableControllerAttachDetach": true,
       "makeIPTablesUtilChains": true,
       "iptablesMasqueradeBit": 14,
       "iptablesDropBit": 15,
       "featureGates": {
         "AllAlpha": false
       },
       "failSwapOn": false,
       "memorySwap": {},
       "containerLogMaxSize": "10Mi",
       "containerLogMaxFiles": 5,
       "configMapAndSecretChangeDetectionStrategy": "Watch",
       "enforceNodeAllocatable": [
         "pods"
       ],
       "volumePluginDir": "/usr/libexec/kubernetes/kubelet-plugins/volume/exec/",
       "logging": {
         "format": "text",
         "flushFrequency": "5s",
         "verbosity": 3,
         "options": {
           "json": {
             "infoBufferSize": "0"
           }
         }
       },
       "enableSystemLogHandler": true,
       "enableSystemLogQuery": false,
       "shutdownGracePeriod": "0s",
       "shutdownGracePeriodCriticalPods": "0s",
       "enableProfilingHandler": true,
       "enableDebugFlagsHandler": true,
       "seccompDefault": false,
       "registerNode": true,
       "localStorageCapacityIsolation": true,
       "containerRuntimeEndpoint": "unix:///var/run/crio/crio.sock"
     }
   }
   ```

<!-- discussion -->

## {{% heading "whatsnext" %}}

- برای آشنایی بیشتر با پیکربندی kubelet، مرجع
  [`KubeletConfiguration`](/docs/reference/config-api/kubelet-config.v1beta1/)
  را ببینید.
- برای آشنایی بیشتر با ادغام پیکربندی kubelet،
  [سند مرجع](/docs/reference/node/kubelet-config-directory-merging) را ببینید.
