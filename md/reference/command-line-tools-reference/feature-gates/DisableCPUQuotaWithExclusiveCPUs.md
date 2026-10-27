---
title: DisableCPUQuotaWithExclusiveCPUs
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
---

زمانی که feature gate با نام `DisableCPUQuotaWithExclusiveCPUs` فعال باشد (که حالت پیش‌فرض است)، کوبرنتیز سهمیه CPU را برای Podهایی که از
{{< glossary_tooltip text="کلاس QoS" term_id="qos-class" >}} با نام [Guaranteed](/docs/concepts/workloads/pods/pod-qos/#guaranteed) استفاده می‌کنند، **اعمال نمی‌کند**.

برای بازگرداندن رفتار قدیمی، می‌توانید feature gate با نام `DisableCPUQuotaWithExclusiveCPUs` را غیرفعال کنید.
