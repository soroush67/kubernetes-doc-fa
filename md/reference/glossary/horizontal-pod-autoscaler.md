---
title: Horizontal Pod Autoscaler
id: horizontal-pod-autoscaler
full_link: docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
short_description: >
  آبجکتی که تعداد رپلیکاهای پاد را بر اساس میزان بهره‌وری هدف از منابع یا اهداف معیارهای سفارشی، به‌طور خودکار مقیاس‌دهی می‌کند.

aka: 
- HPA
tags:
- operation
---
یک {{< glossary_tooltip text="آبجکت" term_id="object" >}} که تعداد رپلیکاهای {{< glossary_tooltip term_id="pod" >}} را بر اساس میزان بهره‌وری هدف از {{< glossary_tooltip text="منابع" term_id="infrastructure-resource" >}} یا اهداف معیارهای سفارشی، به‌طور خودکار مقیاس‌دهی می‌کند.

<!--more--> 

معمولاً HorizontalPodAutoscaler (HPA) همراه با {{< glossary_tooltip text="Deploymentها" term_id="deployment" >}} یا {{< glossary_tooltip text="ReplicaSetها" term_id="replica-set" >}} استفاده می‌شود. این آبجکت را نمی‌توان روی آبجکت‌هایی که قابلیت مقیاس‌دهی ندارند، مانند {{< glossary_tooltip text="DaemonSetها" term_id="daemonset" >}}، اعمال کرد.
