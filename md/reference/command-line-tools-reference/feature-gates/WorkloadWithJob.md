---
title: WorkloadWithJob
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.36"
---

کنترل‌کننده Job را قادر می‌سازد پیکربندی `.spec.scheduling` یک Job را پیش از ایجاد هر Pod، به آبجکت‌های
[Workload](/docs/concepts/workloads/workload-api/) و [PodGroup](/docs/concepts/workloads/podgroup-api/)
تبدیل (کامپایل) کند.
در صورتی که `.spec.scheduling` مشخص نشده باشد، Job به‌طور پیش‌فرض از سیاست زمان‌بندی `Basic` استفاده می‌کند. برای جزئیات بیشتر، به
[یکپارچه‌سازی با APIهای Workload](/docs/concepts/workloads/controllers/job#integrate-with-workload-apis)
مراجعه کنید.
