---
reviewers:
- dchen1107
- liggitt
title: ارتباط میان نودها و control plane
content_type: concept
weight: 20
aliases:
- master-node-communication
---

<!-- overview -->

این سند مسیرهای ارتباطی میان {{< glossary_tooltip term_id="kube-apiserver" text="سرور API" >}}
و {{< glossary_tooltip text="کلاستر" term_id="cluster" length="all" >}} کوبرنتیز را فهرست می‌کند.
هدف این است که کاربران بتوانند نصب خود را سفارشی کنند و پیکربندی شبکه را مستحکم سازند
تا کلاستر بتواند روی یک شبکهٔ غیرقابل‌اعتماد (یا روی نشانی‌های IP کاملاً عمومی در یک ارائه‌دهندهٔ
ابری) اجرا شود.

<!-- body -->

## از نود به control plane

کوبرنتیز از الگوی API «هاب و پره» (hub-and-spoke) پیروی می‌کند. همهٔ استفاده‌ها از API که از سوی نودها (یا پادهایی که اجرا می‌کنند) انجام می‌شود،
به سرور API ختم می‌شود. هیچ‌یک از دیگر اجزای control plane برای در معرض قرار دادن
سرویس‌های راه دور طراحی نشده‌اند. سرور API طوری پیکربندی می‌شود که روی یک درگاه امن HTTPS
(معمولاً 443) به اتصال‌های راه دور گوش دهد و یک یا چند شکل از
[احراز هویت](/docs/reference/access-authn-authz/authentication/) کلاینت در آن فعال باشد.
یک یا چند شکل از [مجوزدهی](/docs/reference/access-authn-authz/authorization/) نیز باید
فعال باشد، به‌ویژه اگر [درخواست‌های ناشناس](/docs/reference/access-authn-authz/authentication/#anonymous-requests)
یا [توکن‌های حساب سرویس](/docs/reference/access-authn-authz/authentication/#service-account-tokens)
مجاز باشند.

نودها باید با {{< glossary_tooltip text="گواهی" term_id="certificate" >}} ریشهٔ عمومی کلاستر تأمین شوند تا بتوانند
به‌همراه اعتبارنامه‌های معتبر کلاینت، به‌طور امن به سرور API متصل شوند. یک رویکرد مناسب این است که
اعتبارنامه‌های کلاینتی که به kubelet داده می‌شود، به شکل یک گواهی کلاینت باشد. برای
تأمین خودکار گواهی‌های کلاینت kubelet، به
[راه‌اندازی اولیهٔ TLS در kubelet](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/)
مراجعه کنید.

{{< glossary_tooltip text="پادهایی" term_id="pod" >}} که می‌خواهند به سرور API متصل شوند، می‌توانند با بهره‌گیری از یک حساب سرویس این کار را به‌طور امن انجام دهند،
به‌گونه‌ای که کوبرنتیز هنگام نمونه‌سازی پاد، گواهی ریشهٔ عمومی و یک توکن حامل (bearer token) معتبر را
به‌طور خودکار به درون آن تزریق کند.
سرویس `kubernetes` (در فضای نام `default`) با یک نشانی IP مجازی پیکربندی شده است که
(از طریق `{{< glossary_tooltip text="kube-proxy" term_id="kube-proxy" >}}`) به نقطهٔ پایانی HTTPS روی سرور API هدایت می‌شود.

اجزای control plane نیز از طریق درگاه امن با سرور API ارتباط برقرار می‌کنند.

در نتیجه، حالت عملیاتی پیش‌فرض برای اتصال‌ها از نودها و پادهای در حال اجرا روی
نودها به control plane، به‌طور پیش‌فرض امن است و می‌تواند روی شبکه‌های غیرقابل‌اعتماد و/یا
عمومی اجرا شود.

## از control plane به نود

دو مسیر ارتباطی اصلی از control plane (سرور API) به نودها وجود دارد.
مسیر نخست از سرور API به فرایند {{< glossary_tooltip text="kubelet" term_id="kubelet" >}} است که روی هر نود کلاستر اجرا می‌شود.
مسیر دوم از سرور API به هر نود، پاد یا سرویسی از طریق قابلیت _پراکسی_ سرور API
است.

### از سرور API به kubelet

اتصال‌های سرور API به kubelet برای موارد زیر استفاده می‌شوند:

* دریافت لاگ‌های پادها.
* اتصال (معمولاً از طریق `kubectl`) به پادهای در حال اجرا.
* فراهم‌کردن قابلیت هدایت درگاه (port-forwarding) در kubelet.

این اتصال‌ها به نقطهٔ پایانی HTTPS مربوط به kubelet ختم می‌شوند. به‌طور پیش‌فرض، سرور API
گواهی سرویس‌دهی kubelet را تأیید نمی‌کند؛ این امر اتصال را در معرض حملات مرد میانی
قرار می‌دهد و اجرای آن را روی شبکه‌های غیرقابل‌اعتماد و/یا عمومی **ناامن** می‌سازد.

برای تأیید این اتصال، از پرچم `--kubelet-certificate-authority` استفاده کنید تا
بستهٔ گواهی ریشه‌ای را در اختیار سرور API قرار دهید که برای تأیید گواهی سرویس‌دهی kubelet به کار رود.

اگر این کار ممکن نیست، در صورت نیاز از [تونل‌زنی SSH](#ssh-tunnels) میان سرور API و kubelet
استفاده کنید تا از اتصال از طریق یک شبکهٔ
غیرقابل‌اعتماد یا عمومی پرهیز شود.


در نهایت، [احراز هویت و/یا مجوزدهی kubelet](/docs/reference/access-authn-authz/kubelet-authn-authz/)
باید برای ایمن‌سازی API مربوط به kubelet فعال شود.

### از سرور API به نودها، پادها و سرویس‌ها

اتصال‌های سرور API به یک نود، پاد یا سرویس به‌طور پیش‌فرض اتصال‌های HTTP ساده هستند
و بنابراین نه احراز هویت می‌شوند و نه رمزگذاری. می‌توان آن‌ها را با افزودن پیشوند `https:`
به نام نود، پاد یا سرویس در URL مربوط به API، روی یک اتصال امن HTTPS اجرا کرد، اما در این حالت
گواهی ارائه‌شده توسط نقطهٔ پایانی HTTPS اعتبارسنجی نمی‌شود و اعتبارنامهٔ کلاینت نیز ارائه نمی‌شود. بنابراین
اگرچه اتصال رمزگذاری می‌شود، هیچ تضمینی برای یکپارچگی فراهم نمی‌کند. اجرای این
اتصال‌ها روی شبکه‌های غیرقابل‌اعتماد یا عمومی **در حال حاضر امن نیست**.

### تونل‌های SSH

کوبرنتیز از [تونل‌های SSH](https://www.ssh.com/academy/ssh/tunneling) برای محافظت از مسیرهای ارتباطی control plane به نودها پشتیبانی می‌کند. در این
پیکربندی، سرور API یک تونل SSH به هر نود کلاستر برقرار می‌کند (با اتصال به
سرور SSH که روی درگاه 22 گوش می‌دهد) و همهٔ ترافیک مقصد kubelet، نود، پاد یا
سرویس را از طریق این تونل عبور می‌دهد.
این تونل تضمین می‌کند که ترافیک بیرون از شبکه‌ای که نودها در آن
اجرا می‌شوند در معرض دید قرار نگیرد.

{{< note >}}
تونل‌های SSH در حال حاضر منسوخ شده‌اند، بنابراین نباید استفاده از آن‌ها را برگزینید، مگر اینکه بدانید
چه می‌کنید. [سرویس Konnectivity](#konnectivity-service) جایگزینی برای این
کانال ارتباطی است.
{{< /note >}}

### سرویس Konnectivity

{{< feature-state for_k8s_version="v1.18" state="beta" >}}

سرویس Konnectivity به‌عنوان جایگزین تونل‌های SSH، یک پراکسی در سطح TCP برای
ارتباط control plane با کلاستر فراهم می‌کند. سرویس Konnectivity از دو بخش تشکیل شده است:
سرور Konnectivity در شبکهٔ control plane و عامل‌های Konnectivity در شبکهٔ نودها.
عامل‌های Konnectivity اتصال‌ها را به سرور Konnectivity آغاز می‌کنند و اتصال‌های شبکه
را برقرار نگه می‌دارند.
پس از فعال‌سازی سرویس Konnectivity، همهٔ ترافیک control plane به نودها از طریق این
اتصال‌ها عبور می‌کند.

برای راه‌اندازی سرویس Konnectivity در کلاستر خود، [وظیفهٔ سرویس Konnectivity](/docs/tasks/extend-kubernetes/setup-konnectivity/) را
دنبال کنید.

## {{% heading "whatsnext" %}}

* دربارهٔ [اجزای control plane کوبرنتیز](/docs/concepts/architecture/#control-plane-components) بخوانید
* دربارهٔ [مدل هاب و پره](https://book.kubebuilder.io/multiversion-tutorial/conversion-concepts.html#hubs-spokes-and-other-wheel-metaphors) بیشتر بیاموزید
* بیاموزید چگونه [یک کلاستر را ایمن کنید](/docs/tasks/administer-cluster/securing-a-cluster/)
* دربارهٔ [API کوبرنتیز](/docs/concepts/overview/kubernetes-api/) بیشتر بیاموزید
* [سرویس Konnectivity را راه‌اندازی کنید](/docs/tasks/extend-kubernetes/setup-konnectivity/)
* [از هدایت درگاه برای دسترسی به برنامه‌ها در یک کلاستر استفاده کنید](/docs/tasks/access-application-cluster/port-forward-access-application-cluster/)
* بیاموزید چگونه [لاگ‌های پادها را دریافت کنید](/docs/tasks/debug/debug-application/debug-running-pod/#examine-pod-logs) و [از kubectl port-forward استفاده کنید](/docs/tasks/access-application-cluster/port-forward-access-application-cluster/#forward-a-local-port-to-a-port-on-the-pod)
