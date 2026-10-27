---
title: گسترش API کوبرنتیز
weight: 30
no_list: true
---

منابع سفارشی (Custom resources) افزونه‌هایی برای API کوبرنتیز هستند. کوبرنتیز دو روش برای افزودن منابع سفارشی به کلاستر شما فراهم می‌کند:

- سازوکار [CustomResourceDefinition](/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
  (به اختصار CRD) به شما امکان می‌دهد یک API سفارشی جدید را با گروه API، kind و
  طرح‌واره (schema) مورد نظر خود به‌صورت اعلانی (declarative) تعریف کنید.
  control plane کوبرنتیز، ارائه و ذخیره‌سازی منبع سفارشی شما را بر عهده می‌گیرد. CRDها به شما امکان می‌دهند
  بدون نوشتن و اجرای یک API server سفارشی، انواع جدیدی از منابع را برای کلاستر خود ایجاد کنید.
- [لایه تجمیع (aggregation layer)](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)
  پشت API server اصلی قرار می‌گیرد و API server اصلی نقش یک پروکسی را ایفا می‌کند.
  این ساختار «تجمیع API» (API Aggregation یا AA) نامیده می‌شود و به شما امکان می‌دهد
  با نوشتن و استقرار API server اختصاصی خود، پیاده‌سازی‌های
  ویژه‌ای برای منابع سفارشی خود ارائه دهید.
  API server اصلی درخواست‌های مربوط به APIهای سفارشی مشخص‌شده توسط شما را به API server شما واگذار می‌کند
  و به این ترتیب آن‌ها را در دسترس همه کلاینت‌های خود قرار می‌دهد.
