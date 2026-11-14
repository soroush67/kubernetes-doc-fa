---
title: اعمال استانداردهای امنیتی Pod با برچسب‌های فضای نام
reviewers:
- tallclair
- liggitt
content_type: task
weight: 250
---

می‌توان با برچسب‌گذاری فضاهای نام (namespace)، [استانداردهای امنیتی Pod](/docs/concepts/security/pod-security-standards) را بر آن‌ها اعمال کرد. سه سیاست
[privileged](/docs/concepts/security/pod-security-standards/#privileged)، [baseline](/docs/concepts/security/pod-security-standards/#baseline)
و [restricted](/docs/concepts/security/pod-security-standards/#restricted) طیف امنیتی را به‌طور گسترده پوشش می‌دهند
و {{< glossary_tooltip
text="کنترل‌کنندهٔ پذیرش" term_id="admission-controller" >}} [Pod Security](/docs/concepts/security/pod-security-admission/) آن‌ها را پیاده‌سازی می‌کند.

## {{% heading "prerequisites" %}}

قابلیت Pod Security Admission در کوبرنتیز نسخهٔ v1.23 به‌صورت پیش‌فرض و در مرحلهٔ بتا در دسترس بود.
از نسخهٔ 1.25 به بعد، Pod Security Admission به‌طور عمومی در دسترس (GA) است.

{{% version-check %}}

## الزام به رعایت استاندارد امنیتی `baseline` برای Pod با برچسب‌های فضای نام

این مانیفست یک Namespace با نام `my-baseline-namespace` تعریف می‌کند که:

- هر Podی را که الزامات سیاست `baseline` را برآورده نکند، _مسدود می‌کند_.
- برای هر Pod ایجادشده‌ای که الزامات سیاست `restricted` را برآورده نکند، هشداری به کاربر نمایش می‌دهد
  و یک حاشیه‌نویسی (annotation) ممیزی به آن اضافه می‌کند.
- نسخهٔ سیاست‌های `baseline` و `restricted` را روی v{{< skew currentVersion >}} ثابت می‌کند.

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: my-baseline-namespace
  labels:
    pod-security.kubernetes.io/enforce: baseline
    pod-security.kubernetes.io/enforce-version: v{{< skew currentVersion >}}

    # We are setting these to our _desired_ `enforce` level.
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/audit-version: v{{< skew currentVersion >}}
    pod-security.kubernetes.io/warn: restricted
    pod-security.kubernetes.io/warn-version: v{{< skew currentVersion >}}
```

## افزودن برچسب به فضاهای نام موجود با `kubectl label`

{{< note >}}
هنگامی که برچسب سیاست (یا نسخهٔ) `enforce` اضافه یا تغییر داده می‌شود، افزونهٔ پذیرش هر Pod موجود در
فضای نام را با سیاست جدید می‌سنجد. موارد نقض به‌صورت هشدار به کاربر برگردانده می‌شوند.
{{< /note >}}

هنگام ارزیابی اولیهٔ تغییرات پروفایل امنیتی فضاهای نام، استفاده از فلگ `--dry-run` مفید است.
در حالت _اجرای آزمایشی_ (dry run) نیز بررسی‌های استاندارد امنیتی Pod انجام می‌شوند و به این ترتیب، بی‌آنکه
سیاستی واقعاً به‌روزرسانی شود، می‌توانید ببینید سیاست جدید با Podهای موجود چگونه رفتار می‌کند.

```shell
kubectl label --dry-run=server --overwrite ns --all \
    pod-security.kubernetes.io/enforce=baseline
```

### اعمال بر همهٔ فضاهای نام

اگر تازه کار با استانداردهای امنیتی Pod را آغاز کرده‌اید، گام نخست مناسب این است که همهٔ فضاهای نام را
با حاشیه‌نویسی‌های ممیزی برای سطحی سخت‌گیرانه‌تر مانند `baseline` پیکربندی کنید:

```shell
kubectl label --overwrite ns --all \
  pod-security.kubernetes.io/audit=baseline \
  pod-security.kubernetes.io/warn=baseline
```

توجه کنید که این دستور سطح enforce را تنظیم نمی‌کند تا بتوان فضاهای نامی را که هنوز به‌طور صریح ارزیابی
نشده‌اند، از بقیه تشخیص داد. با این دستور می‌توانید فضاهای نامی را که سطح enforce برایشان به‌طور صریح
تنظیم نشده است، فهرست کنید:

```shell
kubectl get namespaces --selector='!pod-security.kubernetes.io/enforce'
```

### اعمال بر یک فضای نام

می‌توانید یک فضای نام مشخص را نیز به‌روزرسانی کنید. این دستور سیاست `enforce=restricted` را به
`my-existing-namespace` اضافه می‌کند و نسخهٔ سیاست restricted را روی v{{< skew currentVersion >}} ثابت می‌کند.

```shell
kubectl label --overwrite ns my-existing-namespace \
  pod-security.kubernetes.io/enforce=restricted \
  pod-security.kubernetes.io/enforce-version=v{{< skew currentVersion >}}
```
