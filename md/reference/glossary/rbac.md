---
title: RBAC (کنترل دسترسی مبتنی بر نقش)
id: rbac
full_link: /docs/reference/access-authn-authz/rbac/
short_description: >
  تصمیم‌های مجوزدهی را مدیریت می‌کند و به مدیران امکان می‌دهد سیاست‌های دسترسی را از طریق API کوبرنتیز به‌صورت پویا پیکربندی کنند.

aka: 
tags:
- security
- fundamental
---
 تصمیم‌های مجوزدهی (authorization) را مدیریت می‌کند و به مدیران امکان می‌دهد سیاست‌های دسترسی را از طریق {{< glossary_tooltip text="API کوبرنتیز" term_id="kubernetes-api" >}} به‌صورت پویا پیکربندی کنند.

<!--more--> 

سازوکار RBAC از چهار نوع آبجکت کوبرنتیز استفاده می‌کند:

Role
: قواعد مجوز را در یک فضای نام (namespace) مشخص تعریف می‌کند.

ClusterRole
: قواعد مجوز را در سطح کل کلاستر تعریف می‌کند.

RoleBinding
: مجوزهای تعریف‌شده در یک نقش را در یک فضای نام مشخص به مجموعه‌ای از کاربران اعطا می‌کند.

ClusterRoleBinding
: مجوزهای تعریف‌شده در یک نقش را در سطح کل کلاستر به مجموعه‌ای از کاربران اعطا می‌کند.

برای اطلاعات بیشتر، [RBAC](/docs/reference/access-authn-authz/rbac/) را ببینید.
