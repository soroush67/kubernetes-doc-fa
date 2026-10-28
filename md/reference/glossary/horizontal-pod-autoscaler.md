---
title: Horizontal Pod Autoscaler
id: horizontal-pod-autoscaler
full_link: docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
short_description: >
  آبجکتی که تعداد replicaهای پاد را بر اساس میزان مصرف منابع هدف یا اهداف معیارهای سفارشی به‌طور خودکار مقیاس‌دهی می‌کند.

aka: 
- HPA
tags:
- operation
---
یک {{< glossary_tooltip text="آبجکت" term_id="object" >}} که تعداد replicaهای {{< glossary_tooltip term_id="pod" >}} را بر اساس میزان مصرف {{< glossary_tooltip text="منبع" term_id="infrastructure-resource" >}} هدف یا اهداف معیارهای سفارشی، به‌طور خودکار مقیاس‌دهی می‌کند.

<!--more--> 

HorizontalPodAutoscaler (HPA) معمولاً همراه با {{< glossary_tooltip text="Deploymentها" term_id="deployment" >}} یا {{< glossary_tooltip text="ReplicaSetها" term_id="replica-set" >}} به کار می‌رود. این آبجکت را نمی‌توان روی آبجکت‌هایی که قابلیت مقیاس‌دهی ندارند، مانند {{< glossary_tooltip text="DaemonSetها" term_id="daemonset" >}}، اعمال کرد.
