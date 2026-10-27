---
title: SELinuxChangePolicy
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.32"
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    fromVersion: "1.36"
---
فیلد `spec.securityContext.seLinuxChangePolicy` را فعال می‌کند.
از این فیلد می‌توان برای انصراف از اعمال برچسب SELinux بر حجم‌های (volume) Pod با استفاده از گزینه‌های مونت (mount options) استفاده کرد. این قابلیت زمانی لازم است که یک حجم واحد که از مونت با گزینه مونت SELinux پشتیبانی می‌کند، میان Podهایی مشترک باشد که برچسب‌های SELinux متفاوتی دارند، مانند Podهای دارای سطح دسترسی ویژه (privileged) و بدون سطح دسترسی ویژه (unprivileged).

فعال‌سازی feature gate با نام `SELinuxChangePolicy` مستلزم آن است که feature gate با نام `SELinuxMountReadWriteOncePod` نیز فعال باشد.
