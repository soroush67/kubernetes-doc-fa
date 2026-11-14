---
title: استفاده از Antrea برای NetworkPolicy
content_type: task
weight: 10
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه افزونهٔ CNI به نام Antrea را روی کوبرنتیز نصب کنید و از آن استفاده کنید.
برای آشنایی با پیش‌زمینهٔ پروژهٔ Antrea، [مقدمه‌ای بر Antrea](https://antrea.io/docs/) را بخوانید.

## {{% heading "prerequisites" %}}

به یک کلاستر کوبرنتیز نیاز دارید. برای راه‌اندازی آن،
[راهنمای شروع کار با kubeadm](/docs/reference/setup-tools/kubeadm/) را دنبال کنید.

<!-- steps -->

## استقرار Antrea با kubeadm

برای استقرار Antrea با kubeadm، راهنمای [شروع به کار](https://github.com/vmware-tanzu/antrea/blob/main/docs/getting-started.md) را دنبال کنید.

## {{% heading "whatsnext" %}}

پس از راه‌اندازی کلاستر، می‌توانید راهنمای [اعلان سیاست شبکه](/docs/tasks/administer-cluster/declare-network-policy/) را دنبال کنید تا NetworkPolicy کوبرنتیز را امتحان کنید.
