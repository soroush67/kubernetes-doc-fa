---
reviewers:
- caseydavenport
title: استفاده از Calico برای NetworkPolicy
content_type: task
weight: 20
---

<!-- overview -->
این صفحه چند روش سریع برای ایجاد یک کلاستر Calico روی کوبرنتیز را نشان می‌دهد.


## {{% heading "prerequisites" %}}

ابتدا تصمیم بگیرید که می‌خواهید یک کلاستر [ابری](#creating-a-calico-cluster-with-google-kubernetes-engine-gke) مستقر کنید یا یک کلاستر [محلی](#creating-a-local-calico-cluster-with-kubeadm).


<!-- steps -->
## ایجاد یک کلاستر Calico با Google Kubernetes Engine (GKE)

**پیش‌نیاز**: [gcloud](https://cloud.google.com/sdk/docs/quickstarts).

1.  برای راه‌اندازی یک کلاستر GKE همراه با Calico، فلگ `--enable-network-policy` را به فرمان اضافه کنید.

    **نحو**
    ```shell
    gcloud container clusters create [CLUSTER_NAME] --enable-network-policy
    ```

    **مثال**
    ```shell
    gcloud container clusters create my-calico-cluster --enable-network-policy
    ```

1.  برای بررسی صحت استقرار، از فرمان زیر استفاده کنید.

    ```shell
    kubectl get pods --namespace=kube-system
    ```

    نام Podهای Calico با `calico` شروع می‌شود. بررسی کنید که وضعیت همهٔ آن‌ها `Running` باشد.

## ایجاد یک کلاستر Calico محلی با kubeadm

برای راه‌اندازی یک کلاستر Calico محلی و تک‌میزبانی با kubeadm در پانزده دقیقه، به
[راهنمای شروع سریع Calico](https://projectcalico.docs.tigera.io/getting-started/kubernetes/) مراجعه کنید.




## {{% heading "whatsnext" %}}

پس از آنکه کلاستر شما اجرا شد، می‌توانید راهنمای [اعلان سیاست شبکه](/docs/tasks/administer-cluster/declare-network-policy/) را دنبال کنید تا NetworkPolicy کوبرنتیز را امتحان کنید.
