---
title: پاد آینه‌ای (Mirror Pod)
id: mirror-pod
short_description: >
  آبجکتی در API server که یک پاد ایستا را روی یک kubelet ردیابی می‌کند.

aka: 
tags:
- fundamental
---
 یک آبجکت {{< glossary_tooltip text="پاد" term_id="pod" >}} که {{< glossary_tooltip text="kubelet" term_id="kubelet" >}} از آن
 برای نمایش یک {{< glossary_tooltip text="پاد ایستا" term_id="static-pod" >}} استفاده می‌کند.

<!--more--> 

هنگامی که kubelet یک پاد ایستا را در پیکربندی خود پیدا می‌کند، به‌طور خودکار تلاش می‌کند یک آبجکت Pod متناظر با آن را روی API server کوبرنتیز ایجاد کند. به این ترتیب، این پاد روی API server قابل مشاهده است، اما نمی‌توان آن را از آنجا کنترل کرد.

(برای مثال، حذف یک پاد آینه‌ای مانع از آن نمی‌شود که سرویس پس‌زمینهٔ kubelet به اجرای آن ادامه دهد.)
