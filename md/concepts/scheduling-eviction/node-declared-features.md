---
title: قابلیت‌های اعلام‌شده توسط نود
content_type: concept
weight: 160
---

<!-- overview -->

{{< feature-state feature_gate_name="NodeDeclaredFeatures" >}}

نودهای کوبرنتیز از _قابلیت‌های اعلام‌شده_ (declared features) برای گزارش در دسترس بودن قابلیت‌های
مشخصی که جدید هستند یا تحت feature gate قرار دارند، استفاده می‌کنند. اجزای control plane
از این اطلاعات برای گرفتن تصمیم‌های بهتر استفاده می‌کنند. kube-scheduler از طریق
افزونهٔ `NodeDeclaredFeatures` اطمینان حاصل می‌کند که Podها تنها روی نودهایی قرار می‌گیرند که
به‌طور صریح از قابلیت‌های موردنیاز Pod پشتیبانی می‌کنند. افزون بر این،
کنترل‌کنندهٔ پذیرش `NodeDeclaredFeatureValidator` به‌روزرسانی‌های Pod را
بر اساس قابلیت‌های اعلام‌شدهٔ نود اعتبارسنجی می‌کند.

این سازوکار به مدیریت ناهمخوانی نسخه‌ها (version skew) و بهبود پایداری کلاستر کمک می‌کند،
به‌ویژه در طول ارتقای کلاستر یا در محیط‌هایی با نسخه‌های مختلط که ممکن است همهٔ نودها
قابلیت‌های فعال یکسانی نداشته باشند. این سازوکار برای توسعه‌دهندگان قابلیت‌های کوبرنتیز
در نظر گرفته شده است که قابلیت‌های جدید سطح نود را معرفی می‌کنند و در پس‌زمینه کار می‌کند؛
توسعه‌دهندگان برنامه که Podها را مستقر می‌کنند نیازی به تعامل مستقیم با
این چارچوب ندارند.

<!-- body -->

## نحوهٔ کار

قابلیت اعلام‌شده رشته‌ای است که نود آن را در
فیلد `.status.declaredFeatures` آبجکت Node فهرست می‌کند. هر قابلیت قابل اعلام،
یک قابلیت سطح نود را مشخص می‌کند که هنوز در حال گذر از مراحل
قابلیت‌های کوبرنتیز است.

1.  **گزارش قابلیت‌ها توسط kubelet:** در زمان راه‌اندازی، kubelet روی هر نود تشخیص می‌دهد
    که کدام قابلیت‌های مدیریت‌شدهٔ کوبرنتیز در حال حاضر فعال هستند و آن‌ها را
    در فیلد `.status.declaredFeatures` نود گزارش می‌کند. تنها قابلیت‌هایی
    که در حال توسعهٔ فعال هستند در این فیلد گنجانده می‌شوند.
2.  **فیلتر کردن توسط زمان‌بند:** kube-scheduler پیش‌فرض از افزونهٔ
    `NodeDeclaredFeatures` استفاده می‌کند. این افزونه:
    * در مرحلهٔ `PreFilter`، `PodSpec` را بررسی می‌کند تا مجموعهٔ قابلیت‌های
      نود موردنیاز Pod را استنتاج کند.
    * در مرحلهٔ `Filter`، بررسی می‌کند که آیا قابلیت‌های فهرست‌شده در
      `.status.declaredFeatures` نود، الزامات استنتاج‌شده برای Pod را برآورده می‌کنند یا نه.
      Podها روی نودهایی که قابلیت‌های موردنیاز را ندارند، زمان‌بندی نمی‌شوند.

    زمان‌بندهای سفارشی نیز می‌توانند از
    فیلد `.status.declaredFeatures` برای اعمال قیدهای مشابه استفاده کنند.
3.  **کنترل پذیرش:** کنترل‌کنندهٔ پذیرش
    [`NodeDeclaredFeatureValidator`](/docs/reference/access-authn-authz/admission-controllers/#nodedeclaredfeaturevalidator)
    می‌تواند Podهایی را که به قابلیت‌هایی نیاز دارند که نود متصل به آن‌ها
    اعلام نکرده است، رد کند و از بروز مشکل در طول به‌روزرسانی‌های Pod جلوگیری کند.
4.  **پذیرش در kubelet:** به‌عنوان آخرین سازوکار حفاظتی، kubelet پیش از اجرای Pod،
    الزامات قابلیت‌های Pod را دوباره با قابلیت‌های در دسترس روی نود خود بررسی می‌کند
    و اگر یک قابلیت موردنیاز وجود نداشته باشد، Pod را رد می‌کند.
5.  **پاک‌سازی پس از GA:** هنگامی که یک قابلیت روی همهٔ نودهای یک
    کلاستر در دسترس باشد (پس از اینکه قابلیت به GA ارتقا یافت و بازهٔ ناهمخوانی نسخهٔ پشتیبانی‌شده
    بین control plane و نودها سپری شد)، نودها اعلام آن
    قابلیت را متوقف می‌کنند. این کار با تعیین یک نسخهٔ بیشینه (`MaxVersion`) برای
    هر قابلیت اعلام‌شده انجام می‌شود: kubeletهای جدیدتر از این نسخه فهرست کردن
    آن قابلیت در `.status.declaredFeatures` را متوقف می‌کنند و زمان‌بند و
    کنترل‌کنندهٔ پذیرش آن قابلیت را به‌طور همگانی در دسترس در نظر می‌گیرند و بررسی آن را
    متوقف می‌کنند. در نهایت، این قابلیت به‌عنوان بخشی از پاک‌سازی استاندارد قابلیت‌ها پس از GA
    از مجموعهٔ قابلیت‌های اعلام‌شده حذف می‌شود.

## نمونه‌ای از یک قابلیت اعلام‌شده

قابلیت اعلام‌شدهٔ `RestartAllContainersOnContainerExits` نشان می‌دهد که یک
نود از
[راه‌اندازی مجدد درجای همهٔ کانتینرهای یک Pod](/docs/concepts/workloads/pods/pod-lifecycle/#restart-all-containers) پشتیبانی می‌کند.
هنگامی که feature gate
[`RestartAllContainersOnContainerExits`](/docs/reference/command-line-tools-reference/feature-gates/#RestartAllContainersOnContainerExits)
برای kubelet فعال باشد، kubelet این قابلیت را در
وضعیت نود خود اعلام می‌کند:

```yaml
apiVersion: v1
kind: Node
metadata:
  name: example-node
status:
  declaredFeatures:
  - RestartAllContainersOnContainerExits
```

یک Pod در صورتی به این قابلیت نیاز دارد که یکی از کانتینرهای آن یک قاعدهٔ راه‌اندازی مجدد
با اقدام `RestartAllContainers` مشخص کند:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  containers:
  - name: main
    image: registry.k8s.io/busybox:1.27.2
    restartPolicy: Never     # Container restart policy must be specified if rules are specified
    restartPolicyRules:      # Restart the whole Pod in place on exit code 42
    - action: RestartAllContainers
      exitCodes:
        operator: In
        values: [42]
```

هنگام زمان‌بندی این Pod، kube-scheduler تنها نودهایی را در نظر می‌گیرد که
`RestartAllContainersOnContainerExits` را در `.status.declaredFeatures` خود فهرست کرده‌اند.
در کلاستری که تنها برخی از نودها آن feature gate را فعال دارند (برای
مثال، در میانهٔ ارتقای کلاستر)، این کار از اختصاص Pod به نودی که kubelet آن
قاعدهٔ راه‌اندازی مجدد را نادیده می‌گیرد، جلوگیری می‌کند.

قابلیت‌های اعلام‌شده همچنین به‌روزرسانی‌های Podهای در حال اجرا را کنترل می‌کنند. برای مثال،
قابلیت اعلام‌شدهٔ `InPlacePodVerticalScalingInitContainers` نشان می‌دهد که یک
نود از تغییر اندازهٔ درجای منابع init containerها پشتیبانی می‌کند.
اگر تلاشی برای تغییر اندازهٔ یک init container در یک Pod در حال اجرا صورت گیرد،
کنترل‌کنندهٔ پذیرش `NodeDeclaredFeatureValidator` به‌روزرسانی را رد می‌کند، مگر اینکه
نودی که آن Pod را اجرا می‌کند این قابلیت را اعلام کرده باشد.

## {{% heading "whatsnext" %}}

* دربارهٔ [کنترل‌کنندهٔ پذیرش `NodeDeclaredFeatureValidator`](/docs/reference/access-authn-authz/admission-controllers/#nodedeclaredfeaturevalidator) بخوانید.
* برای جزئیات بیشتر، KEP را بخوانید:
    [KEP-5328: قابلیت‌های اعلام‌شده توسط نود](https://github.com/kubernetes/enhancements/blob/6d3210f7dd5d547c8f7f6a33af6a09eb45193cd7/keps/sig-node/5328-node-declared-features/README.md)
