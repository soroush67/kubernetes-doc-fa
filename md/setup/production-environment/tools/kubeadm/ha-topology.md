---
reviewers:
- sig-cluster-lifecycle
title: گزینه‌های توپولوژی با دسترس‌پذیری بالا
content_type: concept
weight: 50
---

<!-- overview -->

این صفحه دو گزینه برای پیکربندی توپولوژی کلاسترهای کوبرنتیز با دسترس‌پذیری بالا (HA) را توضیح می‌دهد.

یک کلاستر HA را می‌توانید به یکی از این دو روش راه‌اندازی کنید:

- با نودهای control plane پشته‌ای (stacked)، که در آن نودهای etcd در کنار نودهای control plane قرار می‌گیرند
- با نودهای etcd خارجی، که در آن etcd روی نودهایی جدا از control plane اجرا می‌شود

پیش از راه‌اندازی یک کلاستر HA، مزایا و معایب هر توپولوژی را به‌دقت بسنجید.

{{< note >}}
ابزار kubeadm کلاستر etcd را به‌صورت ایستا راه‌اندازی می‌کند. برای جزئیات بیشتر،
[راهنمای کلاسترسازی](https://github.com/etcd-io/etcd/blob/release-3.4/Documentation/op-guide/clustering.md#static)
etcd را مطالعه کنید.
{{< /note >}}

<!-- body -->

## توپولوژی etcd پشته‌ای

کلاستر HA پشته‌ای یک [توپولوژی](https://en.wikipedia.org/wiki/Network_topology) است که در آن کلاستر ذخیره‌سازی توزیع‌شده‌ی داده که etcd فراهم می‌کند، روی کلاستری قرار می‌گیرد که از نودهای مدیریت‌شده با kubeadm و اجراکننده‌ی مؤلفه‌های control plane تشکیل شده است.

هر نود control plane یک نمونه از `kube-apiserver`، `kube-scheduler` و `kube-controller-manager` را اجرا می‌کند. مؤلفه‌ی `kube-apiserver` از طریق یک متعادل‌کننده‌ی بار (load balancer) در دسترس نودهای کارگر قرار می‌گیرد.

هر نود control plane یک عضو محلی etcd ایجاد می‌کند و این عضو etcd فقط با `kube-apiserver` همان نود ارتباط برقرار می‌کند. همین موضوع درباره‌ی نمونه‌های محلی `kube-controller-manager` و `kube-scheduler` نیز صدق می‌کند.

این توپولوژی control planeها و اعضای etcd را روی نودهای یکسان به هم پیوند می‌دهد. راه‌اندازی آن ساده‌تر از کلاستری با نودهای etcd خارجی است و مدیریت آن برای تکثیر (replication) نیز ساده‌تر است.

با این حال، کلاستر پشته‌ای در معرض خطر شکست ناشی از این پیوستگی است. اگر یک نود از کار بیفتد، هم یک عضو etcd و هم یک نمونه‌ی control plane از دست می‌روند و افزونگی کلاستر آسیب می‌بیند. می‌توانید با افزودن نودهای control plane بیشتر این خطر را کاهش دهید.

بنابراین برای یک کلاستر HA باید دست‌کم سه نود control plane پشته‌ای اجرا کنید.

این توپولوژی پیش‌فرض kubeadm است. هنگام استفاده از `kubeadm init` و `kubeadm join --control-plane`، یک عضو محلی etcd به‌طور خودکار روی نودهای control plane ایجاد می‌شود.

![توپولوژی etcd پشته‌ای](/images/kubeadm/kubeadm-ha-topology-stacked-etcd.svg)

## توپولوژی etcd خارجی

کلاستر HA با etcd خارجی یک [توپولوژی](https://en.wikipedia.org/wiki/Network_topology) است که در آن کلاستر ذخیره‌سازی توزیع‌شده‌ی داده که etcd فراهم می‌کند، بیرون از کلاستری قرار دارد که از نودهای اجراکننده‌ی مؤلفه‌های control plane تشکیل شده است.

همانند توپولوژی etcd پشته‌ای، در توپولوژی etcd خارجی نیز هر نود control plane یک نمونه از `kube-apiserver`، `kube-scheduler` و `kube-controller-manager` را اجرا می‌کند و مؤلفه‌ی `kube-apiserver` از طریق یک متعادل‌کننده‌ی بار در دسترس نودهای کارگر قرار می‌گیرد. با این حال، اعضای etcd روی میزبان‌های جداگانه اجرا می‌شوند و هر میزبان etcd با `kube-apiserver` تک‌تک نودهای control plane ارتباط برقرار می‌کند.

این توپولوژی control plane و عضو etcd را از هم جدا می‌کند. از این رو، پیکربندی HA‌ای فراهم می‌کند که در آن از دست رفتن یک نمونه‌ی control plane یا یک عضو etcd اثر کمتری دارد و به اندازه‌ی توپولوژی HA پشته‌ای بر افزونگی کلاستر تأثیر نمی‌گذارد.

با این حال، این توپولوژی به دو برابر تعداد میزبان‌های توپولوژی HA پشته‌ای نیاز دارد. برای یک کلاستر HA با این توپولوژی، دست‌کم سه میزبان برای نودهای control plane و سه میزبان برای نودهای etcd لازم است.

![توپولوژی etcd خارجی](/images/kubeadm/kubeadm-ha-topology-external-etcd.svg)

## {{% heading "whatsnext" %}}

- [راه‌اندازی یک کلاستر با دسترس‌پذیری بالا با kubeadm](/docs/setup/production-environment/tools/kubeadm/high-availability/)
