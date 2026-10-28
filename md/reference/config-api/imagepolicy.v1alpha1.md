---
title: API سیاست ایمیج (v1alpha1)
content_type: tool-reference
package: imagepolicy.k8s.io/v1alpha1
auto_generated: true
---


## انواع منابع {#resource-types}


- [ImageReview](#imagepolicy-k8s-io-v1alpha1-ImageReview)
  

## `ImageReview`     {#imagepolicy-k8s-io-v1alpha1-ImageReview}
    


<p>ImageReview بررسی می‌کند که آیا مجموعه ایمیج‌های موجود در یک Pod مجاز هستند یا خیر.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>imagepolicy.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>ImageReview</code></td></tr>
    
  
<tr><td><code>metadata</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#objectmeta-v1-meta"><code>meta/v1.ObjectMeta</code></a>
</td>
<td>
   <p>metadata فراداده استاندارد آبجکت است.
اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</p>
برای مشاهده فیلدهای <code>metadata</code> به مستندات API کوبرنتیز مراجعه کنید.</td>
</tr>
<tr><td><code>spec</code><br/>
<a href="#imagepolicy-k8s-io-v1alpha1-ImageReviewSpec"><code>ImageReviewSpec</code></a>
</td>
<td>
   <p>spec شامل اطلاعاتی درباره Podی است که در حال ارزیابی است.</p>
</td>
</tr>
<tr><td><code>status</code><br/>
<a href="#imagepolicy-k8s-io-v1alpha1-ImageReviewStatus"><code>ImageReviewStatus</code></a>
</td>
<td>
   <p>status توسط بک‌اند تکمیل می‌شود و نشان می‌دهد که آیا Pod باید مجاز شناخته شود یا خیر.</p>
</td>
</tr>
</tbody>
</table>

## `ImageReviewContainerSpec`     {#imagepolicy-k8s-io-v1alpha1-ImageReviewContainerSpec}
    

**Appears in:**

- [ImageReviewSpec](#imagepolicy-k8s-io-v1alpha1-ImageReviewSpec)


<p>ImageReviewContainerSpec توصیف یک کانتینر در درخواست ایجاد Pod است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>image</code><br/>
<code>string</code>
</td>
<td>
   <p>image می‌تواند به شکل image:tag یا image@SHA:012345679abcdef باشد.</p>
</td>
</tr>
</tbody>
</table>

## `ImageReviewSpec`     {#imagepolicy-k8s-io-v1alpha1-ImageReviewSpec}
    

**Appears in:**

- [ImageReview](#imagepolicy-k8s-io-v1alpha1-ImageReview)


<p>ImageReviewSpec توصیف درخواست ایجاد Pod است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>containers</code><br/>
<a href="#imagepolicy-k8s-io-v1alpha1-ImageReviewContainerSpec"><code>[]ImageReviewContainerSpec</code></a>
</td>
<td>
   <p>containers فهرستی از زیرمجموعه‌ای از اطلاعات هر کانتینر در Podی است که در حال ایجاد می‌باشد.</p>
</td>
</tr>
<tr><td><code>annotations</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>annotations فهرستی از جفت‌های کلید-مقدار است که از حاشیه‌نویسی‌های (annotations) Pod استخراج شده‌اند.
این فهرست فقط شامل کلیدهایی است که با الگوی <code>*.image-policy.k8s.io/*</code> مطابقت دارند.
تصمیم‌گیری درباره نحوه تفسیر این annotationها، در صورت لزوم، بر عهده هر بک‌اند webhook است.</p>
</td>
</tr>
<tr><td><code>namespace</code><br/>
<code>string</code>
</td>
<td>
   <p>namespace فضای نامی (namespace) است که Pod در آن ایجاد می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `ImageReviewStatus`     {#imagepolicy-k8s-io-v1alpha1-ImageReviewStatus}
    

**Appears in:**

- [ImageReview](#imagepolicy-k8s-io-v1alpha1-ImageReview)


<p>ImageReviewStatus نتیجه بررسی درخواست ایجاد Pod است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>allowed</code><br/>
<code>bool</code>
</td>
<td>
   <p>allowed نشان می‌دهد که اجرای همه ایمیج‌ها مجاز شمرده شده است.</p>
</td>
</tr>
<tr><td><code>reason</code><br/>
<code>string</code>
</td>
<td>
   <p>reason باید خالی باشد، مگر زمانی که Allowed مقدار false داشته باشد؛ در این صورت
ممکن است شامل توضیح کوتاهی درباره مشکل باشد. کوبرنتیز
ممکن است خطاهای بسیار طولانی را هنگام نمایش به کاربر کوتاه کند.</p>
</td>
</tr>
<tr><td><code>auditAnnotations</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>auditAnnotations با استفاده از 'AddAnnotation' به آبجکت attributes
درخواست admission controller افزوده می‌شود. کلیدها باید
بدون پیشوند باشند (یعنی admission controller
پیشوند مناسب را خودش اضافه می‌کند).</p>
</td>
</tr>
</tbody>
</table>
