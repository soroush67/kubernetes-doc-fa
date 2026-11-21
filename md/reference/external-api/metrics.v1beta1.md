---
title: معیارهای کوبرنتیز (v1beta1)
content_type: tool-reference
package: metrics.k8s.io/v1beta1
auto_generated: true
---
<p>بستهٔ v1beta1 نسخهٔ v1beta1 از API معیارها (metrics) است.</p>


## انواع منبع 


- [NodeMetrics](#metrics-k8s-io-v1beta1-NodeMetrics)
- [NodeMetricsList](#metrics-k8s-io-v1beta1-NodeMetricsList)
- [PodMetrics](#metrics-k8s-io-v1beta1-PodMetrics)
- [PodMetricsList](#metrics-k8s-io-v1beta1-PodMetricsList)
  

## `NodeMetrics`     {#metrics-k8s-io-v1beta1-NodeMetrics}
    

**در این موارد آمده است:**

- [NodeMetricsList](#metrics-k8s-io-v1beta1-NodeMetricsList)


<p>نوع NodeMetrics معیارهای مصرف منابع یک نود را مشخص می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>metrics.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>NodeMetrics</code></td></tr>
    
  
<tr><td><code>metadata</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#objectmeta-v1-meta"><code>meta/v1.ObjectMeta</code></a>
</td>
<td>
   <p>فراداده‌های استاندارد آبجکت.
اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</p>
برای آشنایی با فیلدهای فیلد <code>metadata</code> به مستندات API کوبرنتیز مراجعه کنید.</td>
</tr>
<tr><td><code>timestamp</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>فیلدهای زیر بازهٔ زمانی گردآوری معیارها را مشخص می‌کنند؛ این بازه
[Timestamp-Window, Timestamp] است.</p>
</td>
</tr>
<tr><td><code>window</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>usage</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#resourcelist-v1-core"><code>core/v1.ResourceList</code></a>
</td>
<td>
   <p>مقدار مصرف حافظه همان مجموعهٔ کاری حافظه (memory working set) است.</p>
</td>
</tr>
</tbody>
</table>

## `NodeMetricsList`     {#metrics-k8s-io-v1beta1-NodeMetricsList}
    


<p>نوع NodeMetricsList فهرستی از NodeMetrics است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>metrics.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>NodeMetricsList</code></td></tr>
    
  
<tr><td><code>metadata</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#listmeta-v1-meta"><code>meta/v1.ListMeta</code></a>
</td>
<td>
   <p>فراداده‌های استاندارد فهرست.
اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</p>
</td>
</tr>
<tr><td><code>items</code> <B>[الزامی]</B><br/>
<a href="#metrics-k8s-io-v1beta1-NodeMetrics"><code>[]NodeMetrics</code></a>
</td>
<td>
   <p>فهرست معیارهای نودها.</p>
</td>
</tr>
</tbody>
</table>

## `PodMetrics`     {#metrics-k8s-io-v1beta1-PodMetrics}
    

**در این موارد آمده است:**

- [PodMetricsList](#metrics-k8s-io-v1beta1-PodMetricsList)


<p>نوع PodMetrics معیارهای مصرف منابع یک پاد را مشخص می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>metrics.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>PodMetrics</code></td></tr>
    
  
<tr><td><code>metadata</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#objectmeta-v1-meta"><code>meta/v1.ObjectMeta</code></a>
</td>
<td>
   <p>فراداده‌های استاندارد آبجکت.
اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</p>
برای آشنایی با فیلدهای فیلد <code>metadata</code> به مستندات API کوبرنتیز مراجعه کنید.</td>
</tr>
<tr><td><code>timestamp</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>فیلدهای زیر بازهٔ زمانی گردآوری معیارها را مشخص می‌کنند؛ این بازه
[Timestamp-Window, Timestamp] است.</p>
</td>
</tr>
<tr><td><code>window</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>containers</code> <B>[الزامی]</B><br/>
<a href="#metrics-k8s-io-v1beta1-ContainerMetrics"><code>[]ContainerMetrics</code></a>
</td>
<td>
   <p>معیارهای همهٔ کانتینرها در یک بازهٔ زمانی یکسان گردآوری می‌شوند.</p>
</td>
</tr>
</tbody>
</table>

## `PodMetricsList`     {#metrics-k8s-io-v1beta1-PodMetricsList}
    


<p>نوع PodMetricsList فهرستی از PodMetrics است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>metrics.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>PodMetricsList</code></td></tr>
    
  
<tr><td><code>metadata</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#listmeta-v1-meta"><code>meta/v1.ListMeta</code></a>
</td>
<td>
   <p>فراداده‌های استاندارد فهرست.
اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</p>
</td>
</tr>
<tr><td><code>items</code> <B>[الزامی]</B><br/>
<a href="#metrics-k8s-io-v1beta1-PodMetrics"><code>[]PodMetrics</code></a>
</td>
<td>
   <p>فهرست معیارهای پادها.</p>
</td>
</tr>
</tbody>
</table>

## `ContainerMetrics`     {#metrics-k8s-io-v1beta1-ContainerMetrics}
    

**در این موارد آمده است:**

- [PodMetrics](#metrics-k8s-io-v1beta1-PodMetrics)


<p>نوع ContainerMetrics معیارهای مصرف منابع یک کانتینر را مشخص می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>نام کانتینر، مطابق با نام آن در pod.spec.containers.</p>
</td>
</tr>
<tr><td><code>usage</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#resourcelist-v1-core"><code>core/v1.ResourceList</code></a>
</td>
<td>
   <p>مقدار مصرف حافظه همان مجموعهٔ کاری حافظه است.</p>
</td>
</tr>
</tbody>
</table>
