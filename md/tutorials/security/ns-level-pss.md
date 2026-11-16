---
title: اعمال استانداردهای امنیتی Pod در سطح فضای نام
content_type: tutorial
weight: 20
---

{{% alert title="توجه" %}}
این آموزش فقط برای کلاسترهای جدید کاربرد دارد.
{{% /alert %}}

پذیرش امنیتی Pod (Pod Security Admission) یک کنترل‌کنندهٔ پذیرش (admission controller) است که هنگام ایجاد Podها،
[استانداردهای امنیتی Pod](/docs/concepts/security/pod-security-standards/)
را اعمال می‌کند. این قابلیت از نسخهٔ v1.25 به وضعیت GA رسیده است.
در این آموزش، استاندارد امنیتی `baseline` را برای Podها، هر بار در یک فضای نام (namespace)، اجباری می‌کنید.

همچنین می‌توانید استانداردهای امنیتی Pod را به‌طور هم‌زمان در سطح کلاستر بر چندین فضای نام اعمال کنید.
برای دستورالعمل‌های لازم، به
[اعمال استانداردهای امنیتی Pod در سطح کلاستر](/docs/tutorials/security/cluster-level-pss/) مراجعه کنید.

## {{% heading "prerequisites" %}}

موارد زیر را روی رایانهٔ کاری خود نصب کنید:

- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
- [kubectl](/docs/tasks/tools/)

## ایجاد کلاستر

1. یک کلاستر `kind` را به‌صورت زیر ایجاد کنید:

   ```shell
   kind create cluster --name psa-ns-level
   ```

   خروجی مشابه زیر است:

   ```
   Creating cluster "psa-ns-level" ...
    ✓ Ensuring node image (kindest/node:v{{< skew currentPatchVersion >}}) 🖼 
    ✓ Preparing nodes 📦  
    ✓ Writing configuration 📜 
    ✓ Starting control-plane 🕹️ 
    ✓ Installing CNI 🔌 
    ✓ Installing StorageClass 💾 
   Set kubectl context to "kind-psa-ns-level"
   You can now use your cluster with:
    
   kubectl cluster-info --context kind-psa-ns-level
    
   Not sure what to do next? 😅  Check out https://kind.sigs.k8s.io/docs/user/quick-start/
   ```

1. زمینهٔ (context) ابزار kubectl را روی کلاستر جدید تنظیم کنید:

   ```shell
   kubectl cluster-info --context kind-psa-ns-level
   ```
   خروجی مشابه زیر است:

   ```
   Kubernetes control plane is running at https://127.0.0.1:50996
   CoreDNS is running at https://127.0.0.1:50996/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
    
   To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
   ```

## ایجاد یک فضای نام

یک فضای نام جدید با نام `example` ایجاد کنید:

```shell
kubectl create ns example
```

خروجی مشابه زیر است:

```
namespace/example created
```

## فعال‌سازی بررسی استانداردهای امنیتی Pod برای آن فضای نام

1. با استفاده از برچسب‌هایی که پذیرش امنیتی Pod داخلی پشتیبانی می‌کند، استانداردهای امنیتی Pod را در این فضای نام فعال کنید.
   در این مرحله، بررسی‌ای را پیکربندی می‌کنید که برای Podهایی که با آخرین نسخهٔ استاندارد امنیتی _baseline_ مطابقت ندارند، هشدار می‌دهد.

   ```shell
   kubectl label --overwrite ns example \
      pod-security.kubernetes.io/warn=baseline \
      pod-security.kubernetes.io/warn-version=latest
   ```

2. با استفاده از برچسب‌ها می‌توانید چندین بررسی استاندارد امنیتی Pod را روی هر فضای نامی پیکربندی کنید.
   دستور زیر استاندارد امنیتی `baseline` را به حالت `enforce` اجباری می‌کند،
   اما برای استاندارد امنیتی `restricted` بر اساس آخرین نسخه (مقدار پیش‌فرض)، در حالت‌های `warn` و `audit` عمل می‌کند.

   ```shell
   kubectl label --overwrite ns example \
     pod-security.kubernetes.io/enforce=baseline \
     pod-security.kubernetes.io/enforce-version=latest \
     pod-security.kubernetes.io/warn=restricted \
     pod-security.kubernetes.io/warn-version=latest \
     pod-security.kubernetes.io/audit=restricted \
     pod-security.kubernetes.io/audit-version=latest
   ```

## تأیید اجرای استاندارد امنیتی Pod

1. یک Pod مطابق استاندارد baseline در فضای نام `example` ایجاد کنید:

   ```shell
   kubectl apply -n example -f https://k8s.io/examples/security/example-baseline-pod.yaml
   ```
   این Pod بدون مشکل اجرا می‌شود، اما خروجی شامل یک هشدار است. برای مثال:

   ```
   Warning: would violate PodSecurity "restricted:latest": allowPrivilegeEscalation != false (container "nginx" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (container "nginx" must set securityContext.capabilities.drop=["ALL"]), runAsNonRoot != true (pod or container "nginx" must set securityContext.runAsNonRoot=true), seccompProfile (pod or container "nginx" must set securityContext.seccompProfile.type to "RuntimeDefault" or "Localhost")
   pod/nginx created
   ```

1. یک Pod مطابق استاندارد baseline در فضای نام `default` ایجاد کنید:

   ```shell
   kubectl apply -n default -f https://k8s.io/examples/security/example-baseline-pod.yaml
   ```
   خروجی مشابه زیر است:

   ```
   pod/nginx created
   ```

تنظیمات اجبار و هشدار استانداردهای امنیتی Pod فقط بر فضای نام `example` اعمال شدند.
به همین دلیل توانستید همان Pod را بدون هیچ هشداری در فضای نام `default` ایجاد کنید.

## پاک‌سازی

اکنون با اجرای دستور زیر، کلاستری را که پیش‌تر ایجاد کردید حذف کنید:

```shell
kind delete cluster --name psa-ns-level
```

## {{% heading "whatsnext" %}}

- یک
  [اسکریپت شل](/examples/security/kind-with-namespace-level-baseline-pod-security.sh)
  را اجرا کنید تا همهٔ مراحل پیشین را یک‌جا انجام دهد:

  1. ایجاد کلاستر kind
  2. ایجاد فضای نام جدید
  3. اعمال استاندارد امنیتی `baseline` در حالت `enforce` و هم‌زمان اعمال استاندارد امنیتی
     `restricted` در حالت‌های `warn` و `audit`.
  4. ایجاد یک Pod جدید با اعمال استانداردهای امنیتی Pod ذکرشده

- [پذیرش امنیتی Pod](/docs/concepts/security/pod-security-admission/)
- [استانداردهای امنیتی Pod](/docs/concepts/security/pod-security-standards/)
- [اعمال استانداردهای امنیتی Pod در سطح کلاستر](/docs/tutorials/security/cluster-level-pss/)
