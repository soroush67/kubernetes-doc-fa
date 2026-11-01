---
api_metadata:
  apiVersion: "autoscaling/v2"
  import: "k8s.io/api/autoscaling/v2"
  kind: "HorizontalPodAutoscaler"
content_type: "api_reference"
description: "آبجکت HorizontalPodAutoscaler پیکربندی یک مقیاس‌دهندهٔ خودکار افقی پاد است که بر اساس متریک‌های مشخص‌شده، تعداد رپلیکاهای هر منبعی را که زیرمنبع scale را پیاده‌سازی می‌کند به‌طور خودکار مدیریت می‌کند."
title: "HorizontalPodAutoscaler"
weight: 10
auto_generated: true
---

<!--
The file is auto-generated from the Go source code of the component using a generic
[generator](https://github.com/kubernetes-sigs/reference-docs/). To learn how
to generate the reference documentation, please read
[Contributing to the reference documentation](/docs/contribute/generate-ref-docs/).
To update the reference content, please follow the
[Contributing upstream](/docs/contribute/generate-ref-docs/contribute-upstream/)
guide. You can file document formatting bugs against the
[reference-docs](https://github.com/kubernetes-sigs/reference-docs/) project.
-->

`apiVersion: autoscaling/v2`

`import "k8s.io/api/autoscaling/v2"`


## HorizontalPodAutoscaler {#HorizontalPodAutoscaler}

آبجکت HorizontalPodAutoscaler پیکربندی یک مقیاس‌دهندهٔ خودکار افقی پاد (horizontal pod autoscaler) است که بر اساس متریک‌های مشخص‌شده، تعداد رپلیکاهای هر منبعی را که زیرمنبع scale را پیاده‌سازی می‌کند به‌طور خودکار مدیریت می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>فیلد APIVersion طرح‌وارهٔ نسخه‌دار این بازنمایی از آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>فیلد Kind یک مقدار رشته‌ای است که منبع REST متناظر با این آبجکت را نشان می‌دهد. سرورها ممکن است این مقدار را از endpointای که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. این فیلد قابل به‌روزرسانی نیست و به‌صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فیلد metadata فرادادهٔ استاندارد آبجکت است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>spec</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#HorizontalPodAutoscalerSpec" >}}">HorizontalPodAutoscalerSpec</a></em></td>
      <td>فیلد spec مشخصات رفتار مقیاس‌دهندهٔ خودکار است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "#HorizontalPodAutoscalerStatus" >}}">HorizontalPodAutoscalerStatus</a></em></td>
      <td>فیلد status اطلاعات فعلی دربارهٔ مقیاس‌دهندهٔ خودکار است.</td>
    </tr>
  </tbody>
</table>


## HorizontalPodAutoscalerSpec {#HorizontalPodAutoscalerSpec}

آبجکت HorizontalPodAutoscalerSpec عملکرد مطلوب HorizontalPodAutoscaler را توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>behavior</code><br/><em><a href="{{< ref "#HorizontalPodAutoscalerBehavior" >}}">HorizontalPodAutoscalerBehavior</a></em></td>
      <td>فیلد behavior رفتار مقیاس‌دهی هدف را در هر دو جهت افزایش و کاهش (به‌ترتیب با فیلدهای scaleUp و scaleDown) پیکربندی می‌کند. اگر تنظیم نشود، HPAScalingRules پیش‌فرض برای افزایش و کاهش مقیاس استفاده می‌شود.</td>
    </tr>
    <tr>
      <td><code>maxReplicas</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>فیلد maxReplicas حد بالای تعداد رپلیکاهایی است که مقیاس‌دهندهٔ خودکار می‌تواند مقیاس را تا آن افزایش دهد. این مقدار نمی‌تواند کمتر از minReplicas باشد.</td>
    </tr>
    <tr>
      <td><code>metrics</code><br/><em><a href="{{< ref "#MetricSpec" >}}">MetricSpec array</a></em></td>
      <td>فیلد metrics مشخصاتی را دربر دارد که برای محاسبهٔ تعداد مطلوب رپلیکاها به کار می‌روند (بیشترین تعداد رپلیکا در میان همهٔ متریک‌ها استفاده خواهد شد). تعداد مطلوب رپلیکاها از ضرب نسبت مقدار هدف به مقدار فعلی در تعداد فعلی پادها محاسبه می‌شود. بنابراین، متریک‌های استفاده‌شده باید با افزایش تعداد پادها کاهش یابند و برعکس. برای اطلاعات بیشتر دربارهٔ اینکه هر نوع متریک چگونه باید واکنش نشان دهد، انواع منبع متریک را جداگانه ببینید. اگر تنظیم نشود، متریک پیش‌فرض، میانگین ۸۰ درصدی بهره‌وری CPU خواهد بود.</td>
    </tr>
    <tr>
      <td><code>minReplicas</code><br/><em>integer</em></td>
      <td>فیلد minReplicas حد پایین تعداد رپلیکاهایی است که مقیاس‌دهندهٔ خودکار می‌تواند مقیاس را تا آن کاهش دهد. مقدار پیش‌فرض آن ۱ پاد است. اگر feature gate آلفای HPAScaleToZero فعال باشد و دست‌کم یک متریک از نوع Object یا External پیکربندی شده باشد، مقدار minReplicas می‌تواند ۰ باشد. تا زمانی که دست‌کم مقدار یک متریک در دسترس باشد، مقیاس‌دهی فعال است.</td>
    </tr>
    <tr>
      <td><code>scaleTargetRef</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#CrossVersionObjectReference" >}}">CrossVersionObjectReference</a></em></td>
      <td>فیلد scaleTargetRef به منبع هدفی اشاره می‌کند که باید مقیاس‌دهی شود. از این فیلد هم برای تعیین پادهایی که باید متریک‌هایشان جمع‌آوری شود و هم برای تغییر واقعی تعداد رپلیکاها استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>


## HorizontalPodAutoscalerStatus {#HorizontalPodAutoscalerStatus}

آبجکت HorizontalPodAutoscalerStatus وضعیت فعلی یک مقیاس‌دهندهٔ خودکار افقی پاد را توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>conditions</code><br/><em><a href="{{< ref "#HorizontalPodAutoscalerCondition" >}}">HorizontalPodAutoscalerCondition array</a></em><br/><em>patch strategy: merge on key <code>type</code></em></td>
      <td>فیلد conditions مجموعهٔ شرایطی است که این مقیاس‌دهندهٔ خودکار برای مقیاس‌دهی هدف خود به آن‌ها نیاز دارد، و نشان می‌دهد که آیا این شرایط برقرار هستند یا نه.</td>
    </tr>
    <tr>
      <td><code>currentMetrics</code><br/><em><a href="{{< ref "#MetricStatus" >}}">MetricStatus array</a></em></td>
      <td>فیلد currentMetrics آخرین وضعیت خوانده‌شده از متریک‌هایی است که این مقیاس‌دهندهٔ خودکار استفاده می‌کند.</td>
    </tr>
    <tr>
      <td><code>currentReplicas</code><br/><em>integer</em></td>
      <td>فیلد currentReplicas تعداد فعلی رپلیکاهای پادهایی است که این مقیاس‌دهندهٔ خودکار مدیریت می‌کند، بر اساس آخرین مشاهدهٔ مقیاس‌دهندهٔ خودکار.</td>
    </tr>
    <tr>
      <td><code>desiredReplicas</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>فیلد desiredReplicas تعداد مطلوب رپلیکاهای پادهایی است که این مقیاس‌دهندهٔ خودکار مدیریت می‌کند، بر اساس آخرین محاسبهٔ مقیاس‌دهندهٔ خودکار.</td>
    </tr>
    <tr>
      <td><code>lastScaleTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>فیلد lastScaleTime آخرین زمانی است که HorizontalPodAutoscaler تعداد پادها را مقیاس‌دهی کرده است. مقیاس‌دهندهٔ خودکار از این مقدار برای کنترل دفعات تغییر تعداد پادها استفاده می‌کند.</td>
    </tr>
    <tr>
      <td><code>observedGeneration</code><br/><em>integer</em></td>
      <td>فیلد observedGeneration جدیدترین نسلی (generation) است که این مقیاس‌دهندهٔ خودکار مشاهده کرده است.</td>
    </tr>
  </tbody>
</table>


## HorizontalPodAutoscalerList {#HorizontalPodAutoscalerList}

آبجکت HorizontalPodAutoscalerList فهرستی از آبجکت‌های مقیاس‌دهندهٔ خودکار افقی پاد است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>فیلد APIVersion طرح‌وارهٔ نسخه‌دار این بازنمایی از آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler array</a></em></td>
      <td>فیلد items فهرست آبجکت‌های مقیاس‌دهندهٔ خودکار افقی پاد است.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>فیلد Kind یک مقدار رشته‌ای است که منبع REST متناظر با این آبجکت را نشان می‌دهد. سرورها ممکن است این مقدار را از endpointای که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. این فیلد قابل به‌روزرسانی نیست و به‌صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فیلد metadata فرادادهٔ استاندارد فهرست است.</td>
    </tr>
  </tbody>
</table>


## ContainerResourceMetricSource {#ContainerResourceMetricSource}

آبجکت ContainerResourceMetricSource نشان می‌دهد که مقیاس‌دهی چگونه بر اساس یک متریک منبعِ شناخته‌شده برای کوبرنتیز (مثلاً CPU یا حافظه) انجام شود؛ متریکی که در requests و limits مشخص شده است و هر پاد در هدف فعلی مقیاس‌دهی را توصیف می‌کند. مقادیر پیش از مقایسه با هدف، با هم میانگین‌گیری می‌شوند. این متریک‌ها در خود کوبرنتیز تعبیه شده‌اند و افزون بر گزینه‌هایی که برای متریک‌های معمولیِ هر پاد با منبع &#34;pods&#34; در دسترس است، گزینه‌های مقیاس‌دهی ویژه‌ای نیز دارند. فقط یک نوع &#34;target&#34; باید تنظیم شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>container</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد container نام کانتینر در پادهای هدف مقیاس‌دهی است.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد name نام منبع مورد نظر است.</td>
    </tr>
    <tr>
      <td><code>target</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricTarget" >}}">MetricTarget</a></em></td>
      <td>فیلد target مقدار هدف را برای متریک داده‌شده مشخص می‌کند.</td>
    </tr>
  </tbody>
</table>


## ContainerResourceMetricStatus {#ContainerResourceMetricStatus}

آبجکت ContainerResourceMetricStatus مقدار فعلی یک متریک منبعِ شناخته‌شده برای کوبرنتیز (مثلاً CPU یا حافظه) را نشان می‌دهد؛ متریکی که در requests و limits مشخص شده است و یک کانتینر واحد را در هر پاد از هدف فعلی مقیاس‌دهی توصیف می‌کند. این متریک‌ها در خود کوبرنتیز تعبیه شده‌اند و افزون بر گزینه‌هایی که برای متریک‌های معمولیِ هر پاد با منبع &#34;pods&#34; در دسترس است، گزینه‌های مقیاس‌دهی ویژه‌ای نیز دارند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>container</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد container نام کانتینر در پادهای هدف مقیاس‌دهی است.</td>
    </tr>
    <tr>
      <td><code>current</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricValueStatus" >}}">MetricValueStatus</a></em></td>
      <td>فیلد current مقدار فعلی متریک داده‌شده را دربر دارد.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد name نام منبع مورد نظر است.</td>
    </tr>
  </tbody>
</table>


## CrossVersionObjectReference {#CrossVersionObjectReference}

آبجکت CrossVersionObjectReference اطلاعات کافی برای شناسایی منبع ارجاع‌شده را در اختیار شما می‌گذارد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>فیلد apiVersion نسخهٔ API منبع ارجاع‌شده است.</td>
    </tr>
    <tr>
      <td><code>kind</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد kind نوع منبع ارجاع‌شده است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد name نام منبع ارجاع‌شده است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</td>
    </tr>
  </tbody>
</table>


## ExternalMetricSource {#ExternalMetricSource}

آبجکت ExternalMetricSource نشان می‌دهد که مقیاس‌دهی چگونه بر اساس متریکی انجام شود که به هیچ آبجکت کوبرنتیز وابسته نیست (برای مثال طول صف در یک سرویس پیام‌رسانی ابری، یا QPS یک متعادل‌کنندهٔ بار که بیرون از کلاستر اجرا می‌شود).

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>metric</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricIdentifier" >}}">MetricIdentifier</a></em></td>
      <td>فیلد metric متریک هدف را با نام و انتخابگر (selector) آن مشخص می‌کند.</td>
    </tr>
    <tr>
      <td><code>target</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricTarget" >}}">MetricTarget</a></em></td>
      <td>فیلد target مقدار هدف را برای متریک داده‌شده مشخص می‌کند.</td>
    </tr>
  </tbody>
</table>


## ExternalMetricStatus {#ExternalMetricStatus}

آبجکت ExternalMetricStatus مقدار فعلی یک متریک سراسری را نشان می‌دهد که به هیچ آبجکت کوبرنتیز وابسته نیست.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>current</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricValueStatus" >}}">MetricValueStatus</a></em></td>
      <td>فیلد current مقدار فعلی متریک داده‌شده را دربر دارد.</td>
    </tr>
    <tr>
      <td><code>metric</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricIdentifier" >}}">MetricIdentifier</a></em></td>
      <td>فیلد metric متریک هدف را با نام و انتخابگر آن مشخص می‌کند.</td>
    </tr>
  </tbody>
</table>


## HPAScalingPolicy {#HPAScalingPolicy}

آبجکت HPAScalingPolicy یک سیاست واحد است که باید در طول یک بازهٔ زمانی مشخص در گذشته برقرار باشد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>periodSeconds</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>فیلد periodSeconds بازهٔ زمانی‌ای را مشخص می‌کند که سیاست باید در طول آن برقرار باشد. مقدار PeriodSeconds باید بزرگ‌تر از صفر و کوچک‌تر یا مساوی ۱۸۰۰ (۳۰ دقیقه) باشد.</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد type برای تعیین سیاست مقیاس‌دهی استفاده می‌شود.</td>
    </tr>
    <tr>
      <td><code>value</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>فیلد value میزان تغییری را که سیاست اجازه می‌دهد دربر دارد. این مقدار باید بزرگ‌تر از صفر باشد.</td>
    </tr>
  </tbody>
</table>


## HPAScalingRules {#HPAScalingRules}

آبجکت HPAScalingRules رفتار مقیاس‌دهی را برای یک جهت، از طریق قواعد سیاست مقیاس‌دهی و یک تلرانس قابل پیکربندی برای متریک، پیکربندی می‌کند.

قواعد سیاست مقیاس‌دهی پس از محاسبهٔ DesiredReplicas از روی متریک‌های HPA اعمال می‌شوند. این قواعد می‌توانند با تعیین سیاست‌های مقیاس‌دهی، سرعت مقیاس‌دهی را محدود کنند. همچنین می‌توانند با تعیین پنجرهٔ پایدارسازی از نوسان مکرر (flapping) جلوگیری کنند؛ به این ترتیب تعداد رپلیکاها بی‌درنگ تنظیم نمی‌شود، بلکه امن‌ترین مقدار در پنجرهٔ پایدارسازی انتخاب می‌شود.

تلرانس روی مقادیر متریک اعمال می‌شود و از مقیاس‌دهی شتاب‌زده در برابر تغییرات کوچک متریک جلوگیری می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>policies</code><br/><em><a href="{{< ref "#HPAScalingPolicy" >}}">HPAScalingPolicy array</a></em></td>
      <td>فیلد policies فهرستی از سیاست‌های ممکن برای مقیاس‌دهی است که می‌توان در هنگام مقیاس‌دهی از آن‌ها استفاده کرد. اگر تنظیم نشود، مقادیر پیش‌فرض استفاده می‌شوند: - برای افزایش مقیاس: اجازهٔ دو برابر کردن تعداد پادها یا تغییر مطلق ۴ پاد در یک پنجرهٔ ۱۵ ثانیه‌ای. - برای کاهش مقیاس: اجازهٔ حذف همهٔ پادها در یک پنجرهٔ ۱۵ ثانیه‌ای.</td>
    </tr>
    <tr>
      <td><code>selectPolicy</code><br/><em>string</em></td>
      <td>فیلد selectPolicy مشخص می‌کند که کدام سیاست باید استفاده شود. اگر تنظیم نشود، مقدار پیش‌فرض Max استفاده می‌شود.</td>
    </tr>
    <tr>
      <td><code>stabilizationWindowSeconds</code><br/><em>integer</em></td>
      <td>فیلد stabilizationWindowSeconds تعداد ثانیه‌هایی است که توصیه‌های گذشته در هنگام افزایش یا کاهش مقیاس در نظر گرفته می‌شوند. مقدار StabilizationWindowSeconds باید بزرگ‌تر یا مساوی صفر و کوچک‌تر یا مساوی ۳۶۰۰ (یک ساعت) باشد. اگر تنظیم نشود، مقادیر پیش‌فرض استفاده می‌شوند: - برای افزایش مقیاس: ۰ (یعنی هیچ پایدارسازی‌ای انجام نمی‌شود). - برای کاهش مقیاس: ۳۰۰ (یعنی طول پنجرهٔ پایدارسازی ۳۰۰ ثانیه است).</td>
    </tr>
    <tr>
      <td><code>tolerance</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>فیلد tolerance تلرانس نسبت میان مقدار فعلی و مقدار مطلوب متریک است؛ تا زمانی که این نسبت درون محدودهٔ تلرانس باشد، تعداد مطلوب رپلیکاها به‌روزرسانی نمی‌شود (مثلاً 0.01 برای ۱٪). این مقدار باید بزرگ‌تر یا مساوی صفر باشد. اگر تنظیم نشود، تلرانس پیش‌فرض سراسری کلاستر (به‌طور پیش‌فرض ۱۰٪) اعمال می‌شود. برای مثال، اگر مقیاس‌دهی خودکار با هدف مصرف حافظهٔ 100Mi و تلرانس‌های ۵٪ برای کاهش مقیاس و ۱٪ برای افزایش مقیاس پیکربندی شده باشد، مقیاس‌دهی زمانی آغاز می‌شود که مصرف واقعی به کمتر از 95Mi برسد یا از 101Mi فراتر رود.</td>
    </tr>
  </tbody>
</table>


## HorizontalPodAutoscalerBehavior {#HorizontalPodAutoscalerBehavior}

آبجکت HorizontalPodAutoscalerBehavior رفتار مقیاس‌دهی هدف را در هر دو جهت افزایش و کاهش (به‌ترتیب با فیلدهای scaleUp و scaleDown) پیکربندی می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>scaleDown</code><br/><em><a href="{{< ref "#HPAScalingRules" >}}">HPAScalingRules</a></em></td>
      <td>فیلد scaleDown سیاست مقیاس‌دهی برای کاهش مقیاس است. اگر تنظیم نشود، مقدار پیش‌فرض اجازه می‌دهد مقیاس تا minReplicas پاد کاهش یابد و پنجرهٔ پایدارسازی ۳۰۰ ثانیه‌ای اعمال شود (یعنی بالاترین توصیه در ۳۰۰ ثانیهٔ اخیر استفاده می‌شود).</td>
    </tr>
    <tr>
      <td><code>scaleUp</code><br/><em><a href="{{< ref "#HPAScalingRules" >}}">HPAScalingRules</a></em></td>
      <td>فیلد scaleUp سیاست مقیاس‌دهی برای افزایش مقیاس است. اگر تنظیم نشود، مقدار پیش‌فرض بیشترینِ این دو مقدار است:   * افزایش حداکثر ۴ پاد در هر ۶۰ ثانیه   * دو برابر کردن تعداد پادها در هر ۶۰ ثانیه. هیچ پایدارسازی‌ای استفاده نمی‌شود.</td>
    </tr>
  </tbody>
</table>

## HorizontalPodAutoscalerCondition {#HorizontalPodAutoscalerCondition}

نوع HorizontalPodAutoscalerCondition وضعیت یک HorizontalPodAutoscaler را در یک لحظهٔ مشخص توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>lastTransitionTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>فیلد lastTransitionTime آخرین زمانی است که این شرط از یک وضعیت به وضعیت دیگری تغییر کرده است.</td>
    </tr>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>فیلد message توضیحی خوانا برای انسان است که جزئیات این تغییر وضعیت را در بر دارد.</td>
    </tr>
    <tr>
      <td><code>observedGeneration</code><br/><em>integer</em></td>
      <td>فیلد observedGeneration مقدار .metadata.generation را نشان می‌دهد که شرط بر اساس آن تنظیم شده است. برای مثال، اگر مقدار فعلی .metadata.generation برابر ۱۲ باشد اما مقدار .status.conditions[x].observedGeneration برابر ۹ باشد، این شرط نسبت به وضعیت فعلی نمونه قدیمی است.</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>فیلد reason دلیل آخرین تغییر وضعیت این شرط است.</td>
    </tr>
    <tr>
      <td><code>status</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد status وضعیت شرط را نشان می‌دهد (True، False یا Unknown).</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد type شرط فعلی را توصیف می‌کند.</td>
    </tr>
  </tbody>
</table>


## MetricIdentifier {#MetricIdentifier}

نوع MetricIdentifier نام و، به‌صورت اختیاری، انتخابگر (selector) یک متریک را تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد name نام متریک موردنظر است.</td>
    </tr>
    <tr>
      <td><code>selector</code><br/><em><a href="{{< ref "../definitions/label-selector-v1-meta#LabelSelector" >}}">LabelSelector</a></em></td>
      <td>فیلد selector شکل رشته‌ای‌شدهٔ یک انتخابگر برچسب استاندارد کوبرنتیز برای متریک موردنظر است. اگر تنظیم شود، به‌عنوان پارامتری اضافی به سرور متریک‌ها ارسال می‌شود تا دامنهٔ متریک‌ها دقیق‌تر مشخص شود. اگر تنظیم نشود، فقط از metricName برای جمع‌آوری متریک‌ها استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>


## MetricSpec {#MetricSpec}

نوع MetricSpec مشخص می‌کند که مقیاس‌دهی بر اساس یک متریک واحد چگونه انجام شود (در هر لحظه فقط باید `type` و یکی دیگر از فیلدهای متناظر با آن تنظیم شود).

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>containerResource</code><br/><em><a href="{{< ref "#ContainerResourceMetricSource" >}}">ContainerResourceMetricSource</a></em></td>
      <td>فیلد containerResource به یک متریک منبع شناخته‌شده برای کوبرنتیز (مانند منابعی که در requests و limits مشخص می‌شوند) اشاره می‌کند که یک کانتینر مشخص را در هر پاد از هدف مقیاس‌دهی فعلی توصیف می‌کند (مثلاً CPU یا حافظه). این متریک‌ها در خود کوبرنتیز تعبیه شده‌اند و علاوه بر گزینه‌های موجود برای متریک‌های معمولیِ مبتنی بر هر پاد که از منبع «pods» استفاده می‌کنند، گزینه‌های مقیاس‌دهی ویژه‌ای نیز دارند.</td>
    </tr>
    <tr>
      <td><code>external</code><br/><em><a href="{{< ref "#ExternalMetricSource" >}}">ExternalMetricSource</a></em></td>
      <td>فیلد external به یک متریک سراسری اشاره می‌کند که با هیچ آبجکت کوبرنتیز مرتبط نیست. با این فیلد می‌توان مقیاس‌دهی خودکار را بر اساس اطلاعاتی انجام داد که از اجزای در حال اجرا در بیرون از کلاستر می‌آیند (برای مثال، طول صف در یک سرویس پیام‌رسانی ابری یا QPS یک متعادل‌کنندهٔ بار که بیرون از کلاستر اجرا می‌شود).</td>
    </tr>
    <tr>
      <td><code>object</code><br/><em><a href="{{< ref "#ObjectMetricSource" >}}">ObjectMetricSource</a></em></td>
      <td>فیلد object به متریکی اشاره می‌کند که یک آبجکت مشخص کوبرنتیز را توصیف می‌کند (برای مثال، تعداد درخواست‌ها در ثانیه روی یک آبجکت Ingress).</td>
    </tr>
    <tr>
      <td><code>pods</code><br/><em><a href="{{< ref "#PodsMetricSource" >}}">PodsMetricSource</a></em></td>
      <td>فیلد pods به متریکی اشاره می‌کند که هر پاد را در هدف مقیاس‌دهی فعلی توصیف می‌کند (برای مثال، تعداد تراکنش‌های پردازش‌شده در ثانیه). پیش از مقایسه با مقدار هدف، از مقادیر میانگین گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>resource</code><br/><em><a href="{{< ref "#ResourceMetricSource" >}}">ResourceMetricSource</a></em></td>
      <td>فیلد resource به یک متریک منبع شناخته‌شده برای کوبرنتیز (مانند منابعی که در requests و limits مشخص می‌شوند) اشاره می‌کند که هر پاد را در هدف مقیاس‌دهی فعلی توصیف می‌کند (مثلاً CPU یا حافظه). این متریک‌ها در خود کوبرنتیز تعبیه شده‌اند و علاوه بر گزینه‌های موجود برای متریک‌های معمولیِ مبتنی بر هر پاد که از منبع «pods» استفاده می‌کنند، گزینه‌های مقیاس‌دهی ویژه‌ای نیز دارند.</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد type نوع منبع متریک است. مقدار آن باید یکی از "ContainerResource"، "External"، "Object"، "Pods" یا "Resource" باشد که هرکدام به فیلد متناظری در آبجکت نگاشت می‌شود.</td>
    </tr>
  </tbody>
</table>


## MetricStatus {#MetricStatus}

نوع MetricStatus آخرین وضعیت خوانده‌شدهٔ یک متریک واحد را توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>containerResource</code><br/><em><a href="{{< ref "#ContainerResourceMetricStatus" >}}">ContainerResourceMetricStatus</a></em></td>
      <td>فیلد containerResource به یک متریک منبع شناخته‌شده برای کوبرنتیز (مانند منابعی که در requests و limits مشخص می‌شوند) اشاره می‌کند که یک کانتینر مشخص را در هر پاد از هدف مقیاس‌دهی فعلی توصیف می‌کند (مثلاً CPU یا حافظه). این متریک‌ها در خود کوبرنتیز تعبیه شده‌اند و علاوه بر گزینه‌های موجود برای متریک‌های معمولیِ مبتنی بر هر پاد که از منبع «pods» استفاده می‌کنند، گزینه‌های مقیاس‌دهی ویژه‌ای نیز دارند.</td>
    </tr>
    <tr>
      <td><code>external</code><br/><em><a href="{{< ref "#ExternalMetricStatus" >}}">ExternalMetricStatus</a></em></td>
      <td>فیلد external به یک متریک سراسری اشاره می‌کند که با هیچ آبجکت کوبرنتیز مرتبط نیست. با این فیلد می‌توان مقیاس‌دهی خودکار را بر اساس اطلاعاتی انجام داد که از اجزای در حال اجرا در بیرون از کلاستر می‌آیند (برای مثال، طول صف در یک سرویس پیام‌رسانی ابری یا QPS یک متعادل‌کنندهٔ بار که بیرون از کلاستر اجرا می‌شود).</td>
    </tr>
    <tr>
      <td><code>object</code><br/><em><a href="{{< ref "#ObjectMetricStatus" >}}">ObjectMetricStatus</a></em></td>
      <td>فیلد object به متریکی اشاره می‌کند که یک آبجکت مشخص کوبرنتیز را توصیف می‌کند (برای مثال، تعداد درخواست‌ها در ثانیه روی یک آبجکت Ingress).</td>
    </tr>
    <tr>
      <td><code>pods</code><br/><em><a href="{{< ref "#PodsMetricStatus" >}}">PodsMetricStatus</a></em></td>
      <td>فیلد pods به متریکی اشاره می‌کند که هر پاد را در هدف مقیاس‌دهی فعلی توصیف می‌کند (برای مثال، تعداد تراکنش‌های پردازش‌شده در ثانیه). پیش از مقایسه با مقدار هدف، از مقادیر میانگین گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>resource</code><br/><em><a href="{{< ref "#ResourceMetricStatus" >}}">ResourceMetricStatus</a></em></td>
      <td>فیلد resource به یک متریک منبع شناخته‌شده برای کوبرنتیز (مانند منابعی که در requests و limits مشخص می‌شوند) اشاره می‌کند که هر پاد را در هدف مقیاس‌دهی فعلی توصیف می‌کند (مثلاً CPU یا حافظه). این متریک‌ها در خود کوبرنتیز تعبیه شده‌اند و علاوه بر گزینه‌های موجود برای متریک‌های معمولیِ مبتنی بر هر پاد که از منبع «pods» استفاده می‌کنند، گزینه‌های مقیاس‌دهی ویژه‌ای نیز دارند.</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد type نوع منبع متریک است. مقدار آن یکی از "ContainerResource"، "External"، "Object"، "Pods" یا "Resource" خواهد بود که هرکدام با فیلد متناظری در آبجکت مطابقت دارد.</td>
    </tr>
  </tbody>
</table>


## MetricTarget {#MetricTarget}

نوع MetricTarget مقدار هدف، مقدار میانگین یا میانگین بهره‌وری یک متریک مشخص را تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>averageUtilization</code><br/><em>integer</em></td>
      <td>فیلد averageUtilization مقدار هدف برای میانگین متریک منبع در میان همهٔ پادهای مرتبط است و به‌صورت درصدی از مقدار درخواست‌شدهٔ آن منبع برای پادها بیان می‌شود. این فیلد در حال حاضر فقط برای منبع متریک از نوع Resource معتبر است.</td>
    </tr>
    <tr>
      <td><code>averageValue</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>فیلد averageValue مقدار هدف برای میانگین متریک در میان همهٔ پادهای مرتبط است (به‌صورت یک کمیت).</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد type نشان می‌دهد که نوع متریک Utilization، Value یا AverageValue است.</td>
    </tr>
    <tr>
      <td><code>value</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>فیلد value مقدار هدف متریک است (به‌صورت یک کمیت).</td>
    </tr>
  </tbody>
</table>


## MetricValueStatus {#MetricValueStatus}

نوع MetricValueStatus مقدار فعلی یک متریک را نگه می‌دارد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>averageUtilization</code><br/><em>integer</em></td>
      <td>فیلد averageUtilization مقدار فعلی میانگین متریک منبع در میان همهٔ پادهای مرتبط است و به‌صورت درصدی از مقدار درخواست‌شدهٔ آن منبع برای پادها بیان می‌شود.</td>
    </tr>
    <tr>
      <td><code>averageValue</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>فیلد averageValue مقدار فعلی میانگین متریک در میان همهٔ پادهای مرتبط است (به‌صورت یک کمیت).</td>
    </tr>
    <tr>
      <td><code>value</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>فیلد value مقدار فعلی متریک است (به‌صورت یک کمیت).</td>
    </tr>
  </tbody>
</table>


## ObjectMetricSource {#ObjectMetricSource}

نوع ObjectMetricSource نشان می‌دهد که مقیاس‌دهی بر اساس متریکی که یک آبجکت کوبرنتیز را توصیف می‌کند چگونه انجام شود (برای مثال، تعداد درخواست‌ها در ثانیه روی یک آبجکت Ingress).

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>describedObject</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#CrossVersionObjectReference" >}}">CrossVersionObjectReference</a></em></td>
      <td>فیلد describedObject مشخصات یک آبجکت، مانند kind، name و apiVersion، را تعیین می‌کند.</td>
    </tr>
    <tr>
      <td><code>metric</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricIdentifier" >}}">MetricIdentifier</a></em></td>
      <td>فیلد metric متریک هدف را با نام و انتخابگر آن شناسایی می‌کند.</td>
    </tr>
    <tr>
      <td><code>target</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricTarget" >}}">MetricTarget</a></em></td>
      <td>فیلد target مقدار هدف را برای متریک موردنظر مشخص می‌کند.</td>
    </tr>
  </tbody>
</table>


## ObjectMetricStatus {#ObjectMetricStatus}

نوع ObjectMetricStatus مقدار فعلی متریکی را نشان می‌دهد که یک آبجکت کوبرنتیز را توصیف می‌کند (برای مثال، تعداد درخواست‌ها در ثانیه روی یک آبجکت Ingress).

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>current</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricValueStatus" >}}">MetricValueStatus</a></em></td>
      <td>فیلد current مقدار فعلی متریک موردنظر را در بر دارد.</td>
    </tr>
    <tr>
      <td><code>describedObject</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#CrossVersionObjectReference" >}}">CrossVersionObjectReference</a></em></td>
      <td>فیلد describedObject مشخصات یک آبجکت، مانند kind، name و apiVersion، را تعیین می‌کند.</td>
    </tr>
    <tr>
      <td><code>metric</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricIdentifier" >}}">MetricIdentifier</a></em></td>
      <td>فیلد metric متریک هدف را با نام و انتخابگر آن شناسایی می‌کند.</td>
    </tr>
  </tbody>
</table>


## PodsMetricSource {#PodsMetricSource}

نوع PodsMetricSource نشان می‌دهد که مقیاس‌دهی بر اساس متریکی که هر پاد را در هدف مقیاس‌دهی فعلی توصیف می‌کند چگونه انجام شود (برای مثال، تعداد تراکنش‌های پردازش‌شده در ثانیه). پیش از مقایسه با مقدار هدف، از مقادیر میانگین گرفته می‌شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>metric</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricIdentifier" >}}">MetricIdentifier</a></em></td>
      <td>فیلد metric متریک هدف را با نام و انتخابگر آن شناسایی می‌کند.</td>
    </tr>
    <tr>
      <td><code>target</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricTarget" >}}">MetricTarget</a></em></td>
      <td>فیلد target مقدار هدف را برای متریک موردنظر مشخص می‌کند.</td>
    </tr>
  </tbody>
</table>


## PodsMetricStatus {#PodsMetricStatus}

نوع PodsMetricStatus مقدار فعلی متریکی را نشان می‌دهد که هر پاد را در هدف مقیاس‌دهی فعلی توصیف می‌کند (برای مثال، تعداد تراکنش‌های پردازش‌شده در ثانیه).

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>current</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricValueStatus" >}}">MetricValueStatus</a></em></td>
      <td>فیلد current مقدار فعلی متریک موردنظر را در بر دارد.</td>
    </tr>
    <tr>
      <td><code>metric</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricIdentifier" >}}">MetricIdentifier</a></em></td>
      <td>فیلد metric متریک هدف را با نام و انتخابگر آن شناسایی می‌کند.</td>
    </tr>
  </tbody>
</table>


## ResourceMetricSource {#ResourceMetricSource}

نوع ResourceMetricSource نشان می‌دهد که مقیاس‌دهی بر اساس یک متریک منبع شناخته‌شده برای کوبرنتیز، مطابق آنچه در requests و limits مشخص شده است، چگونه انجام شود؛ متریکی که هر پاد را در هدف مقیاس‌دهی فعلی توصیف می‌کند (مثلاً CPU یا حافظه). پیش از مقایسه با هدف، از مقادیر میانگین گرفته می‌شود. این متریک‌ها در خود کوبرنتیز تعبیه شده‌اند و علاوه بر گزینه‌های موجود برای متریک‌های معمولیِ مبتنی بر هر پاد که از منبع «pods» استفاده می‌کنند، گزینه‌های مقیاس‌دهی ویژه‌ای نیز دارند. فقط یک نوع «target» باید تنظیم شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد name نام منبع موردنظر است.</td>
    </tr>
    <tr>
      <td><code>target</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricTarget" >}}">MetricTarget</a></em></td>
      <td>فیلد target مقدار هدف را برای متریک موردنظر مشخص می‌کند.</td>
    </tr>
  </tbody>
</table>


## ResourceMetricStatus {#ResourceMetricStatus}

نوع ResourceMetricStatus مقدار فعلی یک متریک منبع شناخته‌شده برای کوبرنتیز را، مطابق آنچه در requests و limits مشخص شده است، نشان می‌دهد؛ متریکی که هر پاد را در هدف مقیاس‌دهی فعلی توصیف می‌کند (مثلاً CPU یا حافظه). این متریک‌ها در خود کوبرنتیز تعبیه شده‌اند و علاوه بر گزینه‌های موجود برای متریک‌های معمولیِ مبتنی بر هر پاد که از منبع «pods» استفاده می‌کنند، گزینه‌های مقیاس‌دهی ویژه‌ای نیز دارند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>current</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#MetricValueStatus" >}}">MetricValueStatus</a></em></td>
      <td>فیلد current مقدار فعلی متریک موردنظر را در بر دارد.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد name نام منبع موردنظر است.</td>
    </tr>
  </tbody>
</table>



## عملیات‌ها {#Operations}

<hr>

### ایجاد (`post`)

#### درخواست HTTP

درخواست `POST /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنه‌ی احراز هویت، برای مثال برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همه‌ی مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldManager نامی است که به عامل یا موجودیتِ اعمال‌کننده‌ی این تغییرات مربوط است. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط نویسه‌های قابل‌چاپ را، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، در بر بگیرد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldValidation به سرور اعلام می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: در این حالت، فیلدهای ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شوند نادیده گرفته می‌شوند و از میان فیلدهای تکراری، همه به‌جز آخرین فیلدی که رمزگشا (decoder) با آن روبه‌رو می‌شود نادیده گرفته می‌شوند. این رفتار پیش‌فرض در نسخه‌های پیش از v1.23 است. - Warn: در این حالت، برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که با آن روبه‌رو می‌شود، یک هشدار از طریق سرآیند استاندارد هشدار در پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان با موفقیت انجام می‌شود و از میان فیلدهای تکراری فقط آخرین آن‌ها ماندگار می‌شود. این رفتار پیش‌فرض در v1.23 و نسخه‌های بعدی است. - Strict: در این حالت، اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگشتی از سرور همه‌ی فیلدهای ناشناخته و تکراری‌ای را که با آن‌ها روبه‌رو شده است در بر می‌گیرد.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>موفق (OK)</td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد (Created)</td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>پذیرفته شد (Accepted)</td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
    </tr>
  </tbody>
</table>


### وصله (`patch`)

#### درخواست HTTP

درخواست `PATCH /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers/{name}`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام HorizontalPodAutoscaler</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنه‌ی احراز هویت، برای مثال برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همه‌ی مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldManager نامی است که به عامل یا موجودیتِ اعمال‌کننده‌ی این تغییرات مربوط است. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط نویسه‌های قابل‌چاپ را، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، در بر بگیرد. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع وصله‌ای که از نوع apply نیستند (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldValidation به سرور اعلام می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: در این حالت، فیلدهای ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شوند نادیده گرفته می‌شوند و از میان فیلدهای تکراری، همه به‌جز آخرین فیلدی که رمزگشا با آن روبه‌رو می‌شود نادیده گرفته می‌شوند. این رفتار پیش‌فرض در نسخه‌های پیش از v1.23 است. - Warn: در این حالت، برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که با آن روبه‌رو می‌شود، یک هشدار از طریق سرآیند استاندارد هشدار در پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان با موفقیت انجام می‌شود و از میان فیلدهای تکراری فقط آخرین آن‌ها ماندگار می‌شود. این رفتار پیش‌فرض در v1.23 و نسخه‌های بعدی است. - Strict: در این حالت، اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگشتی از سرور همه‌ی فیلدهای ناشناخته و تکراری‌ای را که با آن‌ها روبه‌رو شده است در بر می‌گیرد.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>گزینه‌ی Force درخواست‌های Apply را «به‌اجبار» اعمال می‌کند؛ یعنی کاربر مالکیت فیلدهای متعارضی را که در اختیار دیگران است دوباره به دست می‌گیرد. برای درخواست‌های وصله‌ای که از نوع apply نیستند، پرچم Force نباید تنظیم شود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/patch-v1-meta#Patch" >}}">Patch</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>موفق</td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد</td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
    </tr>
  </tbody>
</table>


### جایگزینی (`put`)

#### درخواست HTTP

درخواست `PUT /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers/{name}`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام HorizontalPodAutoscaler</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنه‌ی احراز هویت، برای مثال برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همه‌ی مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldManager نامی است که به عامل یا موجودیتِ اعمال‌کننده‌ی این تغییرات مربوط است. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط نویسه‌های قابل‌چاپ را، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، در بر بگیرد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldValidation به سرور اعلام می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: در این حالت، فیلدهای ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شوند نادیده گرفته می‌شوند و از میان فیلدهای تکراری، همه به‌جز آخرین فیلدی که رمزگشا با آن روبه‌رو می‌شود نادیده گرفته می‌شوند. این رفتار پیش‌فرض در نسخه‌های پیش از v1.23 است. - Warn: در این حالت، برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که با آن روبه‌رو می‌شود، یک هشدار از طریق سرآیند استاندارد هشدار در پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان با موفقیت انجام می‌شود و از میان فیلدهای تکراری فقط آخرین آن‌ها ماندگار می‌شود. این رفتار پیش‌فرض در v1.23 و نسخه‌های بعدی است. - Strict: در این حالت، اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگشتی از سرور همه‌ی فیلدهای ناشناخته و تکراری‌ای را که با آن‌ها روبه‌رو شده است در بر می‌گیرد.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>موفق</td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد</td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
    </tr>
  </tbody>
</table>


### حذف (`delete`)

#### درخواست HTTP

درخواست `DELETE /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers/{name}`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام HorizontalPodAutoscaler</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنه‌ی احراز هویت، برای مثال برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همه‌ی مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت‌زمانی برحسب ثانیه که باید پیش از حذف آبجکت سپری شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، مهلت پیش‌فرض برای نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرضِ مختص هر آبجکت به کار می‌رود. صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناایمنِ منبع آغاز می‌شود. یک منبع زمانی خراب در نظر گرفته می‌شود که نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد، به این دلیل که الف) داده‌های آن قابل تبدیل نیست، برای مثال رمزگشایی آن ناموفق است، یا ب) تبدیل آن به یک آبجکت شکست می‌خورد. نکته: حذف ناایمن محدودیت‌های finalizer را نادیده می‌گیرد، از بررسی پیش‌شرط‌ها صرف‌نظر می‌کند و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را از کار بیندازد. فقط در صورتی از آن استفاده کنید که واقعاً می‌دانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آگاهانه آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه‌ی 1.7 منسوخ خواهد شد. تعیین می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر true/false باشد، finalizer «orphan» به فهرست finalizerهای آبجکت افزوده/از آن حذف می‌شود. می‌توان یا این فیلد را تنظیم کرد یا PropagationPolicy را، اما نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>تعیین می‌کند که آیا و چگونه جمع‌آوری زباله (garbage collection) انجام شود. می‌توان یا این فیلد را تنظیم کرد یا OrphanDependents را، اما نه هر دو را. سیاست پیش‌فرض بر اساس مجموعه‌ی finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرضِ مختص منبع تعیین می‌شود. مقادیر قابل‌قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - به جمع‌آورنده‌ی زباله اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - سیاستی آبشاری که همه‌ی وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/delete-options-v1-meta#DeleteOptions" >}}">DeleteOptions</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>موفق</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>پذیرفته شد</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
  </tbody>
</table>

### `delete` حذف مجموعه

#### درخواست HTTP

DELETE /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنهٔ احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینهٔ continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار (consistent) نیاز داشته باشد، باید درخواست فهرست را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را همراه با توکن دریافت‌شده در خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی شروع می‌شود، اما بر پایهٔ آخرین snapshot است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion بازگردانده‌شده از سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار (persist) شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. به‌طور پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت‌زمانی به ثانیه که پیش از حذف آبجکت باید سپری شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، مهلت پیش‌فرض برای نوع مشخص‌شده استفاده می‌شود. اگر مشخص نشود، مقدار پیش‌فرض به ازای هر آبجکت تعیین می‌شود. صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناامن منبع را آغاز می‌کند. یک منبع زمانی خراب به شمار می‌آید که نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد، به این دلیل که الف) داده‌های آن قابل تبدیل نیستند، برای مثال رمزگشایی آن‌ها شکست می‌خورد، یا ب) تبدیل آن به آبجکت (decode) ناموفق است. نکته: حذف ناامن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی پیش‌شرط‌ها را انجام نمی‌دهد و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناامن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را از کار بیندازد. فقط در صورتی از آن استفاده کنید که واقعاً می‌دانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آگاهانه آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. به‌طور پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list بازمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده (metadata) فهرست با مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواستی فیلتر شوند، تنظیم limit ممکن است تعدادی کمتر از آیتم‌های درخواستی (حتی صفر آیتم) بازگرداند؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص وجود نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و همهٔ نتایج موجود را بازگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری وجود ندارد. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود.  سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از ارسال نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامهٔ بعدی گنجانده نمی‌شود. گاهی به این ویژگی snapshot سازگار (consistent snapshot) گفته می‌شود و تضمین می‌کند کلاینتی که با استفاده از limit یک نتیجهٔ بسیار بزرگ را در تکه‌های کوچک‌تر دریافت می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین دریافت تکه‌تکهٔ فهرست به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. تعیین می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر true/false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت افزوده یا از آن حذف می‌شود. می‌توان یا این فیلد یا PropagationPolicy را تنظیم کرد، اما نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>تعیین می‌کند که آیا جمع‌آوری زباله (garbage collection) انجام شود و چگونه. می‌توان یا این فیلد یا OrphanDependents را تنظیم کرد، اما نه هر دو را. سیاست پیش‌فرض بر اساس مجموعهٔ finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض ویژهٔ هر منبع تعیین می‌شود. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - به جمع‌آورندهٔ زباله اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - سیاستی آبشاری که همهٔ وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که درخواست را می‌توان از کدام نسخه‌های منبع پاسخ داد. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید.  به‌طور پیش‌فرض تنظیم نشده است</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید.  به‌طور پیش‌فرض تنظیم نشده است</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این صورت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظر را ارسال می‌کند.  هنگامی که گزینهٔ `sendInitialEvents` تنظیم شده باشد، لازم است گزینهٔ `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - اگر `resourceVersionMatch` = NotOlderThan باشد، به معنای «داده‌هایی دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگی مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» (consistent read) تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا اصلاً تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود.  مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. این قالب از تابع shardRange() همراه با || (OR منطقی) برای مشخص‌کردن یک یا چند بازهٔ hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object استفاده می‌کنند (برای مثال "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون نقل‌قول تکی با پیشوند '0x' هستند که کران پایین (شامل) و کران بالای (غیرشامل) را روی فضای hash ‏۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی (timeout) برای فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت، محدود می‌کند.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/delete-options-v1-meta#DeleteOptions" >}}">DeleteOptions</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
  </tbody>
</table>


### `get` خواندن

#### درخواست HTTP

GET /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام HorizontalPodAutoscaler</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنهٔ احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
    </tr>
  </tbody>
</table>

### عملیات `get` برای فهرست‌گیری

#### درخواست HTTP

GET /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنهٔ احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا یک ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>این فیلد رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه‌های زمانی مشخصی بازگردانده می‌شوند و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست حتماً رویدادی از نوع BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور، باید گزینهٔ continue تنظیم شود. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما از آخرین snapshot گرفته شده و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، به شرط آنکه کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور بازگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>این فیلد بیشینهٔ تعداد پاسخ‌هایی را تعیین می‌کند که یک فراخوانی فهرست برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فرادادهٔ فهرست به مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواستی فیلتر شوند، تعیین limit ممکن است به بازگشت آیتم‌هایی کمتر از تعداد درخواستی (حتی صفر آیتم) منجر شود؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص وجود نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و همهٔ نتایج موجود را برگردانند. اگر limit مشخص شده و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری وجود ندارد. اگر watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. گاهی به این ویژگی snapshot سازگار (consistent snapshot) گفته می‌شود. این ویژگی تضمین می‌کند کلاینتی که با استفاده از limit نتیجه‌ای بسیار بزرگ را در تکه‌های کوچک‌تر دریافت می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>این فیلد محدودیتی تعیین می‌کند که درخواست را بتوان از کدام نسخه‌های منبع پاسخ داد. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>این فیلد تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>مقدار `sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این صورت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark نسخهٔ منبع (ResourceVersion یا RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌دهد و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات آبجکت‌های تحت نظر (پس از RV) را ارسال می‌کند. وقتی گزینهٔ `sendInitialEvents` تنظیم شده باشد، لازم است گزینهٔ `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - اگر `resourceVersionMatch` = NotOlderThan باشد، به معنای «داده‌ای دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا `resourceVersion`ی همگام شده باشد که دست‌کم به تازگی مقدار ارائه‌شده در ListOptions است. اگر `resourceVersion` تنظیم نشده باشد، به معنای «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` به هر مقدار دیگری تنظیم شده یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>این فیلد فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با || (OR منطقی) برای تعیین یک یا چند بازهٔ هش به کار می‌رود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object استفاده می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون تک‌نقل‌قول و با پیشوند '0x' هستند و کران پایین (شامل) و کران بالا (غیرشامل) را روی فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  نمونه‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد در مرحلهٔ آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscalerList" >}}">HorizontalPodAutoscalerList</a></em></td>
    </tr>
  </tbody>
</table>

### عملیات `get`: فهرست کردن در همهٔ فضاهای نام

#### درخواست HTTP

GET /apis/autoscaling/v2/horizontalpodautoscalers



#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>فیلد allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmarkها را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند. ارسال bookmarkها نیز به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی بازگردانده می‌شوند. همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست اصلاً رویداد BOOKMARK ارسال خواهد کرد. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینهٔ continue را تنظیم کرد. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند. سرور نیز ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired به همراه یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند. در این حالت، سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما بر پایهٔ آخرین snapshot است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، به شرط آنکه کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور بازگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض آن همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض آن همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>مقدار limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست بازمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فرادادهٔ فهرست به مقداری تنظیم می‌کند که می‌توان آن را همراه همان پرس‌وجوی اولیه برای دریافت مجموعهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواستی فیلتر شوند، تنظیم limit ممکن است به بازگشت تعدادی کمتر از آیتم‌های درخواستی (حتی صفر آیتم) منجر شود. بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و در این صورت همهٔ نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری در دسترس نیست. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. گاهی به این ویژگی snapshot سازگار (consistent snapshot) گفته می‌شود. این ویژگی تضمین می‌کند کلاینتی که با استفاده از limit یک نتیجهٔ بسیار بزرگ را در قطعه‌های کوچک‌تر دریافت می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول یک فهرست‌گیری قطعه‌قطعه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت قالب‌بندی‌شده و خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersion محدودیتی تعیین می‌کند که یک درخواست را می‌توان از کدام نسخه‌های منبع پاسخ داد. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. این فیلد به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. این فیلد به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را بسازد. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark نسخهٔ منبع (ResourceVersion یا RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. وقتی گزینهٔ `sendInitialEvents` تنظیم شده باشد، گزینهٔ `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به این صورت است:<br/> - اگر `resourceVersionMatch` برابر NotOlderThan باشد، به‌معنای «داده‌ای دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگی نسخهٔ ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا اصلاً تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد، مقدار پیش‌فرض true است (به دلایل سازگاری با نسخه‌های قبلی) و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>فیلد shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازهٔ هش به کار می‌رود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object استفاده می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون تک‌نقل‌قول و با پیشوند '0x' هستند که کران پایینِ شامل و کران بالای غیرشامل را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که کران بالای غیرشامل آن برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و برای استفاده از آن باید feature gate با نام ShardedListAndWatch را فعال کنید.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار، مدت فراخوانی را صرف‌نظر از وجود یا نبود فعالیت محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscalerList" >}}">HorizontalPodAutoscalerList</a></em></td>
    </tr>
  </tbody>
</table>

### نظارت (`get` Watch)

#### درخواست HTTP

GET /apis/autoscaling/v2/watch/namespaces/{namespace}/horizontalpodautoscalers/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام HorizontalPodAutoscaler</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنهٔ احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاح‌دید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی بازگردانده می‌شوند و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینهٔ continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار (consistent) نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست list دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما بر پایهٔ جدیدترین snapshot تهیه شده و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست list ایجاد، تغییر یا حذف شده‌اند، به شرط آنکه کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده از سرور آغاز کنند تا هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list بازمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده‌های فهرست به مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت دستهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواستی فیلتر شوند، تعیین limit ممکن است به بازگشت آیتم‌هایی کمتر از تعداد درخواستی (حتی صفر آیتم) منجر شود؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و همهٔ نتایج موجود را بازگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری در دسترس نیست. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود.  سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی list بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این وضعیت گاهی snapshot سازگار (consistent snapshot) گفته می‌شود و تضمین می‌کند کلاینتی که با استفاده از limit یک نتیجهٔ بسیار بزرگ را در تکه‌های کوچک‌تر دریافت می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول یک فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی با قالب‌بندی خوانا (pretty print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که درخواست بر اساس کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات، https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions را ببینید.  به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های listای که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات، https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions را ببینید.  به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>مقدار `sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark نسخهٔ منبع (ResourceVersion یا RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظارت را ارسال می‌کند.  هنگامی که گزینهٔ `sendInitialEvents` تنظیم شده باشد، گزینهٔ `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به این صورت است:<br/> - اگر `resourceVersionMatch` برابر NotOlderThan باشد، به معنای «داده‌ای دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگی مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود.  مقدار پیش‌فرض، در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی)، true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. این قالب از تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازهٔ هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو ریشه‌دار در object به سبک CEL استفاده می‌کنند (مانند "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر عبارت‌اند از:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون تک‌نقل‌قول با پیشوند '0x' هستند که کران پایینِ شامل و کران بالای غیرشامل را در فضای هش ۶۴ بیتی FNV-1a تعیین می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد در مرحلهٔ آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت زمان فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>

### پایش فهرست با `get`

#### درخواست HTTP

GET /apis/autoscaling/v2/watch/namespaces/{namespace}/horizontalpodautoscalers


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنهٔ احراز هویت و مجوز، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>این پارامتر رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که بوکمارک‌ها را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال بوکمارک‌ها به صلاحدید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که بوکمارک‌ها در بازه‌های زمانی مشخصی بازگردانده می‌شوند و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست اصلاً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینهٔ continue باید هنگام بازیابی نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما بر پایهٔ جدیدترین تصویر لحظه‌ای (snapshot) است و با نتایج فهرست قبلی سازگار نیست: آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، در صورتی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور بازگردانده است آغاز کنند، بی‌آنکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>این پارامتر حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فرادادهٔ فهرست برابر مقداری قرار می‌دهد که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای بازیابی مجموعهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواستی فیلتر شوند، تعیین limit ممکن است به بازگشت آیتم‌هایی کمتر از تعداد درخواستی (حتی صفر آیتم) بینجامد؛ بنابراین کلاینت‌ها فقط باید وجود فیلد continue را ملاک تشخیص در دسترس بودن نتایج بیشتر قرار دهند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و در این صورت همهٔ نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری وجود ندارد. اگر watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. گاهی به این ویژگی snapshot سازگار گفته می‌شود و تضمین می‌کند کلاینتی که با استفاده از limit یک نتیجهٔ بسیار بزرگ را در تکه‌های کوچک‌تر دریافت می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین دریافت تکه‌تکهٔ فهرست به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به شکل خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>این پارامتر محدودیتی تعیین می‌کند که درخواست را بتوان از کدام نسخه‌های منبع پاسخ داد. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>این پارامتر تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را بازسازی می‌کنند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این بوکمارک، ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch مربوط به تغییرات (پس از RV) در آبجکت‌های تحت پایش را ارسال می‌کند. وقتی گزینهٔ `sendInitialEvents` تنظیم شده باشد، لازم است گزینهٔ `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این شرح است:<br/> - اگر `resourceVersionMatch` = NotOlderThan باشد، به معنای «داده‌ای دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد بوکمارک زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگی مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» تفسیر می‌شود و رویداد بوکمارک زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` برابر هر مقدار دیگری باشد یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض، در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی)، true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>این پارامتر فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر شارد مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با || (OR منطقی) برای تعیین یک یا چند بازهٔ هش به کار می‌رود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object استفاده می‌کنند (برای مثال "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون تک‌نقل‌قول و با پیشوند '0x' هستند که کران پایین (شامل) و کران بالای (غیرشامل) بازه را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     شارد 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     شارد 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را پایش می‌کند و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>

### عملیات `get`: پایش فهرست در همه فضاهای نام

#### درخواست HTTP

درخواست: `GET /apis/autoscaling/v2/watch/horizontalpodautoscalers`



#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که بوک‌مارک را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال بوک‌مارک‌ها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که بوک‌مارک‌ها در فاصله‌های زمانی مشخصی بازگردانده می‌شوند و همچنین نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست list دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی آغاز می‌شود، اما از آخرین تصویر لحظه‌ای (snapshot) تهیه شده است و با نتایج فهرست قبلی سازگار نیست: آبجکت‌هایی که پس از نخستین درخواست list ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده از سرور آغاز کنند، بی‌آنکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض، همه آبجکت‌ها است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه آبجکت‌ها است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit بیشینه تعداد پاسخ‌هایی است که یک فراخوانی list بازمی‌گرداند. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست با مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه بعدی نتایج به کار برد. اگر همه آبجکت‌های درخواستی فیلتر شوند، تنظیم limit ممکن است به بازگشت مواردی کمتر از تعداد درخواستی (حتی صفر مورد) بینجامد؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است آرگومان limit را پشتیبانی نکنند و همه نتایج موجود را بازگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری در دسترس نیست. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجه یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. گاهی به این ویژگی «تصویر لحظه‌ای سازگار» (consistent snapshot) گفته می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تری از یک نتیجه بسیار بزرگ استفاده می‌کند، همه آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول یک فهرست‌گیری بخش‌بخش به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبه نخستین نتیجه فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که درخواست می‌تواند بر اساس کدام نسخه‌های منبع پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این صورت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این بوک‌مارک نسخه منبع (ResourceVersion یا RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch مربوط به تغییرات (پس از RV) در آبجکت‌های پایش‌شده را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این صورت است:<br/> - اگر `resourceVersionMatch` برابر NotOlderThan باشد، به‌معنای «داده‌ای دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد بوک‌مارک زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگیِ نسخه‌ای که ListOptions ارائه کرده است همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌معنای «خواندن سازگار» (consistent read) تفسیر می‌شود و رویداد بوک‌مارک زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم‌نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر شارد مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازه هش به کار می‌رود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو ریشه‌دار در object به سبک CEL استفاده می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون تک‌نقل‌قول با پیشوند '0x' هستند که کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر با 2^64 است.  نمونه‌ها:   تقسیم به ۲ شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     شارد 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     شارد 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد در مرحله آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را پایش می‌کند و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>موفق</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>


### عملیات `patch`: وصله‌کردن وضعیت

#### درخواست HTTP

درخواست: `PATCH /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers/{name}/status`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام HorizontalPodAutoscaler</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنه احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را ایجاد می‌کند نسبت داده می‌شود. طول این مقدار باید حداکثر ۱۲۸ کاراکتر باشد و فقط شامل کاراکترهای قابل چاپ، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شود نادیده می‌گیرد و از میان فیلدهای تکراری که رمزگشا با آن‌ها روبه‌رو می‌شود، همه را به‌جز آخرین مورد نادیده می‌گیرد. این رفتار پیش‌فرض در نسخه‌های پیش از v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن روبه‌رو می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در v1.23 به بعد است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگردانده‌شده از سرور شامل همه فیلدهای ناشناخته و تکراری یافت‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر Force درخواست‌های Apply را «اجباری» می‌کند؛ یعنی کاربر فیلدهای متعارضی را که مالکیتشان با دیگران است دوباره در اختیار می‌گیرد. در درخواست‌های patch غیر از apply، پرچم Force باید تنظیم‌نشده باقی بماند.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/patch-v1-meta#Patch" >}}">Patch</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>موفق</td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد</td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
    </tr>
  </tbody>
</table>


### عملیات `get`: خواندن وضعیت

#### درخواست HTTP

درخواست: `GET /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers/{name}/status`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام HorizontalPodAutoscaler</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنه احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>موفق</td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
    </tr>
  </tbody>
</table>


### عملیات `put`: جایگزینی وضعیت

#### درخواست HTTP

درخواست: `PUT /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers/{name}/status`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام HorizontalPodAutoscaler</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنه احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را ایجاد می‌کند نسبت داده می‌شود. طول این مقدار باید حداکثر ۱۲۸ کاراکتر باشد و فقط شامل کاراکترهای قابل چاپ، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شود نادیده می‌گیرد و از میان فیلدهای تکراری که رمزگشا با آن‌ها روبه‌رو می‌شود، همه را به‌جز آخرین مورد نادیده می‌گیرد. این رفتار پیش‌فرض در نسخه‌های پیش از v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن روبه‌رو می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در v1.23 به بعد است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگردانده‌شده از سرور شامل همه فیلدهای ناشناخته و تکراری یافت‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>موفق</td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد</td>
      <td><em><a href="{{< ref "horizontal-pod-autoscaler-v2#HorizontalPodAutoscaler" >}}">HorizontalPodAutoscaler</a></em></td>
    </tr>
  </tbody>
</table>
