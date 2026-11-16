---
title: آموزش مبانی کوبرنتیز
main_menu: true
no_list: true
weight: 20
content_type: concept
card:
  name: tutorials
  weight: 20
  title: آشنایی گام‌به‌گام با مبانی
---

## {{% heading "objectives" %}}

این آموزش شما را گام‌به‌گام با مبانی سامانهٔ هماهنگ‌سازی کلاستر (cluster orchestration) کوبرنتیز آشنا می‌کند. هر بخش شامل اطلاعات پیش‌زمینه‌ای دربارهٔ ویژگی‌ها و مفاهیم اصلی کوبرنتیز و یک آموزش عملی است که می‌توانید هم‌زمان آن را دنبال کنید.

با استفاده از این آموزش‌ها می‌توانید یاد بگیرید که:

* یک برنامهٔ کانتینری‌شده را روی یک کلاستر مستقر کنید.
* مقیاس استقرار را تغییر دهید.
* برنامهٔ کانتینری‌شده را به نسخهٔ جدیدی از نرم‌افزار به‌روزرسانی کنید.
* برنامهٔ کانتینری‌شده را اشکال‌زدایی کنید.

## کوبرنتیز چه کاری می‌تواند برای شما انجام دهد؟

در سرویس‌های وب امروزی، کاربران انتظار دارند برنامه‌ها به‌صورت شبانه‌روزی و در تمام روزهای هفته در دسترس باشند و توسعه‌دهندگان نیز انتظار دارند بتوانند نسخه‌های جدید این برنامه‌ها را چندین بار در روز مستقر کنند. کانتینری‌سازی به بسته‌بندی نرم‌افزار برای دستیابی به این اهداف کمک می‌کند و امکان انتشار و به‌روزرسانی برنامه‌ها را بدون توقف سرویس فراهم می‌سازد. کوبرنتیز به شما کمک می‌کند مطمئن شوید این برنامه‌های کانتینری‌شده در همان جا و همان زمانی که می‌خواهید اجرا می‌شوند، و به آن‌ها کمک می‌کند منابع و ابزارهایی را که برای کار خود نیاز دارند پیدا کنند. کوبرنتیز یک پلتفرم متن‌باز و آمادهٔ محیط عملیاتی است که بر پایهٔ تجربهٔ انباشتهٔ گوگل در هماهنگ‌سازی کانتینرها و در کنار بهترین ایده‌های جامعهٔ کاربری طراحی شده است.

## بخش‌های آموزش مبانی کوبرنتیز

<!-- For translators, translate only the values of the ‘alt’ and ‘title’ keys -->
{{< tutorials/modules >}}
  {{< tutorials/module
      path="/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/"
      image="/docs/tutorials/kubernetes-basics/public/images/module_01.svg?v=1469803628347"
      alt="بخش ۱"
      title="۱. ایجاد یک کلاستر کوبرنتیز" >}}

  {{< tutorials/module
      path="/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/"
      image="/docs/tutorials/kubernetes-basics/public/images/module_02.svg?v=1469803628347"
      alt="بخش ۲"
      title="۲. استقرار یک برنامه" >}}

  {{< tutorials/module
      path="/docs/tutorials/kubernetes-basics/explore/explore-intro/"
      image="/docs/tutorials/kubernetes-basics/public/images/module_03.svg?v=1469803628347"
      alt="بخش ۳"
      title="۳. بررسی برنامهٔ خود" >}}

  {{< tutorials/module
      path="/docs/tutorials/kubernetes-basics/expose/expose-intro/"
      image="/docs/tutorials/kubernetes-basics/public/images/module_04.svg?v=1469803628347"
      alt="بخش ۴"
      title="۴. در دسترس قرار دادن عمومی برنامهٔ خود" >}}

  {{< tutorials/module
      path="/docs/tutorials/kubernetes-basics/scale/scale-intro/"
      image="/docs/tutorials/kubernetes-basics/public/images/module_05.svg?v=1469803628347"
      alt="بخش ۵"
      title="۵. افزایش مقیاس برنامهٔ خود" >}}

  {{< tutorials/module
      path="/docs/tutorials/kubernetes-basics/update/update-intro/"
      image="/docs/tutorials/kubernetes-basics/public/images/module_06.svg?v=1469803628347"
      alt="بخش ۶"
      title="۶. به‌روزرسانی برنامهٔ خود" >}}
{{< /tutorials/modules >}}

## {{% heading "whatsnext" %}}

* برای آشنایی بیشتر با کلاسترهای تمرینی و نحوهٔ راه‌اندازی کلاستر شخصی خود، صفحهٔ [محیط یادگیری](/docs/setup/learning-environment/) را ببینید.
* آموزش [استفاده از Minikube برای ایجاد یک کلاستر](/docs/tutorials/kubernetes-basics/create-cluster/)
