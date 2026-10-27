---
title: CRIListStreaming
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.36"
---
فعال‌سازی RPCهای استریمینگ برای عملیات list در CRI (`ListContainers`،
`ListPodSandbox` و `ListImages`). در صورت فعال بودن، kubelet از RPCهای استریمینگ سمت سرور
(برای مثال `StreamContainers` و `StreamPodSandboxes`) استفاده می‌کند که به
container runtime اجازه می‌دهند نتایج را میان چندین پیام پاسخ تقسیم کند و
از محدودیت اندازهٔ پیام gRPC یعنی ۱۶ مبی‌بایت (MiB) عبور کند. این قابلیت امکان فهرست‌کردن کانتینرها
در نودهایی را که هزاران کانتینر دارند، بدون بروز خطا فراهم می‌کند. اگر container
runtime از RPCهای استریمینگ پشتیبانی نکند، kubelet به RPCهای unary بازمی‌گردد.
