---
content_type: "reference"
title: فایل‌ها و مسیرهای محلی مورد استفاده kubelet
weight: 42
---

مؤلفه {{< glossary_tooltip text="kubelet" term_id="kubelet" >}} در بیشتر موارد فرایندی بدون حالت (stateless) است که روی یک {{< glossary_tooltip text="نود" term_id="node" >}} کوبرنتیز اجرا می‌شود. این سند فایل‌هایی را که kubelet می‌خواند و می‌نویسد، به‌طور کلی معرفی می‌کند.

{{< note >}}

این سند صرفاً جنبه اطلاع‌رسانی دارد و هیچ رفتار یا API تضمین‌شده‌ای را توصیف نمی‌کند. منابعی که در اینجا فهرست شده‌اند و kubelet از آن‌ها استفاده می‌کند، جزئیات پیاده‌سازی هستند و ممکن است در هر انتشار تغییر کنند.

{{< /note >}}

معمولاً kubelet برای دانستن اینکه چه چیزی باید روی نود اجرا شود، {{< glossary_tooltip text="control plane" term_id="control-plane" >}} را مرجع معتبر می‌داند و وضعیت فعلی کانتینرها را از {{<glossary_tooltip text="محیط اجرای کانتینر" term_id="container-runtime">}} دریافت می‌کند. اگر یک _kubeconfig_ (پیکربندی کلاینت API) در اختیار kubelet قرار دهید، kubelet به control plane شما متصل می‌شود؛ در غیر این صورت، نود در _حالت مستقل_ (standalone mode) کار می‌کند.

روی نودهای لینوکسی، kubelet برای جمع‌آوری متریک‌ها به خواندن cgroupها و فایل‌های سیستمی گوناگون نیز متکی است.

روی نودهای ویندوزی، kubelet متریک‌ها را با سازوکار دیگری جمع‌آوری می‌کند که به مسیرها وابسته نیست.

از آنجا که kubelet از طریق سوکت‌های محلی دامنه یونیکس ارتباط برقرار می‌کند، از چند فایل دیگر نیز استفاده می‌کند. kubelet به برخی از این سوکت‌ها گوش می‌دهد و برخی دیگر را شناسایی می‌کند و سپس در نقش کلاینت به آن‌ها متصل می‌شود.

{{< note >}}

در این صفحه، مسیرها به‌صورت مسیرهای لینوکسی آمده‌اند. برای به‌دست‌آوردن مسیر معادل در ویندوز، به‌جای `/` دیسک ریشه `C:\` را قرار دهید (مگر آنکه خلاف آن ذکر شده باشد). برای مثال، مسیر `/var/lib/kubelet/device-plugins` با `C:\var\lib\kubelet\device-plugins` متناظر است.

{{< /note >}}

## پیکربندی

### فایل‌های پیکربندی kubelet

مسیر فایل پیکربندی kubelet را می‌توان با آرگومان خط فرمان `--config` تعیین کرد. افزون بر این، kubelet برای تکمیل پیکربندی از [فایل‌های پیکربندی افزودنی (drop-in)](/docs/tasks/administer-cluster/kubelet-config-file/#kubelet-conf-d) نیز پشتیبانی می‌کند.

### گواهی‌ها

گواهی‌ها و کلیدهای خصوصی معمولاً در `/var/lib/kubelet/pki` قرار دارند، اما می‌توان این مسیر را با آرگومان خط فرمان `--cert-dir` در kubelet تغییر داد. نام فایل‌های گواهی نیز قابل پیکربندی است.

### مانیفست‌ها

مانیفست‌های Podهای ایستا (static) معمولاً در `/etc/kubernetes/manifests` قرار دارند. این مکان را می‌توان با گزینه پیکربندی `staticPodPath` در kubelet تغییر داد.

### تنظیمات واحد systemd

هنگامی که kubelet به‌صورت یک واحد systemd اجرا می‌شود، ممکن است بخشی از پیکربندی آن در فایل تنظیمات واحد systemd تعریف شود. این پیکربندی معمولاً شامل موارد زیر است:

- آرگومان‌های خط فرمان برای [اجرای kubelet](/docs/reference/command-line-tools-reference/kubelet/)
- متغیرهای محیطی که kubelet از آن‌ها استفاده می‌کند یا برای [پیکربندی محیط اجرای golang](https://pkg.go.dev/runtime#hdr-Environment_Variables) به کار می‌روند

## وضعیت

### فایل‌های نقطه وارسی مدیران منابع {#resource-managers-state}

همه مدیران منابع، نگاشت Podها به منابع تخصیص‌یافته را در فایل‌های وضعیت نگه می‌دارند. این فایل‌ها در پوشه پایه kubelet قرار دارند که _پوشه ریشه_ نیز نامیده می‌شود (البته این پوشه با `/`، یعنی پوشه ریشه نود، یکسان نیست). پوشه پایه kubelet را می‌توانید با آرگومان خط فرمان `--root-dir` پیکربندی کنید.

نام فایل‌ها:

- فایل `memory_manager_state` برای [مدیر حافظه](/docs/tasks/administer-cluster/memory-manager/)
- فایل `cpu_manager_state` برای [مدیر CPU](/docs/tasks/administer-cluster/cpu-management-policies/)
- فایل `dra_manager_state` برای [DRA](/docs/concepts/resource-management/dynamic-resource-allocation/)

### فایل نقطه وارسی مدیر دستگاه {#device-manager-state}

مدیر دستگاه، نقطه‌های وارسی (checkpoint) را در همان پوشه فایل‌های سوکت، یعنی `/var/lib/kubelet/device-plugins/`، ایجاد می‌کند. این مسیر در کد ثابت شده است و نسبت به پوشه ریشه kubelet سنجیده نمی‌شود. نام فایل نقطه وارسی برای [مدیر دستگاه](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-integration-with-the-topology-manager)، `kubelet_internal_checkpoint` است.

### نقطه‌های وارسی منابع Pod

{{< feature-state feature_gate_name="InPlacePodVerticalScaling" >}}

اگر [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `InPlacePodVerticalScaling` روی یک نود فعال باشد، kubelet سابقه‌ای محلی از منابع _تخصیص‌یافته_ و _اعمال‌شده_ Podها نگه می‌دارد. برای آشنایی بیشتر با نحوه استفاده از این سوابق، به [تغییر اندازه منابع CPU و حافظه تخصیص‌یافته به کانتینرها](/docs/tasks/configure-pod-container/resize-container-resources/) مراجعه کنید.

نام فایل‌ها:

- فایل `allocated_pods_state` منابع تخصیص‌یافته به هر Pod در حال اجرا روی نود را ثبت می‌کند.
- فایل `actuated_pods_state` منابعی را ثبت می‌کند که محیط اجرا برای هر Pod در حال اجرا روی نود پذیرفته است.

این فایل‌ها در پوشه پایه kubelet قرار دارند (که در لینوکس به‌طور پیش‌فرض `/var/lib/kubelet` است و با `--root-dir` قابل پیکربندی است).

### محیط اجرای کانتینر

مؤلفه kubelet از طریق سوکتی با محیط اجرای کانتینر ارتباط برقرار می‌کند که با این پارامترهای پیکربندی تعیین می‌شود:

- پارامتر `containerRuntimeEndpoint` برای عملیات محیط اجرا
- پارامتر `imageServiceEndpoint` برای عملیات مدیریت ایمیج

مقادیر واقعی این نقطه‌های پایانی به محیط اجرای کانتینر مورد استفاده بستگی دارد.

### افزونه‌های دستگاه

مؤلفه kubelet سوکتی را در مسیر `/var/lib/kubelet/device-plugins/kubelet.sock` در دسترس قرار می‌دهد تا [افزونه‌های دستگاه گوناگون بتوانند خود را ثبت کنند](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-implementation).

هر افزونه دستگاه هنگام ثبت خود، مسیر سوکتش را اعلام می‌کند تا kubelet به آن متصل شود.

سوکت افزونه دستگاه باید در پوشه `/var/lib/kubelet/device-plugins/` قرار داشته باشد. این مسیر در کد ثابت شده است و نسبت به پوشه پایه kubelet (پوشه ریشه) سنجیده نمی‌شود. در لینوکس، این مسیر همیشه `/var/lib/kubelet/device-plugins` است.

### API منابع Pod

[API منابع Pod](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#monitoring-device-plugin-resources) در مسیر `pod-resources` درون پوشه پایه kubelet (پوشه ریشه) در دسترس قرار می‌گیرد. روی یک نود لینوکسی معمولی، این مسیر `/var/lib/kubelet/pod-resources` است.

### افزونه‌های DRA، CSI و افزونه‌های دستگاه

مؤلفه kubelet به‌دنبال فایل‌های سوکتی می‌گردد که افزونه‌های دستگاهِ مدیریت‌شده با [DRA](/docs/concepts/resource-management/dynamic-resource-allocation/) یا مدیر دستگاه، یا افزونه‌های ذخیره‌سازی ایجاد کرده‌اند و سپس تلاش می‌کند به این سوکت‌ها متصل شود. پوشه‌ای که kubelet در آن جست‌وجو می‌کند، `plugins_registry` درون پوشه پایه kubelet است؛ بنابراین روی یک نود لینوکسی معمولی، این مسیر `/var/lib/kubelet/plugins_registry` خواهد بود.

توجه کنید که برای افزونه‌های دستگاه، دو سازوکار ثبت جایگزین وجود دارد و برای هر افزونه باید فقط از یکی از آن‌ها استفاده شود.

انواع افزونه‌هایی که می‌توانند فایل‌های سوکت را در این پوشه قرار دهند، عبارت‌اند از:

- افزونه‌های CSI
- افزونه‌های DRA
- افزونه‌های مدیر دستگاه

(معمولاً `/var/lib/kubelet/plugins_registry`).

### خاموش‌شدن تدریجی نود

{{< feature-state feature_gate_name="GracefulNodeShutdown" >}}

قابلیت [خاموش‌شدن تدریجی نود](/docs/concepts/cluster-administration/node-shutdown/#graceful-node-shutdown) وضعیت خود را به‌صورت محلی در `/var/lib/kubelet/graceful_node_shutdown_state` ذخیره می‌کند.

### سوابق دریافت ایمیج

{{< feature-state feature_gate_name="KubeletEnsureSecretPulledImages" >}}

مؤلفه kubelet سوابق تلاش‌ها و موفقیت‌های دریافت ایمیج را ذخیره می‌کند و با استفاده از آن‌ها بررسی می‌کند که ایمیج قبلاً با همان اعتبارنامه‌ها با موفقیت دریافت شده باشد.

این سوابق به‌صورت فایل در پوشه `image_registry` درون پوشه پایه kubelet ذخیره می‌شوند. روی یک نود لینوکسی معمولی، این مسیر `/var/lib/kubelet/image_manager` است. پوشه `image_manager` دو زیرپوشه دارد:
* پوشه `pulling`: سوابق ایمیج‌هایی را نگه می‌دارد که kubelet در تلاش برای دریافت آن‌هاست.
* پوشه `pulled`: سوابق ایمیج‌هایی را که kubelet با موفقیت دریافت کرده است، همراه با فراداده‌ای درباره اعتبارنامه‌های استفاده‌شده برای دریافت آن‌ها نگه می‌دارد.

برای جزئیات بیشتر، به [اطمینان از راستی‌آزمایی اعتبارنامه دریافت ایمیج](/docs/concepts/containers/images#ensureimagepullcredentialverification) مراجعه کنید.

## پروفایل‌ها و پیکربندی امنیتی

### پروفایل‌های Seccomp

فایل‌های پروفایل Seccomp که Podها به آن‌ها ارجاع می‌دهند، باید در `/var/lib/kubelet/seccomp` قرار گیرند. برای جزئیات بیشتر، به [مرجع seccomp](/docs/reference/node/seccomp/) مراجعه کنید.

### پروفایل‌های AppArmor

مؤلفه kubelet پروفایل‌های AppArmor را از مسیری مختص کوبرنتیز بارگذاری نمی‌کند و به چنین مسیری نیز ارجاع نمی‌دهد. این پروفایل‌ها به‌جای ارجاع از طریق مسیرشان، به‌واسطه سیستم‌عامل نود بارگذاری می‌شوند.

## قفل‌گذاری

{{< feature-state state="alpha" for_k8s_version="v1.2" >}}


فایل قفل kubelet معمولاً در `/var/run/kubelet.lock` قرار دارد. kubelet با استفاده از این فایل اطمینان حاصل می‌کند که دو kubelet مختلف هم‌زمان به‌صورت متعارض اجرا نشوند. مسیر فایل قفل را می‌توانید با آرگومان خط فرمان `--lock-file` در kubelet پیکربندی کنید.

اگر دو kubelet روی یک نود مقدارهای متفاوتی برای مسیر فایل قفل داشته باشند، هنگام اجرای هم‌زمان نمی‌توانند تعارض را تشخیص دهند.


## {{% heading "whatsnext" %}}

- با [آرگومان‌های خط فرمان](/docs/reference/command-line-tools-reference/kubelet/) kubelet آشنا شوید.
- [مرجع پیکربندی Kubelet (v1beta1)](/docs/reference/config-api/kubelet-config.v1beta1/) را مرور کنید.
