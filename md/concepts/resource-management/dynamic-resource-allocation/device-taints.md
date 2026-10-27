---
reviewers:
- klueska
- pohly
title: Taintها و Tolerationهای دستگاه
content_type: concept
weight: 50
api_metadata:
- apiVersion: "resource.k8s.io/v1alpha3"
  kind: "DeviceTaintRule"
- apiVersion: "resource.k8s.io/v1beta2"
  kind: "DeviceTaintRule"
- apiVersion: "resource.k8s.io/v1"
  kind: "DeviceTaintRule"
---

<!-- overview -->

این صفحه taintها و tolerationهای دستگاه در DRA را شرح می‌دهد که به درایورها و
مدیران اجازه می‌دهند پادها را از دستگاه‌های مشخصی دور نگه دارند، یا پادهایی را که از قبل از آن‌ها استفاده می‌کنند بیرون برانند.

<!-- body -->

## Taintها و tolerationهای دستگاه {#device-taints-and-tolerations}

{{< feature-state feature_gate_name="DRADeviceTaints" >}}

taintهای دستگاه مشابه taintهای نود هستند: یک taint یک کلید رشته‌ای، یک مقدار رشته‌ای و یک اثر (effect) دارد.
این اثر بر ResourceClaimای که از دستگاه دارای taint استفاده می‌کند و بر همهٔ پادهایی که به آن ResourceClaim ارجاع می‌دهند اعمال می‌شود.
اثر «NoSchedule» از زمان‌بندی آن پادها جلوگیری می‌کند.
دستگاه‌های دارای taint هنگام تلاش برای تخصیص یک ResourceClaim نادیده گرفته می‌شوند، زیرا استفاده از آن‌ها مانع زمان‌بندی پادها می‌شود.

اثر «NoExecute» شامل «NoSchedule» نیز می‌شود و علاوه بر آن باعث بیرون‌راندن همهٔ پادهایی
می‌شود که از قبل زمان‌بندی شده‌اند.
این بیرون‌راندن در کنترل‌کنندهٔ بیرون‌راندن مبتنی بر taint دستگاه در kube-controller-manager و با حذف پادهای متأثر پیاده‌سازی شده است.

اثر «None» توسط زمان‌بند و کنترل‌کنندهٔ بیرون‌راندن نادیده گرفته می‌شود.
درایورهای DRA می‌توانند از آن برای اطلاع‌رسانی موارد استثنایی به مدیران یا کنترل‌کننده‌های دیگر استفاده کنند،
برای مثال کاهش سلامت یک دستگاه. مدیران نیز می‌توانند از آن برای
اجرای آزمایشی (dry-run) بیرون‌راندن پاد در DeviceTaintRuleها استفاده کنند (در ادامه بیشتر توضیح داده می‌شود).

ResourceClaimها می‌توانند taintها را تحمل (tolerate) کنند. اگر یک taint تحمل شود، اثر آن اعمال نمی‌شود.
یک toleration خالی با همهٔ taintها منطبق می‌شود. یک toleration را می‌توان به اثرهای مشخصی محدود کرد
و/یا با جفت‌های کلید/مقدار مشخصی منطبق کرد.
یک toleration می‌تواند بررسی کند که کلید مشخصی، صرف‌نظر از مقدار آن، وجود دارد یا می‌تواند
مقادیر مشخصی از یک کلید را بررسی کند.
برای اطلاعات بیشتر دربارهٔ این تطبیق، به
[مفاهیم taint نود](/docs/concepts/scheduling-eviction/taint-and-toleration#concepts) مراجعه کنید.

بیرون‌راندن را می‌توان با تحمل یک taint برای مدت زمان مشخصی به تأخیر انداخت.
این تأخیر از زمانی آغاز می‌شود که taint به دستگاه اضافه می‌شود و این زمان در یکی از فیلدهای taint ثبت می‌شود.

taintها همان‌طور که در بالا توضیح داده شد، بر ResourceClaimهایی که «همهٔ» دستگاه‌های یک نود را تخصیص می‌دهند نیز اعمال می‌شوند.
همهٔ دستگاه‌ها باید بدون taint باشند یا همهٔ taintهای آن‌ها باید تحمل شوند.
تخصیص یک دستگاه با [دسترسی مدیر](/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#admin-access)
نیز مستثنا نیست. مدیری که از این حالت استفاده می‌کند باید به‌طور صریح همهٔ taintها را تحمل کند
تا به دستگاه‌های دارای taint دسترسی پیدا کند.

می‌توانید به روش‌های زیر، با استفاده از kind ‏DeviceTaintRule در API، taintهایی به دستگاه‌ها اضافه کنید.

### Taintهای تنظیم‌شده توسط درایور

یک درایور DRA می‌تواند taintهایی را به اطلاعات دستگاهی که در ResourceSliceها منتشر می‌کند اضافه کند.
برای اینکه بدانید آیا یک درایور DRA از taintها استفاده می‌کند و کلیدها و مقادیر آن‌ها چیست، به مستندات آن درایور مراجعه کنید.

### Taintهای تنظیم‌شده توسط مدیر

{{< feature-state feature_gate_name="DRADeviceTaintRules" >}}

یک مدیر یا یک جزء control plane می‌تواند بدون نیاز به اینکه از
درایور DRA بخواهد taintها را در اطلاعات دستگاه خود در ResourceSliceها بگنجاند، به دستگاه‌ها taint اضافه کند.
این کار با ایجاد DeviceTaintRuleها انجام می‌شود.
هر DeviceTaintRule یک taint به دستگاه‌هایی اضافه می‌کند که با انتخابگر دستگاه منطبق باشند.
بدون چنین انتخابگری، هیچ دستگاهی taint نمی‌شود.
این امر بیرون‌راندن تصادفی همهٔ پادهایی را که از ResourceClaimها استفاده می‌کنند، در صورت جاافتادن اشتباهی انتخابگر، دشوارتر می‌کند.

دستگاه‌ها را می‌توان با ارائهٔ نام یک DeviceClass، درایور، pool و/یا دستگاه انتخاب کرد.
DeviceClass همهٔ دستگاه‌هایی را انتخاب می‌کند که توسط انتخابگرهای آن DeviceClass انتخاب شده‌اند.
یک مدیر تنها با نام درایور می‌تواند همهٔ دستگاه‌هایی را که آن درایور مدیریت می‌کند taint کند،
برای مثال هنگام انجام نوعی نگه‌داری از آن درایور در سراسر کلاستر.
افزودن نام pool می‌تواند taint را به یک نود واحد محدود کند، در صورتی که درایور دستگاه‌های محلی نود را مدیریت کند.

در نهایت، افزودن نام دستگاه می‌تواند یک دستگاه مشخص را انتخاب کند.
در صورت تمایل، نام دستگاه و نام pool را می‌توان به‌تنهایی نیز استفاده کرد.
برای مثال، به درایورهای دستگاه‌های محلی نود توصیه می‌شود از نام نود به‌عنوان نام pool خود استفاده کنند.
در این صورت taint کردن با آن نام pool به‌طور خودکار همهٔ دستگاه‌های یک نود را taint می‌کند.

درایورها ممکن است از نام‌های پایداری مانند «gpu-0» استفاده کنند که پنهان می‌کنند کدام دستگاه مشخص در حال حاضر به آن نام اختصاص یافته است.
برای پشتیبانی از taint کردن یک نمونهٔ سخت‌افزاری مشخص، می‌توان از انتخابگرهای CEL در یک DeviceTaintRule
برای تطبیق با یک ویژگی شناسهٔ یکتای مخصوص فروشنده استفاده کرد، در صورتی که درایور چنین ویژگی‌ای را برای سخت‌افزار خود پشتیبانی کند.

taint تا زمانی که DeviceTaintRule وجود دارد اعمال می‌شود.
آن را می‌توان در هر زمان تغییر داد یا حذف کرد.
در اینجا یک نمونه از DeviceTaintRule برای یک درایور DRA فرضی آمده است:

```yaml
apiVersion: resource.k8s.io/v1
kind: DeviceTaintRule
metadata:
  name: example
spec:
  # The entire hardware installation for this
  # particular driver is broken.
  # Evict all pods and don't schedule new ones.
  deviceSelector:
    driver: dra.example.com
  taint:
    key: dra.example.com/unhealthy
    value: Broken
    effect: NoExecute
```

kube-apiserver به‌طور خودکار زمان ایجاد این taint را با تنظیم فیلد
`timeAdded` در `spec` ثبت می‌کند. دورهٔ تحمل از همان مهر زمانی
آغاز می‌شود. در طول به‌روزرسانی‌هایی که اثر را تغییر می‌دهند (به جریان بیرون‌راندن شبیه‌سازی‌شده
در ادامه مراجعه کنید)، kube-apiserver مهر زمانی را به‌طور خودکار به‌روزرسانی می‌کند. کاربران می‌توانند
مهر زمانی را به‌طور صریح کنترل کنند؛ با تنظیم این فیلد هنگام ایجاد یک DeviceTaintRule و
تغییر آن به مقداری دیگر هنگام به‌روزرسانی.

وضعیت (status) شامل یک condition است که کنترل‌کنندهٔ بیرون‌راندن اضافه می‌کند:

```
kubectl describe devicetaintrules
```

```
Name:         example
...
Spec:
  Device Selector:
    Driver:  dra.example.com
  Taint:
    Effect:      NoExecute
    Key:         dra.example.com/unhealthy
    Time Added:  2025-11-05T18:15:37Z
    Value:       Broken
Status:
  Conditions:
    Last Transition Time:  2025-11-05T18:15:37Z
    Message:               1 pod evicted since starting the controller.
    Observed Generation:   1
    Reason:                Completed
    Status:                False
    Type:                  EvictionInProgress
Events:                    <none>
```

پادها با حذف‌شدن بیرون رانده می‌شوند. معمولاً این کار بسیار سریع انجام می‌شود،
مگر زمانی که یک toleration برای taint آن را برای مدت مشخصی به تأخیر بیندازد یا
زمانی که پادهای بسیار زیادی باید بیرون رانده شوند. هنگامی که این کار
بیشتر طول بکشد، پیام اطلاعاتی دربارهٔ وضعیت فعلی ارائه می‌دهد:

    2 pods need to be evicted in 2 different namespaces. 1 pod evicted since starting the controller.

از این condition می‌توان برای بررسی اینکه آیا بیرون‌راندنی در حال حاضر فعال است استفاده کرد:

    kubectl wait --for=condition=EvictionInProgress=false DeviceTaintRule/example

مراقب رقابت (race) احتمالی میان زمان‌بند و کنترل‌کننده باشید که taint جدید را
در زمان‌های متفاوتی مشاهده می‌کنند؛ این امر می‌تواند باعث شود پادها همچنان در زمانی زمان‌بندی شوند
که کنترل‌کننده تصور می‌کند هیچ پادی برای بیرون‌راندن وجود ندارد
و در نتیجه این condition را روی `False` تنظیم می‌کند. در عمل، این رقابت با
به‌روزرسانی وضعیت تنها پس از یک تأخیر عمدی چندثانیه‌ای بسیار
نامحتمل شده است.

برای `effect: None`، پیام اطلاعاتی دربارهٔ تعداد
دستگاه‌های متأثر، تعداد دستگاه‌های تخصیص‌یافته از میان آن‌ها و تعداد پادهایی که در صورت
`NoExecute` بودن اثر بیرون رانده می‌شدند ارائه می‌دهد. از این اطلاعات می‌توان برای اجرای آزمایشی پیش از
راه‌اندازی واقعی بیرون‌راندن استفاده کرد:

- یک DeviceTaintRule با انتخابگرهای مورد نظر و `effect: None` ایجاد کنید.

- پیام را بازبینی کنید:

  ```
  3 published devices selected. 1 allocated device selected.
  1 pod would be evicted in 1 namespace if the effect was NoExecute.
  This information will not be updated again. Recreate the DeviceTaintRule to trigger an update.
  ```

  دستگاه‌های منتشرشده آن‌هایی هستند که در ResourceSliceها فهرست شده‌اند. taint کردن آن‌ها
  از تخصیص برای پادهای جدید جلوگیری می‌کند. فقط دستگاه‌های تخصیص‌یافته باعث
  بیرون‌راندن پادهایی می‌شوند که از آن‌ها استفاده می‌کنند.

- DeviceTaintRule را ویرایش کنید و اثر را به `NoExecute` تغییر دهید.

