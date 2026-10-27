---
title: AuthorizePodWebsocketUpgradeCreatePermission
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.35"
---
هنگامی که feature gate با نام `AuthorizePodWebsocketUpgradeCreatePermission` برابر با `true` باشد،
کلاینت‌ها باید برای **create** کردن زیرمنابع Pod مجوز داشته باشند، حتی زمانی که ایجاد آن‌ها
را از طریق WebSocket آغاز می‌کنند.

درخواست ارتقای اتصال (connection upgrade) برای هر یک از زیرمنابع زیر رخ می‌دهد: `pods/exec`،
`pods/attach` و `pods/portforward`. این feature gate یک شکاف امنیتی را برطرف می‌کند که
در اثر گذار پروتکل ایجاد شده بود: درحالی‌که درخواست‌های SPDY از HTTP `POST` استفاده می‌کنند (که
به‌طور طبیعی با مجوز RBAC مربوط به **create** هم‌خوان است)، پروتکل WebSocket برای
مرحله‌ی handshake به یک درخواست HTTP `GET` نیاز دارد. برای رفع این نقص، اکنون یک بررسی RBAC
مصنوعی (synthetic) اعمال می‌شود تا اطمینان حاصل شود که ارتقاهای WebSocket نیز مجوز **create**
را به‌طور کامل و سخت‌گیرانه الزامی می‌کنند و با مدل امنیتی موجود SPDY همسو هستند.

اگر کلاینت‌ها یا ابزارهای سفارشی موجودی دارید که به رفتار قبلی متکی هستند، ممکن است بخواهید این
feature gate را غیرفعال کنید؛ به‌طور مشخص، اگر این کلاینت‌ها از طریق WebSocket متصل می‌شوند اما
در حال حاضر مجوز RBAC مربوط به **create** را *ندارند*.
