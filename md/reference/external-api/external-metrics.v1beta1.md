---
title: Kubernetes External Metrics (v1beta1)
content_type: tool-reference
package: external.metrics.k8s.io/v1beta1
auto_generated: true
---
<p>بسته v1beta1 نسخه v1beta1 از API متریک‌های خارجی (external metrics) است.</p>


## انواع منابع 


- [ExternalMetricValue](#external-metrics-k8s-io-v1beta1-ExternalMetricValue)
- [ExternalMetricValueList](#external-metrics-k8s-io-v1beta1-ExternalMetricValueList)
  

## `ExternalMetricValue`     {#external-metrics-k8s-io-v1beta1-ExternalMetricValue}
    

**در این موارد ظاهر می‌شود:**

- [ExternalMetricValueList](#external-metrics-k8s-io-v1beta1-ExternalMetricValueList)


<p>ExternalMetricValue مقدار یک متریک برای یک متریک خارجی است.
هر مقدار متریک با نام متریک و مجموعه‌ای از برچسب‌های رشته‌ای شناسایی می‌شود.
برای یک متریک می‌تواند چندین مقدار با مجموعه‌های متفاوتی از برچسب‌ها وجود داشته باشد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>external.metrics.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>ExternalMetricValue</code></td></tr>
    
  
<tr><td><code>metricName</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>نام متریک</p>
</td>
</tr>
<tr><td><code>metricLabels</code> <B>[Required]</B><br/>
<code>map[string]string</code>
</td>
<td>
   <p>مجموعه‌ای از برچسب‌ها که یک سری زمانی واحد را برای متریک مشخص می‌کنند</p>
</td>
</tr>
<tr><td><code>timestamp</code> <B>[Required]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>زمانی را نشان می‌دهد که متریک‌ها در آن تولید شده‌اند</p>
</td>
</tr>
<tr><td><code>window</code> <B>[Required]</B><br/>
<code>int64</code>
</td>
<td>
   <p>بازه زمانی ([Timestamp-Window, Timestamp]) را نشان می‌دهد که
این متریک‌ها در آن محاسبه شده‌اند؛ این مقدار هنگام بازگرداندن متریک‌های نرخ
که از متریک‌های تجمعی محاسبه شده‌اند تعیین می‌شود (و برای
متریک‌های لحظه‌ای غیرمحاسبه‌شده صفر است).</p>
</td>
</tr>
<tr><td><code>value</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity"><code>k8s.io/apimachinery/pkg/api/resource.Quantity</code></a>
</td>
<td>
   <p>مقدار متریک</p>
</td>
</tr>
</tbody>
</table>

## `ExternalMetricValueList`     {#external-metrics-k8s-io-v1beta1-ExternalMetricValueList}
    


<p>ExternalMetricValueList فهرستی از مقادیر یک متریک مشخص برای مجموعه‌ای از برچسب‌هاست.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>external.metrics.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>ExternalMetricValueList</code></td></tr>
    
  
<tr><td><code>metadata</code> <B>[Required]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#listmeta-v1-meta"><code>meta/v1.ListMeta</code></a>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>items</code> <B>[Required]</B><br/>
<a href="#external-metrics-k8s-io-v1beta1-ExternalMetricValue"><code>[]ExternalMetricValue</code></a>
</td>
<td>
   <p>مقدار متریک مطابق با یک مجموعه مشخص از برچسب‌ها</p>
</td>
</tr>
</tbody>
</table>
