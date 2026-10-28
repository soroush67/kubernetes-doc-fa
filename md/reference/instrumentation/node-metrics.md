---
title: داده‌های معیارهای نود
content_type: reference
weight: 50
description: >-
  سازوکارهای دسترسی به معیارها در سطح نود، حجم (volume)، Pod و کانتینر،
  آن‌گونه که kubelet آن‌ها را مشاهده می‌کند.
---

[kubelet](/docs/reference/command-line-tools-reference/kubelet/)
آمار معیارها را در سطح نود، حجم (volume)، Pod و کانتینر گردآوری می‌کند
و این اطلاعات را از طریق
[Summary API](/docs/reference/kubelet-api/stats.v1alpha1/)
ارائه می‌دهد.

می‌توانید از طریق kube-apiserver یک درخواست پراکسی‌شده به API خلاصه آمار (stats summary) ارسال کنید.

در ادامه نمونه‌ای از یک درخواست Summary API برای نودی با نام `minikube` آمده است:

```shell
kubectl get --raw "/api/v1/nodes/minikube/proxy/stats/summary"
```

در ادامه همین فراخوانی API با استفاده از `curl` آمده است:

```shell
# You need to run "kubectl proxy" first
# Change 8080 to the port that "kubectl proxy" assigns
curl http://localhost:8080/api/v1/nodes/minikube/proxy/stats/summary
```

{{< note >}}
از `metrics-server` نسخه 0.6.x به بعد، `metrics-server` به‌جای `/stats/summary`، از endpoint با مسیر `/metrics/resource` در kubelet پرس‌وجو می‌کند.
{{< /note >}}

## منبع Summary metrics API {#summary-api-source}

به‌طور پیش‌فرض، کوبرنتیز داده‌های معیارهای خلاصه نود را با استفاده از
[cAdvisor](https://github.com/google/cadvisor) تعبیه‌شده‌ای که درون kubelet اجرا می‌شود، دریافت می‌کند. اگر
`PodAndContainerStatsFromCRI` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/)
را در کلاستر خود فعال کنید و از یک container runtime استفاده کنید که دسترسی به آمار را از طریق
{{< glossary_tooltip term_id="cri" text="Container Runtime Interface">}} (CRI) پشتیبانی می‌کند، آنگاه
kubelet [داده‌های معیارهای سطح Pod و کانتینر را با استفاده از CRI دریافت می‌کند](/docs/reference/instrumentation/cri-pod-container-metrics) و نه از طریق cAdvisor.

## Pressure Stall Information (PSI) {#psi}

{{< feature-state feature_gate_name="KubeletPSI" >}}

به‌عنوان یک قابلیت پایدار، کوبرنتیز به شما امکان می‌دهد kubelet را طوری پیکربندی کنید که
[Pressure Stall Information](https://docs.kernel.org/accounting/psi.html)
(PSI) هسته لینوکس را برای میزان استفاده از CPU، حافظه و I/O گردآوری کند. این اطلاعات در سطح نود، Pod و کانتینر گردآوری می‌شود.
برای مشاهده طرح‌واره (schema) کامل، به [Summary API](/docs/reference/kubelet-api/stats.v1alpha1/) مراجعه کنید.
از کوبرنتیز نسخه v1.36 به بعد، `KubeletPSI` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) روی true قفل شده است و نمی‌توان آن را غیرفعال کرد. این اطلاعات همچنین در
[معیارهای Prometheus](/docs/concepts/cluster-administration/system-metrics#psi-metrics) ارائه می‌شود.

می‌توانید یاد بگیرید معیارهای PSI را چگونه تفسیر کنید، در [درک معیارهای PSI](/docs/reference/instrumentation/understand-psi-metrics/).

### الزامات {#requirements}

Pressure Stall Information به موارد زیر نیاز دارد:

- [هسته لینوکس نسخه 4.20 یا بالاتر](/docs/reference/node/kernel-version-requirements#requirements-psi).
- [cgroup v2](/docs/concepts/architecture/cgroups)

## {{% heading "whatsnext" %}}

صفحات وظیفه [عیب‌یابی کلاسترها](/docs/tasks/debug/debug-cluster/) نحوه استفاده از یک خط لوله معیارها (metrics pipeline) را که به این داده‌ها متکی است، شرح می‌دهند.
