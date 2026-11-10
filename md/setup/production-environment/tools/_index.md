---
title: نصب کوبرنتیز با ابزارهای استقرار
weight: 30
no_list: true
---

روش‌ها و ابزارهای زیادی برای راه‌اندازی کلاستر کوبرنتیز عملیاتی (production) خودتان وجود دارد.
برای مثال:

- [kubeadm](/docs/setup/production-environment/tools/kubeadm/)

- [Cluster API](https://cluster-api.sigs.k8s.io/): زیرپروژه‌ای از کوبرنتیز که بر فراهم‌کردن APIها و ابزارهای اعلانی (declarative) تمرکز دارد تا آماده‌سازی، ارتقا و راهبری چندین کلاستر کوبرنتیز را ساده کند.
  
- [kops](https://kops.sigs.k8s.io/): ابزاری خودکار برای آماده‌سازی کلاستر.
  برای دیدن آموزش‌ها، بهترین شیوه‌ها، گزینه‌های پیکربندی و اطلاعات مربوط به
  ارتباط با جامعه، لطفاً جزئیات را در
  [وب‌سایت `kOps`](https://kops.sigs.k8s.io/) ببینید.

- [kubespray](https://kubespray.io/):
  مجموعه‌ای از playbookهای [Ansible](https://docs.ansible.com/)،
  [فهرست میزبان‌ها (inventory)](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/ansible/inventory.md)،
  ابزارهای آماده‌سازی و دانش تخصصی برای انجام وظایف مدیریت پیکربندی سیستم‌عامل و کلاسترهای کوبرنتیز
  به‌صورت عمومی. می‌توانید از طریق کانال
  [#kubespray](https://kubernetes.slack.com/messages/kubespray/) در Slack با جامعه در ارتباط باشید.
