---
title: صفحه‌های z در کوبرنتیز
content_type: reference
weight: 60
reviewers:
- dashpole
description: >-
  اطلاعات عیب‌یابی زمان اجرا را برای مؤلفه‌های کوبرنتیز فراهم می‌کند و دیدی از وضعیت زمان اجرا و فلگ‌های پیکربندی هر مؤلفه ارائه می‌دهد.
---


<!-- overview -->

{{< feature-state for_k8s_version="v1.36" state="beta" >}}

مؤلفه‌های اصلی کوبرنتیز می‌توانند مجموعه‌ای از _نقاط پایانی z_ (z-endpoints) را در دسترس قرار دهند تا کاربران راحت‌تر بتوانند کلاستر و مؤلفه‌های آن را عیب‌یابی کنند. این نقاط پایانی فقط برای بررسی انسانی در نظر گرفته شده‌اند و اطلاعات عیب‌یابی بی‌درنگ دربارهٔ فایل اجرایی یک مؤلفه ارائه می‌دهند. در کوبرنتیز {{< skew currentVersion >}} این قابلیت‌ها در مرحلهٔ **بتا** هستند.

<!-- body -->

## z-pages

در کوبرنتیز نسخهٔ v{{< skew currentVersion >}} می‌توانید _صفحه‌های z_ (z-pages) را فعال کنید تا مشکلات مؤلفه‌های اصلی control plane را راحت‌تر عیب‌یابی کنید. این نقاط پایانی ویژهٔ عیب‌یابی، اطلاعات داخلی مؤلفه‌های در حال اجرا را ارائه می‌دهند. در کوبرنتیز {{< skew currentVersion >}}، مؤلفه‌ها (در صورت فعال بودن) نقاط پایانی زیر را ارائه می‌کنند:

- [صفحه‌های z](#z-pages)
	- [statusz](#statusz)
		- [پاسخ ساختاریافتهٔ statusz](#statusz-structured)
	- [flagz](#flagz)
		- [پاسخ ساختاریافتهٔ flagz](#flagz-structured)

### statusz

نقطهٔ پایانی `/statusz` با [feature gate](/docs/reference/command-line-tools-reference/feature-gates#ComponentStatusz) با نام `ComponentStatusz` فعال می‌شود و اطلاعات کلی مؤلفه، از جمله نسخهٔ کوبرنتیز، نسخهٔ شبیه‌سازی‌شده، زمان شروع و موارد دیگر را نمایش می‌دهد.

پاسخ متنی سادهٔ `/statusz` از سرور API مشابه زیر است:

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

#### پاسخ ساختاریافتهٔ statusz

{{< feature-state feature_gate_name="ComponentStatusz" >}}

از کوبرنتیز نسخهٔ v1.35، نقطهٔ پایانی `/statusz` در صورتی که با سرآیند `Accept` مناسب درخواست شود، از قالب پاسخ ساختاریافته و نسخه‌دار پشتیبانی می‌کند. اگر سرآیند `Accept` ارسال نشود، این نقطهٔ پایانی به‌طور پیش‌فرض پاسخ را در قالب متن ساده برمی‌گرداند.

برای درخواست پاسخ ساختاریافته، از سرآیند زیر استفاده کنید:
```
Accept: application/json;v=v1beta1;g=config.k8s.io;as=Statusz
```

{{< note >}}
اگر `application/json` را بدون مشخص کردن همهٔ پارامترهای الزامی (`g`، `v` و `as`) درخواست کنید، سرور با `406 Not Acceptable` پاسخ می‌دهد.
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

طرح‌وارهٔ `config.k8s.io/v1beta1` برای پاسخ ساختاریافتهٔ `/statusz` به شکل زیر است:

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

### flagz

نقطهٔ پایانی `/flagz` با [feature gate](/docs/reference/command-line-tools-reference/feature-gates#ComponentFlagz) با نام `ComponentFlagz` فعال می‌شود و آرگومان‌های خط فرمانی را که مؤلفه با آن‌ها اجرا شده است نشان می‌دهد.

{{< note >}}
نقطهٔ پایانی `/flagz` فلگ‌های خط فرمان و مقادیر پیش‌فرض آن‌ها را گزارش می‌کند. در مؤلفه‌هایی که فایل‌های پیکربندی را نیز بارگذاری می‌کنند، مانند kubelet و kube-proxy، پیکربندی مؤثر در حال اجرا ممکن است با خروجی `/flagz` متفاوت باشد. در این موارد، اگر نقطهٔ پایانی `/configz` در دسترس است، برای بررسی پیکربندی ادغام‌شدهٔ مؤلفه از آن استفاده کنید.
{{< /note >}}

پاسخ متنی سادهٔ `/flagz` از سرور API تقریباً به شکل زیر است:

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

#### پاسخ ساختاریافتهٔ flagz

{{< feature-state feature_gate_name="ComponentFlagz" >}}

از کوبرنتیز نسخهٔ v1.35، نقطهٔ پایانی `/flagz` در صورتی که با سرآیند `Accept` مناسب درخواست شود، از قالب پاسخ ساختاریافته و نسخه‌دار پشتیبانی می‌کند. اگر سرآیند `Accept` ارسال نشود، این نقطهٔ پایانی به‌طور پیش‌فرض پاسخ را در قالب متن ساده برمی‌گرداند.

برای درخواست پاسخ ساختاریافته، از سرآیند زیر استفاده کنید:
```
Accept: application/json;v=v1beta1;g=config.k8s.io;as=Flagz
```

{{< note >}}
اگر `application/json` را بدون مشخص کردن همهٔ پارامترهای الزامی (`g`، `v` و `as`) درخواست کنید، سرور با `406 Not Acceptable` پاسخ می‌دهد.
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

طرح‌وارهٔ `config.k8s.io/v1beta1` برای پاسخ ساختاریافتهٔ `/flagz` به شکل زیر است:

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
پاسخ‌های ساختاریافتهٔ `/statusz` و `/flagz` هر دو در نسخهٔ v1.36 قابلیت‌هایی در مرحلهٔ بتا هستند. هدف از این پاسخ‌ها، فراهم کردن خروجی قابل پردازش با ماشین برای ابزارهای عیب‌یابی و درون‌نگری است.
{{< /note >}}
