---
title: Mirror Pod
id: mirror-pod
short_description: >
  آبجکتی در API server که یک static pod را روی یک kubelet پیگیری می‌کند.

aka: 
tags:
- fundamental
---
 یک آبجکت {{< glossary_tooltip text="Pod" term_id="pod" >}} که {{< glossary_tooltip text="kubelet" term_id="kubelet" >}} از آن برای نمایش یک {{< glossary_tooltip text="static pod" term_id="static-pod" >}} استفاده می‌کند.

<!--more--> 

هنگامی که kubelet یک static pod را در پیکربندی خود پیدا می‌کند، به‌طور خودکار تلاش می‌کند برای آن یک آبجکت Pod روی API server کوبرنتیز ایجاد کند. این بدان معناست که Pod روی API server قابل مشاهده خواهد بود، اما از طریق آن قابل کنترل نیست.

(برای مثال، حذف یک mirror pod باعث نمی‌شود که دیمن kubelet از اجرای آن متوقف شود.)
