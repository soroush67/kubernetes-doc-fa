---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "ObjectReference"
content_type: "api_reference"
description: "ObjectReference اطلاعات کافی را در اختیار شما قرار می‌دهد تا بتوانید آبجکت ارجاع‌شده را بررسی یا ویرایش کنید."
title: "ObjectReference"
weight: 320
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

`apiVersion: v1`

`import "k8s.io/api/core/v1"`


## ObjectReference {#ObjectReference}

ObjectReference اطلاعات کافی را در اختیار شما قرار می‌دهد تا بتوانید آبجکت ارجاع‌شده را بررسی یا ویرایش کنید.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>نسخه API آبجکت ارجاع‌شده (referent).</td>
    </tr>
    <tr>
      <td><code>fieldPath</code><br/><em>string</em></td>
      <td>اگر ارجاع به بخشی از یک آبجکت باشد و نه کل آبجکت، این رشته باید شامل یک عبارت معتبر دسترسی به فیلد در قالب JSON/Go باشد، مانند desiredState.manifest.containers[2]. برای مثال، اگر ارجاع آبجکت به یک کانتینر درون یک pod باشد، مقدار آن به شکل "spec.containers{name}" خواهد بود (که در آن "name" نام کانتینری است که رویداد را ایجاد کرده است)، و اگر نام کانتینر مشخص نشده باشد، به شکل "spec.containers[2]" خواهد بود (کانتینر با اندیس ۲ در این pod). این قالب صرفاً برای داشتن روشی کاملاً تعریف‌شده جهت ارجاع به بخشی از یک آبجکت انتخاب شده است.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>نوع (kind) آبجکت ارجاع‌شده. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>نام آبجکت ارجاع‌شده. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</td>
    </tr>
    <tr>
      <td><code>namespace</code><br/><em>string</em></td>
      <td>فضای نام (namespace) آبجکت ارجاع‌شده. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code><br/><em>string</em></td>
      <td>resourceVersion مشخصی که این ارجاع به آن اشاره دارد، در صورت وجود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency</td>
    </tr>
    <tr>
      <td><code>uid</code><br/><em>string</em></td>
      <td>UID آبجکت ارجاع‌شده. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids</td>
    </tr>
  </tbody>
</table>
