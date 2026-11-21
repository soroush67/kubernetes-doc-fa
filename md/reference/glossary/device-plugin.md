---
title: افزونه دستگاه
id: device-plugin
full_link: /docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
short_description: >
  افزونه‌های نرم‌افزاری که به Podها امکان دسترسی به دستگاه‌هایی را می‌دهند که به راه‌اندازی یا پیکربندی ویژهٔ سازنده نیاز دارند
aka:
tags:
- fundamental
- extension
---
 افزونه‌های دستگاه (device plugin) روی {{< glossary_tooltip term_id="node" text="نودهای">}} کارگر اجرا می‌شوند و دسترسی
{{< glossary_tooltip term_id="pod" text="Podها">}} را به
{{< glossary_tooltip text="منابع" term_id="infrastructure-resource" >}} زیرساختی، مانند سخت‌افزار محلی، فراهم می‌کنند؛ منابعی که به مراحل راه‌اندازی یا پیکربندی ویژهٔ سازنده نیاز دارند.

<!--more-->

افزونه‌های دستگاه منابع را به
{{< glossary_tooltip term_id="kubelet" text="kubelet" >}} اعلام می‌کنند تا Podهای بار کاری بتوانند به قابلیت‌های سخت‌افزاری نودی که روی آن اجرا می‌شوند دسترسی داشته باشند.
می‌توانید افزونهٔ دستگاه را به‌صورت یک {{< glossary_tooltip term_id="daemonset" >}} مستقر کنید یا نرم‌افزار آن را مستقیماً روی هر نود هدف نصب کنید.

برای اطلاعات بیشتر، صفحهٔ
[افزونه‌های دستگاه](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
را ببینید.
