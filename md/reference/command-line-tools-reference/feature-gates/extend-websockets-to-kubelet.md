---
title: ExtendWebSocketsToKubelet
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
هنگامی که ExtendWebSocketsToKubelet فعال باشد و یک نود kubelet اعلام کند که از این قابلیت پشتیبانی می‌کند،
جریان‌های (stream) exec/attach/portforward مستقیماً به kubelet پراکسی می‌شوند و
دیگر در سطح API server ترجمه یا تونل‌سازی نمی‌شوند. نکتهٔ مهم این است که همان
کنترل‌کننده‌های (handler) ترجمه و تونل‌سازی جریان که پیش‌تر در API server استفاده می‌شدند، اکنون
به‌صورت یکسان در kubelet نیز راه‌اندازی می‌شوند؛ به بیان دیگر، این منطق صرفاً به محیط نزدیک‌تری به
container runtime منتقل شده است. این قابلیت به ارتقای NodeDeclaredFeatures به مرحلهٔ بتا وابسته است تا
اعلام قابلیت‌های kubelet در کلاسترهای production قابل اتکا باشد.
