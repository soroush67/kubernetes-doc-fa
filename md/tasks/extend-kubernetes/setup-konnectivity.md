---
title: راه‌اندازی سرویس Konnectivity
content_type: task
weight: 70
---

<!-- overview -->

سرویس Konnectivity یک پراکسی در سطح TCP برای ارتباط control plane با کلاستر فراهم می‌کند.

## {{% heading "prerequisites" %}}

باید یک کلاستر کوبرنتیز داشته باشید و ابزار خط فرمان kubectl نیز طوری پیکربندی شده باشد که بتواند با کلاستر شما ارتباط برقرار کند. توصیه می‌شود این آموزش را روی کلاستری اجرا کنید که دست‌کم دو نود داشته باشد که نقش میزبان control plane را ندارند. اگر هنوز کلاستری ندارید، می‌توانید با استفاده از [minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/) یک کلاستر بسازید.

<!-- steps -->

## پیکربندی سرویس Konnectivity

برای انجام مراحل زیر به یک پیکربندی ترافیک خروجی (egress) نیاز دارید؛ برای نمونه:

{{% code_sample file="admin/konnectivity/egress-selector-configuration.yaml" %}}

باید API Server را طوری پیکربندی کنید که از سرویس Konnectivity استفاده کند و ترافیک شبکه را به نودهای کلاستر هدایت کند:

1. مطمئن شوید که قابلیت [Service Account Token Volume Projection](/docs/tasks/configure-pod-container/configure-service-account/#serviceaccount-token-volume-projection) در کلاستر شما فعال است. این قابلیت از نسخهٔ v1.20 کوبرنتیز به‌طور پیش‌فرض فعال است.
1. یک فایل پیکربندی ترافیک خروجی، مانند `admin/konnectivity/egress-selector-configuration.yaml`، ایجاد کنید.
1. مقدار فلگ `--egress-selector-config-file` در API Server را برابر با مسیر فایل پیکربندی ترافیک خروجی API Server قرار دهید.
1. اگر از اتصال UDS استفاده می‌کنید، پیکربندی حجم‌ها (volumes) را به kube-apiserver اضافه کنید:
   ```yaml
   spec:
     containers:
       volumeMounts:
       - name: konnectivity-uds
         mountPath: /etc/kubernetes/konnectivity-server
         readOnly: false
     volumes:
     - name: konnectivity-uds
       hostPath:
         path: /etc/kubernetes/konnectivity-server
         type: DirectoryOrCreate
   ```

برای konnectivity-server یک گواهی و یک فایل kubeconfig تولید یا تهیه کنید. برای نمونه، می‌توانید با ابزار خط فرمان OpenSSL و با استفاده از گواهی CA کلاستر، یعنی `/etc/kubernetes/pki/ca.crt`، روی یکی از میزبان‌های control plane یک گواهی X.509 صادر کنید.

```bash
openssl req -subj "/CN=system:konnectivity-server" -new -newkey rsa:2048 -noenc -out konnectivity.csr -keyout konnectivity.key
openssl x509 -req -in konnectivity.csr -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -out konnectivity.crt -days 375 -sha256
SERVER=$(kubectl config view -o jsonpath='{.clusters..server}')
kubectl --kubeconfig /etc/kubernetes/konnectivity-server.conf config set-credentials system:konnectivity-server --client-certificate konnectivity.crt --client-key konnectivity.key --embed-certs=true
kubectl --kubeconfig /etc/kubernetes/konnectivity-server.conf config set-cluster kubernetes --server "$SERVER" --certificate-authority /etc/kubernetes/pki/ca.crt --embed-certs=true
kubectl --kubeconfig /etc/kubernetes/konnectivity-server.conf config set-context system:konnectivity-server@kubernetes --cluster kubernetes --user system:konnectivity-server
kubectl --kubeconfig /etc/kubernetes/konnectivity-server.conf config use-context system:konnectivity-server@kubernetes
rm -f konnectivity.crt konnectivity.key konnectivity.csr
```

در گام بعد، باید سرور و عامل‌های (agents) Konnectivity را مستقر کنید. پروژهٔ [kubernetes-sigs/apiserver-network-proxy](https://github.com/kubernetes-sigs/apiserver-network-proxy) یک پیاده‌سازی مرجع برای این کار است.

سرور Konnectivity را روی نود control plane خود مستقر کنید. مانیفست `konnectivity-server.yaml` که در اینجا ارائه شده است، فرض می‌کند که مؤلفه‌های کوبرنتیز در کلاستر شما به‌صورت {{< glossary_tooltip text="Pod ایستا"
term_id="static-pod" >}} مستقر شده‌اند. در غیر این صورت، می‌توانید سرور Konnectivity را به‌صورت یک DaemonSet مستقر کنید.

{{% code_sample file="admin/konnectivity/konnectivity-server.yaml" %}}

سپس عامل‌های Konnectivity را در کلاستر خود مستقر کنید:

{{% code_sample file="admin/konnectivity/konnectivity-agent.yaml" %}}

در پایان، اگر RBAC در کلاستر شما فعال است، قواعد RBAC مربوط را ایجاد کنید:

{{% code_sample file="admin/konnectivity/konnectivity-rbac.yaml" %}}
