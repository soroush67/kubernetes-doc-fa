---
title: API خلاصه Kubelet (v1alpha1)
content_type: tool-reference
package: v1alpha1
auto_generated: true
---


## انواع منبع 


- [Summary](#Summary)
  
    
    

## `AcceleratorStats`     {#AcceleratorStats}
    

**در این موارد ظاهر می‌شود:**

- [ContainerStats](#ContainerStats)


<p>نوع AcceleratorStats آمار شتاب‌دهنده‌های متصل به کانتینر را در بر دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>make</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>سازندهٔ شتاب‌دهنده (nvidia، amd، google و غیره).</p>
</td>
</tr>
<tr><td><code>model</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>مدل شتاب‌دهنده (tesla-p100، tesla-k80 و غیره).</p>
</td>
</tr>
<tr><td><code>id</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>شناسهٔ شتاب‌دهنده.</p>
</td>
</tr>
<tr><td><code>memoryTotal</code> <B>[الزامی]</B><br/>
<code>uint64</code>
</td>
<td>
   <p>کل حافظهٔ شتاب‌دهنده.
واحد: بایت</p>
</td>
</tr>
<tr><td><code>memoryUsed</code> <B>[الزامی]</B><br/>
<code>uint64</code>
</td>
<td>
   <p>کل حافظهٔ تخصیص‌یافتهٔ شتاب‌دهنده.
واحد: بایت</p>
</td>
</tr>
<tr><td><code>dutyCycle</code> <B>[الزامی]</B><br/>
<code>uint64</code>
</td>
<td>
   <p>درصدی از زمان دورهٔ نمونه‌برداری اخیر (۱۰ ثانیه) که شتاب‌دهنده در آن
به‌طور فعال مشغول پردازش بوده است.</p>
</td>
</tr>
</tbody>
</table>

## `CPUStats`     {#CPUStats}
    

**در این موارد ظاهر می‌شود:**

- [ContainerStats](#ContainerStats)

- [NodeStats](#NodeStats)

- [PodStats](#PodStats)


<p>نوع CPUStats داده‌های مربوط به مصرف CPU را در بر دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>time</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>زمانی که این آمار به‌روزرسانی شده است.</p>
</td>
</tr>
<tr><td><code>usageNanoCores</code><br/>
<code>uint64</code>
</td>
<td>
   <p>کل مصرف CPU (مجموع همهٔ هسته‌ها) که در طول پنجرهٔ نمونه‌برداری میانگین‌گیری شده است.
واحد «core» را می‌توان به‌صورت نانوثانیه‌-هستهٔ CPU در هر ثانیه تفسیر کرد.</p>
</td>
</tr>
<tr><td><code>usageCoreNanoSeconds</code><br/>
<code>uint64</code>
</td>
<td>
   <p>مصرف تجمعی CPU (مجموع همهٔ هسته‌ها) از زمان ایجاد آبجکت.</p>
</td>
</tr>
<tr><td><code>psi</code><br/>
<a href="#PSIStats"><code>PSIStats</code></a>
</td>
<td>
   <p>آمار PSI مربوط به CPU.</p>
</td>
</tr>
</tbody>
</table>

## `ContainerStats`     {#ContainerStats}
    

**در این موارد ظاهر می‌شود:**

- [NodeStats](#NodeStats)

- [PodStats](#PodStats)


<p>نوع ContainerStats آمار نمونه‌برداری‌شده و پردازش‌نشده در سطح کانتینر را نگه می‌دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>ارجاع به کانتینر اندازه‌گیری‌شده.</p>
</td>
</tr>
<tr><td><code>startTime</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>زمانی که جمع‌آوری داده برای این کانتینر آغاز (یا از نو آغاز) شده است.</p>
</td>
</tr>
<tr><td><code>cpu</code><br/>
<a href="#CPUStats"><code>CPUStats</code></a>
</td>
<td>
   <p>آمار مربوط به منابع CPU.</p>
</td>
</tr>
<tr><td><code>memory</code><br/>
<a href="#MemoryStats"><code>MemoryStats</code></a>
</td>
<td>
   <p>آمار مربوط به منابع حافظه (RAM).</p>
</td>
</tr>
<tr><td><code>io</code><br/>
<a href="#IOStats"><code>IOStats</code></a>
</td>
<td>
   <p>آمار مربوط به منابع ورودی/خروجی (IO).</p>
</td>
</tr>
<tr><td><code>accelerators</code> <B>[الزامی]</B><br/>
<a href="#AcceleratorStats"><code>[]AcceleratorStats</code></a>
</td>
<td>
   <p>متریک‌های شتاب‌دهنده‌ها. هر شتاب‌دهنده با یک عنصر از این آرایه متناظر است.</p>
</td>
</tr>
<tr><td><code>rootfs</code><br/>
<a href="#FsStats"><code>FsStats</code></a>
</td>
<td>
   <p>آمار مربوط به میزان استفادهٔ rootfs کانتینر از منابع فایل‌سیستم.
مقدار Rootfs.UsedBytes تعداد بایت‌هایی است که برای لایهٔ نوشتنی کانتینر استفاده شده است.</p>
</td>
</tr>
<tr><td><code>logs</code><br/>
<a href="#FsStats"><code>FsStats</code></a>
</td>
<td>
   <p>آمار مربوط به میزان استفادهٔ لاگ‌های کانتینر از منابع فایل‌سیستم.
مقدار Logs.UsedBytes تعداد بایت‌هایی است که برای لاگ‌های کانتینر استفاده شده است.</p>
</td>
</tr>
<tr><td><code>userDefinedMetrics</code> <B>[الزامی]</B><br/>
<a href="#UserDefinedMetric"><code>[]UserDefinedMetric</code></a>
</td>
<td>
   <p>متریک‌های کاربرتعریف که کانتینرهای درون پاد ارائه می‌کنند. معمولاً انتظار می‌رود فقط یک کانتینر در پاد متریک‌های کاربرتعریف را ارائه کند. اگر چند کانتینر متریک ارائه کنند، متریک‌های آن‌ها در اینجا با هم ترکیب می‌شوند.</p>
</td>
</tr>
<tr><td><code>swap</code><br/>
<a href="#SwapStats"><code>SwapStats</code></a>
</td>
<td>
   <p>آمار مربوط به منابع swap. این آمار فقط برای سیستم‌های غیرویندوزی گزارش می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `FsStats`     {#FsStats}
    

**در این موارد ظاهر می‌شود:**

- [ContainerStats](#ContainerStats)

- [NodeStats](#NodeStats)

- [PodStats](#PodStats)

- [RuntimeStats](#RuntimeStats)

- [VolumeStats](#VolumeStats)


<p>نوع FsStats داده‌های مربوط به مصرف فایل‌سیستم را در بر دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>time</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>زمانی که این آمار به‌روزرسانی شده است.</p>
</td>
</tr>
<tr><td><code>availableBytes</code><br/>
<code>uint64</code>
</td>
<td>
   <p>فیلد AvailableBytes فضای ذخیره‌سازی در دسترس فایل‌سیستم را (بر حسب بایت) نشان می‌دهد.</p>
</td>
</tr>
<tr><td><code>capacityBytes</code><br/>
<code>uint64</code>
</td>
<td>
   <p>فیلد CapacityBytes ظرفیت کل فضای ذخیره‌سازی زیربنایی فایل‌سیستم را (بر حسب بایت) نشان می‌دهد.</p>
</td>
</tr>
<tr><td><code>usedBytes</code><br/>
<code>uint64</code>
</td>
<td>
   <p>فیلد UsedBytes بایت‌هایی را نشان می‌دهد که برای یک کار مشخص روی فایل‌سیستم استفاده شده‌اند.
این مقدار ممکن است با کل بایت‌های استفاده‌شده روی فایل‌سیستم متفاوت باشد و لزوماً با CapacityBytes - AvailableBytes برابر نیست.
برای مثال، در ContainerStats.Rootfs این مقدار برابر با بایت‌هایی است که rootfs کانتینر روی فایل‌سیستم استفاده کرده است.</p>
</td>
</tr>
<tr><td><code>inodesFree</code><br/>
<code>uint64</code>
</td>
<td>
   <p>فیلد InodesFree تعداد inodeهای آزاد فایل‌سیستم را نشان می‌دهد.</p>
</td>
</tr>
<tr><td><code>inodes</code><br/>
<code>uint64</code>
</td>
<td>
   <p>فیلد Inodes تعداد کل inodeهای فایل‌سیستم را نشان می‌دهد.</p>
</td>
</tr>
<tr><td><code>inodesUsed</code> <B>[الزامی]</B><br/>
<code>uint64</code>
</td>
<td>
   <p>فیلد InodesUsed تعداد inodeهایی را نشان می‌دهد که فایل‌سیستم استفاده کرده است.
این مقدار ممکن است با Inodes - InodesFree برابر نباشد، زیرا این فایل‌سیستم ممکن است inodeها را با «فایل‌سیستم‌های» دیگر به اشتراک بگذارد.
برای مثال، در ContainerStats.Rootfs این مقدار فقط شامل inodeهایی است که همان کانتینر استفاده کرده است و inodeهای مصرف‌شدهٔ کانتینرهای دیگر را در بر نمی‌گیرد.</p>
</td>
</tr>
</tbody>
</table>

## `IOStats`     {#IOStats}
    

**در این موارد ظاهر می‌شود:**

- [ContainerStats](#ContainerStats)

- [NodeStats](#NodeStats)

- [PodStats](#PodStats)


<p>نوع IOStats داده‌های مربوط به مصرف ورودی/خروجی را در بر دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>time</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>زمانی که این آمار به‌روزرسانی شده است.</p>
</td>
</tr>
<tr><td><code>psi</code><br/>
<a href="#PSIStats"><code>PSIStats</code></a>
</td>
<td>
   <p>آمار PSI مربوط به ورودی/خروجی.</p>
</td>
</tr>
</tbody>
</table>

## `InterfaceStats`     {#InterfaceStats}
    

**در این موارد ظاهر می‌شود:**

- [NetworkStats](#NetworkStats)


<p>نوع InterfaceStats داده‌های مقادیر منابع مربوط به رابط شبکه را در بر دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>نام رابط شبکه</p>
</td>
</tr>
<tr><td><code>rxBytes</code><br/>
<code>uint64</code>
</td>
<td>
   <p>تعداد تجمعی بایت‌های دریافت‌شده.</p>
</td>
</tr>
<tr><td><code>rxErrors</code><br/>
<code>uint64</code>
</td>
<td>
   <p>تعداد تجمعی خطاهای رخ‌داده هنگام دریافت.</p>
</td>
</tr>
<tr><td><code>txBytes</code><br/>
<code>uint64</code>
</td>
<td>
   <p>تعداد تجمعی بایت‌های ارسال‌شده.</p>
</td>
</tr>
<tr><td><code>txErrors</code><br/>
<code>uint64</code>
</td>
<td>
   <p>تعداد تجمعی خطاهای رخ‌داده هنگام ارسال.</p>
</td>
</tr>
</tbody>
</table>

## `MemoryStats`     {#MemoryStats}
    

**در این موارد ظاهر می‌شود:**

- [ContainerStats](#ContainerStats)

- [NodeStats](#NodeStats)

- [PodStats](#PodStats)


<p>نوع MemoryStats داده‌های مربوط به مصرف حافظه را در بر دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>time</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>زمانی که این آمار به‌روزرسانی شده است.</p>
</td>
</tr>
<tr><td><code>availableBytes</code><br/>
<code>uint64</code>
</td>
<td>
   <p>حافظهٔ در دسترس برای استفاده. این مقدار به‌صورت محدودیت حافظه منهای workingSetBytes تعریف می‌شود.
اگر محدودیت حافظه تعریف نشده باشد، مقدار بایت‌های در دسترس حذف می‌شود.</p>
</td>
</tr>
<tr><td><code>usageBytes</code><br/>
<code>uint64</code>
</td>
<td>
   <p>کل حافظهٔ در حال استفاده. این مقدار همهٔ حافظه را، صرف‌نظر از زمان دسترسی به آن، در بر می‌گیرد.</p>
</td>
</tr>
<tr><td><code>workingSetBytes</code><br/>
<code>uint64</code>
</td>
<td>
   <p>مقدار حافظهٔ working set. این مقدار شامل حافظه‌ای است که اخیراً به آن دسترسی شده،
حافظهٔ dirty و حافظهٔ کرنل. همواره رابطهٔ WorkingSetBytes &lt;= UsageBytes برقرار است.</p>
</td>
</tr>
<tr><td><code>rssBytes</code><br/>
<code>uint64</code>
</td>
<td>
   <p>مقدار حافظهٔ ناشناس (anonymous) و حافظهٔ کش swap (شامل transparent
hugepages).</p>
</td>
</tr>
<tr><td><code>pageFaults</code><br/>
<code>uint64</code>
</td>
<td>
   <p>تعداد تجمعی خطاهای صفحهٔ جزئی (minor page fault).</p>
</td>
</tr>
<tr><td><code>majorPageFaults</code><br/>
<code>uint64</code>
</td>
<td>
   <p>تعداد تجمعی خطاهای صفحهٔ اصلی (major page fault).</p>
</td>
</tr>
<tr><td><code>psi</code><br/>
<a href="#PSIStats"><code>PSIStats</code></a>
</td>
<td>
   <p>آمار PSI مربوط به حافظه.</p>
</td>
</tr>
</tbody>
</table>

## `NetworkStats`     {#NetworkStats}
    

**در این موارد ظاهر می‌شود:**

- [NodeStats](#NodeStats)

- [PodStats](#PodStats)


<p>نوع NetworkStats داده‌های مربوط به منابع شبکه را در بر دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>time</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>زمانی که این آمار به‌روزرسانی شده است.</p>
</td>
</tr>
<tr><td><code>InterfaceStats</code> <B>[الزامی]</B><br/>
<a href="#InterfaceStats"><code>InterfaceStats</code></a>
</td>
<td>
   <p>آمار رابط شبکهٔ پیش‌فرض، در صورتی که یافت شود</p>
</td>
</tr>
<tr><td><code>interfaces</code> <B>[الزامی]</B><br/>
<a href="#InterfaceStats"><code>[]InterfaceStats</code></a>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `NodeStats`     {#NodeStats}
    

**در این موارد ظاهر می‌شود:**

- [Summary](#Summary)


<p>نوع NodeStats آمار نمونه‌برداری‌شده و پردازش‌نشده در سطح نود را نگه می‌دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>nodeName</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>ارجاع به نود اندازه‌گیری‌شده.</p>
</td>
</tr>
<tr><td><code>systemContainers</code><br/>
<a href="#ContainerStats"><code>[]ContainerStats</code></a>
</td>
<td>
   <p>آمار دیمن‌های سیستمی که به‌صورت کانتینرهای خام ردیابی می‌شوند.
نام کانتینرهای سیستمی بر اساس ثابت‌های SystemContainer* تعیین می‌شود.</p>
</td>
</tr>
<tr><td><code>startTime</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>زمانی که جمع‌آوری داده برای آمار در سطح نود (یعنی آمار تجمیعی) آغاز (یا از نو آغاز) شده است.</p>
</td>
</tr>
<tr><td><code>cpu</code><br/>
<a href="#CPUStats"><code>CPUStats</code></a>
</td>
<td>
   <p>آمار مربوط به منابع CPU.</p>
</td>
</tr>
<tr><td><code>memory</code><br/>
<a href="#MemoryStats"><code>MemoryStats</code></a>
</td>
<td>
   <p>آمار مربوط به منابع حافظه (RAM).</p>
</td>
</tr>
<tr><td><code>io</code><br/>
<a href="#IOStats"><code>IOStats</code></a>
</td>
<td>
   <p>آمار مربوط به منابع ورودی/خروجی.</p>
</td>
</tr>
<tr><td><code>network</code><br/>
<a href="#NetworkStats"><code>NetworkStats</code></a>
</td>
<td>
   <p>آمار مربوط به منابع شبکه.</p>
</td>
</tr>
<tr><td><code>fs</code><br/>
<a href="#FsStats"><code>FsStats</code></a>
</td>
<td>
   <p>آمار مربوط به مصرف کل منابع فایل‌سیستم روی rootfs که اجزای k8s نود از آن استفاده می‌کنند.
مقدار NodeFs.Used کل بایت‌های استفاده‌شده روی فایل‌سیستم است.</p>
</td>
</tr>
<tr><td><code>runtime</code><br/>
<a href="#RuntimeStats"><code>RuntimeStats</code></a>
</td>
<td>
   <p>آمار مربوط به محیط اجرای کانتینر زیربنایی.</p>
</td>
</tr>
<tr><td><code>rlimit</code><br/>
<a href="#RlimitStats"><code>RlimitStats</code></a>
</td>
<td>
   <p>آمار مربوط به rlimit سیستم.</p>
</td>
</tr>
<tr><td><code>swap</code><br/>
<a href="#SwapStats"><code>SwapStats</code></a>
</td>
<td>
   <p>آمار مربوط به منابع swap. این آمار فقط برای سیستم‌های غیرویندوزی گزارش می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `PSIData`     {#PSIData}
    

**در این موارد ظاهر می‌شود:**

- [PSIStats](#PSIStats)


<p>داده‌های PSI برای یک منبع مجزا.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>total</code> <B>[الزامی]</B><br/>
<code>uint64</code>
</td>
<td>
   <p>کل مدت زمانی که وظایف (task) موجود در cgroup به‌دلیل ازدحام منتظر مانده‌اند.
واحد: نانوثانیه.</p>
</td>
</tr>
<tr><td><code>avg10</code> <B>[الزامی]</B><br/>
<code>float64</code>
</td>
<td>
   <p>میانگین (بر حسب درصد) زمانی که وظایف در یک پنجرهٔ ۱۰ ثانیه‌ای به‌دلیل ازدحام منتظر مانده‌اند.</p>
</td>
</tr>
<tr><td><code>avg60</code> <B>[الزامی]</B><br/>
<code>float64</code>
</td>
<td>
   <p>میانگین (بر حسب درصد) زمانی که وظایف در یک پنجرهٔ ۶۰ ثانیه‌ای به‌دلیل ازدحام منتظر مانده‌اند.</p>
</td>
</tr>
<tr><td><code>avg300</code> <B>[الزامی]</B><br/>
<code>float64</code>
</td>
<td>
   <p>میانگین (بر حسب درصد) زمانی که وظایف در یک پنجرهٔ ۳۰۰ ثانیه‌ای به‌دلیل ازدحام منتظر مانده‌اند.</p>
</td>
</tr>
</tbody>
</table>

## `PSIStats`     {#PSIStats}
    

**در این موارد ظاهر می‌شود:**

- [CPUStats](#CPUStats)

- [IOStats](#IOStats)

- [MemoryStats](#MemoryStats)


<p>آمار PSI برای یک منبع مجزا.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>full</code> <B>[الزامی]</B><br/>
<a href="#PSIData"><code>PSIData</code></a>
</td>
<td>
   <p>داده‌های PSI برای همهٔ وظایف موجود در cgroup.</p>
</td>
</tr>
<tr><td><code>some</code> <B>[الزامی]</B><br/>
<a href="#PSIData"><code>PSIData</code></a>
</td>
<td>
   <p>داده‌های PSI برای برخی از وظایف موجود در cgroup.</p>
</td>
</tr>
</tbody>
</table>

## `PVCReference`     {#PVCReference}
    

**در این موارد ظاهر می‌شود:**

- [VolumeStats](#VolumeStats)


<p>نوع PVCReference اطلاعات کافی برای توصیف PVC ارجاع‌شده را در بر دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>namespace</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `PodReference`     {#PodReference}
    

**در این موارد ظاهر می‌شود:**

- [PodStats](#PodStats)


<p>نوع PodReference اطلاعات کافی برای یافتن پاد ارجاع‌شده را در بر دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>namespace</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>uid</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `PodStats`     {#PodStats}
    

**در این موارد ظاهر می‌شود:**

- [Summary](#Summary)


<p>نوع PodStats آمارهای نمونه‌ای پردازش‌نشده را در سطح Pod نگه می‌دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>podRef</code> <B>[الزامی]</B><br/>
<a href="#PodReference"><code>PodReference</code></a>
</td>
<td>
   <p>ارجاع به Pod اندازه‌گیری‌شده.</p>
</td>
</tr>
<tr><td><code>startTime</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>زمانی که جمع‌آوری داده برای آمارهای در سطح Pod (مانند آمار شبکه) آغاز یا دوباره آغاز شده است.</p>
</td>
</tr>
<tr><td><code>containers</code> <B>[الزامی]</B><br/>
<a href="#ContainerStats"><code>[]ContainerStats</code></a>
</td>
<td>
   <p>آمار کانتینرهای موجود در Pod اندازه‌گیری‌شده.</p>
</td>
</tr>
<tr><td><code>cpu</code><br/>
<a href="#CPUStats"><code>CPUStats</code></a>
</td>
<td>
   <p>آمار مربوط به منابع CPU مصرف‌شده توسط cgroup مربوط به Pod (که مصرف منابع همه کانتینرها و سربار Pod را دربر می‌گیرد).</p>
</td>
</tr>
<tr><td><code>memory</code><br/>
<a href="#MemoryStats"><code>MemoryStats</code></a>
</td>
<td>
   <p>آمار مربوط به منابع حافظه (RAM) مصرف‌شده توسط cgroup مربوط به Pod (که مصرف منابع همه کانتینرها و سربار Pod را دربر می‌گیرد).</p>
</td>
</tr>
<tr><td><code>io</code><br/>
<a href="#IOStats"><code>IOStats</code></a>
</td>
<td>
   <p>آمار مربوط به منابع ورودی/خروجی (IO) مصرف‌شده توسط cgroup مربوط به Pod (که مصرف منابع همه کانتینرها و سربار Pod را دربر می‌گیرد).</p>
</td>
</tr>
<tr><td><code>network</code><br/>
<a href="#NetworkStats"><code>NetworkStats</code></a>
</td>
<td>
   <p>آمار مربوط به منابع شبکه.</p>
</td>
</tr>
<tr><td><code>volume</code><br/>
<a href="#VolumeStats"><code>[]VolumeStats</code></a>
</td>
<td>
   <p>آمار مربوط به مصرف منابع فایل‌سیستم توسط حجم‌ها (volume).
مقدار VolumeStats.UsedBytes تعداد بایت‌هایی است که Volume استفاده کرده است.</p>
</td>
</tr>
<tr><td><code>ephemeral-storage</code><br/>
<a href="#FsStats"><code>FsStats</code></a>
</td>
<td>
   <p>فیلد EphemeralStorage کل مصرف فایل‌سیستم را برای کانتینرها و حجم‌های مبتنی بر emptyDir در Pod اندازه‌گیری‌شده گزارش می‌کند.</p>
</td>
</tr>
<tr><td><code>process_stats</code><br/>
<a href="#ProcessStats"><code>ProcessStats</code></a>
</td>
<td>
   <p>آمار ProcessStats مربوط به پردازه‌ها.</p>
</td>
</tr>
<tr><td><code>swap</code><br/>
<a href="#SwapStats"><code>SwapStats</code></a>
</td>
<td>
   <p>آمار مربوط به منابع swap. این آمار فقط برای سیستم‌های غیر Windows گزارش می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `ProcessStats`     {#ProcessStats}
    

**در این موارد ظاهر می‌شود:**

- [PodStats](#PodStats)


<p>نوع ProcessStats آمارهای مربوط به پردازه‌ها است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>process_count</code><br/>
<code>uint64</code>
</td>
<td>
   <p>تعداد پردازه‌ها</p>
</td>
</tr>
</tbody>
</table>

## `RlimitStats`     {#RlimitStats}
    

**در این موارد ظاهر می‌شود:**

- [NodeStats](#NodeStats)


<p>نوع RlimitStats آمارهای rlimit سیستم‌عامل است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>time</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>maxpid</code> <B>[الزامی]</B><br/>
<code>int64</code>
</td>
<td>
   <p>حداکثر تعداد پردازه‌های موجود (در Linux، به‌طور دقیق‌تر، رشته‌ها یا threadها) در سیستم‌عامل. برای اطلاعات بیشتر، RLIMIT_NPROC را در getrlimit(2) ببینید.
این مقدار سقفی است که سیستم‌عامل برای تعداد شناسه‌های پردازه (PID) قابل‌تخصیص تعیین می‌کند.
در Linux، هر task (چه پردازه و چه thread) یک PID مصرف می‌کند.</p>
</td>
</tr>
<tr><td><code>curproc</code> <B>[الزامی]</B><br/>
<code>int64</code>
</td>
<td>
   <p>تعداد پردازه‌های در حال اجرا (در Linux، به‌طور دقیق‌تر، threadها) در سیستم‌عامل.</p>
</td>
</tr>
</tbody>
</table>

## `RuntimeStats`     {#RuntimeStats}
    

**در این موارد ظاهر می‌شود:**

- [NodeStats](#NodeStats)


<p>نوع RuntimeStats آمارهای مربوط به محیط اجرای کانتینر زیرین است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>imageFs</code><br/>
<a href="#FsStats"><code>FsStats</code></a>
</td>
<td>
   <p>آمار مربوط به فایل‌سیستم زیرینی که ایمیج‌های کانتینر در آن ذخیره می‌شوند.
این فایل‌سیستم ممکن است همان فایل‌سیستم اصلی (root) باشد.
منظور از مصرف در اینجا، کل تعداد بایت‌هایی است که ایمیج‌ها روی فایل‌سیستم اشغال کرده‌اند.</p>
</td>
</tr>
<tr><td><code>containerFs</code><br/>
<a href="#FsStats"><code>FsStats</code></a>
</td>
<td>
   <p>آمار مربوط به فایل‌سیستم زیرینی که لایه قابل‌نوشتن کانتینر در آن ذخیره می‌شود.
این فایل‌سیستم ممکن است همان فایل‌سیستم اصلی (root) یا ImageFS باشد.
منظور از مصرف در اینجا، کل تعداد بایت‌هایی است که لایه قابل‌نوشتن روی فایل‌سیستم اشغال کرده است.</p>
</td>
</tr>
</tbody>
</table>

## `SwapStats`     {#SwapStats}
    

**در این موارد ظاهر می‌شود:**

- [ContainerStats](#ContainerStats)

- [NodeStats](#NodeStats)

- [PodStats](#PodStats)


<p>نوع SwapStats داده‌هایی درباره مصرف حافظه دربر دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>time</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>زمانی که این آمارها به‌روزرسانی شده‌اند.</p>
</td>
</tr>
<tr><td><code>swapAvailableBytes</code><br/>
<code>uint64</code>
</td>
<td>
   <p>حافظه swap در دسترس برای استفاده. این مقدار به‌صورت <!-- raw HTML omitted --> - <!-- raw HTML omitted --> تعریف می‌شود.
اگر محدودیت swap تعریف نشده باشد، این مقدار حذف می‌شود.</p>
</td>
</tr>
<tr><td><code>swapUsageBytes</code><br/>
<code>uint64</code>
</td>
<td>
   <p>کل حافظه swap در حال استفاده.</p>
</td>
</tr>
</tbody>
</table>

## `UserDefinedMetric`     {#UserDefinedMetric}
    

**در این موارد ظاهر می‌شود:**

- [ContainerStats](#ContainerStats)


<p>نوع UserDefinedMetric معیاری (metric) را نشان می‌دهد که کاربران آن را تعریف و تولید کرده‌اند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>UserDefinedMetricDescriptor</code> <B>[الزامی]</B><br/>
<a href="#UserDefinedMetricDescriptor"><code>UserDefinedMetricDescriptor</code></a>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>time</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>زمانی که این آمارها به‌روزرسانی شده‌اند.</p>
</td>
</tr>
<tr><td><code>value</code> <B>[الزامی]</B><br/>
<code>float64</code>
</td>
<td>
   <p>مقدار معیار. دقت مقادیر Float64 برابر با ۵۳ بیت است.
پیش‌بینی نمی‌کنیم هیچ معیاری از این مقدار فراتر رود.</p>
</td>
</tr>
</tbody>
</table>

## `UserDefinedMetricDescriptor`     {#UserDefinedMetricDescriptor}
    

**در این موارد ظاهر می‌شود:**

- [UserDefinedMetric](#UserDefinedMetric)


<p>نوع UserDefinedMetricDescriptor فراداده‌ای را دربر دارد که یک معیار تعریف‌شده توسط کاربر را توصیف می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>نام معیار.</p>
</td>
</tr>
<tr><td><code>type</code> <B>[الزامی]</B><br/>
<a href="#UserDefinedMetricType"><code>UserDefinedMetricType</code></a>
</td>
<td>
   <p>نوع معیار.</p>
</td>
</tr>
<tr><td><code>units</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>واحدهای نمایش آمارها.</p>
</td>
</tr>
<tr><td><code>labels</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>برچسب‌های فراداده‌ای مرتبط با این معیار.</p>
</td>
</tr>
</tbody>
</table>

## `UserDefinedMetricType`     {#UserDefinedMetricType}
    
(نام مستعار `string`)

**در این موارد ظاهر می‌شود:**

- [UserDefinedMetricDescriptor](#UserDefinedMetricDescriptor)


<p>نوع UserDefinedMetricType مشخص می‌کند که کاربر چگونه باید معیار را تفسیر کند.</p>




## `VolumeStats`     {#VolumeStats}
    

**در این موارد ظاهر می‌شود:**

- [PodStats](#PodStats)


<p>نوع VolumeStats داده‌هایی درباره مصرف فایل‌سیستم Volume دربر دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>FsStats</code> <B>[الزامی]</B><br/>
<a href="#FsStats"><code>FsStats</code></a>
</td>
<td>
   <p>نوع FsStats به‌صورت تعبیه‌شده (embedded)</p>
</td>
</tr>
<tr><td><code>name</code><br/>
<code>string</code>
</td>
<td>
   <p>نامی که به Volume داده شده است.</p>
</td>
</tr>
<tr><td><code>pvcRef</code><br/>
<a href="#PVCReference"><code>PVCReference</code></a>
</td>
<td>
   <p>ارجاع به PVC، در صورت وجود.</p>
</td>
</tr>
</tbody>
</table>
