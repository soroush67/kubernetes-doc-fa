---
title: "راهنمای سخت‌سازی - تخصیص پویای منابع"
description: >
  اطلاعاتی دربارهٔ سخت‌سازی مجوزدهی و الگوهای دسترسی تخصیص پویای منابع (DRA).
content_type: concept
weight: 90
---

<!-- overview -->

تخصیص پویای منابع (DRA) قابلیت‌های قدرتمندی برای زمان‌بندی و مدیریت دستگاه‌ها
اضافه می‌کند. از آنجا که مؤلفه‌های DRA وضعیت (status) `ResourceClaim` را به‌روزرسانی می‌کنند، مدیران
کلاستر باید مجوزدهی این به‌روزرسانی‌ها را با RBAC صریح و مبتنی بر
کمترین امتیاز پیکربندی کنند.

{{< feature-state feature_gate_name="DRAResourceClaimGranularStatusAuthorization" >}}

از کوبرنتیز v1.36 به بعد، به‌روزرسانی‌های وضعیت DRA از زیرمنابع مصنوعی (synthetic) و،
در برخی موارد، از افعال تخصصی آگاه از نود استفاده می‌کنند.

<!-- body -->

## سخت‌سازی مجوزهای به‌روزرسانی وضعیت DRA

برای به‌روزرسانی‌های وضعیت DRA، مدیران کلاستر علاوه بر اعطای مجوز `update` روی
زیرمنبع `resourceclaims/status`، باید مجوزهایی را روی
زیرمنابع «مصنوعی» مشخصی اعطا کنند که بر اساس فیلدهای دقیقی که یک مؤلفه نیاز به تغییرشان دارد تعیین می‌شوند.
این کار اصل کمترین امتیاز را میان زمان‌بند، کنترل‌کننده‌های سفارشی
و درایورهای DRA اعمال می‌کند.

بررسی‌های مجوزدهی DRA به دو زیرمنبع مصنوعی تقسیم می‌شوند:

- **`resourceclaims/binding`**
  - برای تغییر `status.allocation` و `status.reservedFor` لازم است.
  - معمولاً به kube-scheduler و کنترل‌کننده‌های تخصیص سفارشی اعطا می‌شود.
  - از افعال استاندارد `update` و `patch` استفاده می‌کند.
- **`resourceclaims/driver`**
  - برای تغییر `status.devices` لازم است.
  - این بررسی به‌ازای هر درایور انجام می‌شود تا از دستکاری دستگاه‌ها روی نودهای دیگر
  و/یا دستگاه‌های سایر درایورها توسط درایورها جلوگیری شود.
  - برای دامنهٔ سخت‌گیرانه‌تر از افعال آگاه از نود استفاده می‌کند.

## افعال DRA آگاه از نود

هنگام مجوزدهی به‌روزرسانی‌های `resourceclaims/driver`، از پیشوند فعل
تخصصی مناسب استفاده کنید:

- **`associated-node:<verb>`** (برای مثال، `associated-node:update`)
  - برای درایورهای محلی نود.
  - API server وابستگی نود را برای درایور درخواست‌کننده بررسی می‌کند.
- **`arbitrary-node:<verb>`** (برای مثال، `arbitrary-node:patch`)
  - برای کنترل‌کننده‌های control plane یا چندنودی که ممکن است claimها را از
    هر نودی به‌روزرسانی کنند.

## نمونه‌الگوهای RBAC

### مجوزهای زمان‌بند و کنترل‌کنندهٔ تخصیص

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

### مجوزهای درایور DRA محلی نود

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

### مجوزهای کنترل‌کنندهٔ وضعیت چندنودی

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

## وظیفهٔ مرتبط مدیر کلاستر

برای اعمال این الگوها در یک کلاستر در حال اجرا، به
[سخت‌سازی تخصیص پویای منابع در کلاستر](/docs/tasks/administer-cluster/hardening-dra/) مراجعه کنید.

## {{% heading "whatsnext" %}}

- [مجوزدهی](/docs/reference/access-authn-authz/authorization/)
- [راه‌اندازی DRA در یک کلاستر](/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster/)
- [تخصیص پویای منابع](/docs/concepts/resource-management/dynamic-resource-allocation/)
