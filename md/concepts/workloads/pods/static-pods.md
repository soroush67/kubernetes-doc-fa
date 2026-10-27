---
title: "Podهای ایستا"
content_type: concept
weight: 150
---

_Podهای ایستا_ (Static Pods) مستقیماً توسط دیمن kubelet روی یک نود مشخص مدیریت می‌شوند،
بدون آنکه {{< glossary_tooltip text="API server" term_id="kube-apiserver" >}}
آن‌ها را مشاهده کند.
برخلاف Podهایی که توسط control plane مدیریت می‌شوند (برای مثال، یک
{{< glossary_tooltip text="Deployment" term_id="deployment" >}})،
kubelet هر Pod ایستا را زیر نظر دارد و در صورت از کار افتادن، آن را دوباره راه‌اندازی می‌کند.

Podهای ایستا همواره به یک {{< glossary_tooltip text="kubelet" term_id="kubelet" >}} روی یک نود مشخص وابسته‌اند.

کاربرد اصلی Podهای ایستا، اجرای یک control plane خودمیزبان (self-hosted) است؛ به بیان دیگر،
استفاده از kubelet برای نظارت بر تک‌تک
[اجزای control plane](/docs/concepts/overview/components/#control-plane-components).
برای مثال، [kubeadm](/docs/reference/setup-tools/kubeadm/) از Podهای ایستا برای اجرای
`kube-apiserver`، `kube-controller-manager`، `kube-scheduler` و `etcd` روی نودهای control plane استفاده می‌کند.

{{< note >}}
اگر کلاستر شما اجزای control plane را به‌صورت Pod اجرا می‌کند، احتمالاً آن‌ها
Podهای ایستا هستند. می‌توانید Podهای آینه‌ای (mirror) آن‌ها را در فضای نام `kube-system`
از روی حاشیه‌نویسی `kubernetes.io/config.mirror` تشخیص دهید.
{{< /note >}}

## Podهای آینه‌ای {#mirror-pods}

kubelet به‌طور خودکار تلاش می‌کند برای هر Pod ایستا یک
{{< glossary_tooltip text="Pod آینه‌ای" term_id="mirror-pod" >}}
روی API server کوبرنتیز ایجاد کند.
این بدان معناست که Podهای در حال اجرا روی یک نود در API server قابل مشاهده هستند،
اما نمی‌توان آن‌ها را از آنجا کنترل کرد.
نام این Podها با پسوندی شامل نام میزبان نود که با یک خط تیره آغاز می‌شود همراه خواهد بود.

kubelet {{< glossary_tooltip text="برچسب‌ها" term_id="label" >}}
را از Pod ایستا به Pod آینه‌ای منتقل می‌کند. می‌توانید از این برچسب‌ها به‌صورت عادی از طریق
{{< glossary_tooltip text="انتخابگرها" term_id="selector" >}} استفاده کنید.

اگر تلاش کنید با `kubectl` Pod آینه‌ای را از API server حذف کنید،
kubelet Pod ایستا را حذف _نمی‌کند_. kubelet
Pod آینه‌ای را دوباره ایجاد خواهد کرد.

## محدودیت‌ها {#limitations}

spec یک Pod ایستا نمی‌تواند به سایر آبجکت‌های API
مانند {{< glossary_tooltip text="ServiceAccount" term_id="service-account" >}}،
{{< glossary_tooltip text="ConfigMap" term_id="configmap" >}} یا
{{< glossary_tooltip text="Secret" term_id="secret" >}} ارجاع دهد.

Podهای ایستا از [کانتینرهای موقت (ephemeral)](/docs/concepts/workloads/pods/ephemeral-containers/) پشتیبانی نمی‌کنند.

## مقایسه‌ی Podهای ایستا با DaemonSetها {#static-pods-vs-daemonsets}

<!-- Source: tasks/configure-pod-container/static-pod/ -->
اگر کوبرنتیز را به‌صورت کلاستری اجرا می‌کنید و از Podهای ایستا برای اجرای یک Pod
روی هر نود استفاده می‌کنید، احتمالاً بهتر است به جای آن از یک
{{< glossary_tooltip text="DaemonSet" term_id="daemonset" >}} استفاده کنید.

Podهای ایستا توسط control plane مدیریت نمی‌شوند، بنابراین نمی‌توان آن‌ها را با سازوکارهای
استاندارد کوبرنتیز منتشر (roll out)، به نسخه‌ی قبل بازگرداند (roll back) یا مقیاس‌دهی کرد. DaemonSetها
این قابلیت‌ها را فراهم می‌کنند و رویکرد توصیه‌شده برای اجرای بارهای کاری سطح نود هستند.

Podهای ایستا پیش از در دسترس قرار گرفتن API server توسط kubelet راه‌اندازی می‌شوند، و همین امر
آن‌ها را برای راه‌اندازی اولیه‌ی (bootstrapping) اجزای control plane مناسب می‌کند. DaemonSetها به
یک control plane در حال اجرا نیاز دارند.

## {{% heading "whatsnext" %}}

- بیاموزید چگونه [Podهای ایستا ایجاد کنید](/docs/tasks/configure-pod-container/static-pod/).
- درباره‌ی [اجزای کوبرنتیز](/docs/concepts/overview/components/) و نحوه‌ی استفاده‌ی control plane از Podهای ایستا بیاموزید.
- درباره‌ی [DaemonSetها](/docs/concepts/workloads/controllers/daemonset/) به‌عنوان جایگزینی برای Podهای ایستا بیاموزید.
