---
api_metadata:
  apiVersion: "resource.k8s.io/v1beta1"
  import: "k8s.io/api/resource/v1beta1"
  kind: "BasicDevice"
content_type: "api_reference"
description: "BasicDevice یک نمونه از دستگاه (device) را تعریف می‌کند."
title: "BasicDevice"
weight: 50
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

`apiVersion: resource.k8s.io/v1beta1`

`import "k8s.io/api/resource/v1beta1"`


## BasicDevice {#BasicDevice}

BasicDevice یک نمونه از دستگاه (device) را تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allNodes</code><br/><em>boolean</em></td>
      <td>AllNodes نشان می‌دهد که همهٔ نودها به این دستگاه دسترسی دارند. فقط در صورتی باید تنظیم شود که Spec.PerDeviceNodeSelection روی true تنظیم شده باشد. حداکثر یکی از فیلدهای NodeName، NodeSelector و AllNodes را می‌توان تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>allowMultipleAllocations</code><br/><em>boolean</em></td>
      <td>AllowMultipleAllocations مشخص می‌کند که آیا اجازه داده می‌شود دستگاه به چندین DeviceRequest تخصیص یابد یا خیر. اگر AllowMultipleAllocations روی true تنظیم شود، دستگاه را می‌توان بیش از یک بار تخصیص داد و تمام ظرفیت آن، صرف‌نظر از اینکه requestPolicy تعریف شده باشد یا نه، قابل مصرف است.</td>
    </tr>
    <tr>
      <td><code>attributes</code><br/><em>object</em></td>
      <td>Attributes مجموعه ویژگی‌های (attributes) این دستگاه را تعریف می‌کند. نام هر ویژگی باید در این مجموعه یکتا باشد. حداکثر تعداد مجموع ویژگی‌ها و ظرفیت‌ها ۳۲ است.</td>
    </tr>
    <tr>
      <td><code>bindingConditions</code><br/><em>string array</em></td>
      <td>BindingConditions شرایط لازم برای ادامهٔ فرایند اتصال (binding) را تعریف می‌کند. برای اینکه هنگام زمان‌بندی Pod، اتصال آن به نود ادامه یابد، همهٔ این شرایط باید در شرایط وضعیت (status conditions) هر دستگاه با مقدار True تنظیم شده باشند. حداکثر تعداد شرایط اتصال ۴ است. شرایط باید رشته‌ای معتبر برای نوع شرط (condition type) باشند. این فیلد در سطح بتا است و برای استفاده از آن باید feature gateهای DRADeviceBindingConditions و DRAResourceClaimDeviceStatus فعال شوند.</td>
    </tr>
    <tr>
      <td><code>bindingFailureConditions</code><br/><em>string array</em></td>
      <td>BindingFailureConditions شرایط مربوط به شکست اتصال را تعریف می‌کند. این شرایط را می‌توان در شرایط وضعیت (status conditions) هر دستگاه تنظیم کرد. اگر هرکدام از آن‌ها true باشد، یعنی اتصال با شکست مواجه شده است. حداکثر تعداد شرایط شکست اتصال ۴ است. شرایط باید رشته‌ای معتبر برای نوع شرط (condition type) باشند. این فیلد در سطح بتا است و برای استفاده از آن باید feature gateهای DRADeviceBindingConditions و DRAResourceClaimDeviceStatus فعال شوند.</td>
    </tr>
    <tr>
      <td><code>bindsToNode</code><br/><em>boolean</em></td>
      <td>BindsToNode نشان می‌دهد که آیا استفاده از یک تخصیص شامل این دستگاه باید دقیقاً به نودی محدود شود که هنگام تخصیص claim انتخاب شده است یا خیر. اگر روی true تنظیم شود، زمان‌بند مقدار ResourceClaim.Status.Allocation.NodeSelector را طوری تنظیم می‌کند که با نودی که تخصیص در آن انجام شده است مطابقت داشته باشد. این فیلد در سطح بتا است و برای استفاده از آن باید feature gateهای DRADeviceBindingConditions و DRAResourceClaimDeviceStatus فعال شوند.</td>
    </tr>
    <tr>
      <td><code>capacity</code><br/><em>object</em></td>
      <td>Capacity مجموعه ظرفیت‌های این دستگاه را تعریف می‌کند. نام هر ظرفیت باید در این مجموعه یکتا باشد. حداکثر تعداد مجموع ویژگی‌ها و ظرفیت‌ها ۳۲ است.</td>
    </tr>
    <tr>
      <td><code>consumesCounters</code><br/><em><a href="{{< ref "../resource/resource-slice-v1#DeviceCounterConsumption" >}}">DeviceCounterConsumption array</a></em></td>
      <td>ConsumesCounters فهرستی از ارجاع‌ها به sharedCounters و مجموعه شمارنده‌هایی را تعریف می‌کند که دستگاه از آن مجموعه‌های شمارنده مصرف خواهد کرد. برای هر counterSet فقط یک ورودی می‌تواند وجود داشته باشد. حداکثر تعداد مصرف شمارندهٔ دستگاه (device counter consumption) برای هر دستگاه ۲ است.</td>
    </tr>
    <tr>
      <td><code>nodeAllocatableResources</code><br/><em>object</em></td>
      <td>NodeAllocatableResources نگاشت منابع نود را تعریف می‌کند که توسط درایور DRA عرضه‌کنندهٔ این دستگاه مدیریت می‌شوند. این شامل منابعی است که در حال حاضر در `status.allocatable` آبجکت v1.Node گزارش می‌شوند و منبع توسعه‌یافته (extended resource) نیستند (به https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#extended-resources مراجعه کنید). از نمونه‌های آن می‌توان به "cpu"، "memory"، "ephemeral-storage" و hugepages اشاره کرد. افزون بر درخواست‌های معمول که از طریق `spec` در Pod ثبت می‌شوند، این منابع را می‌توان از طریق claimها نیز درخواست کرد و درایور DRA آن‌ها را تخصیص می‌دهد. برای مثال، یک درایور DRA برای CPU ممکن است CPUهای اختصاصی یا وابستگی‌های حافظهٔ کمکی نود برای یک دستگاه شتاب‌دهنده (accelerator) را تخصیص دهد. کلیدهای این نگاشت، نام منابع قابل تخصیص نود (node-allocatable) هستند (برای مثال "cpu" و "memory"). نام منابع توسعه‌یافته به‌عنوان کلید مجاز نیست.</td>
    </tr>
    <tr>
      <td><code>nodeName</code><br/><em>string</em></td>
      <td>NodeName نودی را مشخص می‌کند که دستگاه در آن در دسترس است. فقط در صورتی باید تنظیم شود که Spec.PerDeviceNodeSelection روی true تنظیم شده باشد. حداکثر یکی از فیلدهای NodeName، NodeSelector و AllNodes را می‌توان تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>nodeSelector</code><br/><em><a href="{{< ref "node-selector-v1#NodeSelector" >}}">NodeSelector</a></em></td>
      <td>NodeSelector نودهایی را تعریف می‌کند که دستگاه در آن‌ها در دسترس است. باید دقیقاً از یک term استفاده کند. فقط در صورتی باید تنظیم شود که Spec.PerDeviceNodeSelection روی true تنظیم شده باشد. حداکثر یکی از فیلدهای NodeName، NodeSelector و AllNodes را می‌توان تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>taints</code><br/><em><a href="{{< ref "../resource/device-taint-rule-v1#DeviceTaint" >}}">DeviceTaint array</a></em></td>
      <td>در صورت مشخص شدن، این‌ها taintهایی هستند که درایور تعریف کرده است. حداکثر تعداد taintها ۱۶ است. اگر برای هر دستگاه در یک ResourceSlice، taint تنظیم شود، حداکثر تعداد دستگاه‌های مجاز در هر ResourceSlice به‌جای ۱۲۸، برابر با ۶۴ خواهد بود. این فیلد در سطح بتا است و برای استفاده از آن باید feature gate با نام DRADeviceTaints فعال شود.</td>
    </tr>
  </tbody>
</table>
