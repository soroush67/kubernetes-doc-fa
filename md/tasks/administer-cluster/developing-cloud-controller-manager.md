---
reviewers:
- luxas
- thockin
- wlan0
title: توسعهٔ Cloud Controller Manager
content_type: concept
weight: 190
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.11" state="beta" >}}

{{< glossary_definition term_id="cloud-controller-manager" length="all" prepend="The cloud-controller-manager is">}}



<!-- body -->

## پیش‌زمینه

ارائه‌دهندگان ابری با سرعتی متفاوت از پروژهٔ کوبرنتیز توسعه می‌دهند و نسخه منتشر می‌کنند. به همین دلیل، جداسازی کدِ مختص هر ارائه‌دهنده و انتقال آن به فایل اجرایی `cloud-controller-manager` باعث می‌شود فروشندگان ابری بتوانند مستقل از کد هستهٔ کوبرنتیز پیشرفت کنند.

پروژهٔ کوبرنتیز یک کد اسکلت برای cloud-controller-manager همراه با اینترفیس‌های Go فراهم می‌کند تا شما (یا ارائه‌دهندهٔ ابری‌تان) بتوانید پیاده‌سازی‌های خود را به آن متصل کنید. به این ترتیب، هر ارائه‌دهندهٔ ابری می‌تواند با import کردن بسته‌هایی از هستهٔ کوبرنتیز، یک cloud-controller-manager پیاده‌سازی کند. هر ارائه‌دهندهٔ ابری کد خود را با فراخوانی `cloudprovider.RegisterCloudProvider` ثبت می‌کند تا یک متغیر سراسری شامل فهرست ارائه‌دهندگان ابری موجود به‌روزرسانی شود.

## توسعه

### خارج از درخت (Out of tree)

برای ساخت یک cloud-controller-manager خارج از درخت برای ابر خود، این مراحل را دنبال کنید:

1. یک بستهٔ Go بسازید که پیاده‌سازی آن الزامات [cloudprovider.Interface](https://github.com/kubernetes/cloud-provider/blob/master/cloud.go) را برآورده کند.
2. از [فایل `main.go` در cloud-controller-manager](https://github.com/kubernetes/kubernetes/blob/master/cmd/cloud-controller-manager/main.go) در هستهٔ کوبرنتیز به‌عنوان الگویی برای فایل `main.go` خود استفاده کنید. همان‌طور که پیش‌تر گفته شد، تنها تفاوت باید بستهٔ ابری‌ای باشد که import می‌شود.
3. بستهٔ ابری خود را در `main.go` وارد (import) کنید و مطمئن شوید که بستهٔ شما یک بلوک `init` برای اجرای [`cloudprovider.RegisterCloudProvider`](https://github.com/kubernetes/cloud-provider/blob/master/plugins.go) دارد.

بسیاری از ارائه‌دهندگان ابری کد controller manager خود را به‌صورت متن‌باز منتشر می‌کنند. اگر یک cloud-controller-manager جدید را از صفر می‌سازید، می‌توانید یک cloud controller manager خارج از درختِ موجود را نقطهٔ شروع کار خود قرار دهید.

### درون درخت (In tree)

برای ارائه‌دهندگان ابری درون درخت، می‌توانید cloud controller manager درون درخت را به‌صورت یک {{< glossary_tooltip term_id="daemonset" >}} در کلاستر خود اجرا کنید. برای جزئیات بیشتر، [مدیریت Cloud Controller Manager](/docs/tasks/administer-cluster/running-cloud-controller/) را ببینید.
