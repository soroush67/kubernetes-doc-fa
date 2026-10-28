---
title: Kubernetes Custom Metrics (v1beta2)
content_type: tool-reference
package: custom.metrics.k8s.io/v1beta2
auto_generated: true
---
<p>بسته v1beta2 نسخه v1beta2 از API مربوط به custom_metrics است.</p>


## انواع منابع 


- [MetricListOptions](#custom-metrics-k8s-io-v1beta2-MetricListOptions)
- [MetricValue](#custom-metrics-k8s-io-v1beta2-MetricValue)
- [MetricValueList](#custom-metrics-k8s-io-v1beta2-MetricValueList)
  

## `MetricListOptions`     {#custom-metrics-k8s-io-v1beta2-MetricListOptions}
    


<p>MetricListOptions برای انتخاب متریک‌ها بر اساس انتخابگرهای برچسب آن‌ها استفاده می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>custom.metrics.k8s.io/v1beta2</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>MetricListOptions</code></td></tr>
    
  
<tr><td><code>labelSelector</code><br/>
<code>string</code>
</td>
<td>
   <p>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌های آن‌ها.
مقدار پیش‌فرض، همه‌چیز است.</p>
</td>
</tr>
<tr><td><code>metricLabelSelector</code><br/>
<code>string</code>
</td>
<td>
   <p>یک انتخابگر (selector) برای محدود کردن فهرست متریک‌های بازگردانده‌شده بر اساس برچسب‌های آن‌ها</p>
</td>
</tr>
</tbody>
</table>

## `MetricValue`     {#custom-metrics-k8s-io-v1beta2-MetricValue}
    

**ظاهر می‌شود در:**

- [MetricValueList](#custom-metrics-k8s-io-v1beta2-MetricValueList)


<p>MetricValue مقدار متریک برای یک آبجکت است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>custom.metrics.k8s.io/v1beta2</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>MetricValue</code></td></tr>
    
  
<tr><td><code>describedObject</code> <B>[Required]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#objectreference-v1-core"><code>core/v1.ObjectReference</code></a>
</td>
<td>
   <p>ارجاعی به آبجکت توصیف‌شده</p>
</td>
</tr>
<tr><td><code>metric</code> <B>[Required]</B><br/>
<a href="#custom-metrics-k8s-io-v1beta2-MetricIdentifier"><code>MetricIdentifier</code></a>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>timestamp</code> <B>[Required]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>زمانی را که متریک‌ها در آن تولید شده‌اند نشان می‌دهد.</p>
</td>
</tr>
<tr><td><code>windowSeconds</code> <B>[Required]</B><br/>
<code>int64</code>
</td>
<td>
   <p>پنجره زمانی ([Timestamp-Window, Timestamp]) را نشان می‌دهد که این متریک‌ها از آن محاسبه شده‌اند؛ این مقدار هنگام بازگرداندن متریک‌های نرخ (rate) که از متریک‌های تجمعی محاسبه شده‌اند تعیین می‌شود (و برای متریک‌های لحظه‌ای غیرمحاسبه‌شده صفر است).</p>
</td>
</tr>
<tr><td><code>value</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity"><code>k8s.io/apimachinery/pkg/api/resource.Quantity</code></a>
</td>
<td>
   <p>مقدار متریک برای این آبجکت</p>
</td>
</tr>
</tbody>
</table>

## `MetricValueList`     {#custom-metrics-k8s-io-v1beta2-MetricValueList}
    


<p>MetricValueList فهرستی از مقادیر یک متریک مشخص برای مجموعه‌ای از آبجکت‌هاست.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>custom.metrics.k8s.io/v1beta2</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>MetricValueList</code></td></tr>
    
  
<tr><td><code>metadata</code> <B>[Required]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#listmeta-v1-meta"><code>meta/v1.ListMeta</code></a>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>items</code> <B>[Required]</B><br/>
<a href="#custom-metrics-k8s-io-v1beta2-MetricValue"><code>[]MetricValue</code></a>
</td>
<td>
   <p>مقدار متریک در میان آبجکت‌های توصیف‌شده</p>
</td>
</tr>
</tbody>
</table>

## `MetricIdentifier`     {#custom-metrics-k8s-io-v1beta2-MetricIdentifier}
    

**ظاهر می‌شود در:**

- [MetricValue](#custom-metrics-k8s-io-v1beta2-MetricValue)


<p>MetricIdentifier یک متریک را با نام و در صورت نیاز با انتخابگر (selector) شناسایی می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>name نام متریک مورد نظر است.</p>
</td>
</tr>
<tr><td><code>selector</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#labelselector-v1-meta"><code>meta/v1.LabelSelector</code></a>
</td>
<td>
   <p>selector نشان‌دهنده انتخابگر برچسبی است که می‌توان از آن برای انتخاب این متریک استفاده کرد و معمولاً همان انتخابگری است که در پرس‌وجوی مورد استفاده برای دریافت این متریک ارسال شده است.
اگر این فیلد خالی بماند، برای جمع‌آوری متریک‌ها فقط نام (Name) متریک استفاده می‌شود.</p>
</td>
</tr>
</tbody>
</table>
