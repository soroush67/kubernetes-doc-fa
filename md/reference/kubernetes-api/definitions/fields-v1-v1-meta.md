---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "FieldsV1"
content_type: "api_reference"
description: "FieldsV1 مجموعه‌ای از فیلدها را در قالب JSON و در یک ساختار داده شبیه Trie ذخیره می‌کند.\n\nهر کلید یا برابر با «.» است که خودِ فیلد را نشان می‌دهد و همیشه به یک مجموعه تهی نگاشت می‌شود، یا رشته‌ای است که یک زیرفیلد یا یک آیتم را نمایش می‌دهد. این رشته از یکی از چهار قالب زیر پیروی می‌کند: «f:&lt;name&gt;» که در آن &lt;name&gt; نام یک فیلد در یک struct یا کلید یک map است؛ «v:&lt;value&gt;» که در آن &lt;value&gt; مقدار دقیقاً قالب‌بندی‌شده با JSON برای یک آیتم لیست است؛ «i:&lt;index&gt;» که در آن &lt;index&gt; جایگاه یک آیتم در لیست است؛ «k:&lt;keys&gt;» که در آن &lt;keys&gt; نگاشتی از فیلدهای کلید یک آیتم لیست به مقادیر یکتای آن‌هاست. اگر یک کلید به مقدار تهی Fields نگاشت شود، فیلدی که آن کلید نمایندگی می‌کند عضوی از این مجموعه است.\n\nقالب دقیق در sigs.k8s.io/structured-merge-diff تعریف شده است"
title: "FieldsV1"
weight: 130
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


## FieldsV1 {#FieldsV1}

FieldsV1 مجموعه‌ای از فیلدها را در قالب JSON و در یک ساختار داده شبیه Trie ذخیره می‌کند.

هر کلید یا برابر با «.» است که خودِ فیلد را نشان می‌دهد و همیشه به یک مجموعه تهی نگاشت می‌شود، یا رشته‌ای است که یک زیرفیلد یا یک آیتم را نمایش می‌دهد. این رشته از یکی از چهار قالب زیر پیروی می‌کند: «f:&lt;name&gt;» که در آن &lt;name&gt; نام یک فیلد در یک struct یا کلید یک map است؛ «v:&lt;value&gt;» که در آن &lt;value&gt; مقدار دقیقاً قالب‌بندی‌شده با JSON برای یک آیتم لیست است؛ «i:&lt;index&gt;» که در آن &lt;index&gt; جایگاه یک آیتم در لیست است؛ «k:&lt;keys&gt;» که در آن &lt;keys&gt; نگاشتی از فیلدهای کلید یک آیتم لیست به مقادیر یکتای آن‌هاست. اگر یک کلید به مقدار تهی Fields نگاشت شود، فیلدی که آن کلید نمایندگی می‌کند عضوی از این مجموعه است.

قالب دقیق در sigs.k8s.io/structured-merge-diff تعریف شده است

<hr>
