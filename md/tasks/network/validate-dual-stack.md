---
reviewers:
- lachie83
- khenidak
- bridgetkromhout
min-kubernetes-server-version: v1.23
title: اعتبارسنجی دوپشته‌ای IPv4/IPv6
content_type: task
---

<!-- overview -->
این سند نحوهٔ اعتبارسنجی کلاسترهای کوبرنتیز را که دوپشته‌ای (dual-stack) IPv4/IPv6 در آن‌ها فعال است، شرح می‌دهد.

## {{% heading "prerequisites" %}}

* پشتیبانی ارائه‌دهنده از شبکه‌بندی دوپشته‌ای (ارائه‌دهندهٔ ابری یا هر ارائه‌دهندهٔ دیگری باید بتواند
  نودهای کوبرنتیز را با رابط‌های شبکهٔ IPv4/IPv6 قابل‌مسیریابی فراهم کند)
* یک [افزونهٔ شبکه](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
  که از شبکه‌بندی دوپشته‌ای پشتیبانی کند.
* کلاستری که [دوپشته‌ای در آن فعال باشد](/docs/concepts/services-networking/dual-stack/)

{{< version-check >}}

{{< note >}}
هرچند می‌توانید با نسخه‌ای قدیمی‌تر نیز اعتبارسنجی را انجام دهید، این قابلیت تنها از نسخهٔ v1.23 به وضعیت GA رسیده و به‌طور رسمی پشتیبانی می‌شود.
{{< /note >}}

<!-- steps -->

## اعتبارسنجی آدرس‌دهی

### اعتبارسنجی آدرس‌دهی نود

به هر Node دوپشته‌ای باید یک بلوک IPv4 و یک بلوک IPv6 تخصیص داده شده باشد.
با اجرای دستور زیر، بررسی کنید که بازه‌های آدرس Pod برای IPv4/IPv6 پیکربندی شده باشند.
نام نود نمونه را با نام یک Node دوپشته‌ای معتبر از کلاستر خود جایگزین کنید. در این مثال،
نام Node برابر با `k8s-linuxpool1-34450317-0` است:

```shell
kubectl get nodes k8s-linuxpool1-34450317-0 -o go-template --template='{{range .spec.podCIDRs}}{{printf "%s\n" .}}{{end}}'
```

```
10.244.1.0/24
2001:db8::/64
```

باید یک بلوک IPv4 و یک بلوک IPv6 تخصیص داده شده باشد.

بررسی کنید که یک رابط IPv4 و یک رابط IPv6 برای نود شناسایی شده باشد.
نام نود را با نام یک نود معتبر از کلاستر جایگزین کنید.
در این مثال، نام نود `k8s-linuxpool1-34450317-0` است:

```shell
kubectl get nodes k8s-linuxpool1-34450317-0 -o go-template --template='{{range .status.addresses}}{{printf "%s: %s\n" .type .address}}{{end}}'
```

```
Hostname: k8s-linuxpool1-34450317-0
InternalIP: 10.0.0.5
InternalIP: 2001:db8:10::5
```

### اعتبارسنجی آدرس‌دهی Pod

بررسی کنید که به Pod یک آدرس IPv4 و یک آدرس IPv6 اختصاص داده شده باشد. نام Pod را با
نام یک Pod معتبر در کلاستر خود جایگزین کنید. در این مثال، نام Pod برابر با `pod01` است:

```shell
kubectl get pods pod01 -o go-template --template='{{range .status.podIPs}}{{printf "%s\n" .ip}}{{end}}'
```

```
10.244.1.4
2001:db8::4
```

همچنین می‌توانید IPهای Pod را با استفاده از Downward API و از طریق fieldPath با مقدار `status.podIPs` اعتبارسنجی کنید.
قطعه‌کد زیر نشان می‌دهد که چگونه می‌توانید IPهای Pod را از طریق یک متغیر محیطی
به نام `MY_POD_IPS` در داخل یک کانتینر در دسترس قرار دهید.

```yaml
        env:
        - name: MY_POD_IPS
          valueFrom:
            fieldRef:
              fieldPath: status.podIPs
```

دستور زیر مقدار متغیر محیطی `MY_POD_IPS` را از داخل یک کانتینر چاپ می‌کند.
این مقدار فهرستی جداشده با ویرگول است که با آدرس‌های IPv4 و IPv6 مربوط به Pod
متناظر است.

```shell
kubectl exec -it pod01 -- set | grep MY_POD_IPS
```

```
MY_POD_IPS=10.244.1.4,2001:db8::4
```

آدرس‌های IP مربوط به Pod در فایل `/etc/hosts` داخل کانتینر نیز نوشته می‌شوند.
دستور زیر فرمان cat را روی فایل `/etc/hosts` در یک Pod دوپشته‌ای اجرا می‌کند.
با بررسی خروجی می‌توانید هر دو آدرس IPv4 و IPv6 مربوط به Pod را تأیید کنید.

```shell
kubectl exec -it pod01 -- cat /etc/hosts
```

```
# Kubernetes-managed hosts file.
127.0.0.1    localhost
::1    localhost ip6-localhost ip6-loopback
fe00::0    ip6-localnet
fe00::0    ip6-mcastprefix
fe00::1    ip6-allnodes
fe00::2    ip6-allrouters
10.244.1.4    pod01
2001:db8::4    pod01
```

## اعتبارسنجی Serviceها

Service زیر را که فیلد `.spec.ipFamilyPolicy` را به‌طور صریح تعریف نمی‌کند، ایجاد کنید.
کوبرنتیز یک cluster IP از نخستین بازهٔ پیکربندی‌شده در `service-cluster-ip-range`
به این Service اختصاص می‌دهد و مقدار `.spec.ipFamilyPolicy` را برابر با `SingleStack` قرار می‌دهد.

{{% code_sample file="service/networking/dual-stack-default-svc.yaml" %}}

با استفاده از `kubectl`، YAML این Service را مشاهده کنید.

```shell
kubectl get svc my-service -o yaml
```

در این Service، مقدار `.spec.ipFamilyPolicy` برابر با `SingleStack` است و مقدار `.spec.clusterIP`
یک آدرس IPv4 از نخستین بازهٔ پیکربندی‌شده است که از طریق فلگ `--service-cluster-ip-range`
در kube-controller-manager تعیین شده است.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
  namespace: default
spec:
  clusterIP: 10.0.217.164
  clusterIPs:
  - 10.0.217.164
  ipFamilies:
  - IPv4
  ipFamilyPolicy: SingleStack
  ports:
  - port: 80
    protocol: TCP
    targetPort: 9376
  selector:
    app.kubernetes.io/name: MyApp
  sessionAffinity: None
  type: ClusterIP
status:
  loadBalancer: {}
```

Service زیر را که `IPv6` را به‌طور صریح به‌عنوان نخستین عنصر آرایهٔ `.spec.ipFamilies`
تعریف می‌کند، ایجاد کنید. کوبرنتیز یک cluster IP از بازهٔ IPv6 پیکربندی‌شده در
`service-cluster-ip-range` به این Service اختصاص می‌دهد و مقدار `.spec.ipFamilyPolicy` را برابر با `SingleStack` قرار می‌دهد.

{{% code_sample file="service/networking/dual-stack-ipfamilies-ipv6.yaml" %}}

با استفاده از `kubectl`، YAML این Service را مشاهده کنید.

```shell
kubectl get svc my-service -o yaml
```

در این Service، مقدار `.spec.ipFamilyPolicy` برابر با `SingleStack` است و مقدار `.spec.clusterIP`
یک آدرس IPv6 از بازهٔ IPv6 است که از طریق فلگ `--service-cluster-ip-range` در kube-controller-manager تعیین شده است.

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/name: MyApp
  name: my-service
spec:
  clusterIP: 2001:db8:fd00::5118
  clusterIPs:
  - 2001:db8:fd00::5118
  ipFamilies:
  - IPv6
  ipFamilyPolicy: SingleStack
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app.kubernetes.io/name: MyApp
  sessionAffinity: None
  type: ClusterIP
status:
  loadBalancer: {}
```

Service زیر را که مقدار `PreferDualStack` را به‌طور صریح در `.spec.ipFamilyPolicy` تعریف می‌کند، ایجاد کنید.
کوبرنتیز هر دو آدرس IPv4 و IPv6 را اختصاص می‌دهد (زیرا دوپشته‌ای در این کلاستر فعال است) و
مقدار `.spec.ClusterIP` را بر اساس خانوادهٔ آدرسِ نخستین عنصر آرایهٔ `.spec.ipFamilies`
از میان فهرست `.spec.ClusterIPs` انتخاب می‌کند.

{{% code_sample file="service/networking/dual-stack-preferred-svc.yaml" %}}

{{< note >}}
دستور `kubectl get svc` فقط IP اصلی را در فیلد `CLUSTER-IP` نشان می‌دهد.

```shell
kubectl get svc -l app.kubernetes.io/name=MyApp
```

```
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
my-service   ClusterIP   10.0.216.242   <none>        80/TCP    5s
```
{{< /note >}}

با استفاده از `kubectl describe` بررسی کنید که Service، cluster IPهای خود را از بلوک‌های آدرس IPv4 و IPv6
دریافت کرده باشد. سپس می‌توانید دسترسی به سرویس را از طریق IPها و پورت‌ها اعتبارسنجی کنید.

```shell
kubectl describe svc -l app.kubernetes.io/name=MyApp
```

```
Name:              my-service
Namespace:         default
Labels:            app.kubernetes.io/name=MyApp
Annotations:       <none>
Selector:          app.kubernetes.io/name=MyApp
Type:              ClusterIP
IP Family Policy:  PreferDualStack
IP Families:       IPv4,IPv6
IP:                10.0.216.242
IPs:               10.0.216.242,2001:db8:fd00::af55
Port:              <unset>  80/TCP
TargetPort:        9376/TCP
Endpoints:         <none>
Session Affinity:  None
Events:            <none>
```

### ایجاد یک Service دوپشته‌ای با توزیع بار

اگر ارائه‌دهندهٔ ابری از ایجاد توزیع‌کننده‌های بار خارجی با قابلیت IPv6 پشتیبانی می‌کند،
Service زیر را با مقدار `PreferDualStack` در `.spec.ipFamilyPolicy`، مقدار `IPv6` به‌عنوان
نخستین عنصر آرایهٔ `.spec.ipFamilies` و فیلد `type` با مقدار `LoadBalancer` ایجاد کنید.

{{% code_sample file="service/networking/dual-stack-prefer-ipv6-lb-svc.yaml" %}}

Service را بررسی کنید:

```shell
kubectl get svc -l app.kubernetes.io/name=MyApp
```

بررسی کنید که Service یک آدرس `CLUSTER-IP` از بلوک آدرس IPv6 به همراه یک `EXTERNAL-IP`
دریافت کرده باشد. سپس می‌توانید دسترسی به سرویس را از طریق IP و پورت اعتبارسنجی کنید.

```
NAME         TYPE           CLUSTER-IP            EXTERNAL-IP        PORT(S)        AGE
my-service   LoadBalancer   2001:db8:fd00::7ebc   2603:1030:805::5   80:30790/TCP   35s
```
