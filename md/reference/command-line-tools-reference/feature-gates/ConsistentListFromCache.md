---
title: ConsistentListFromCache
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.33"
  - stage: stable
    defaultValue: true
    fromVersion: "1.34"

---
عملکرد API server کوبرنتیز با پاسخ‌دهی به درخواست‌های **list** سازگار (consistent) مستقیماً از watch cache آن بهبود می‌یابد و این امر مقیاس‌پذیری و زمان پاسخ‌دهی را افزایش می‌دهد.
برای انجام list سازگار از حافظه نهان (cache)، کوبرنتیز به نسخه جدیدتری از etcd (نسخه v3.4.31 به بالا یا v3.5.13 به بالا) نیاز دارد
که شامل اصلاحاتی برای قابلیت درخواست پیشرفت watch (watch progress request) است.
اگر نسخه قدیمی‌تری از etcd ارائه شده باشد، کوبرنتیز آن را به‌طور خودکار تشخیص می‌دهد و به پاسخ‌دهی خواندن‌های سازگار از طریق etcd بازمی‌گردد.
اعلان‌های پیشرفت (progress notifications) تضمین می‌کنند که watch cache با etcd سازگار باشد و در عین حال نیاز به خواندن‌های quorum پرهزینه از etcd را کاهش می‌دهند.

برای جزئیات بیشتر، مستندات کوبرنتیز درباره [معناشناسی **get** و **list**](/docs/reference/using-api/api-concepts/#semantics-for-get-and-list) را ببینید.
