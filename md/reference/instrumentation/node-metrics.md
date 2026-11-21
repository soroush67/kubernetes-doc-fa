---
title: داده‌های متریک نود
content_type: reference
weight: 50
description: >-
  سازوکارهای دسترسی به متریک‌ها در سطح نود، حجم، پاد و کانتینر،
  آن‌گونه که kubelet آن‌ها را می‌بیند.
---

مؤلفهٔ [kubelet](/docs/reference/command-line-tools-reference/kubelet/)
آمار متریک‌ها را در سطح نود، حجم (volume)، پاد و کانتینر جمع‌آوری می‌کند
و این اطلاعات را در
[Summary API](/docs/reference/kubelet-api/stats.v1alpha1/) منتشر می‌کند.

می‌توانید از طریق سرور API کوبرنتیز، یک درخواست پراکسی‌شده به API خلاصهٔ آمار (stats summary API) بفرستید.

در اینجا نمونه‌ای از درخواست Summary API برای نودی با نام `minikube` آمده است:

```shell
kubectl get --raw "/api/v1/nodes/minikube/proxy/stats/summary"
```

همین فراخوانی API با استفاده از `curl` به این صورت است:

```shell
# You need to run "kubectl proxy" first
# Change 8080 to the port that "kubectl proxy" assigns
curl http://localhost:8080/api/v1/nodes/minikube/proxy/stats/summary
```

{{< note >}}
از نسخهٔ 0.6.x به بعد، `metrics-server` به‌جای `/stats/summary` از endpoint ‏`/metrics/resource` در kubelet پرس‌وجو می‌کند.
{{< /note >}}

## منبع API متریک‌های خلاصه {#summary-api-source}

کوبرنتیز به‌طور پیش‌فرض داده‌های متریک خلاصهٔ نود را با استفاده از یک
[cAdvisor](https://github.com/google/cadvisor) تعبیه‌شده که درون kubelet اجرا می‌شود، دریافت می‌کند. اگر
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) ‏`PodAndContainerStatsFromCRI` را
در کلاستر خود فعال کنید و از محیط اجرای کانتینری استفاده کنید که دسترسی به آمار را از طریق
{{< glossary_tooltip term_id="cri" text="رابط محیط اجرای کانتینر">}} (CRI) پشتیبانی می‌کند،
kubelet [داده‌های متریک سطح پاد و کانتینر را به‌جای cAdvisor از طریق CRI دریافت می‌کند](/docs/reference/instrumentation/cri-pod-container-metrics).

## اطلاعات توقف ناشی از فشار (PSI) {#psi}

{{< feature-state feature_gate_name="KubeletPSI" >}}

کوبرنتیز به‌عنوان یک قابلیت پایدار به شما امکان می‌دهد kubelet را طوری پیکربندی کنید که
[اطلاعات توقف ناشی از فشار](https://docs.kernel.org/accounting/psi.html)
(Pressure Stall Information یا PSI) هستهٔ لینوکس را برای مصرف CPU، حافظه و I/O جمع‌آوری کند. این اطلاعات در سطح نود، پاد و کانتینر جمع‌آوری می‌شود.
برای مشاهدهٔ طرح‌وارهٔ (schema) تفصیلی، به [Summary API](/docs/reference/kubelet-api/stats.v1alpha1/) مراجعه کنید.
از کوبرنتیز نسخهٔ v.1.36 به بعد، [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) ‏`KubeletPSI` روی مقدار true قفل شده است و نمی‌توان آن را غیرفعال کرد. این اطلاعات همچنین در
[متریک‌های Prometheus](/docs/concepts/cluster-administration/system-metrics#psi-metrics) در دسترس قرار می‌گیرد.

برای آشنایی با نحوهٔ تفسیر متریک‌های PSI، صفحهٔ [درک متریک‌های PSI](/docs/reference/instrumentation/understand-psi-metrics/) را ببینید.

### پیش‌نیازها

اطلاعات توقف ناشی از فشار به موارد زیر نیاز دارد:

- [هستهٔ لینوکس نسخهٔ 4.20 یا بالاتر](/docs/reference/node/kernel-version-requirements#requirements-psi).
- [cgroup v2](/docs/concepts/architecture/cgroups)

## {{% heading "whatsnext" %}}

صفحه‌های وظایف مربوط به [عیب‌یابی کلاسترها](/docs/tasks/debug/debug-cluster/) نحوهٔ استفاده از یک خط لولهٔ متریک‌ها (metrics pipeline) را که به این داده‌ها متکی است، شرح می‌دهند.
