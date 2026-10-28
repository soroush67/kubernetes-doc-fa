---
title: Device Plugin
id: device-plugin
full_link: /docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
short_description: >
  افزونه‌های نرم‌افزاری که به Podها امکان دسترسی به دستگاه‌هایی را می‌دهند که به راه‌اندازی یا پیکربندی اولیه مختص سازنده نیاز دارند
aka:
tags:
- fundamental
- extension
---
 Device pluginها روی {{< glossary_tooltip term_id="node" text="نودهای">}} کارگر اجرا می‌شوند و برای {{< glossary_tooltip term_id="pod" text="Podها">}} امکان دسترسی به {{< glossary_tooltip text="منابع" term_id="infrastructure-resource" >}} زیرساختی، مانند سخت‌افزار محلی، را فراهم می‌کنند؛ منابعی که به مراحل راه‌اندازی یا پیکربندی اولیه مختص سازنده نیاز دارند.

<!--more-->

Device pluginها منابع را به {{< glossary_tooltip term_id="kubelet" text="kubelet" >}} اعلام می‌کنند تا Podهای بار کاری بتوانند به قابلیت‌های سخت‌افزاری مرتبط با نودی که آن Pod روی آن اجرا می‌شود دسترسی داشته باشند.
می‌توانید یک device plugin را به‌صورت {{< glossary_tooltip term_id="daemonset" >}} مستقر کنید یا نرم‌افزار device plugin را مستقیماً روی هر نود هدف نصب کنید.

برای اطلاعات بیشتر به
[Device Plugins](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
مراجعه کنید.
