---
title: "مروری بر kubectl-convert"
description: >-
  افزونه‌ای برای kubectl که با آن می‌توانید مانیفست‌ها را از یک نسخه از API
  کوبرنتیز به نسخهٔ دیگری تبدیل کنید.
headless: true
_build:
  list: never
  render: never
  publishResources: false
---

این ابزار افزونه‌ای (plugin) برای `kubectl`، ابزار خط فرمان کوبرنتیز، است که با آن می‌توانید مانیفست‌ها را میان نسخه‌های مختلف API تبدیل کنید. این افزونه به‌ویژه هنگام انتقال مانیفست‌ها به یک نسخهٔ منسوخ‌نشدهٔ API در نسخه‌های جدیدتر کوبرنتیز مفید است.
برای اطلاعات بیشتر، به [مهاجرت به APIهای منسوخ‌نشده](/docs/reference/using-api/deprecation-guide/#migrate-to-non-deprecated-apis) مراجعه کنید.
