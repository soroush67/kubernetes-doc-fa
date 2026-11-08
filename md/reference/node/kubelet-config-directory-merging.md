---
content_type: "reference"
title: ادغام پیکربندی kubelet از دایرکتوری
weight: 50
---

وقتی با فلگ `--config-dir` در kubelet یک دایرکتوری drop-in برای پیکربندی مشخص می‌کنید، انواع مختلف داده به شیوه‌های خاصی با یکدیگر ادغام می‌شوند.

در ادامه، با چند مثال می‌بینید که انواع مختلف داده هنگام ادغام پیکربندی چگونه رفتار می‌کنند:

### فیلدهای ساختاری
در یک ساختار YAML، دو نوع فیلد ساختاری وجود دارد: فیلدهای منفرد (یا از نوع اسکالر) و فیلدهای تودرتو (ساختارهایی که خود شامل انواع اسکالر هستند). فرایند ادغام پیکربندی، فیلدهای منفرد و فیلدهای ساختاری تودرتو را بازنویسی می‌کند و از این راه پیکربندی نهایی kubelet را می‌سازد.

برای نمونه، ممکن است بخواهید برای همهٔ نودها یک پیکربندی پایهٔ kubelet داشته باشید، اما فیلدهای `address` و `authorization` را سفارشی کنید. این کار را می‌توان به شکل زیر انجام داد:

محتوای فایل اصلی پیکربندی kubelet:
```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
port: 20250
authorization:
  mode: Webhook
  webhook:
    cacheAuthorizedTTL: "5m"
    cacheUnauthorizedTTL: "30s"
serializeImagePulls: false
address: "192.168.0.1"
```

محتوای یک فایل در دایرکتوری `--config-dir`:
```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
authorization:
  mode: AlwaysAllow
  webhook:
    cacheAuthorizedTTL: "8m"
    cacheUnauthorizedTTL: "45s"
address: "192.168.0.8"
```

پیکربندی نهایی به این شکل خواهد بود:
```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
port: 20250
serializeImagePulls: false
authorization:
  mode: AlwaysAllow
  webhook:
    cacheAuthorizedTTL: "8m"
    cacheUnauthorizedTTL: "45s"
address: "192.168.0.8"
```

### فهرست‌ها
می‌توانید مقادیر برش‌ها/فهرست‌های (slices/lists) پیکربندی kubelet را بازنویسی کنید، اما در فرایند ادغام، کل فهرست جایگزین می‌شود. برای مثال، فهرست `clusterDNS` را می‌توان به شکل زیر بازنویسی کرد:

محتوای فایل اصلی پیکربندی kubelet:
```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
port: 20250
serializeImagePulls: false
clusterDNS:
  - "192.168.0.9"
  - "192.168.0.8"
```

محتوای یک فایل در دایرکتوری `--config-dir`:
```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
clusterDNS:
  - "192.168.0.2"
  - "192.168.0.3"
  - "192.168.0.5"
```

پیکربندی نهایی به این شکل خواهد بود:
```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
port: 20250
serializeImagePulls: false
clusterDNS:
  - "192.168.0.2"
  - "192.168.0.3"
  - "192.168.0.5"
```

### نگاشت‌ها، از جمله ساختارهای تودرتو

فیلدهای یک نگاشت (map) را، فارغ از نوع مقدارشان (بولی، رشته و غیره)، می‌توان به‌صورت جداگانه و انتخابی بازنویسی کرد. با این حال، در نوع `map[string][]string` کل فهرست مربوط به هر فیلد جایگزین می‌شود. برای درک بهتر این موضوع، به مثال زیر دربارهٔ فیلدهایی مانند `featureGates` و `staticPodURLHeader` توجه کنید:

محتوای فایل اصلی پیکربندی kubelet:
```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
port: 20250
serializeImagePulls: false
featureGates:
  AllAlpha: false
  MemoryQoS: true
staticPodURLHeader:
  kubelet-api-support:
  - "Authorization: 234APSDFA"
  - "X-Custom-Header: 123"
  custom-static-pod:
  - "Authorization: 223EWRWER"
  - "X-Custom-Header: 456"
```

محتوای یک فایل در دایرکتوری `--config-dir`:
```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
featureGates:
  MemoryQoS: false
  KubeletTracing: true
  DynamicResourceAllocation: true
staticPodURLHeader:
  custom-static-pod:
  - "Authorization: 223EWRWER"
  - "X-Custom-Header: 345"
```

پیکربندی نهایی به این شکل خواهد بود:
```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
port: 20250
serializeImagePulls: false
featureGates:
  AllAlpha: false
  MemoryQoS: false
  KubeletTracing: true
  DynamicResourceAllocation: true
staticPodURLHeader:
  kubelet-api-support:
  - "Authorization: 234APSDFA"
  - "X-Custom-Header: 123"
  custom-static-pod:
  - "Authorization: 223EWRWER"
  - "X-Custom-Header: 345"
```
