---
title: پیکربندی ارائه‌دهندهٔ اعتبارنامهٔ ایمیج برای kubelet
reviewers:
- liggitt
- cheftako
content_type: task
min-kubernetes-server-version: v1.26
weight: 120
---

{{< feature-state for_k8s_version="v1.26" state="stable" >}}

<!-- overview -->

از نسخهٔ v1.20 کوبرنتیز به بعد، kubelet می‌تواند اعتبارنامه‌های (credentials) یک رجیستری ایمیج کانتینر را به‌صورت پویا و با استفاده از افزونه‌های exec دریافت کند. ارتباط kubelet و افزونهٔ exec از طریق stdio (یعنی stdin، stdout و stderr) و با استفاده از APIهای نسخه‌دار کوبرنتیز برقرار می‌شود. این افزونه‌ها به kubelet امکان می‌دهند به‌جای ذخیرهٔ اعتبارنامه‌های ثابت روی دیسک، اعتبارنامهٔ رجیستری کانتینر را به‌صورت پویا درخواست کند. برای مثال، افزونه می‌تواند با یک سرور فرادادهٔ محلی ارتباط برقرار کند تا اعتبارنامه‌های کوتاه‌مدت را برای ایمیجی که kubelet در حال دریافت (pull) آن است، به دست آورد.

اگر هر یک از موارد زیر در مورد شما صدق می‌کند، احتمالاً استفاده از این قابلیت برایتان مفید خواهد بود:

* برای دریافت اطلاعات احراز هویت یک رجیستری، باید سرویس یک ارائه‌دهندهٔ ابری را از طریق API فراخوانی کنید.
* اعتبارنامه‌ها مدت انقضای کوتاهی دارند و باید مرتباً اعتبارنامهٔ جدید درخواست شود.
* ذخیرهٔ اعتبارنامه‌های رجیستری روی دیسک یا در imagePullSecrets پذیرفتنی نیست.

این راهنما نحوهٔ پیکربندی سازوکار افزونهٔ ارائه‌دهندهٔ اعتبارنامهٔ ایمیج در kubelet را نشان می‌دهد.

## توکن حساب سرویس برای دریافت ایمیج‌ها
{{< feature-state feature_gate_name="KubeletServiceAccountTokenForCredentialProviders" >}}

از نسخهٔ v1.33 کوبرنتیز به بعد، می‌توان kubelet را طوری پیکربندی کرد که توکن حساب سرویس (service account) مقیدشده به پادی را که ایمیج برای آن دریافت می‌شود، به افزونهٔ ارائه‌دهندهٔ اعتبارنامه بفرستد.

به این ترتیب، افزونه می‌تواند این توکن را با اعتبارنامه‌های لازم برای دسترسی به رجیستری ایمیج مبادله کند.

برای فعال‌کردن این قابلیت، باید feature gate با نام `KubeletServiceAccountTokenForCredentialProviders` روی kubelet فعال شود و فیلد `tokenAttributes` نیز در فایل `CredentialProviderConfig` برای آن افزونه تنظیم شده باشد.

فیلد `tokenAttributes` اطلاعاتی دربارهٔ توکن حساب سرویسی که به افزونه ارسال می‌شود در بر دارد؛ از جمله مخاطب (audience) موردنظر توکن و اینکه آیا افزونه الزام می‌کند پاد حساب سرویس داشته باشد یا نه.

استفاده از اعتبارنامه‌های مبتنی بر توکن حساب سرویس، موارد استفادهٔ زیر را ممکن می‌کند:

* دیگر برای دریافت ایمیج از رجیستری به هویتی مبتنی بر kubelet یا نود نیازی نیست.
* بارهای کاری می‌توانند بر اساس هویت زمان اجرای خودشان و بدون نیاز به Secretهای بلندمدت یا ماندگار، ایمیج‌ها را دریافت کنند.

## {{% heading "prerequisites" %}}

* به یک کلاستر کوبرنتیز نیاز دارید که نودهای آن از افزونه‌های ارائه‌دهندهٔ اعتبارنامهٔ kubelet پشتیبانی کنند. این پشتیبانی در کوبرنتیز {{< skew currentVersion >}} وجود دارد؛ در کوبرنتیز v1.24 و v1.25 این قابلیت به‌صورت بتا و به‌طور پیش‌فرض فعال ارائه شده بود.
* اگر افزونهٔ ارائه‌دهندهٔ اعتبارنامه‌ای را پیکربندی می‌کنید که به توکن حساب سرویس نیاز دارد، به یک کلاستر کوبرنتیز نیاز دارید که نودهای آن کوبرنتیز v1.33 یا بالاتر را اجرا کنند و feature gate با نام `KubeletServiceAccountTokenForCredentialProviders` روی kubelet آن‌ها فعال باشد.
* یک پیاده‌سازی کارآمد از افزونهٔ exec ارائه‌دهندهٔ اعتبارنامه. می‌توانید افزونهٔ خودتان را بسازید یا از افزونه‌ای استفاده کنید که ارائه‌دهندگان ابری عرضه می‌کنند.

{{< version-check >}}

<!-- steps -->

## نصب افزونه‌ها روی نودها

افزونهٔ ارائه‌دهندهٔ اعتبارنامه یک فایل باینری اجرایی است که kubelet آن را اجرا می‌کند. مطمئن شوید که باینری افزونه روی تک‌تک نودهای کلاستر شما وجود دارد و در یک پوشهٔ مشخص ذخیره شده است. بعداً هنگام پیکربندی فلگ‌های kubelet به مسیر این پوشه نیاز خواهید داشت.

## پیکربندی kubelet

برای استفاده از این قابلیت، kubelet انتظار دارد دو فلگ زیر تنظیم شده باشند:

* `--image-credential-provider-config`: مسیر فایل پیکربندی افزونهٔ ارائه‌دهندهٔ اعتبارنامه.
* `--image-credential-provider-bin-dir`: مسیر پوشه‌ای که باینری‌های افزونه‌های ارائه‌دهندهٔ اعتبارنامه در آن قرار دارند.

### پیکربندی ارائه‌دهندهٔ اعتبارنامهٔ kubelet

kubelet فایل پیکربندی‌ای را که به `--image-credential-provider-config` داده می‌شود می‌خواند تا مشخص کند کدام افزونه‌های exec باید برای کدام ایمیج‌های کانتینر فراخوانی شوند. در ادامه نمونه‌ای از فایل پیکربندی آمده است که اگر از [افزونهٔ مبتنی بر ECR](https://github.com/kubernetes/cloud-provider-aws/tree/master/cmd/ecr-credential-provider) استفاده کنید، احتمالاً به چیزی شبیه آن خواهید رسید:

```yaml
apiVersion: kubelet.config.k8s.io/v1
kind: CredentialProviderConfig
# providers is a list of credential provider helper plugins that will be enabled by the kubelet.
# Multiple providers may match against a single image, in which case credentials
# from all providers will be returned to the kubelet. If multiple providers are called
# for a single image, the results are combined. If providers return overlapping
# auth keys, the value from the provider earlier in this list is used.
providers:
  # name is the required name of the credential provider. It must match the name of the
  # provider executable as seen by the kubelet. The executable must be in the kubelet's
  # bin directory (set by the --image-credential-provider-bin-dir flag).
  - name: ecr-credential-provider
    # matchImages is a required list of strings used to match against images in order to
    # determine if this provider should be invoked. If one of the strings matches the
    # requested image from the kubelet, the plugin will be invoked and given a chance
    # to provide credentials. Images are expected to contain the registry domain
    # and URL path.
    #
    # Each entry in matchImages is a pattern which can optionally contain a port and a path.
    # Globs can be used in the domain, but not in the port or the path. Globs are supported
    # as subdomains like '*.k8s.io' or 'k8s.*.io', and top-level-domains such as 'k8s.*'.
    # Matching partial subdomains like 'app*.k8s.io' is also supported. Each glob can only match
    # a single subdomain segment, so `*.io` does **not** match `*.k8s.io`.
    #
    # A match exists between an image and a matchImage when all of the below are true:
    # - Both contain the same number of domain parts and each part matches.
    # - The URL path of an matchImages must be a prefix of the target image URL path.
    # - If the matchImages contains a port, then the port must match in the image as well.
    #
    # Example values of matchImages:
    # - 123456789.dkr.ecr.us-east-1.amazonaws.com
    # - *.azurecr.io
    # - gcr.io
    # - *.*.registry.io
    # - registry.io:8080/path
    matchImages:
      - "*.dkr.ecr.*.amazonaws.com"
      - "*.dkr.ecr.*.amazonaws.com.cn"
      - "*.dkr.ecr-fips.*.amazonaws.com"
      - "*.dkr.ecr.us-iso-east-1.c2s.ic.gov"
      - "*.dkr.ecr.us-isob-east-1.sc2s.sgov.gov"
    # defaultCacheDuration is the default duration the plugin will cache credentials in-memory
    # if a cache duration is not provided in the plugin response. This field is required.
    defaultCacheDuration: "12h"
    # Required input version of the exec CredentialProviderRequest. The returned CredentialProviderResponse
    # MUST use the same encoding version as the input. Current supported values are:
    # - credentialprovider.kubelet.k8s.io/v1
    apiVersion: credentialprovider.kubelet.k8s.io/v1
    # Arguments to pass to the command when executing it.
    # +optional
    # args:
    #   - --example-argument
    # Env defines additional environment variables to expose to the process. These
    # are unioned with the host's environment, as well as variables client-go uses
    # to pass argument to the plugin.
    # +optional
    env:
      - name: AWS_PROFILE
        value: example_profile

    # tokenAttributes is the configuration for the service account token that will be passed to the plugin.
    # The credential provider opts in to using service account tokens for image pull by setting this field.
    # if this field is set without the `KubeletServiceAccountTokenForCredentialProviders` feature gate enabled, 
    # kubelet will fail to start with invalid configuration error.
    # +optional
    tokenAttributes:
      # serviceAccountTokenAudience is the intended audience for the projected service account token.
      # +required
      serviceAccountTokenAudience: "<audience for the token>"
      # cacheType indicates the type of cache key use for caching the credentials returned by the plugin
      # when the service account token is used.
      # The most conservative option is to set this to "Token", which means the kubelet will cache
      # returned credentials on a per-token basis. This should be set if the returned credential's
      # lifetime is limited to the service account token's lifetime.
      # If the plugin's credential retrieval logic depends only on the service account and not on
      # pod-specific claims, then the plugin can set this to "ServiceAccount". In this case, the
      # kubelet will cache returned credentials on a per-serviceaccount basis. Use this when the
      # returned credential is valid for all pods using the same service account.
      # +required
      cacheType: "<Token or ServiceAccount>"
      # requireServiceAccount indicates whether the plugin requires the pod to have a service account.
      # If set to true, kubelet will only invoke the plugin if the pod has a service account.
      # If set to false, kubelet will invoke the plugin even if the pod does not have a service account
      # and will not include a token in the CredentialProviderRequest. This is useful for plugins
      # that are used to pull images for pods without service accounts (e.g., static pods).
      # +required
      requireServiceAccount: true
      # requiredServiceAccountAnnotationKeys is the list of annotation keys that the plugin is interested in
      # and that are required to be present in the service account.
      # The keys defined in this list will be extracted from the corresponding service account and passed
      # to the plugin as part of the CredentialProviderRequest. If any of the keys defined in this list
      # are not present in the service account, kubelet will not invoke the plugin and will return an error.
      # This field is optional and may be empty. Plugins may use this field to extract additional information
      # required to fetch credentials or allow workloads to opt in to using service account tokens for image pull.
      # If non-empty, requireServiceAccount must be set to true.
      # The keys defined in this list must be unique and not overlap with the keys defined in the
      # optionalServiceAccountAnnotationKeys list.
      # +optional
      requiredServiceAccountAnnotationKeys:
      - "example.com/required-annotation-key-1"
      - "example.com/required-annotation-key-2"
      # optionalServiceAccountAnnotationKeys is the list of annotation keys that the plugin is interested in
      # and that are optional to be present in the service account.
      # The keys defined in this list will be extracted from the corresponding service account and passed
      # to the plugin as part of the CredentialProviderRequest. The plugin is responsible for validating the
      # existence of annotations and their values. This field is optional and may be empty.
      # Plugins may use this field to extract additional information required to fetch credentials.
      # The keys defined in this list must be unique and not overlap with the keys defined in the
      # requiredServiceAccountAnnotationKeys list.
      # +optional
      optionalServiceAccountAnnotationKeys:
      - "example.com/optional-annotation-key-1"
      - "example.com/optional-annotation-key-2"
```

فیلد `providers` فهرستی از افزونه‌های فعالی است که kubelet از آن‌ها استفاده می‌کند. هر مدخل چند فیلد الزامی دارد:

* `name`: نام افزونه که حتماً باید با نام باینری اجرایی موجود در پوشهٔ داده‌شده به `--image-credential-provider-bin-dir` یکسان باشد.
* `matchImages`: فهرستی از رشته‌ها که برای تطبیق با ایمیج‌ها به کار می‌رود تا مشخص شود آیا این ارائه‌دهنده باید فراخوانی شود یا نه. توضیحات بیشتر در ادامه آمده است.
* `defaultCacheDuration`: مدت زمان پیش‌فرضی که kubelet اعتبارنامه‌ها را در حافظه کش می‌کند، در صورتی که افزونه مدت کش را مشخص نکرده باشد.
* `apiVersion`: نسخهٔ API که kubelet و افزونهٔ exec هنگام ارتباط با یکدیگر از آن استفاده می‌کنند.

برای هر ارائه‌دهندهٔ اعتبارنامه می‌توان آرگومان‌ها و متغیرهای محیطی اختیاری نیز تعیین کرد. برای اطلاع از اینکه یک افزونهٔ مشخص به چه آرگومان‌ها و متغیرهای محیطی‌ای نیاز دارد، به پیاده‌سازان آن افزونه مراجعه کنید.

اگر از feature gate با نام KubeletServiceAccountTokenForCredentialProviders استفاده می‌کنید و با تنظیم فیلد tokenAttributes، افزونه را برای استفاده از توکن حساب سرویس پیکربندی می‌کنید، فیلدهای زیر الزامی هستند:

* `serviceAccountTokenAudience`:
  مخاطب موردنظر برای توکن حساب سرویس تصویرشده (projected).
  این مقدار نمی‌تواند رشتهٔ خالی باشد.
  هنگامی که [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `ServiceAccountNodeAudienceRestriction` فعال است،
  kubelet باید مجوز درخواست توکن برای این مخاطب را داشته باشد؛
  در غیر این صورت، ارائه‌دهندهٔ اعتبارنامه فراخوانی نمی‌شود. باید از طریق RBAC
  به گروه `system:nodes` اجازهٔ استفاده از فعل `request-serviceaccounts-token-audience` را روی این مخاطب بدهید.
  برای جزئیات و نمونه‌ها، به
  [محدودسازی مخاطب توکن حساب سرویس](/docs/reference/access-authn-authz/node/#service-account-token-audience-restriction) مراجعه کنید.
* `cacheType`:
  نوع کلید کشی که برای کش‌کردن اعتبارنامه‌های بازگشتی افزونه، هنگام استفاده از توکن حساب سرویس، به کار می‌رود.
  محافظه‌کارانه‌ترین گزینه، تنظیم این مقدار روی `Token` است؛
  یعنی kubelet اعتبارنامه‌های بازگشتی را به‌ازای هر توکن کش می‌کند.
  اگر طول عمر اعتبارنامهٔ بازگشتی به طول عمر توکن حساب سرویس محدود است، باید از این گزینه استفاده شود.
  اگر منطق دریافت اعتبارنامه در افزونه فقط به حساب سرویس وابسته باشد و به ادعاهای (claims) مختص پاد وابسته نباشد،
  افزونه می‌تواند این مقدار را روی `ServiceAccount` تنظیم کند.
  در این حالت، kubelet اعتبارنامه‌های بازگشتی را به‌ازای هر حساب سرویس کش می‌کند.
  زمانی از این گزینه استفاده کنید که اعتبارنامهٔ بازگشتی برای همهٔ پادهایی که از یک حساب سرویس مشترک استفاده می‌کنند معتبر باشد.
* `requireServiceAccount`:
  مشخص می‌کند که آیا افزونه الزام می‌کند پاد حساب سرویس داشته باشد یا نه.
  * اگر روی `true` تنظیم شود، kubelet فقط در صورتی افزونه را فراخوانی می‌کند
که پاد حساب سرویس داشته باشد.
  * اگر روی `false` تنظیم شود، kubelet افزونه را حتی اگر پاد حساب سرویس نداشته باشد
فراخوانی می‌کند و توکنی در `CredentialProviderRequest` قرار نمی‌دهد.

این حالت برای افزونه‌هایی مفید است که برای دریافت ایمیج پادهای فاقد حساب سرویس
(مانند پادهای ایستا)
به کار می‌روند.

#### پیکربندی تطبیق ایمیج

kubelet از فیلد `matchImages` هر ارائه‌دهندهٔ اعتبارنامه استفاده می‌کند تا تعیین کند آیا یک افزونه باید برای ایمیجی که یک Pod از آن استفاده می‌کند فراخوانی شود یا نه. هر مدخل در `matchImages` یک الگوی ایمیج است که می‌تواند به‌صورت اختیاری شامل پورت و مسیر باشد. الگوهای glob را می‌توان در دامنه به کار برد، اما نه در پورت یا مسیر. این الگوها به‌صورت زیردامنه، مانند `*.k8s.io` یا `k8s.*.io`، و همچنین به‌صورت دامنهٔ سطح بالا، مانند `k8s.*`، پشتیبانی می‌شوند. تطبیق بخشی از زیردامنه، مانند `app*.k8s.io`، نیز پشتیبانی می‌شود. هر glob فقط با یک بخش از زیردامنه تطبیق پیدا می‌کند؛ بنابراین `*.io` با `*.k8s.io` تطبیق **ندارد**.

تطبیق میان نام یک ایمیج و یک مدخل `matchImage` زمانی برقرار است که همهٔ شرایط زیر برقرار باشند:

* هر دو تعداد یکسانی بخش دامنه داشته باشند و تک‌تک بخش‌ها با هم تطبیق کنند.
* مسیر URL الگوی تطبیق باید پیشوندی از مسیر URL ایمیج هدف باشد.
* اگر matchImages شامل پورت باشد، پورت ایمیج نیز باید با آن تطبیق داشته باشد.

چند نمونه از مقادیر الگوهای `matchImages`:

* `123456789.dkr.ecr.us-east-1.amazonaws.com`
* `*.azurecr.io`
* `gcr.io`
* `*.*.registry.io`
* `foo.registry.io:8080/path`

## {{% heading "whatsnext" %}}

* جزئیات مربوط به `CredentialProviderConfig` را در
  [مرجع API پیکربندی kubelet (v1)](/docs/reference/config-api/kubelet-config.v1/) بخوانید.
* [مرجع API ارائه‌دهندهٔ اعتبارنامهٔ kubelet (v1)](/docs/reference/config-api/kubelet-credentialprovider.v1/) را بخوانید.
