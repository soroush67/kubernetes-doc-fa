---
title: "راهنمای سخت‌سازی - پیکربندی زمان‌بند"
description: >
    اطلاعاتی دربارهٔ نحوهٔ ایمن‌تر کردن زمان‌بند کوبرنتیز.
content_type: concept
weight: 90
---

<!-- overview -->
{{< glossary_tooltip text="زمان‌بند" term_id="kube-scheduler" >}} کوبرنتیز
یکی از مؤلفه‌های حیاتی
{{< glossary_tooltip text="control plane" term_id="control-plane" >}} است.

این سند نحوهٔ بهبود وضعیت امنیتی زمان‌بند را پوشش می‌دهد.

زمان‌بندی که به‌درستی پیکربندی نشده باشد می‌تواند پیامدهای امنیتی داشته باشد.
چنین زمان‌بندی می‌تواند نودهای مشخصی را هدف قرار دهد و بارهای کاری یا برنامه‌هایی را که نود و منابع آن را به اشتراک می‌گذارند بیرون براند.
این امر می‌تواند به مهاجم در اجرای یک [حملهٔ Yo-Yo](https://arxiv.org/abs/2105.00542) کمک کند: حمله‌ای به یک مقیاس‌دهندهٔ خودکار آسیب‌پذیر.

<!-- body -->
## پیکربندی kube-scheduler

### گزینه‌های خط فرمان احراز هویت و مجوزدهی زمان‌بند

هنگام تنظیم پیکربندی احراز هویت، باید اطمینان حاصل شود که
احراز هویت kube-scheduler با احراز هویت kube-api-server سازگار باقی می‌ماند.
اگر درخواستی فاقد سرآیندهای احراز هویت باشد، احراز هویت باید از طریق kube-api-server انجام شود
تا [همهٔ احراز هویت‌ها در کلاستر سازگار باشند](/docs/tasks/extend-kubernetes/configure-aggregation-layer/#original-request-username-and-group).

- `authentication-kubeconfig`: اطمینان حاصل کنید که یک kubeconfig مناسب ارائه می‌کنید تا
  زمان‌بند بتواند گزینه‌های پیکربندی احراز هویت را از API Server بازیابی کند.
  این فایل kubeconfig باید با مجوزهای فایل سخت‌گیرانه محافظت شود.
- `authentication-tolerate-lookup-failure`: این گزینه را روی `false` تنظیم کنید تا اطمینان حاصل شود
  زمان‌بند _همیشه_ پیکربندی احراز هویت خود را از API server جست‌وجو می‌کند.
- `authentication-skip-lookup`: این گزینه را روی `false` تنظیم کنید تا اطمینان حاصل شود
  زمان‌بند _همیشه_ پیکربندی احراز هویت خود را از API server جست‌وجو می‌کند.
- `authorization-always-allow-paths`: این مسیرها باید با داده‌هایی پاسخ دهند که برای
  مجوزدهی ناشناس مناسب باشند. مقدار پیش‌فرض `/healthz,/readyz,/livez` است.
- `profiling`: آن را روی `false` تنظیم کنید تا endpointهای profiling غیرفعال شوند؛ این endpointها اطلاعات اشکال‌زدایی فراهم می‌کنند
  اما نباید در کلاسترهای تولیدی فعال باشند، زیرا خطر حملهٔ منع سرویس
  یا نشت اطلاعات را به همراه دارند. آرگومان `--profiling` منسوخ شده است و اکنون می‌توان آن را از طریق
  [DebuggingConfiguration مربوط به KubeScheduler](/docs/reference/config-api/kube-scheduler-config.v1/#DebuggingConfiguration) ارائه کرد.
  profiling را می‌توان از طریق پیکربندی kube-scheduler و با تنظیم `enableProfiling` روی `false` غیرفعال کرد.
- `requestheader-client-ca-file`: از ارسال این آرگومان خودداری کنید.

### گزینه‌های خط فرمان شبکهٔ زمان‌بند

- `bind-address`: در بیشتر موارد، kube-scheduler نیازی به دسترس‌پذیری از بیرون ندارد.
  تنظیم نشانی bind روی `localhost` یک رویهٔ ایمن است.
- `permit-address-sharing`: این گزینه را روی `false` تنظیم کنید تا اشتراک اتصال از طریق `SO_REUSEADDR` غیرفعال شود.
  `SO_REUSEADDR` می‌تواند به استفادهٔ مجدد از اتصال‌های خاتمه‌یافته‌ای که در وضعیت `TIME_WAIT` هستند منجر شود.
- `permit-port-sharing`: مقدار پیش‌فرض `false` است. از مقدار پیش‌فرض استفاده کنید، مگر اینکه مطمئن باشید پیامدهای امنیتی آن را درک می‌کنید.

### گزینه‌های خط فرمان TLS زمان‌بند

- `tls-cipher-suites`: همیشه فهرستی از مجموعه‌های رمز (cipher suite) ترجیحی ارائه کنید.
  این کار تضمین می‌کند که رمزگذاری هرگز با مجموعه‌های رمز ناامن انجام نشود.

## پیکربندی‌های زمان‌بندی برای زمان‌بندهای سفارشی

هنگام استفاده از زمان‌بندهای سفارشی مبتنی بر کد زمان‌بندی کوبرنتیز، مدیران کلاستر باید مراقب
افزونه‌هایی باشند که از [نقاط توسعهٔ](/docs/reference/scheduling/config/#extension-points) `queueSort`، `prefilter`، `filter` یا `permit` استفاده می‌کنند.
این نقاط توسعه مراحل مختلف یک فرایند زمان‌بندی را کنترل می‌کنند،
و پیکربندی نادرست می‌تواند بر رفتار kube-scheduler در کلاستر شما تأثیر بگذارد.

### ملاحظات کلیدی

- در هر زمان دقیقاً یک افزونه که از نقطهٔ توسعهٔ `queueSort` استفاده می‌کند می‌تواند فعال باشد.
  هر افزونه‌ای که از `queueSort` استفاده می‌کند باید به‌دقت بررسی شود.
- افزونه‌هایی که نقطهٔ توسعهٔ `prefilter` یا `filter` را پیاده‌سازی می‌کنند به‌طور بالقوه می‌توانند همهٔ نودها را غیرقابل زمان‌بندی علامت‌گذاری کنند.
  این امر می‌تواند زمان‌بندی پادهای جدید را متوقف کند.
- افزونه‌هایی که نقطهٔ توسعهٔ `permit` را پیاده‌سازی می‌کنند می‌توانند از اتصال (binding) یک Pod جلوگیری کنند یا آن را به تأخیر بیندازند.
  چنین افزونه‌هایی باید به‌طور کامل توسط مدیر کلاستر بازبینی شوند.

هنگام استفاده از افزونه‌ای که جزو [افزونه‌های پیش‌فرض](/docs/reference/scheduling/config/#scheduling-plugins) نیست،
غیرفعال کردن نقاط توسعهٔ `queueSort`، `filter` و `permit` را به شکل زیر در نظر بگیرید:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
  - schedulerName: my-scheduler
    plugins:
      # Disable specific plugins for different extension points
      # You can disable all plugins for an extension point using "*"
      queueSort:
        disabled:
        - name: "*"             # Disable all queueSort plugins
      # - name: "PrioritySort"  # Disable specific queueSort plugin
      filter:
        disabled:
        - name: "*"                 # Disable all filter plugins
      # - name: "NodeResourcesFit"  # Disable specific filter plugin
      permit:
        disabled:
        - name: "*"               # Disables all permit plugins
      # - name: "TaintToleration" # Disable specific permit plugin
```
این پیکربندی یک پروفایل زمان‌بند با نام ` my-scheduler` ایجاد می‌کند.
هر زمان که `.spec` یک Pod مقداری برای `.spec.schedulerName` نداشته باشد، kube-scheduler برای آن Pod
با استفاده از پیکربندی اصلی و افزونه‌های پیش‌فرض خود اجرا می‌شود.
اگر Podی را با `.spec.schedulerName` تنظیم‌شده روی `my-scheduler` تعریف کنید، kube-scheduler اجرا می‌شود
اما با یک پیکربندی سفارشی؛ در آن پیکربندی سفارشی،
نقاط توسعهٔ `queueSort`، `filter` و `permit` غیرفعال هستند.
اگر از این KubeSchedulerConfiguration استفاده کنید و هیچ زمان‌بند سفارشی‌ای اجرا نکنید،
و سپس Podی را با `.spec.schedulerName` تنظیم‌شده روی `nonexistent-scheduler`
(یا هر نام زمان‌بند دیگری که در کلاستر شما وجود ندارد) تعریف کنید، هیچ رویدادی برای آن پاد تولید نخواهد شد.

## ممنوع کردن برچسب‌گذاری نودها

مدیر کلاستر باید اطمینان حاصل کند که کاربران کلاستر نمی‌توانند نودها را برچسب‌گذاری کنند.
یک عامل مخرب می‌تواند از `nodeSelector` برای زمان‌بندی بارهای کاری روی نودهایی استفاده کند که آن بارهای کاری نباید در آن‌ها حضور داشته باشند.
