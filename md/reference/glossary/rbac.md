---
title: RBAC (کنترل دسترسی مبتنی بر نقش)
id: rbac
full_link: /docs/reference/access-authn-authz/rbac/
short_description: >
  تصمیم‌های مجوزدهی را مدیریت می‌کند و به مدیران اجازه می‌دهد سیاست‌های دسترسی را به‌صورت پویا از طریق API کوبرنتیز پیکربندی کنند.

aka: 
tags:
- security
- fundamental
---
 تصمیم‌های مجوزدهی را مدیریت می‌کند و به مدیران اجازه می‌دهد سیاست‌های دسترسی را به‌صورت پویا از طریق {{< glossary_tooltip text="API کوبرنتیز" term_id="kubernetes-api" >}} پیکربندی کنند.

<!--more--> 

RBAC از چهار نوع آبجکت کوبرنتیز استفاده می‌کند:

Role
: قوانین مجوز را در یک فضای نام (namespace) مشخص تعریف می‌کند.

ClusterRole
: قوانین مجوز را در سطح کل کلاستر تعریف می‌کند.

RoleBinding
: مجوزهای تعریف‌شده در یک Role را در یک فضای نام (namespace) مشخص به مجموعه‌ای از کاربران اعطا می‌کند.

ClusterRoleBinding
: مجوزهای تعریف‌شده در یک Role را در سطح کل کلاستر به مجموعه‌ای از کاربران اعطا می‌کند.

برای اطلاعات بیشتر، [RBAC](/docs/reference/access-authn-authz/rbac/) را ببینید.
