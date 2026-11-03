---
api_metadata:
  apiVersion: "autoscaling/v1"
  import: "k8s.io/api/autoscaling/v1"
  kind: "Scale"
content_type: "api_reference"
description: "Scale نمایانگر یک درخواست مقیاس‌دهی برای یک منبع است."
title: "Scale"
weight: 440
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

`apiVersion: autoscaling/v1`

`import "k8s.io/api/autoscaling/v1"`


## Scale {#Scale}

Scale نمایانگر یک درخواست مقیاس‌دهی برای یک منبع است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST نمایش‌داده‌شده توسط این آبجکت را مشخص می‌کند. سرورها می‌توانند این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌های خود را به آن ارسال می‌کند استنباط کنند. این فیلد قابل به‌روزرسانی نیست و با قالب CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>metadata فراداده استاندارد آبجکت است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.</td>
    </tr>
    <tr>
      <td><code>spec</code><br/><em><a href="{{< ref "#ScaleSpec" >}}">ScaleSpec</a></em></td>
      <td>spec رفتار مقیاس‌دهی (scale) را تعریف می‌کند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "#ScaleStatus" >}}">ScaleStatus</a></em></td>
      <td>status وضعیت فعلی مقیاس‌دهی (scale) است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. فقط‌خواندنی است.</td>
    </tr>
  </tbody>
</table>


## ScaleSpec {#ScaleSpec}

ScaleSpec ویژگی‌های زیرمنبع scale را توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>replicas</code><br/><em>integer</em></td>
      <td>replicas تعداد مطلوب نمونه‌ها (instances) برای آبجکت مقیاس‌پذیر است.</td>
    </tr>
  </tbody>
</table>


## ScaleStatus {#ScaleStatus}

ScaleStatus وضعیت فعلی زیرمنبع scale را نمایش می‌دهد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>replicas</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>replicas تعداد واقعی نمونه‌های مشاهده‌شده از آبجکت مقیاس‌پذیر است.</td>
    </tr>
    <tr>
      <td><code>selector</code><br/><em>string</em></td>
      <td>selector یک پرس‌وجوی برچسب (label query) روی Podهاست که باید با تعداد replicas مطابقت داشته باشد. این مقدار همان انتخابگر برچسب (label selector) است، اما برای جلوگیری از بررسی ساختار آن توسط کلاینت‌ها، به‌صورت رشته ارائه می‌شود. قالب این رشته مانند نحو query-param است. اطلاعات بیشتر درباره انتخابگرهای برچسب: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/</td>
    </tr>
  </tbody>
</table>
