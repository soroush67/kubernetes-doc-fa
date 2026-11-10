---
title: مقاوم‌سازی تخصیص پویای منابع در کلاستر
content_type: task
weight: 330
---

<!-- overview -->

این صفحه به مدیران کلاستر نشان می‌دهد که چگونه مجوزدهی (authorization) مربوط به
تخصیص پویای منابع (Dynamic Resource Allocation یا DRA) را مقاوم‌سازی کنند. تمرکز این راهنما بر
دسترسی با کمترین سطح امتیاز برای به‌روزرسانی‌های وضعیت `ResourceClaim` است.

<!-- prerequisites -->

## {{% heading "prerequisites" %}}

- {{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}
- تخصیص پویای منابع در کلاستر شما پیکربندی شده باشد.
- بتوانید منابع RBAC را ویرایش کنید و مؤلفه‌های DRA را راه‌اندازی مجدد یا به‌روزرسانی تدریجی (roll out) کنید.

<!-- steps -->

## شناسایی مؤلفه‌های DRA که وضعیت را می‌نویسند

مشخص و مستند کنید که کدام هویت‌ها (معمولاً ServiceAccountها) وضعیت ResourceClaim
را در کلاستر شما به‌روزرسانی می‌کنند. نویسندگان رایج عبارت‌اند از:

- kube-scheduler یا یک کنترل‌کنندهٔ تخصیص سفارشی
- درایورهای DRA محلیِ نود
- کنترل‌کننده‌های وضعیت DRA چندنودی

## اعطای مجوزهای حداقلی برای زیرمنابع مصنوعی

از نسخهٔ v1.36 کوبرنتیز، به‌روزرسانی‌های وضعیت DRA علاوه بر `resourceclaims/status`
به مجوزهای زیرمنبع مصنوعی (synthetic subresource) نیز نیاز دارند.

### اعطای مجوز به زمان‌بند و کنترل‌کنندهٔ تخصیص

نقشی را اعمال کنید که به‌روزرسانی‌های مربوط به اتصال (binding) را مجاز می‌کند:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: dra-binding-updater
rules:
  - apiGroups: ["resource.k8s.io"]
    resources: ["resourceclaims/status"]
    verbs: ["get", "patch", "update"]
  - apiGroups: ["resource.k8s.io"]
    resources: ["resourceclaims/binding"]
    verbs: ["patch", "update"]
```

### اعطای مجوز به درایورهای محلیِ نود

برای درایورهای محلیِ نود از فعل‌های وابسته به نود استفاده کنید:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: dra-node-driver-status-updater
rules:
  - apiGroups: ["resource.k8s.io"]
    resources: ["resourceclaims/status"]
    verbs: ["get", "patch", "update"]
  - apiGroups: ["resource.k8s.io"]
    resources: ["resourceclaims/driver"]
    verbs: ["associated-node:patch", "associated-node:update"]
    resourceNames: ["dra.example.com"]
```

### اعطای مجوز به کنترل‌کننده‌های چندنودی فقط در صورت نیاز

فعل‌های `arbitrary-node:*` را فقط برای مؤلفه‌هایی به کار ببرید که باید بتوانند از هر نودی به‌روزرسانی انجام دهند:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: dra-multinode-status-updater
rules:
  - apiGroups: ["resource.k8s.io"]
    resources: ["resourceclaims/status"]
    verbs: ["get", "patch", "update"]
  - apiGroups: ["resource.k8s.io"]
    resources: ["resourceclaims/driver"]
    verbs: ["arbitrary-node:patch", "arbitrary-node:update"]
    resourceNames: ["dra.example.com"]
```

## اتصال نقش‌ها به هویت‌های مشخص

برای هویت هر مؤلفه، آبجکت‌های `ClusterRoleBinding` جداگانه بسازید و از اشتراک یک نقش
گسترده میان مؤلفه‌های DRA نامرتبط خودداری کنید.

در صورت امکان، قواعد `resourceclaims/driver` را با `resourceNames` محدود کنید تا هر
هویت فقط بتواند وضعیت را برای همان درایور DRA خاصی بنویسد که آن را اجرا می‌کند.

## اعتبارسنجی و پایش

1. بررسی کنید که هر هویت فقط فعل‌ها و زیرمنابع موردنیاز را در اختیار داشته باشد.
1. پس از به‌روزرسانی تدریجی، مطمئن شوید که به‌روزرسانی‌های وضعیت DRA به‌درستی کار می‌کنند.
1. رویدادهای ممیزی (audit) سرور API را برای درخواست‌های ردشدهٔ `resourceclaims/binding` و
   `resourceclaims/driver` زیر نظر داشته باشید.

## {{% heading "whatsnext" %}}

- [راهنمای مقاوم‌سازی - تخصیص پویای منابع](/docs/concepts/security/hardening-guide/dynamic-resource-allocation/)
- [ایمن‌سازی کلاستر](/docs/tasks/administer-cluster/securing-a-cluster/)
- [مجوزدهی](/docs/reference/access-authn-authz/authorization/)
