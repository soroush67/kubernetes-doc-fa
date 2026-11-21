---
title: متریک‌های سفارشی کوبرنتیز (v1beta2)
content_type: tool-reference
package: custom.metrics.k8s.io/v1beta2
auto_generated: true
---
<p>بستهٔ v1beta2 نسخهٔ v1beta2 از API متریک‌های سفارشی (custom_metrics) است.</p>


## انواع منبع


- [MetricListOptions](#custom-metrics-k8s-io-v1beta2-MetricListOptions)
- [MetricValue](#custom-metrics-k8s-io-v1beta2-MetricValue)
- [MetricValueList](#custom-metrics-k8s-io-v1beta2-MetricValueList)
  

## `MetricListOptions`     {#custom-metrics-k8s-io-v1beta2-MetricListOptions}
    


<p>از نوع MetricListOptions برای انتخاب متریک‌ها بر اساس انتخابگرهای (selector) برچسب آن‌ها استفاده می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>custom.metrics.k8s.io/v1beta2</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>MetricListOptions</code></td></tr>
    
  
<tr><td><code>labelSelector</code><br/>
<code>string</code>
</td>
<td>
   <p>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌های آن‌ها. مقدار پیش‌فرض آن همه‌چیز را شامل می‌شود.</p>
</td>
</tr>
<tr><td><code>metricLabelSelector</code><br/>
<code>string</code>
</td>
<td>
   <p>انتخابگری برای محدود کردن فهرست متریک‌های بازگردانده‌شده بر اساس برچسب‌های آن‌ها.</p>
</td>
</tr>
</tbody>
</table>

## `MetricValue`     {#custom-metrics-k8s-io-v1beta2-MetricValue}
    

**در این موارد به کار رفته است:**

- [MetricValueList](#custom-metrics-k8s-io-v1beta2-MetricValueList)


<p>نوع MetricValue مقدار متریک برای یک آبجکت است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>custom.metrics.k8s.io/v1beta2</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>MetricValue</code></td></tr>
    
  
<tr><td><code>describedObject</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#objectreference-v1-core"><code>core/v1.ObjectReference</code></a>
</td>
<td>
   <p>ارجاعی به آبجکتی که توصیف می‌شود.</p>
</td>
</tr>
<tr><td><code>metric</code> <B>[الزامی]</B><br/>
<a href="#custom-metrics-k8s-io-v1beta2-MetricIdentifier"><code>MetricIdentifier</code></a>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>timestamp</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>زمانی را نشان می‌دهد که متریک‌ها در آن تولید شده‌اند.</p>
</td>
</tr>
<tr><td><code>windowSeconds</code> <B>[الزامی]</B><br/>
<code>int64</code>
</td>
<td>
   <p>هنگام بازگرداندن متریک‌های نرخی که از متریک‌های تجمعی محاسبه شده‌اند، بازهٔ زمانی ([Timestamp-Window, Timestamp]) را نشان می‌دهد که این متریک‌ها در آن محاسبه شده‌اند. برای متریک‌های لحظه‌ای که محاسبه نشده‌اند، مقدار آن صفر است.</p>
</td>
</tr>
<tr><td><code>value</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity"><code>k8s.io/apimachinery/pkg/api/resource.Quantity</code></a>
</td>
<td>
   <p>مقدار متریک برای این آبجکت.</p>
</td>
</tr>
</tbody>
</table>

## `MetricValueList`     {#custom-metrics-k8s-io-v1beta2-MetricValueList}
    


<p>نوع MetricValueList فهرستی از مقادیر یک متریک مشخص برای مجموعه‌ای از آبجکت‌ها است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>custom.metrics.k8s.io/v1beta2</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>MetricValueList</code></td></tr>
    
  
<tr><td><code>metadata</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#listmeta-v1-meta"><code>meta/v1.ListMeta</code></a>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>items</code> <B>[الزامی]</B><br/>
<a href="#custom-metrics-k8s-io-v1beta2-MetricValue"><code>[]MetricValue</code></a>
</td>
<td>
   <p>مقدار متریک در میان آبجکت‌های توصیف‌شده.</p>
</td>
</tr>
</tbody>
</table>

## `MetricIdentifier`     {#custom-metrics-k8s-io-v1beta2-MetricIdentifier}
    

**در این موارد به کار رفته است:**

- [MetricValue](#custom-metrics-k8s-io-v1beta2-MetricValue)


<p>نوع MetricIdentifier یک متریک را بر اساس نام و، به‌طور اختیاری، انتخابگر آن شناسایی می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>فیلد name نام متریک مورد نظر است.</p>
</td>
</tr>
<tr><td><code>selector</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#labelselector-v1-meta"><code>meta/v1.LabelSelector</code></a>
</td>
<td>
   <p>فیلد selector انتخابگر برچسبی را نشان می‌دهد که می‌توان از آن برای انتخاب این متریک استفاده کرد. این مقدار معمولاً همان انتخابگری است که به پرس‌وجوی دریافت این متریک داده شده است. اگر این فیلد خالی بماند، فقط از نام (Name) متریک برای گردآوری متریک‌ها استفاده می‌شود.</p>
</td>
</tr>
</tbody>
</table>
