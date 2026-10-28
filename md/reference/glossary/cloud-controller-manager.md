---
title: Cloud Controller Manager
id: cloud-controller-manager
full_link: /docs/concepts/architecture/cloud-controller/
short_description: >
  مؤلفه‌ای از control plane که کوبرنتیز را با ارائه‌دهندگان ابری شخص ثالث یکپارچه می‌کند.
aka: 
tags:
- architecture
- operation
---
 مؤلفه‌ای از {{< glossary_tooltip text="control plane" term_id="control-plane" >}} کوبرنتیز
که منطق کنترلی مختص به فضای ابری را در خود جای داده است. cloud controller manager امکان می‌دهد
کلاستر خود را به API ارائه‌دهنده ابری خود متصل کنید و مؤلفه‌هایی را که با آن پلتفرم ابری تعامل دارند
از مؤلفه‌هایی که فقط با کلاستر شما تعامل می‌کنند جدا می‌کند.

<!--more-->

مؤلفه cloud-controller-manager با جداسازی منطق قابلیت همکاری میان کوبرنتیز و زیرساخت ابری زیربنایی،
به ارائه‌دهندگان ابری امکان می‌دهد قابلیت‌ها را با سرعتی متفاوت از پروژه اصلی کوبرنتیز منتشر کنند.
