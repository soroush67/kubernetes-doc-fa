---
reviewers:
- mikedanese
- liggitt
- smarterclayton
- awly
title: TLS bootstrapping
content_type: concept
weight: 120
---

<!-- overview -->

در یک کلاستر کوبرنتیز، مؤلفه‌هایی که روی نودهای کارگر اجرا می‌شوند، یعنی kubelet و kube-proxy، باید
با مؤلفه‌های control plane کوبرنتیز، به‌طور مشخص kube-apiserver، ارتباط برقرار کنند.
برای اطمینان از اینکه این ارتباط خصوصی می‌ماند، دستکاری نمی‌شود، و هر مؤلفه از کلاستر
با یک مؤلفه قابل‌اعتماد دیگر در ارتباط است، به‌شدت توصیه می‌کنیم از گواهی‌های TLS کلاینت روی نودها استفاده کنید.

فرایند معمول راه‌اندازی اولیه (bootstrapping) این مؤلفه‌ها، به‌ویژه نودهای کارگر که برای ارتباط امن با kube-apiserver
به گواهی نیاز دارند، می‌تواند فرایندی دشوار باشد، زیرا اغلب خارج از
حوزه‌ی کوبرنتیز قرار دارد و به کار اضافی قابل‌توجهی نیاز دارد.
این موضوع به‌نوبه‌ی خود می‌تواند راه‌اندازی یا مقیاس‌دهی یک کلاستر را دشوار کند.

برای ساده‌سازی این فرایند، از نسخه‌ی 1.4 به بعد، کوبرنتیز یک API برای درخواست گواهی
و امضای آن معرفی کرد. پیشنهاد مربوط به آن را می‌توانید [اینجا](https://github.com/kubernetes/kubernetes/pull/20439) ببینید.

این سند فرایند راه‌اندازی اولیه‌ی نود، نحوه‌ی برپایی bootstrapping گواهی کلاینت TLS برای
kubeletها، و چگونگی عملکرد آن را شرح می‌دهد.

<!-- body -->

## فرایند راه‌اندازی اولیه {#initialization-process}

هنگامی که یک نود کارگر راه‌اندازی می‌شود، kubelet کارهای زیر را انجام می‌دهد:

1. به دنبال فایل `kubeconfig` خود می‌گردد
1. نشانی URL سرور API و اعتبارنامه‌ها، که معمولاً یک کلید TLS و گواهی امضاشده هستند، را از فایل `kubeconfig` بازیابی می‌کند
1. تلاش می‌کند با استفاده از اعتبارنامه‌ها با سرور API ارتباط برقرار کند.

با فرض اینکه kube-apiserver اعتبارنامه‌های kubelet را با موفقیت اعتبارسنجی کند،
kubelet را به‌عنوان یک نود معتبر در نظر می‌گیرد و شروع به تخصیص پادها به آن می‌کند.

توجه داشته باشید که فرایند بالا به موارد زیر وابسته است:

* وجود یک کلید و گواهی روی میزبان محلی در `kubeconfig`
* امضای گواهی توسط یک مرجع صدور گواهی (CA) که مورد اعتماد kube-apiserver است

همه‌ی موارد زیر بر عهده‌ی کسی است که کلاستر را راه‌اندازی و مدیریت می‌کند:

1. ایجاد کلید و گواهی CA
1. توزیع گواهی CA به نودهای control plane که kube-apiserver روی آن‌ها اجرا می‌شود
1. ایجاد یک کلید و گواهی برای هر kubelet؛ به‌شدت توصیه می‌شود برای هر kubelet یک کلید و گواهی یکتا با CN یکتا وجود داشته باشد
1. امضای گواهی kubelet با استفاده از کلید CA
1. توزیع کلید kubelet و گواهی امضاشده به نود مشخصی که kubelet روی آن اجرا می‌شود

TLS Bootstrapping که در این سند شرح داده شده است، با هدف ساده‌سازی و خودکارسازی جزئی یا حتی
کامل مراحل ۳ به بعد طراحی شده است، زیرا این مراحل در زمان راه‌اندازی یا مقیاس‌دهی
یک کلاستر بیشترین کاربرد را دارند.

### راه‌اندازی اولیه با bootstrap {#bootstrap-initialization}

در فرایند راه‌اندازی اولیه با bootstrap، موارد زیر رخ می‌دهد:

1. kubelet شروع به کار می‌کند
1. kubelet متوجه می‌شود که فایل `kubeconfig` _ندارد_
1. kubelet به دنبال فایل `bootstrap-kubeconfig` می‌گردد و آن را پیدا می‌کند
1. kubelet فایل bootstrap خود را می‌خواند و نشانی URL سرور API و یک «توکن» با کاربرد محدود را بازیابی می‌کند
1. kubelet به سرور API متصل می‌شود و با استفاده از توکن احراز هویت می‌کند
1. kubelet اکنون اعتبارنامه‌های محدودی برای ایجاد و بازیابی یک درخواست امضای گواهی (CSR) دارد
1. kubelet یک CSR برای خود ایجاد می‌کند که مقدار signerName آن `kubernetes.io/kube-apiserver-client-kubelet` است
1. CSR به یکی از دو روش تأیید می‌شود:
   * در صورت پیکربندی، kube-controller-manager به‌طور خودکار CSR را تأیید می‌کند
   * در صورت پیکربندی، یک فرایند بیرونی، احتمالاً یک شخص، CSR را با استفاده از API کوبرنتیز یا از طریق `kubectl` تأیید می‌کند
1. گواهی برای kubelet ایجاد می‌شود
1. گواهی به kubelet صادر می‌شود
1. kubelet گواهی را بازیابی می‌کند
1. kubelet یک `kubeconfig` مناسب را با کلید و گواهی امضاشده ایجاد می‌کند
1. kubelet عملکرد عادی خود را آغاز می‌کند
1. اختیاری: در صورت پیکربندی، kubelet هنگامی که گواهی نزدیک به انقضا است، به‌طور خودکار درخواست تمدید آن را می‌دهد
1. گواهی تمدیدشده، بسته به پیکربندی، به‌صورت خودکار یا دستی تأیید و صادر می‌شود.

ادامه‌ی این سند مراحل لازم برای پیکربندی TLS Bootstrapping و محدودیت‌های آن را شرح می‌دهد.

## پیکربندی {#configuration}

برای پیکربندی TLS bootstrapping و تأیید خودکار اختیاری، باید گزینه‌هایی را روی مؤلفه‌های زیر پیکربندی کنید:

* kube-apiserver
* kube-controller-manager
* kubelet
* منابع درون کلاستر: `ClusterRoleBinding` و در صورت نیاز `ClusterRole`

علاوه بر این، به مرجع صدور گواهی (CA) کوبرنتیز خود نیاز دارید.

## مرجع صدور گواهی {#certificate-authority}

همانند حالت بدون bootstrapping، به کلید و گواهی مرجع صدور گواهی (CA) نیاز خواهید داشت.
همانند حالت بدون bootstrapping، از این‌ها برای امضای گواهی kubelet استفاده می‌شود. مانند قبل،
توزیع آن‌ها به نودهای control plane بر عهده‌ی شماست.

برای اهداف این سند، فرض می‌کنیم این موارد در مسیرهای `/var/lib/kubernetes/ca.pem` (گواهی) و `/var/lib/kubernetes/ca-key.pem` (کلید)
روی نودهای control plane توزیع شده‌اند.
از این به بعد به آن‌ها «گواهی و کلید CA کوبرنتیز» می‌گوییم.

همه‌ی مؤلفه‌های کوبرنتیز که از این گواهی‌ها استفاده می‌کنند، یعنی kubelet، kube-apiserver و
kube-controller-manager، فرض می‌کنند که کلید و گواهی با قالب PEM کدگذاری شده‌اند.

## پیکربندی kube-apiserver {#kube-apiserver-configuration}

kube-apiserver برای فعال‌سازی TLS bootstrapping چند الزام دارد:

* شناسایی CA که گواهی کلاینت را امضا می‌کند
* احراز هویت kubelet در حال bootstrap به‌عنوان عضوی از گروه `system:bootstrappers`
* مجاز کردن kubelet در حال bootstrap برای ایجاد یک درخواست امضای گواهی (CSR)

### شناسایی گواهی‌های کلاینت {#recognizing-client-certificates}

این کار برای همه‌ی انواع احراز هویت با گواهی کلاینت معمول است.
اگر پیش‌تر تنظیم نشده است، برای فعال‌سازی احراز هویت با گواهی کلاینت، پرچم `--client-ca-file=FILENAME` را به فرمان kube-apiserver اضافه کنید و
به یک بسته‌ی مرجع صدور گواهی که شامل گواهی امضاکننده است ارجاع دهید، برای مثال
`--client-ca-file=/var/lib/kubernetes/ca.pem`.

### احراز هویت اولیه‌ی bootstrap {#initial-bootstrap-authentication}

برای اینکه kubelet در حال bootstrap بتواند به kube-apiserver متصل شود و درخواست گواهی بدهد،
ابتدا باید نزد سرور احراز هویت شود. می‌توانید از هر
[احراز هویت‌کننده (authenticator)](/docs/reference/access-authn-authz/authentication/) که بتواند kubelet را احراز هویت کند استفاده کنید.

اگرچه برای اعتبارنامه‌های اولیه‌ی bootstrap مربوط به kubelet می‌توان از هر راهبرد احراز هویتی استفاده کرد،
دو احراز هویت‌کننده‌ی زیر برای سهولت در تأمین (provisioning) توصیه می‌شوند.

1. [توکن‌های Bootstrap](#bootstrap-tokens)
1. [فایل احراز هویت توکن](#token-authentication-file)

استفاده از توکن‌های bootstrap روشی ساده‌تر و آسان‌تر برای مدیریت احراز هویت kubeletهاست
و هنگام راه‌اندازی kube-apiserver به هیچ پرچم اضافه‌ای نیاز ندارد.

هر روشی که انتخاب کنید، الزام این است که kubelet بتواند به‌عنوان کاربری احراز هویت شود که حق انجام کارهای زیر را دارد:

1. ایجاد و بازیابی CSRها
1. در صورت فعال بودن تأیید خودکار، به‌طور خودکار برای درخواست گواهی‌های کلاینت نود تأیید شود.

kubeletی که با استفاده از توکن‌های bootstrap احراز هویت می‌شود، به‌عنوان کاربری در گروه
`system:bootstrappers` احراز هویت می‌شود، که روش استاندارد مورد استفاده است.

با بالغ‌تر شدن این قابلیت، باید اطمینان حاصل کنید که توکن‌ها به یک سیاست کنترل دسترسی مبتنی بر نقش (RBAC)
مقید شده‌اند که درخواست‌ها (با استفاده از [توکن bootstrap](/docs/reference/access-authn-authz/bootstrap-tokens/)) را
صرفاً به درخواست‌های کلاینت مرتبط با تأمین گواهی محدود می‌کند. با وجود RBAC، محدود کردن
توکن‌ها به یک گروه انعطاف‌پذیری زیادی فراهم می‌کند. برای مثال، می‌توانید پس از اتمام تأمین نودها،
دسترسی یک گروه bootstrap مشخص را غیرفعال کنید.

#### توکن‌های Bootstrap {#bootstrap-tokens}

توکن‌های bootstrap به‌تفصیل [اینجا](/docs/reference/access-authn-authz/bootstrap-tokens/) شرح داده شده‌اند.
این‌ها توکن‌هایی هستند که به‌صورت secret در کلاستر کوبرنتیز ذخیره می‌شوند و سپس به kubeletهای مجزا صادر می‌شوند.
می‌توانید برای کل کلاستر از یک توکن واحد استفاده کنید، یا برای هر نود کارگر یک توکن صادر کنید.

این فرایند دو بخش دارد:

1. یک secret کوبرنتیز با شناسه‌ی توکن، secret و دامنه(های) آن ایجاد کنید.
1. توکن را به kubelet صادر کنید

از دیدگاه kubelet، همه‌ی توکن‌ها مثل هم هستند و معنای خاصی ندارند.
اما از دیدگاه kube-apiserver، توکن bootstrap خاص است.
kube-apiserver به‌دلیل `type`، `namespace` و `name` این توکن، آن را به‌عنوان یک توکن ویژه شناسایی می‌کند
و به هر کسی که با آن توکن احراز هویت شود، حقوق ویژه‌ی bootstrap اعطا می‌کند و به‌طور مشخص
او را عضوی از گروه `system:bootstrappers` در نظر می‌گیرد. این کار یکی از الزامات اساسی
TLS bootstrapping را برآورده می‌کند.

جزئیات ایجاد secret [اینجا](/docs/reference/access-authn-authz/bootstrap-tokens/) در دسترس است.

اگر می‌خواهید از توکن‌های bootstrap استفاده کنید، باید آن را با پرچم زیر روی kube-apiserver فعال کنید:

```console
--enable-bootstrap-token-auth=true
```

#### فایل احراز هویت توکن {#token-authentication-file}

kube-apiserver توانایی پذیرش توکن‌ها برای احراز هویت را دارد.
این توکن‌ها دلخواه هستند، اما باید دست‌کم ۱۲۸ بیت آنتروپی داشته باشند که از یک
مولد اعداد تصادفی امن (مانند `/dev/urandom` در بیشتر سیستم‌های مدرن
لینوکس) به‌دست آمده باشد. راه‌های مختلفی برای تولید توکن وجود دارد. برای مثال:

```shell
head -c 16 /dev/urandom | od -An -t x | tr -d ' '
```

این دستور توکن‌هایی شبیه `02b50b05283e98dd0fd71db496ef01e8` تولید می‌کند.

فایل توکن باید مشابه مثال زیر باشد، که در آن سه مقدار اول
می‌توانند هر چیزی باشند و نام گروهِ داخل گیومه باید دقیقاً به همین شکل باشد:

```console
02b50b05283e98dd0fd71db496ef01e8,kubelet-bootstrap,10001,"system:bootstrappers"
```

برای فعال‌سازی فایل توکن، پرچم `--token-auth-file=FILENAME` را به فرمان kube-apiserver (شاید در
فایل واحد systemd خود) اضافه کنید. برای جزئیات بیشتر، مستندات
[اینجا](/docs/reference/access-authn-authz/authentication/#static-token-file) را ببینید.

### مجاز کردن kubelet برای ایجاد CSR {#authorize-kubelet-to-create-csr}

اکنون که نود در حال bootstrap به‌عنوان عضوی از گروه
`system:bootstrappers` _احراز هویت_ شده است، باید _مجاز_ شود که یک
درخواست امضای گواهی (CSR) ایجاد کند و پس از اتمام کار آن را بازیابی کند.
خوشبختانه کوبرنتیز با یک `ClusterRole` عرضه می‌شود که دقیقاً همین مجوزها (و
فقط همین‌ها) را دارد، یعنی `system:node-bootstrapper`.

برای این کار، فقط لازم است یک `ClusterRoleBinding` ایجاد کنید که گروه `system:bootstrappers`
را به نقش کلاستری `system:node-bootstrapper` متصل کند.

```yaml
# enable bootstrapping nodes to create CSR
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: create-csrs-for-bootstrapping
subjects:
- kind: Group
  name: system:bootstrappers
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: system:node-bootstrapper
  apiGroup: rbac.authorization.k8s.io
```

## پیکربندی kube-controller-manager {#kube-controller-manager-configuration}

درحالی‌که apiserver درخواست‌های گواهی را از kubelet دریافت می‌کند و آن درخواست‌ها را احراز هویت می‌کند،
controller-manager مسئول صدور گواهی‌های امضاشده‌ی واقعی است.

controller-manager این وظیفه را از طریق یک حلقه‌ی کنترلی صدور گواهی انجام می‌دهد.
این کار به شکل یک امضاکننده‌ی محلی
[cfssl](https://blog.cloudflare.com/introducing-cfssl/) و با استفاده از
دارایی‌های روی دیسک انجام می‌شود. در حال حاضر، همه‌ی گواهی‌های صادرشده یک سال اعتبار دارند و
مجموعه‌ی پیش‌فرضی از کاربردهای کلید (key usages) دارند.

برای اینکه controller-manager بتواند گواهی‌ها را امضا کند، به موارد زیر نیاز دارد:

* دسترسی به «کلید و گواهی CA کوبرنتیز» که ایجاد و توزیع کرده‌اید
* فعال‌سازی امضای CSR

### دسترسی به کلید و گواهی {#access-to-key-and-certificate}

همان‌طور که پیش‌تر شرح داده شد، باید یک کلید و گواهی CA کوبرنتیز ایجاد کنید و آن را به نودهای control plane توزیع کنید.
controller-manager از این‌ها برای امضای گواهی‌های kubelet استفاده می‌کند.

از آنجا که این گواهی‌های امضاشده به‌نوبه‌ی خود توسط kubelet برای احراز هویت به‌عنوان یک kubelet عادی
نزد kube-apiserver استفاده می‌شوند، مهم است که CA ارائه‌شده به controller-manager در این مرحله،
مورد اعتماد kube-apiserver برای احراز هویت نیز باشد. این CA با پرچم `--client-ca-file=FILENAME`
(برای مثال، `--client-ca-file=/var/lib/kubernetes/ca.pem`) به kube-apiserver داده می‌شود، همان‌طور که در بخش پیکربندی kube-apiserver شرح داده شد.

برای ارائه‌ی کلید و گواهی CA کوبرنتیز به kube-controller-manager، از پرچم‌های زیر استفاده کنید:

```shell
--cluster-signing-cert-file="/etc/path/to/kubernetes/ca/ca.crt" --cluster-signing-key-file="/etc/path/to/kubernetes/ca/ca.key"
```

برای مثال:

```shell
--cluster-signing-cert-file="/var/lib/kubernetes/ca.pem" --cluster-signing-key-file="/var/lib/kubernetes/ca-key.pem"
```

مدت اعتبار گواهی‌های امضاشده را می‌توان با پرچم زیر پیکربندی کرد:

```shell
--cluster-signing-duration
```

### تأیید {#approval}

برای تأیید CSRها، باید به controller-manager اعلام کنید که تأیید آن‌ها مجاز است. این کار با اعطای
مجوزهای RBAC به گروه صحیح انجام می‌شود.

دو مجموعه‌ی مجوز متمایز وجود دارد:

* `nodeclient`: اگر نودی در حال ایجاد گواهی جدید برای یک نود است، هنوز گواهی ندارد.
  این نود با یکی از توکن‌های ذکرشده در بالا احراز هویت می‌کند و بنابراین عضوی از گروه `system:bootstrappers` است.
* `selfnodeclient`: اگر نودی در حال تمدید گواهی خود است، (طبق تعریف) از قبل گواهی دارد
  و از آن به‌طور مداوم برای احراز هویت به‌عنوان عضوی از گروه `system:nodes` استفاده می‌کند.

برای اینکه kubelet بتواند گواهی جدید درخواست کند و دریافت نماید، یک `ClusterRoleBinding` ایجاد کنید که
گروهی را که نود در حال bootstrap عضو آن است، یعنی `system:bootstrappers`، به `ClusterRole‌ای` که
این مجوز را به آن می‌دهد، یعنی `system:certificates.k8s.io:certificatesigningrequests:nodeclient`، متصل کند:

```yaml
# Approve all CSRs for the group "system:bootstrappers"
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: auto-approve-csrs-for-group
subjects:
- kind: Group
  name: system:bootstrappers
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: system:certificates.k8s.io:certificatesigningrequests:nodeclient
  apiGroup: rbac.authorization.k8s.io
```

برای اینکه kubelet بتواند گواهی کلاینت خود را تمدید کند، یک `ClusterRoleBinding` ایجاد کنید که
گروهی را که نود کاملاً فعال عضو آن است، یعنی `system:nodes`، به `ClusterRole‌ای` که
این مجوز را به آن می‌دهد، یعنی `system:certificates.k8s.io:certificatesigningrequests:selfnodeclient`، متصل کند:

```yaml
# Approve renewal CSRs for the group "system:nodes"
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: auto-approve-renewals-for-nodes
subjects:
- kind: Group
  name: system:nodes
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: system:certificates.k8s.io:certificatesigningrequests:selfnodeclient
  apiGroup: rbac.authorization.k8s.io
```

کنترل‌کننده‌ی `csrapproving` که به‌عنوان بخشی از
[kube-controller-manager](/docs/reference/command-line-tools-reference/kube-controller-manager/) عرضه می‌شود، به‌طور پیش‌فرض
فعال است. این کنترل‌کننده از
[API ‏`SubjectAccessReview`](/docs/reference/access-authn-authz/authorization/#checking-api-access) استفاده می‌کند تا
تعیین کند آیا یک کاربر مشخص مجاز به درخواست CSR است یا خیر، و سپس بر اساس
نتیجه‌ی مجوزدهی، تأیید را انجام می‌دهد. برای جلوگیری از تداخل با سایر تأییدکننده‌ها،
تأییدکننده‌ی توکار CSRها را صراحتاً رد نمی‌کند و فقط درخواست‌های
غیرمجاز را نادیده می‌گیرد. این کنترل‌کننده همچنین گواهی‌های منقضی‌شده را به‌عنوان بخشی از
زباله‌روبی (garbage collection) پاک‌سازی می‌کند.

## پیکربندی kubelet

سرانجام، پس از آنکه نودهای control plane به‌درستی راه‌اندازی شدند و تمام احراز هویت و مجوزدهی لازم برقرار شد، می‌توانیم kubelet را پیکربندی کنیم.

kubelet برای انجام bootstrap به پیکربندی زیر نیاز دارد:

* مسیری برای ذخیره‌سازی کلید و گواهی‌ای که تولید می‌کند (اختیاری، می‌توان از مقدار پیش‌فرض استفاده کرد)
* مسیری به یک فایل `kubeconfig` که هنوز وجود ندارد؛ kubelet فایل پیکربندی bootstrap‌شده را در این مسیر قرار می‌دهد
* مسیری به یک فایل `kubeconfig` برای bootstrap که نشانی سرور و اعتبارنامه‌های bootstrap، برای مثال یک توکن bootstrap، را فراهم می‌کند
* اختیاری: دستورالعمل‌هایی برای چرخش (rotation) گواهی‌ها

فایل `kubeconfig` مربوط به bootstrap باید در مسیری قرار داشته باشد که برای kubelet در دسترس است، برای مثال `/var/lib/kubelet/bootstrap-kubeconfig`.

قالب آن با یک فایل `kubeconfig` معمولی یکسان است. یک فایل نمونه می‌تواند به شکل زیر باشد:

```yaml
apiVersion: v1
kind: Config
clusters:
- cluster:
    certificate-authority: /var/lib/kubernetes/ca.pem
    server: https://my.server.example.com:6443
  name: bootstrap
contexts:
- context:
    cluster: bootstrap
    user: kubelet-bootstrap
  name: bootstrap
current-context: bootstrap
preferences: {}
users:
- name: kubelet-bootstrap
  user:
    token: 07401b.f395accd246ae52d
```

نکات مهمی که باید به آن‌ها توجه کرد عبارت‌اند از:

* `certificate-authority`: مسیر یک فایل CA که برای اعتبارسنجی گواهی سروری که kube-apiserver ارائه می‌دهد استفاده می‌شود
* `server`: نشانی URL مربوط به kube-apiserver
* `token`: توکنی که باید استفاده شود

قالب توکن اهمیتی ندارد، به شرط آنکه با آنچه kube-apiserver انتظار دارد مطابقت داشته باشد. در مثال بالا از یک توکن bootstrap استفاده کردیم.
همان‌طور که پیش‌تر گفته شد، _هر_ روش احراز هویت معتبری را می‌توان به کار برد، نه فقط توکن‌ها.

از آنجا که `kubeconfig` مربوط به bootstrap _خود_ یک `kubeconfig` استاندارد است، می‌توانید برای تولید آن از `kubectl` استفاده کنید. برای ایجاد فایل نمونه بالا:

```
kubectl config --kubeconfig=/var/lib/kubelet/bootstrap-kubeconfig set-cluster bootstrap --server='https://my.server.example.com:6443' --certificate-authority=/var/lib/kubernetes/ca.pem
kubectl config --kubeconfig=/var/lib/kubelet/bootstrap-kubeconfig set-credentials kubelet-bootstrap --token=07401b.f395accd246ae52d
kubectl config --kubeconfig=/var/lib/kubelet/bootstrap-kubeconfig set-context bootstrap --user=kubelet-bootstrap --cluster=bootstrap
kubectl config --kubeconfig=/var/lib/kubelet/bootstrap-kubeconfig use-context bootstrap
```

برای آنکه به kubelet اعلام کنید از `kubeconfig` مربوط به bootstrap استفاده کند، از فلگ‌های kubelet زیر استفاده کنید:

```
--bootstrap-kubeconfig="/var/lib/kubelet/bootstrap-kubeconfig" --kubeconfig="/var/lib/kubelet/kubeconfig"
```

هنگام راه‌اندازی kubelet، اگر فایلی که با `--kubeconfig` مشخص شده وجود نداشته باشد، از kubeconfig مربوط به bootstrap که با `--bootstrap-kubeconfig` مشخص شده است برای درخواست یک گواهی کلاینت از API server استفاده می‌شود. پس از تأیید درخواست گواهی و دریافت آن توسط kubelet، یک فایل kubeconfig که به کلید تولیدشده و گواهی دریافت‌شده ارجاع می‌دهد، در مسیر مشخص‌شده با `--kubeconfig` نوشته می‌شود. فایل‌های گواهی و کلید در دایرکتوری مشخص‌شده با `--cert-dir` قرار می‌گیرند.

### گواهی‌های کلاینت و سرویس‌دهی {#client-and-serving-certificates}

همه موارد بالا به گواهی‌های _کلاینت_ kubelet مربوط می‌شوند، به‌طور مشخص گواهی‌هایی که kubelet برای احراز هویت نزد kube-apiserver از آن‌ها استفاده می‌کند.

kubelet همچنین می‌تواند از گواهی‌های _سرویس‌دهی_ (serving) استفاده کند. خود kubelet برای برخی قابلیت‌ها یک endpoint از نوع https در دسترس قرار می‌دهد.
برای ایمن‌سازی این endpointها، kubelet می‌تواند یکی از کارهای زیر را انجام دهد:

* استفاده از کلید و گواهی فراهم‌شده، از طریق فلگ‌های `--tls-private-key-file` و `--tls-cert-file`
* ایجاد کلید و گواهی خودامضا، در صورتی که کلید و گواهی فراهم نشده باشند
* درخواست گواهی‌های سرویس‌دهی از سرور کلاستر، از طریق CSR API

گواهی کلاینتی که توسط TLS bootstrapping ارائه می‌شود، به‌طور پیش‌فرض فقط برای `client auth` امضا می‌شود و بنابراین نمی‌توان از آن به‌عنوان گواهی سرویس‌دهی، یا `server auth`، استفاده کرد.

با این حال، شما _می‌توانید_ گواهی سرور آن را، دست‌کم تا حدی، از طریق چرخش گواهی فعال کنید.

### چرخش گواهی (Certificate rotation) {#certificate-rotation}

kubelet در کوبرنتیز نسخه 1.8 و بالاتر قابلیت‌هایی را برای فعال‌سازی چرخش گواهی‌های کلاینت و/یا سرویس‌دهی خود پیاده‌سازی می‌کند. توجه کنید که چرخش گواهی سرویس‌دهی یک قابلیت **بتا** است و به feature flag با نام `RotateKubeletServerCertificate` روی kubelet نیاز دارد (که به‌طور پیش‌فرض فعال است).

می‌توانید kubelet را طوری پیکربندی کنید که با منقضی شدن اعتبارنامه‌های موجود خود، با ایجاد CSRهای جدید گواهی‌های کلاینت خود را بچرخاند. برای فعال‌سازی این قابلیت، از فیلد `rotateCertificates` در [فایل پیکربندی kubelet](/docs/tasks/administer-cluster/kubelet-config-file/) استفاده کنید
یا آرگومان خط فرمان زیر را به kubelet بدهید (منسوخ‌شده):

```
--rotate-certificates
```

فعال کردن `RotateKubeletServerCertificate` باعث می‌شود kubelet **هم** پس از bootstrap اعتبارنامه‌های کلاینت خود، یک گواهی سرویس‌دهی درخواست کند **و هم** آن گواهی را بچرخاند. برای فعال‌سازی این رفتار، از فیلد `serverTLSBootstrap` در [فایل پیکربندی kubelet](/docs/tasks/administer-cluster/kubelet-config-file/) استفاده کنید
یا آرگومان خط فرمان زیر را به kubelet بدهید (منسوخ‌شده):

```
--rotate-server-certificates
```

{{< note >}}
کنترل‌کننده‌های تأییدکننده CSR که در هسته کوبرنتیز پیاده‌سازی شده‌اند، به [دلایل امنیتی](https://github.com/kubernetes/community/pull/1982) گواهی‌های _سرویس‌دهی_ نود را تأیید نمی‌کنند. برای استفاده از `RotateKubeletServerCertificate`، اپراتورها باید یک کنترل‌کننده تأییدکننده سفارشی اجرا کنند یا درخواست‌های گواهی سرویس‌دهی را به‌صورت دستی تأیید کنند.

یک فرایند تأیید مختص هر استقرار برای گواهی‌های سرویس‌دهی kubelet باید معمولاً فقط CSRهایی را تأیید کند که:

1. توسط نودها درخواست شده باشند (اطمینان حاصل کنید فیلد `spec.username` به شکل
   `system:node:<nodeName>` باشد و `spec.groups` شامل `system:nodes` باشد)
1. کاربردهای (usages) یک گواهی سرویس‌دهی را درخواست کنند (اطمینان حاصل کنید `spec.usages` شامل `server auth` باشد،
   به‌صورت اختیاری شامل `digital signature` و `key encipherment` باشد، و هیچ کاربرد دیگری نداشته باشد)
1. فقط subjectAltNameهای IP و DNS داشته باشند که متعلق به نود درخواست‌کننده هستند،
   و هیچ subjectAltName از نوع URI و Email نداشته باشند (برای راستی‌آزمایی `subjectAltNames`، درخواست امضای گواهی x509 را
   در `spec.request` تجزیه کنید)

{{< /note >}}

## سایر مؤلفه‌های احراز هویت‌کننده {#other-authenticating-components}

تمام TLS bootstrapping که در این سند شرح داده شد به kubelet مربوط است. با این حال، ممکن است مؤلفه‌های دیگر نیز نیاز داشته باشند مستقیماً با kube-apiserver ارتباط برقرار کنند. نمونه شاخص آن kube-proxy است که بخشی از مؤلفه‌های نود کوبرنتیز است و روی هر نود اجرا می‌شود، اما ممکن است مؤلفه‌های دیگری مانند مؤلفه‌های پایش یا شبکه را نیز شامل شود.

مانند kubelet، این مؤلفه‌های دیگر نیز به روشی برای احراز هویت نزد kube-apiserver نیاز دارند.
برای تولید این اعتبارنامه‌ها چند گزینه پیش رو دارید:

* روش قدیمی: گواهی‌ها را به همان شیوه‌ای ایجاد و توزیع کنید که پیش از TLS bootstrapping برای kubelet انجام می‌دادید
* DaemonSet: از آنجا که خود kubelet روی هر نود بارگذاری می‌شود و برای راه‌اندازی سرویس‌های پایه کافی است،
  می‌توانید kube-proxy و سایر سرویس‌های مختص نود را نه به‌صورت یک فرایند مستقل، بلکه به‌صورت یک
  DaemonSet در فضای نام (namespace) `kube-system` اجرا کنید. از آنجا که درون کلاستر خواهد بود، می‌توانید یک service
  account مناسب با مجوزهای لازم برای انجام فعالیت‌هایش به آن بدهید. این ممکن است ساده‌ترین روش برای پیکربندی
  چنین سرویس‌هایی باشد.

## تأیید با kubectl {#kubectl-approval}

CSRها را می‌توان خارج از جریان‌های تأییدی که در controller manager تعبیه شده‌اند نیز تأیید کرد.

کنترل‌کننده امضاکننده (signing controller) بلافاصله همه درخواست‌های گواهی را امضا نمی‌کند.
در عوض، منتظر می‌ماند تا یک کاربر دارای سطح دسترسی مناسب آن‌ها را با وضعیت «Approved» علامت‌گذاری کند. هدف از این جریان آن است که امکان تأیید خودکار توسط یک کنترل‌کننده تأییدکننده خارجی یا کنترل‌کننده تأییدکننده‌ای که در controller-manager هسته پیاده‌سازی شده است فراهم شود. با این حال، مدیران کلاستر
می‌توانند درخواست‌های گواهی را به‌صورت دستی نیز با kubectl تأیید کنند. مدیر می‌تواند
CSRها را با `kubectl get csr` فهرست کند و یکی را با
`kubectl describe csr <name>` به‌طور کامل شرح دهد. مدیر می‌تواند یک CSR را با
`kubectl certificate approve <name>` و `kubectl certificate deny <name>` تأیید یا رد کند.
