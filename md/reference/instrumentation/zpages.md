---
title: z-pages کوبرنتیز
content_type: reference
weight: 60
reviewers:
- dashpole
description: >-
  تشخیص‌های زمان اجرا را برای مؤلفه‌های کوبرنتیز فراهم می‌کند و دید روشنی از وضعیت زمان اجرا و فلگ‌های پیکربندی مؤلفه ارائه می‌دهد.
---


<!-- overview -->

{{< feature-state for_k8s_version="v1.36" state="beta" >}}

مؤلفه‌های اصلی کوبرنتیز می‌توانند مجموعه‌ای از _z-endpointها_ را در دسترس قرار دهند تا کاربران
بتوانند راحت‌تر کلاستر و مؤلفه‌های آن را اشکال‌زدایی کنند. این اندپوینت‌ها صرفاً برای بررسی توسط انسان در نظر گرفته شده‌اند
تا اطلاعات اشکال‌زدایی بی‌درنگ از یک فایل باینری مؤلفه به دست آید.
در کوبرنتیز {{< skew currentVersion >}} این قابلیت‌ها **بتا** هستند.

<!-- body -->

## z-pages {#z-pages}

کوبرنتیز v{{< skew currentVersion >}} به شما امکان می‌دهد _z-pages_ را فعال کنید تا در عیب‌یابی
مشکلات مؤلفه‌های اصلی control plane کمک بگیرید. این اندپوینت‌های اشکال‌زدایی ویژه، اطلاعات داخلی
مربوط به مؤلفه‌های در حال اجرا را ارائه می‌دهند. در کوبرنتیز {{< skew currentVersion >}}، مؤلفه‌ها
اندپوینت‌های زیر را (در صورت فعال بودن) ارائه می‌کنند:

- [z-pages](#z-pages)
	- [statusz](#statusz)
		- [statusz (structured)](#statusz-structured)
	- [flagz](#flagz)
		- [flagz (structured)](#flagz-structured)

### statusz {#statusz}

اندپوینت `/statusz` که با استفاده از [feature gate](/docs/reference/command-line-tools-reference/feature-gates#ComponentStatusz) با نام `ComponentStatusz` فعال می‌شود،
اطلاعات سطح بالایی درباره مؤلفه، مانند نسخه کوبرنتیز، نسخه شبیه‌سازی (emulation version)، زمان شروع و موارد دیگر را نمایش می‌دهد.

پاسخ متنی ساده `/statusz` از API server مشابه نمونه زیر است:

```
kube-apiserver statusz
Warning: This endpoint is not meant to be machine parseable, has no formatting compatibility guarantees and is for debugging purposes only.

Started: Wed Oct 16 21:03:43 UTC 2024
Up: 0 hr 00 min 16 sec
Go version: go1.23.2
Binary version: 1.32.0-alpha.0.1484&#43;5eeac4f21a491b-dirty
Emulation version: 1.32.0-alpha.0.1484
Paths: /healthz /livez /metrics /readyz /statusz /version
```

#### statusz (structured) {#statusz-structured}

{{< feature-state feature_gate_name="ComponentStatusz" >}}

از کوبرنتیز v1.35 به بعد، اندپوینت `/statusz` در صورتی که با هدر `Accept` مناسب درخواست شود،
قالب پاسخ ساختاریافته و نسخه‌دار را پشتیبانی می‌کند.
اگر هدر `Accept` ارسال نشود، اندپوینت به‌طور پیش‌فرض پاسخ را در قالب متن ساده برمی‌گرداند.

برای درخواست پاسخ ساختاریافته از این مقدار استفاده کنید:
```
Accept: application/json;v=v1beta1;g=config.k8s.io;as=Statusz
```

{{< note >}}
اگر `application/json` را بدون مشخص کردن همه پارامترهای لازم (`g`، `v` و `as`) درخواست کنید،
سرور با کد `406 Not Acceptable` پاسخ می‌دهد.
{{< /note >}}

نمونه‌ای از پاسخ ساختاریافته:
```json
{
  "kind": "Statusz",
  "apiVersion": "config.k8s.io/v1beta1",
  "metadata": {
    "name": "kube-apiserver"
  },
  "startTime": "2025-10-29T00:30:01Z",
  "uptimeSeconds": 856,
  "goVersion": "go1.23.2",
  "binaryVersion": "1.35.0",
  "emulationVersion": "1.35",
  "paths": [
    "/healthz",
    "/livez",
    "/metrics",
    "/readyz",
    "/statusz",
    "/version"
  ]
}
```

طرحواره `config.k8s.io/v1beta1` برای پاسخ ساختاریافته `/statusz` به شرح زیر است:

```go
// Statusz is the config.k8s.io/v1beta1 schema for the /statusz endpoint.
type Statusz struct {
	// Kind is "Statusz".
	Kind string `json:"kind"`
	// APIVersion is the version of the object, e.g., "config.k8s.io/v1beta1".
	APIVersion string `json:"apiVersion"`
	// Standard object's metadata.
	// +optional
	Metadata metav1.ObjectMeta `json:"metadata,omitempty"`
	// StartTime is the time the component process was initiated.
	StartTime metav1.Time `json:"startTime"`
	// UptimeSeconds is the duration in seconds for which the component has been running continuously.
	UptimeSeconds int64 `json:"uptimeSeconds"`
	// GoVersion is the version of the Go programming language used to build the binary.
	// The format is not guaranteed to be consistent across different Go builds.
	// +optional
	GoVersion string `json:"goVersion,omitempty"`
	// BinaryVersion is the version of the component's binary.
	// The format is not guaranteed to be semantic versioning and may be an arbitrary string.
	BinaryVersion string `json:"binaryVersion"`
	// EmulationVersion is the Kubernetes API version which this component is emulating.
	// if present, formatted as "<major>.<minor>"
	// +optional
	EmulationVersion string `json:"emulationVersion,omitempty"`
	// MinimumCompatibilityVersion is the minimum Kubernetes API version with which the component is designed to work.
	// if present, formatted as "<major>.<minor>"
	// +optional
	MinimumCompatibilityVersion string `json:"minimumCompatibilityVersion,omitempty"`
	// Paths contains relative URLs to other essential read-only endpoints for debugging and troubleshooting.
	// +optional
	Paths []string `json:"paths,omitempty"`
}
```

### flagz {#flagz}

اندپوینت `/flagz` که با استفاده از [feature gate](/docs/reference/command-line-tools-reference/feature-gates#ComponentFlagz) با نام `ComponentFlagz` فعال می‌شود، آرگومان‌های خط فرمانی را که برای راه‌اندازی یک مؤلفه استفاده شده‌اند نمایش می‌دهد.

{{< note >}}
`/flagz` فلگ‌های خط فرمان و مقادیر پیش‌فرض را گزارش می‌کند. در مؤلفه‌هایی که فایل‌های پیکربندی نیز بارگذاری می‌کنند، مانند kubelet و kube-proxy، پیکربندی مؤثر در حال اجرا ممکن است با `/flagz` متفاوت باشد؛ برای بررسی پیکربندی ادغام‌شده مؤلفه، در صورت وجود از `/configz` استفاده کنید.
{{< /note >}}

پاسخ متنی ساده `/flagz` از API server تقریباً به این شکل است:

```
kube-apiserver flags
Warning: This endpoint is not meant to be machine parseable, has no formatting compatibility guarantees and is for debugging purposes only.

advertise-address=192.168.8.2
contention-profiling=false
enable-priority-and-fairness=true
profiling=true
authorization-mode=[Node,RBAC]
authorization-webhook-cache-authorized-ttl=5m0s
authorization-webhook-cache-unauthorized-ttl=30s
authorization-webhook-version=v1beta1
default-watch-cache-size=100
```

#### flagz (structured) {#flagz-structured}

{{< feature-state feature_gate_name="ComponentFlagz" >}}

از کوبرنتیز v1.35 به بعد، اندپوینت `/flagz` در صورتی که با هدر `Accept` مناسب درخواست شود،
قالب پاسخ ساختاریافته و نسخه‌دار را پشتیبانی می‌کند.
اگر هدر `Accept` ارسال نشود، اندپوینت به‌طور پیش‌فرض پاسخ را در قالب متن ساده برمی‌گرداند.

برای درخواست پاسخ ساختاریافته از این مقدار استفاده کنید:
```
Accept: application/json;v=v1beta1;g=config.k8s.io;as=Flagz
```

{{< note >}}
اگر `application/json` را بدون مشخص کردن همه پارامترهای لازم (`g`، `v` و `as`) درخواست کنید،
سرور با کد `406 Not Acceptable` پاسخ می‌دهد.
{{< /note >}}

نمونه‌ای از پاسخ ساختاریافته:
```json
{
  "kind": "Flagz",
  "apiVersion": "config.k8s.io/v1beta1",
  "metadata": {
    "name": "kube-apiserver"
  },
  "flags": {
    "advertise-address": "192.168.8.4",
    "allow-privileged": "true",
    "anonymous-auth": "true",
    "authorization-mode": "[Node,RBAC]",
    "enable-priority-and-fairness": "true",
    "profiling": "true",
    "default-watch-cache-size": "100"
  }
}
```

طرحواره `config.k8s.io/v1beta1` برای پاسخ ساختاریافته `/flagz` به شرح زیر است:

```go
// Flagz is the config.k8s.io/v1beta1 schema for the /flagz endpoint.
type Flagz struct {
	// Kind is "Flagz".
	Kind string `json:"kind"`
	// APIVersion is the version of the object, e.g., "config.k8s.io/v1beta1".
	APIVersion string `json:"apiVersion"`
	// Standard object's metadata.
	// +optional
	Metadata metav1.ObjectMeta `json:"metadata,omitempty"`
	// Flags contains the command-line flags and their values.
	// The keys are the flag names and the values are the flag values,
	// possibly with confidential values redacted.
	// +optional
	Flags map[string]string `json:"flags,omitempty"`
}
```

{{< note >}}
پاسخ‌های ساختاریافته برای هر دو اندپوینت `/statusz` و `/flagz` در نسخه v1.36 قابلیت‌های بتا هستند.
هدف از آن‌ها ارائه خروجی قابل پردازش توسط ماشین برای ابزارهای اشکال‌زدایی و بررسی وضعیت درونی است.
{{< /note >}}
