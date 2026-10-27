---
reviewers:
- sftim
- thockin
title: تخصیص ClusterIP به Service
content_type: concept
weight: 120
---


<!-- overview -->

در کوبرنتیز، [Serviceها](/docs/concepts/services-networking/service/) روشی انتزاعی برای در دسترس قرار دادن
برنامه‌ای هستند که روی مجموعه‌ای از Podها اجرا می‌شود. Serviceها
می‌توانند یک نشانی IP مجازی با دامنهٔ کل کلاستر داشته باشند (با استفاده از Serviceای از نوع `type: ClusterIP`).
کلاینت‌ها می‌توانند با استفاده از آن نشانی IP مجازی متصل شوند و سپس کوبرنتیز ترافیک آن
Service را میان Podهای پشتیبان مختلف توزیع بار (load-balance) می‌کند.

<!-- body -->

## ClusterIPهای Service چگونه تخصیص داده می‌شوند؟

هنگامی که کوبرنتیز باید یک نشانی IP مجازی به یک Service اختصاص دهد،
این تخصیص به یکی از دو روش زیر انجام می‌شود:

_به‌صورت پویا_
: control plane کلاستر به‌طور خودکار یک نشانی IP آزاد را از درون بازهٔ IP پیکربندی‌شده برای Serviceهای `type: ClusterIP` انتخاب می‌کند.

_به‌صورت ایستا_
: شما نشانی IP دلخواه خود را از درون بازهٔ IP پیکربندی‌شده برای Serviceها تعیین می‌کنید.

در سراسر کلاستر شما، `ClusterIP` هر Service باید یکتا باشد.
تلاش برای ایجاد یک Service با `ClusterIP` مشخصی که پیش‌تر
تخصیص داده شده است، به خطا منجر می‌شود.

## چرا باید ClusterIPهای Service را رزرو کنید؟

گاهی ممکن است بخواهید Serviceها روی نشانی‌های IP شناخته‌شده اجرا شوند تا سایر مؤلفه‌ها و
کاربران کلاستر بتوانند از آن‌ها استفاده کنند.

بهترین نمونه، Service مربوط به DNS کلاستر است. طبق یک قرارداد غیرالزامی، برخی نصب‌کننده‌های کوبرنتیز دهمین نشانی IP
از بازهٔ IP مربوط به Serviceها را به سرویس DNS اختصاص می‌دهند. با فرض اینکه کلاستر خود را با بازهٔ IP سرویس
10.96.0.0/16 پیکربندی کرده‌اید و می‌خواهید نشانی IP سرویس DNS شما 10.96.0.10 باشد، باید Serviceای مانند
زیر ایجاد کنید:

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    k8s-app: kube-dns
    kubernetes.io/cluster-service: "true"
    kubernetes.io/name: CoreDNS
  name: kube-dns
  namespace: kube-system
spec:
  clusterIP: 10.96.0.10
  ports:
  - name: dns
    port: 53
    protocol: UDP
    targetPort: 53
  - name: dns-tcp
    port: 53
    protocol: TCP
    targetPort: 53
  selector:
    k8s-app: kube-dns
  type: ClusterIP
```

اما همان‌طور که پیش‌تر توضیح داده شد، نشانی IP ‏10.96.0.10 رزرو نشده است.
اگر Serviceهای دیگری پیش از آن یا هم‌زمان با تخصیص پویا ایجاد شوند، این احتمال وجود دارد که این IP را به خود اختصاص دهند.
در نتیجه، نخواهید توانست Service مربوط به DNS را ایجاد کنید، زیرا با خطای تعارض (conflict) با شکست مواجه می‌شود.

## چگونه می‌توان از تعارض ClusterIPهای Service جلوگیری کرد؟ {#avoid-ClusterIP-conflict}

راهبرد تخصیصی که کوبرنتیز برای اختصاص ClusterIP به Serviceها پیاده‌سازی کرده است، خطر
برخورد (collision) را کاهش می‌دهد.

بازهٔ `ClusterIP` بر اساس فرمول `min(max(16, cidrSize / 16), 256)` تقسیم می‌شود
که به این صورت توصیف می‌شود: _هرگز کمتر از ۱۶ یا بیشتر از ۲۵۶ نیست و میان این دو، گامی تدریجی دارد_.

تخصیص پویای IP به‌طور پیش‌فرض از باند بالایی استفاده می‌کند و پس از پر شدن آن،
از بازهٔ پایینی استفاده خواهد کرد. این کار به کاربران اجازه می‌دهد با خطر برخورد کم،
از تخصیص‌های ایستا در باند پایینی استفاده کنند.

## نمونه‌ها {#allocation-examples}

### نمونهٔ ۱ {#allocation-example-1}

این نمونه از بازهٔ نشانی IP ‏10.96.0.0/24 (با نمادگذاری CIDR) برای نشانی‌های IP
مربوط به Serviceها استفاده می‌کند.

اندازهٔ بازه: 2<sup>8</sup> - 2 = 254  
آفست باند: `min(max(16, 256/16), 256)` = `min(16, 256)` = 16  
شروع باند ایستا: 10.96.0.1  
پایان باند ایستا: 10.96.0.16  
پایان بازه: 10.96.0.254   

{{< mermaid >}}
pie showData
    title 10.96.0.0/24
    "Static" : 16
    "Dynamic" : 238
{{< /mermaid >}}

### نمونهٔ ۲ {#allocation-example-2}

این نمونه از بازهٔ نشانی IP ‏10.96.0.0/20 (با نمادگذاری CIDR) برای نشانی‌های IP
مربوط به Serviceها استفاده می‌کند.

اندازهٔ بازه: 2<sup>12</sup> - 2 = 4094  
آفست باند: `min(max(16, 4096/16), 256)` = `min(256, 256)` = 256  
شروع باند ایستا: 10.96.0.1  
پایان باند ایستا: 10.96.1.0  
پایان بازه: 10.96.15.254  

{{< mermaid >}}
pie showData
    title 10.96.0.0/20
    "Static" : 256
    "Dynamic" : 3838
{{< /mermaid >}}

### نمونهٔ ۳ {#allocation-example-3}

این نمونه از بازهٔ نشانی IP ‏10.96.0.0/16 (با نمادگذاری CIDR) برای نشانی‌های IP
مربوط به Serviceها استفاده می‌کند.

اندازهٔ بازه: 2<sup>16</sup> - 2 = 65534  
آفست باند: `min(max(16, 65536/16), 256)` = `min(4096, 256)` = 256  
شروع باند ایستا: 10.96.0.1  
پایان باند ایستا: 10.96.1.0  
پایان بازه: 10.96.255.254  

{{< mermaid >}}
pie showData
    title 10.96.0.0/16
    "Static" : 256
    "Dynamic" : 65278
{{< /mermaid >}}

## {{% heading "whatsnext" %}}

* دربارهٔ [سیاست ترافیک خارجی Service](/docs/tasks/access-application-cluster/create-external-load-balancer/#preserving-the-client-source-ip) بخوانید
* دربارهٔ [اتصال برنامه‌ها با Serviceها](/docs/tutorials/services/connect-applications-service/) بخوانید
* دربارهٔ [Serviceها](/docs/concepts/services-networking/service/) بخوانید
