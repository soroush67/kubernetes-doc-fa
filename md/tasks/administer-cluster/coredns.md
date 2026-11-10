---
reviewers:
- johnbelamaric
title: استفاده از CoreDNS برای کشف سرویس
min-kubernetes-server-version: v1.9
content_type: task
weight: 380
---

<!-- overview -->
این صفحه فرایند ارتقای CoreDNS و روش نصب آن را شرح می‌دهد.


## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}


<!-- steps -->

## دربارهٔ CoreDNS

پروژهٔ [CoreDNS](https://coredns.io) یک سرور DNS انعطاف‌پذیر و توسعه‌پذیر است
که پیاده‌سازی پیش‌فرض DNS کلاستر در کوبرنتیز به شمار می‌رود.
میزبان پروژهٔ CoreDNS نیز، همانند کوبرنتیز، بنیاد
{{< glossary_tooltip text="CNCF" term_id="cncf" >}} است.

## نصب CoreDNS

برای استقرار دستی، مستندات موجود در
[وب‌سایت CoreDNS](https://coredns.io/manual/installation/) را ببینید.

## ارتقای CoreDNS

نسخه‌ای از CoreDNS را که kubeadm برای هر نسخه از کوبرنتیز نصب می‌کند، می‌توانید در صفحهٔ
[نسخهٔ CoreDNS در کوبرنتیز](https://github.com/coredns/deployment/blob/master/kubernetes/CoreDNS-k8s_version.md)
بررسی کنید.

اگر بخواهید فقط CoreDNS را ارتقا دهید یا از ایمیج سفارشی خودتان استفاده کنید،
می‌توانید CoreDNS را به‌صورت دستی ارتقا دهید.
برای اطمینان از ارتقایی بی‌دردسر، یک [راهنما و آموزش گام‌به‌گام](https://github.com/coredns/deployment/blob/master/kubernetes/Upgrading_CoreDNS.md)
مفید در دسترس است.
هنگام ارتقای کلاستر، مطمئن شوید که پیکربندی موجود CoreDNS (یعنی «Corefile») حفظ می‌شود.

اگر کلاستر خود را با ابزار `kubeadm` ارتقا می‌دهید، ابزار `kubeadm`
می‌تواند حفظ پیکربندی موجود CoreDNS را به‌صورت خودکار انجام دهد.


## تنظیم دقیق CoreDNS

هنگامی که میزان مصرف منابع اهمیت دارد، تنظیم دقیق پیکربندی CoreDNS
می‌تواند سودمند باشد. برای جزئیات بیشتر،
[مستندات مقیاس‌پذیری CoreDNS](https://github.com/coredns/deployment/blob/master/kubernetes/Scaling_CoreDNS.md) را ببینید.

## {{% heading "whatsnext" %}}

با تغییر پیکربندی CoreDNS (یعنی «Corefile»)، می‌توانید [CoreDNS](https://coredns.io) را طوری پیکربندی کنید
که علاوه بر تفکیک پایهٔ نام سرویس‌ها، از کاربردهای بسیار دیگری نیز پشتیبانی کند.
برای اطلاعات بیشتر، [مستندات](https://coredns.io/plugins/kubernetes/)
افزونهٔ `kubernetes` در CoreDNS را ببینید یا مطلب
[Custom DNS Entries for Kubernetes](https://coredns.io/2017/05/08/custom-dns-entries-for-kubernetes/)
را در وبلاگ CoreDNS بخوانید.
