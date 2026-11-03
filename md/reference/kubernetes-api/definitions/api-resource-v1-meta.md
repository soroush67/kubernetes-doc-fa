---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "APIResource"
content_type: "api_reference"
description: "APIResource نام یک منبع و namespaced بودن یا نبودن آن را مشخص می‌کند."
title: "APIResource"
weight: 30
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

`apiVersion: meta/v1`

`import "k8s.io/apimachinery/pkg/apis/meta/v1"`


## APIResource {#APIResource}

APIResource نام یک منبع و namespaced بودن یا نبودن آن را مشخص می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>categories</code><br/><em>string array</em></td>
      <td>categories فهرستی از منابع گروه‌بندی‌شده است که این منبع به آن‌ها تعلق دارد (برای مثال 'all').</td>
    </tr>
    <tr>
      <td><code>group</code><br/><em>string</em></td>
      <td>group گروه ترجیحی منبع است. مقدار خالی به این معناست که گروه همان گروهِ فهرست منابعِ حاوی آن است. برای زیرمنبع‌ها (subresource) ممکن است این مقدار متفاوت باشد، برای مثال: Scale".</td>
    </tr>
    <tr>
      <td><code>kind</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>kind نوع (kind) منبع را مشخص می‌کند (برای مثال 'Foo' نوعِ منبع 'foo' است).</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>name نام جمع منبع است.</td>
    </tr>
    <tr>
      <td><code>namespaced</code>&nbsp;<strong>*</strong><br/><em>boolean</em></td>
      <td>namespaced نشان می‌دهد که منبع در فضای نام (namespace) قرار می‌گیرد یا خیر.</td>
    </tr>
    <tr>
      <td><code>shortNames</code><br/><em>string array</em></td>
      <td>shortNames فهرستی از نام‌های کوتاهِ پیشنهادی برای منبع است.</td>
    </tr>
    <tr>
      <td><code>singularName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>singularName نام مفرد منبع است. این فیلد به کلاینت‌ها امکان می‌دهد نام جمع و مفرد را به‌صورت مبهم (opaque) مدیریت کنند. singularName برای گزارش وضعیت یک آیتم واحد مناسب‌تر است و در رابط خط فرمان kubectl هر دو شکل مفرد و جمع مجاز هستند.</td>
    </tr>
    <tr>
      <td><code>storageVersionHash</code><br/><em>string</em></td>
      <td>مقدار hash نسخه ذخیره‌سازی (storage version) است؛ یعنی نسخه‌ای که این منبع هنگام نوشتن در data store به آن تبدیل می‌شود. کلاینت‌ها باید این مقدار را مبهم (opaque) در نظر بگیرند و فقط مقایسه برابری روی آن معتبر است. این قابلیت آلفا است و ممکن است در آینده تغییر کند یا حذف شود. apiserver این فیلد را تنها در صورتی مقداردهی می‌کند که feature gate با نام StorageVersionHash فعال باشد. این فیلد حتی پس از ارتقا به مرحله‌های بعدی نیز اختیاری باقی می‌ماند.</td>
    </tr>
    <tr>
      <td><code>verbs</code>&nbsp;<strong>*</strong><br/><em>string array</em></td>
      <td>verbs فهرستی از افعال (verb) پشتیبانی‌شده در kube است (شامل get، list، watch، create، update، patch، delete، deletecollection و proxy).</td>
    </tr>
    <tr>
      <td><code>version</code><br/><em>string</em></td>
      <td>version نسخه ترجیحی منبع است. مقدار خالی به این معناست که نسخه همان نسخهٔ فهرست منابعِ حاوی آن است. برای زیرمنبع‌ها ممکن است این مقدار متفاوت باشد، برای مثال: v1 (در حالی که درون نسخه v1beta1 از گروه منبع هسته قرار دارد)".</td>
    </tr>
  </tbody>
</table>


## APIResourceList {#APIResourceList}

APIResourceList فهرستی از APIResource است که برای نمایش نام منابع پشتیبانی‌شده در یک گروه و نسخهٔ مشخص و نیز namespaced بودن یا نبودن منبع استفاده می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرحواره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرحواره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>groupVersion</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>groupVersion گروه و نسخه‌ای است که این APIResourceList برای آن است.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind رشته‌ای است که منبع REST مربوط به این آبجکت را مشخص می‌کند. سرورها ممکن است این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. این فیلد قابل به‌روزرسانی نیست و باید به‌صورت CamelCase باشد. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>resources</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "api-resource-v1-meta#APIResource" >}}">APIResource array</a></em></td>
      <td>resources شامل نام منابع و namespaced بودن یا نبودن آن‌هاست.</td>
    </tr>
  </tbody>
</table>
