---
title: اعمال استانداردهای امنیتی Pod با پیکربندی کنترل‌کنندهٔ پذیرش داخلی
reviewers:
- tallclair
- liggitt
content_type: task
weight: 240
---

کوبرنتیز یک [کنترل‌کنندهٔ پذیرش (admission controller)](/docs/reference/access-authn-authz/admission-controllers/#podsecurity) داخلی
برای اعمال [استانداردهای امنیتی Pod](/docs/concepts/security/pod-security-standards) فراهم می‌کند.
می‌توانید این کنترل‌کنندهٔ پذیرش را طوری پیکربندی کنید که پیش‌فرض‌ها و [استثناها](/docs/concepts/security/pod-security-admission/#exemptions)ی سراسری کلاستر را تعیین کند.

## {{% heading "prerequisites" %}}

پذیرش امنیتی Pod (Pod Security Admission) پس از انتشار نسخهٔ آلفا در کوبرنتیز v1.22،
در کوبرنتیز v1.23 به‌صورت بتا و به‌طور پیش‌فرض در دسترس قرار گرفت. از نسخهٔ 1.25 به بعد،
این قابلیت به‌طور عمومی در دسترس (GA) است.

{{% version-check %}}

اگر نسخهٔ کوبرنتیز شما {{< skew currentVersion >}} نیست، می‌توانید این صفحه را
در مستندات مربوط به نسخهٔ کوبرنتیزی که اجرا می‌کنید مشاهده کنید.

## پیکربندی کنترل‌کنندهٔ پذیرش

{{< note >}}
پیکربندی `pod-security.admission.config.k8s.io/v1` به نسخهٔ v1.25 یا بالاتر نیاز دارد.
برای نسخه‌های v1.23 و v1.24 از [v1beta1](https://v1-24.docs.kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-admission-controller/) استفاده کنید.
برای نسخهٔ v1.22 از [v1alpha1](https://v1-22.docs.kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-admission-controller/) استفاده کنید.
{{< /note >}}

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
- name: PodSecurity
  configuration:
    apiVersion: pod-security.admission.config.k8s.io/v1 # see compatibility note
    kind: PodSecurityConfiguration
    # Defaults applied when a mode label is not set.
    #
    # Level label values must be one of:
    # - "privileged" (default)
    # - "baseline"
    # - "restricted"
    #
    # Version label values must be one of:
    # - "latest" (default) 
    # - specific version like "v{{< skew currentVersion >}}"
    defaults:
      enforce: "privileged"
      enforce-version: "latest"
      audit: "privileged"
      audit-version: "latest"
      warn: "privileged"
      warn-version: "latest"
    exemptions:
      # Array of authenticated usernames to exempt.
      usernames: []
      # Array of runtime class names to exempt.
      runtimeClasses: []
      # Array of namespaces to exempt.
      namespaces: []
```

{{< note >}}
مانیفست بالا باید از طریق فلگ `--admission-control-config-file` به kube-apiserver داده شود.
{{< /note >}}
