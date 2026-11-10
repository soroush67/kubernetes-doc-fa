---
title: زبان Common Expression Language در کوبرنتیز
reviewers:
- jpbetz
- cici37
content_type: concept
weight: 35
min-kubernetes-server-version: 1.25
---

<!-- overview -->

در API کوبرنتیز از [زبان Common Expression Language (CEL)](https://github.com/google/cel-go)
برای تعریف قواعد اعتبارسنجی، قواعد سیاست‌ها و سایر محدودیت‌ها یا شرط‌ها استفاده می‌شود.

عبارت‌های CEL مستقیماً در
{{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}} ارزیابی می‌شوند. به همین دلیل،
CEL در بسیاری از کاربردهای توسعه‌پذیری، جایگزین مناسبی برای سازوکارهای خارج از فرایند مانند
وب‌هوک‌ها (webhooks) است. عبارت‌های CEL شما تا زمانی که مؤلفه سرور API در control plane در دسترس
باشد، همچنان اجرا می‌شوند.

<!-- body -->

## مروری بر زبان

[زبان CEL](https://github.com/google/cel-spec/blob/master/doc/langdef.md)
نحو ساده‌ای دارد که به عبارت‌ها در زبان‌های C، C++، Java، JavaScript و Go شباهت دارد.

زبان CEL برای جاسازی در برنامه‌ها طراحی شده است. هر «برنامه» CEL یک عبارت واحد است که
به یک مقدار واحد ارزیابی می‌شود. عبارت‌های CEL معمولاً کوتاه و «تک‌خطی» هستند و به‌خوبی
در فیلدهای رشته‌ای منابع API کوبرنتیز جای می‌گیرند.

ورودی‌های یک برنامه CEL «متغیرها» هستند. هر فیلد API کوبرنتیز که حاوی CEL است، در مستندات
API مشخص می‌کند که چه متغیرهایی برای استفاده در آن فیلد در دسترس‌اند. برای مثال، در فیلد
`x-kubernetes-validations[i].rules` از CustomResourceDefinitionها، متغیرهای `self` و `oldSelf`
در دسترس هستند و به وضعیت قبلی و فعلی داده‌های منبع سفارشی اشاره می‌کنند که عبارت CEL
باید آن‌ها را اعتبارسنجی کند. سایر فیلدهای API کوبرنتیز ممکن است متغیرهای متفاوتی تعریف
کنند. برای اینکه بدانید کدام متغیرها برای یک فیلد در دسترس‌اند، به مستندات API آن فیلد
مراجعه کنید.

نمونه‌هایی از عبارت‌های CEL:

<table>
<caption>نمونه‌هایی از عبارت‌های CEL و هدف هر کدام</caption>
<thead>
<tr>
  <th>قاعده</th>
  <th>هدف</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>self.minReplicas &lt;= self.replicas && self.replicas &lt;= self.maxReplicas</tt></td>
  <td>اعتبارسنجی می‌کند که سه فیلدی که تعداد رپلیکاها را تعیین می‌کنند، ترتیب درستی داشته باشند</td>
</tr>
<tr>
  <td><tt>'Available' in self.stateCounts</tt></td>
  <td>اعتبارسنجی می‌کند که در یک map، ورودی‌ای با کلید 'Available' وجود داشته باشد</td>
</tr>
<tr>
  <td><tt>(self.list1.size() == 0) != (self.list2.size() == 0)</tt></td>
  <td>اعتبارسنجی می‌کند که یکی از دو لیست غیرخالی باشد، اما نه هر دو</td>
</tr>
<tr>
  <td><tt>self.envars.filter(e, e.name = 'MY_ENV').all(e, e.value.matches('^[a-zA-Z]*$'))</tt></td>
  <td>فیلد 'value' را در آن ورودی از listMap که فیلد کلید 'name' آن برابر 'MY_ENV' است، اعتبارسنجی می‌کند</td>
</tr>
<tr>
  <td><tt>has(self.expired) && self.created + self.ttl &lt; self.expired</tt></td>
  <td>اعتبارسنجی می‌کند که تاریخ 'expired' پس از تاریخ 'create' به‌علاوه مدت‌زمان 'ttl' باشد</td>
</tr>
<tr>
  <td><tt>self.health.startsWith('ok')</tt></td>
  <td>اعتبارسنجی می‌کند که فیلد رشته‌ای 'health' پیشوند 'ok' داشته باشد</td>
</tr>
<tr>
  <td><tt>self.widgets.exists(w, w.key == 'x' && w.foo &lt; 10)</tt></td>
  <td>اعتبارسنجی می‌کند که ویژگی 'foo' در آیتمی از listMap که کلید آن 'x' است، کمتر از 10 باشد</td>
</tr>
<tr>
  <td><tt>type(self) == string ? self == '99%' : self == 42</tt></td>
  <td>یک فیلد از نوع int-or-string را در هر دو حالت عدد صحیح و رشته اعتبارسنجی می‌کند</td>
</tr>
<tr>
  <td><tt>self.metadata.name == 'singleton'</tt></td>
  <td>اعتبارسنجی می‌کند که نام یک آبجکت با مقدار مشخصی مطابقت داشته باشد (و در نتیجه آن آبجکت یکتا یا singleton باشد)</td>
</tr>
<tr>
  <td><tt>self.set1.all(e, !(e in self.set2))</tt></td>
  <td>اعتبارسنجی می‌کند که دو listSet هیچ عضو مشترکی نداشته باشند</td>
</tr>
<tr>
  <td><tt>self.names.size() == self.details.size() && self.names.all(n, n in self.details)</tt></td>
  <td>اعتبارسنجی می‌کند که کلیدهای map با نام 'details' همان آیتم‌های listSet با نام 'names' باشند</td>
</tr>
<tr>
  <td><tt>self.details.all(key, key.matches('^[a-zA-Z]*$'))</tt></td>
  <td>کلیدهای map با نام 'details' را اعتبارسنجی می‌کند</td>
</tr>
<tr>
  <td><tt>self.details.all(key, self.details[key].matches('^[a-zA-Z]*$'))</tt></td>
  <td>مقادیر map با نام 'details' را اعتبارسنجی می‌کند</td>
</tr>
</tbody>
</table>

## گزینه‌ها، قابلیت‌های زبانی و کتابخانه‌های CEL

زبان CEL با گزینه‌ها، کتابخانه‌ها و قابلیت‌های زبانی زیر پیکربندی شده است که هر کدام در
نسخه مشخص‌شده‌ای از کوبرنتیز معرفی شده‌اند:

<table>
<thead>
<tr>
  <th>گزینه، کتابخانه یا قابلیت زبانی CEL</th>
  <th>موارد شامل‌شده</th>
  <th>دسترس‌پذیری</th>
</tr>
</thead>
<tbody>
<tr>
  <td><a href="https://github.com/google/cel-spec/blob/v0.7.0/doc/langdef.md#macros">ماکروهای استاندارد</a></td>
  <td><code>has</code>, <code>all</code>, <code>exists</code>, <code>exists_one</code>, <code>map</code>, <code>filter</code></td>
  <td>همه نسخه‌های کوبرنتیز</td>
</tr>
<tr>
  <td><a href="https://github.com/google/cel-spec/blob/master/doc/langdef.md#list-of-standard-definitions">توابع استاندارد</a></td>
  <td>به
    <a href="https://github.com/google/cel-spec/blob/master/doc/langdef.md#list-of-standard-definitions">
      فهرست رسمی تعریف‌های استاندارد
    </a>
    مراجعه کنید
  </td>
  <td>همه نسخه‌های کوبرنتیز</td>
</tr>
<tr>
  <td>
    <a href="https://pkg.go.dev/github.com/google/cel-go@v0.17.4/cel#HomogeneousAggregateLiterals">
      لیترال‌های تجمیعی همگن
    </a>
  </td>
  <td>-</td>
  <td>همه نسخه‌های کوبرنتیز</td>
</tr>
<tr>
  <td><a href="https://pkg.go.dev/github.com/google/cel-go@v0.17.4/cel#DefaultUTCTimeZone">منطقه زمانی پیش‌فرض UTC</a></td>
  <td>-</td>
  <td>همه نسخه‌های کوبرنتیز</td>
</tr>
<tr>
  <td>
    <a href="https://pkg.go.dev/github.com/google/cel-go@v0.17.4/cel#EagerlyValidateDeclarations">
      اعتبارسنجی زودهنگام اعلان‌ها
    </a>
  </td>
  <td>-</td>
  <td>همه نسخه‌های کوبرنتیز</td>
</tr>
<tr>
  <td><a href="https://pkg.go.dev/github.com/google/cel-go/ext#Strings">کتابخانه توسعه‌یافته رشته‌ها</a>، نسخه 1</td>
  <td>
    <code>charAt</code>, <code>indexOf</code>, <code>lastIndexOf</code>, <code>lowerAscii</code>,
    <code>upperAscii</code>, <code>replace</code>, <code>split</code>, <code>join</code>, <code>substring</code>,
    <code>trim</code>
  </td>
  <td>نسخه‌های 1.25 تا 1.30 کوبرنتیز</td>
</tr>
<tr>
  <td><a href="https://pkg.go.dev/github.com/google/cel-go/ext#Strings">کتابخانه توسعه‌یافته رشته‌ها</a>، نسخه 2</td>
  <td>
    <code>charAt</code>, <code>indexOf</code>, <code>lastIndexOf</code>, <code>lowerAscii</code>,
    <code>upperAscii</code>, <code>replace</code>, <code>split</code>, <code>join</code>, <code>substring</code>,
    <code>trim</code>
  </td>
  <td>نسخه 1.30 کوبرنتیز و بالاتر</td>
</tr>
<tr>
  <td>کتابخانه لیست کوبرنتیز</td>
  <td>به
    <a href="#kubernetes-list-library">
      کتابخانه لیست کوبرنتیز
    </a>
    مراجعه کنید
  </td>
  <td>همه نسخه‌های کوبرنتیز</td>
</tr>
<tr>
  <td>کتابخانه عبارت‌های منظم (regex) کوبرنتیز</td>
  <td>به
    <a href="#kubernetes-regex-library">
      کتابخانه regex کوبرنتیز
    </a>
    مراجعه کنید
  </td>
  <td>همه نسخه‌های کوبرنتیز</td>
</tr>
<tr>
  <td>کتابخانه URL کوبرنتیز</td>
  <td>به
    <a href="#kubernetes-url-library">
      کتابخانه URL کوبرنتیز
    </a>
    مراجعه کنید
  </td>
  <td>همه نسخه‌های کوبرنتیز</td>
</tr>
<tr>
  <td>کتابخانه آدرس IP کوبرنتیز</td>
  <td>به
    <a href="#kubernetes-ip-address-library">
      کتابخانه آدرس IP کوبرنتیز
    </a>
    مراجعه کنید
  </td>
  <td>نسخه 1.31 کوبرنتیز و بالاتر</td>
</tr>
<tr>
  <td>کتابخانه CIDR کوبرنتیز</td>
  <td>به
    <a href="#kubernetes-cidr-library">
      کتابخانه CIDR کوبرنتیز
    </a>
    مراجعه کنید
  </td>
  <td>نسخه 1.31 کوبرنتیز و بالاتر</td>
</tr>
<tr>
<tr>
  <td>کتابخانه مجوزدهنده (authorizer) کوبرنتیز</td>
  <td>به
    <a href="#kubernetes-authorizer-library">
      کتابخانه authorizer کوبرنتیز
    </a>
    مراجعه کنید
  </td>
  <td>همه نسخه‌های کوبرنتیز</td>
</tr>
<tr>
  <td>کتابخانه کمیت (quantity) کوبرنتیز</td>
  <td>به
    <a href="#kubernetes-quantity-library">
      کتابخانه quantity کوبرنتیز
    </a>
    مراجعه کنید
  </td>
  <td>نسخه 1.29 کوبرنتیز و بالاتر</td>
</tr>
<tr>
  <td>کتابخانه semver کوبرنتیز</td>
  <td>به
    <a href="#kubernetes-semver-library">
      کتابخانه semver کوبرنتیز
    </a>
    مراجعه کنید
  </td>
  <td>نسخه 1.34 کوبرنتیز و بالاتر</td>
</tr>
<tr>
  <td>کتابخانه قالب (format) کوبرنتیز</td>
  <td>به
    <a href="#kubernetes-format-library">
      کتابخانه format کوبرنتیز
    </a>
    مراجعه کنید
  </td>
  <td>نسخه 1.32 کوبرنتیز و بالاتر</td>
</tr>
<tr>
  <td>انواع اختیاری CEL</td>
  <td>به
    <a href="https://pkg.go.dev/github.com/google/cel-go@v0.17.4/cel#OptionalTypes">
      انواع اختیاری CEL
    </a>
    مراجعه کنید
  </td>
  <td>نسخه 1.29 کوبرنتیز و بالاتر</td>
</tr>
<tr>
  <td>قابلیت CrossTypeNumericComparisons در CEL</td>
  <td>به
    <a href="https://pkg.go.dev/github.com/google/cel-go@v0.17.4/cel#CrossTypeNumericComparisons">
      CrossTypeNumericComparisons در CEL
   </a>
    مراجعه کنید
  </td>
  <td>نسخه 1.29 کوبرنتیز و بالاتر</td>
<tr>
  <td>قابلیت TwoVarComprehensions در CEL</td>
  <td>به
    <a href="https://pkg.go.dev/github.com/google/cel-go@v0.25.0/ext#readme-twovarcomprehensions">
      TwoVarComprehensions در CEL
   </a>
    مراجعه کنید
  </td>
  <td>نسخه 1.33 کوبرنتیز و بالاتر</td>
</tr>
</tbody>
</table>

توابع، قابلیت‌ها و تنظیمات زبانی CEL از بازگردانی (rollback) control plane کوبرنتیز پشتیبانی
می‌کنند. برای مثال، _مقادیر اختیاری CEL_ (CEL Optional Values) در کوبرنتیز 1.29 معرفی شد؛
بنابراین فقط سرورهای API با این نسخه یا نسخه‌های جدیدتر، درخواست‌های نوشتنِ عبارت‌های CEL
را که از _مقادیر اختیاری CEL_ استفاده می‌کنند می‌پذیرند. با این حال، اگر کلاستر به کوبرنتیز
1.28 بازگردانده شود، عبارت‌های CEL که از «مقادیر اختیاری CEL» استفاده می‌کنند و از قبل در
منابع API ذخیره شده‌اند، همچنان به‌درستی ارزیابی می‌شوند.

## کتابخانه‌های CEL کوبرنتیز

کوبرنتیز علاوه بر کتابخانه‌های جامعه CEL، کتابخانه‌های CEL مخصوص به خود را نیز دارد که در
همه جاهایی که CEL در کوبرنتیز استفاده می‌شود، در دسترس هستند.

### کتابخانه لیست کوبرنتیز

کتابخانه لیست شامل توابع `indexOf` و `lastIndexOf` است که مشابه توابع رشته‌ای هم‌نام خود
عمل می‌کنند. این توابع اولین یا آخرین اندیس موقعیتیِ عنصر داده‌شده را در لیست برمی‌گردانند.

کتابخانه لیست همچنین توابع `min`، `max` و `sum` را در بر دارد. تابع sum روی همه انواع عددی
و همچنین نوع duration پشتیبانی می‌شود. توابع min و max روی همه انواع قابل مقایسه پشتیبانی
می‌شوند.

تابع `isSorted` نیز به‌عنوان یک تابع کمکی ارائه شده است و روی همه انواع قابل مقایسه
پشتیبانی می‌شود.

نمونه‌ها:

<table>
<caption>نمونه‌هایی از عبارت‌های CEL که از توابع کتابخانه لیست استفاده می‌کنند</caption>
<thead>
<tr>
  <td>عبارت CEL</td>
  <td>هدف</td>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>names.isSorted()</tt></td>
  <td>بررسی می‌کند که لیستی از نام‌ها به ترتیب الفبایی نگه داشته شده باشد</td>
</tr>
<tr>
  <td><tt>items.map(x, x.weight).sum() == 1.0</tt></td>
  <td>بررسی می‌کند که مجموع «وزن‌های» لیستی از آبجکت‌ها برابر 1.0 باشد</td>
</tr>
<tr>
  <td><tt>lowPriorities.map(x, x.priority).max() &lt; highPriorities.map(x, x.priority).min()</tt></td>
  <td>بررسی می‌کند که دو مجموعه از اولویت‌ها با هم هم‌پوشانی نداشته باشند</td>
</tr>
<tr>
  <td><tt>names.indexOf('should-be-first') == 1</tt></td>
  <td>الزام می‌کند که اولین نام در یک لیست مقدار مشخصی باشد</td>
</tr>
</tbody>
</table>

برای اطلاعات بیشتر، به godoc
[کتابخانه لیست کوبرنتیز](https://pkg.go.dev/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/library#Lists)
مراجعه کنید.

### کتابخانه regex کوبرنتیز

کتابخانه regex علاوه بر تابع `matches` که کتابخانه استاندارد CEL ارائه می‌کند، توابع `find`
و `findAll` را نیز فراهم می‌کند و به این ترتیب، طیف بسیار گسترده‌تری از عملیات regex را ممکن
می‌سازد.

نمونه‌ها:

<table>
<caption>نمونه‌هایی از عبارت‌های CEL که از توابع کتابخانه regex استفاده می‌کنند</caption>
<thead>
<tr>
  <td>عبارت CEL</td>
  <td>هدف</td>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>"abc 123".find('[0-9]+')</tt></td>
  <td>اولین عدد موجود در یک رشته را پیدا می‌کند</td>
</tr>
<tr>
  <td><tt>"1, 2, 3, 4".findAll('[0-9]+').map(x, int(x)).sum() &lt; 100</tt></td>
  <td>بررسی می‌کند که مجموع اعداد موجود در یک رشته کمتر از 100 باشد</td>
</tr>
</tbody>
</table>

برای اطلاعات بیشتر، به godoc
[کتابخانه regex کوبرنتیز](https://pkg.go.dev/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/library#Regex)
مراجعه کنید.

### کتابخانه URL کوبرنتیز

برای اینکه پردازش URLها آسان‌تر و امن‌تر شود، توابع زیر اضافه شده‌اند:

- تابع `isURL(string)` بررسی می‌کند که آیا یک رشته طبق بسته
  [net/url در Go](https://pkg.go.dev/net/url#URL) یک URL معتبر است یا نه. این رشته باید یک
  URL مطلق باشد.
- تابع `url(string) URL` یک رشته را به URL تبدیل می‌کند و اگر رشته یک URL معتبر نباشد،
  خطا برمی‌گرداند.

پس از تجزیه با تابع `url`، آبجکت URL حاصل دسترسی‌دهنده‌های `getScheme`، `getHost`،
`getHostname`، `getPort`، `getEscapedPath` و `getQuery` را در اختیار می‌گذارد.

نمونه‌ها:

<table>
<caption>نمونه‌هایی از عبارت‌های CEL که از توابع کتابخانه URL استفاده می‌کنند</caption>
<thead>
<tr>
  <td>عبارت CEL</td>
  <td>هدف</td>
</tr>
</thead>
<tbody>
</tr>
<tr>
  <td><tt>url('https://example.com:80/').getHost()</tt></td>
  <td>بخش میزبان URL، یعنی 'example.com:80'، را برمی‌گرداند</td>
</tr>
<tr>
  <td><tt>url('https://example.com/path with spaces/').getEscapedPath()</tt></td>
  <td>مقدار '/path%20with%20spaces/' را برمی‌گرداند</td>
</tr>
</tbody>
</table>

برای اطلاعات بیشتر، به godoc
[کتابخانه URL کوبرنتیز](https://pkg.go.dev/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/library#URLs)
مراجعه کنید.

### کتابخانه آدرس IP کوبرنتیز

برای اینکه پردازش آدرس‌های IP آسان‌تر و امن‌تر شود، توابع زیر اضافه شده‌اند:

- تابع `isIP(string)` بررسی می‌کند که آیا یک رشته آدرس IP معتبری است یا نه.
- تابع `ip(string) IP` یک رشته را به آبجکت آدرس IP تبدیل می‌کند و اگر رشته آدرس IP معتبری نباشد، خطا برمی‌گرداند.

در هر دو تابع، آدرس IP باید یک آدرس IPv4 یا IPv6 باشد.
آدرس‌های IPv6 نگاشت‌شده از IPv4 (مانند `::ffff:1.2.3.4`) مجاز نیستند.
آدرس‌های IP دارای zone (مانند `fe80::1%eth0`) مجاز نیستند.
صفرهای ابتدایی در اکتت‌های آدرس IPv4 مجاز نیستند.

پس از تجزیه با تابع `ip`، آبجکت IP حاصل مجموعه توابع عضو زیر را در اختیار می‌گذارد:

<table>
<caption>توابع عضو در دسترس برای آبجکت آدرس IP</caption>
<thead>
<tr>
  <th>تابع عضو</th>
  <th>مقدار بازگشتی CEL</th>
  <th>توضیحات</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>isCanonical()</tt></td>
  <td>bool</td>
  <td>
    اگر آدرس IP به شکل استاندارد (canonical) خود باشد، true برمی‌گرداند.
    هر آدرس IP دقیقاً یک شکل استاندارد دارد؛ بنابراین فیلدهایی که آدرس‌های IP را به شکل استاندارد
    نگه می‌دارند، هنگام بررسی برابری یا یکتایی می‌توانند صرفاً مانند رشته در نظر گرفته شوند.
  </td>
</tr>
<tr>
  <td><tt>family()</tt></td>
  <td>int</td>
  <td>خانواده آدرس IP را برمی‌گرداند: <tt>4</tt> برای IPv4 و <tt>6</tt> برای IPv6.</td>
</tr>
<tr>
  <td><tt>isUnspecified()</tt></td>
  <td>bool</td>
  <td>
    اگر آدرس IP، آدرس نامشخص (unspecified) باشد، true برمی‌گرداند.
    این آدرس یا آدرس IPv4 برابر "0.0.0.0" است یا آدرس IPv6 برابر "::".
  </td>
</tr>
<tr>
  <td><tt>isLoopback()</tt></td>
  <td>bool</td>
  <td>
    اگر آدرس IP، آدرس loopback باشد، true برمی‌گرداند.
    این آدرس یا یک آدرس IPv4 با مقدار 127.x.x.x است یا یک آدرس IPv6 با مقدار ::1.
  </td>
</tr>
<tr>
  <td><tt>isLinkLocalMulticast()</tt></td>
  <td>bool</td>
  <td>
    اگر آدرس IP یک آدرس multicast از نوع link-local باشد، true برمی‌گرداند.
    این آدرس یا یک آدرس IPv4 با مقدار 224.0.0.x است یا یک آدرس IPv6 در شبکه ff00::/8.
  </td>
</tr>
<tr>
  <td><tt>isLinkLocalUnicast()</tt></td>
  <td>bool</td>
  <td>
    اگر آدرس IP یک آدرس unicast از نوع link-local باشد، true برمی‌گرداند.
    این آدرس یا یک آدرس IPv4 با مقدار 169.254.x.x است یا یک آدرس IPv6 در شبکه fe80::/10.
  </td>
</tr>
<tr>
  <td><tt>isGlobalUnicast()</tt></td>
  <td>bool</td>
  <td>
    اگر آدرس IP یک آدرس unicast سراسری (global) باشد، true برمی‌گرداند.
    این آدرس یا یک آدرس IPv4 است که صفر یا 255.255.255.255 نباشد، یا یک آدرس IPv6 است که آدرس unicast از نوع link-local، loopback یا multicast نباشد.
  </td>
</tr>
</tbody>
</table>

نمونه‌ها:

<table>
<caption>نمونه‌هایی از عبارت‌های CEL که از توابع کتابخانه آدرس IP استفاده می‌کنند</caption>
<thead>
<tr>
  <th>عبارت CEL</th>
  <th>هدف</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>isIP('127.0.0.1')</tt></td>
  <td>برای یک IP معتبر، true برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>ip('2001:db8::abcd').isCanonical()</tt></td>
  <td>برای یک آدرس IPv6 به شکل استاندارد، true برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>ip('2001:DB8::ABCD').isCanonical()</tt></td>
  <td>مقدار false برمی‌گرداند، زیرا شکل استاندارد با حروف کوچک نوشته می‌شود.</td>
</tr>
<tr>
  <td><tt>ip('127.0.0.1').family() == 4</tt></td>
  <td>خانواده آدرس یک IP را بررسی می‌کند.</td>
</tr>
<tr>
  <td><tt>ip('::1').isLoopback()</tt></td>
  <td>بررسی می‌کند که آیا یک IP آدرس loopback است یا نه.</td>
</tr>
<tr>
  <td><tt>ip('192.168.0.1').isGlobalUnicast()</tt></td>
  <td>بررسی می‌کند که آیا یک IP آدرس unicast سراسری است یا نه.</td>
</tr>
</tbody>
</table>

برای اطلاعات بیشتر، به godoc [کتابخانه آدرس IP کوبرنتیز](https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#IP) مراجعه کنید.

### کتابخانهٔ CIDR کوبرنتیز

کتابخانهٔ CIDR یک افزونهٔ کتابخانهٔ توابع CEL است که توابعی برای تجزیهٔ نمادگذاری {{< glossary_tooltip text="CIDR" term_id="CIDR" >}} فراهم می‌کند.

#### `cidr`

این تابع رشته‌ای را که با نمادگذاری CIDR نوشته شده است به نمایشی از یک نشانی شبکه تبدیل می‌کند. اگر رشته نمادگذاری CIDR معتبری نباشد، خطا رخ می‌دهد.
مقدار CIDR باید نشانی یک زیرشبکهٔ IPv4 یا IPv6 همراه با ماسک باشد.
صفرهای ابتدایی در هشتایی‌های (octet) نشانی IPv4 مجاز نیستند.
نشانی‌های IPv6 نگاشته‌شده به IPv4 (مانند `::ffff:1.2.3.4/24`) نیز مجاز نیستند.

<tt>cidr(&lt;string&gt;) &lt;CIDR&gt;</tt>

نمونه‌ها:

<table>
<caption>نمونه‌هایی از عبارت‌های CEL که از تابع cidr استفاده می‌کنند</caption>
<thead>
<tr>
  <th>عبارت CEL</th>
  <th>هدف</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>cidr('192.168.0.0/16')</tt></td>
  <td>یک نشانی IPv4 همراه با ماسک CIDR برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>cidr('::1/128')</tt></td>
  <td>یک نشانی IPv6 همراه با ماسک CIDR برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>cidr('192.168.0.0/33')</tt></td>
  <td>خطا رخ می‌دهد، زیرا طول پیشوند از اندازهٔ نشانی IPv4 بیشتر است.</td>
</tr>
<tr>
  <td><tt>cidr('::1/129')</tt></td>
  <td>خطا رخ می‌دهد، زیرا طول پیشوند از اندازهٔ نشانی IPv6 بیشتر است.</td>
</tr>
<tr>
  <td><tt>cidr('192.168.0.1/16')</tt></td>
  <td>خطا رخ می‌دهد، زیرا پس از پیشوند بیت‌های غیرصفر وجود دارد.</td>
</tr>
</tbody>
</table>

#### `isCIDR`

اگر رشته نمایش معتبری از یک زیرشبکه همراه با ماسک در نمادگذاری CIDR باشد، این تابع مقدار true برمی‌گرداند.
مقدار CIDR باید نشانی یک زیرشبکهٔ IPv4 یا IPv6 همراه با ماسک باشد.
صفرهای ابتدایی در هشتایی‌های نشانی IPv4 مجاز نیستند.
نشانی‌های IPv6 نگاشته‌شده به IPv4 (مانند `::ffff:1.2.3.4/24`) نیز مجاز نیستند.

<tt>isCIDR(&lt;string&gt;) &lt;bool&gt;</tt>

نمونه‌ها:

<table>
<caption>نمونه‌هایی از عبارت‌های CEL که از تابع isCIDR استفاده می‌کنند</caption>
<thead>
<tr>
  <th>عبارت CEL</th>
  <th>هدف</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>isCIDR('192.168.0.0/16')</tt></td>
  <td>برای یک CIDR معتبر IPv4 مقدار true برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>isCIDR('::1/128')</tt></td>
  <td>برای یک CIDR معتبر IPv6 مقدار true برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>isCIDR('192.168.0.0/33')</tt></td>
  <td>مقدار false برمی‌گرداند، زیرا طول پیشوند از اندازهٔ نشانی IPv4 بیشتر است.</td>
</tr>
<tr>
  <td><tt>isCIDR('::1/129')</tt></td>
  <td>مقدار false برمی‌گرداند، زیرا طول پیشوند از اندازهٔ نشانی IPv6 بیشتر است.</td>
</tr>
</tbody>
</table>

#### `containsIP` / `containsCIDR` / `ip` / `masked` / `prefixLength`



- تابع `containsIP`: اگر CIDR نشانی IP داده‌شده را در بر بگیرد، مقدار true برمی‌گرداند.
نشانی IP باید یک نشانی IPv4 یا IPv6 باشد.
این تابع می‌تواند یک رشته یا یک نشانی IP را به‌عنوان آرگومان بپذیرد.

- تابع `containsCIDR`: اگر CIDR، CIDR داده‌شده را در بر بگیرد، مقدار true برمی‌گرداند.
مقدار CIDR باید نشانی یک زیرشبکهٔ IPv4 یا IPv6 همراه با ماسک باشد.
این تابع می‌تواند یک رشته یا یک CIDR را به‌عنوان آرگومان بپذیرد.

- تابع `ip`: نمایش نشانی IP مربوط به CIDR را برمی‌گرداند.

- تابع `masked`: نمایش CIDR نشانی شبکه را همراه با پیشوند ماسک‌شده برمی‌گرداند.
از این تابع می‌توان برای به دست آوردن شکل متعارف شبکهٔ CIDR استفاده کرد.

- تابع `prefixLength`: طول پیشوند CIDR را بر حسب بیت برمی‌گرداند.
این مقدار برابر با تعداد بیت‌های ماسک است.

نمونه‌ها:

<table>
<caption>نمونه‌هایی از عبارت‌های CEL که از توابع کتابخانهٔ CIDR استفاده می‌کنند</caption>
<thead>
<tr>
  <th>عبارت CEL</th>
  <th>هدف</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>cidr('192.168.0.0/24').containsIP(ip('192.168.0.1'))</tt></td>
  <td>بررسی می‌کند که آیا یک CIDR نشانی IP داده‌شده (آبجکت IP) را در بر می‌گیرد یا نه.</td>
</tr>
<tr>
  <td><tt>cidr('192.168.0.0/24').containsIP(ip('192.168.1.1'))</tt></td>
  <td>بررسی می‌کند که آیا یک CIDR نشانی IP داده‌شده (آبجکت IP) را در بر می‌گیرد یا نه.</td>
</tr>
<tr>
  <td><tt>cidr('192.168.0.0/24').containsIP('192.168.0.1')</tt></td>
  <td>بررسی می‌کند که آیا یک CIDR نشانی IP داده‌شده (رشته) را در بر می‌گیرد یا نه.</td>
</tr>
<tr>
  <td><tt>cidr('192.168.0.0/24').containsIP('192.168.1.1')</tt></td>
  <td>بررسی می‌کند که آیا یک CIDR نشانی IP داده‌شده (رشته) را در بر می‌گیرد یا نه.</td>
</tr>
<tr>
  <td><tt>cidr('192.168.0.0/16').containsCIDR(cidr('192.168.10.0/24'))</tt></td>
  <td>بررسی می‌کند که آیا یک CIDR، CIDR داده‌شدهٔ دیگری (آبجکت CIDR) را در بر می‌گیرد یا نه.</td>
</tr>
<tr>
  <td><tt>cidr('192.168.1.0/24').containsCIDR(cidr('192.168.2.0/24'))</tt></td>
  <td>بررسی می‌کند که آیا یک CIDR، CIDR داده‌شدهٔ دیگری (آبجکت CIDR) را در بر می‌گیرد یا نه.</td>
</tr>
<tr>
  <td><tt>cidr('192.168.0.0/16').containsCIDR('192.168.10.0/24')</tt></td>
  <td>بررسی می‌کند که آیا یک CIDR، CIDR داده‌شدهٔ دیگری (رشته) را در بر می‌گیرد یا نه.</td>
</tr>
<tr>
  <td><tt>cidr('192.168.1.0/24').containsCIDR('192.168.2.0/24')</tt></td>
  <td>بررسی می‌کند که آیا یک CIDR، CIDR داده‌شدهٔ دیگری (رشته) را در بر می‌گیرد یا نه.</td>
</tr>
<tr>
  <td><tt>cidr('192.168.0.1/24').ip()</tt></td>
  <td>بخش نشانی IP یک CIDR را برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>cidr('192.168.0.1/24').ip().family()</tt></td>
  <td>خانوادهٔ بخش نشانی IP یک CIDR را برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>cidr('::1/128').ip()</tt></td>
  <td>بخش نشانی IP یک CIDR از نوع IPv6 را برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>cidr('::1/128').ip().family()</tt></td>
  <td>خانوادهٔ بخش نشانی IP یک CIDR از نوع IPv6 را برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>cidr('192.168.0.0/24').masked()</tt></td>
  <td>شکل متعارف یک شبکهٔ CIDR را برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>cidr('192.168.0.1/24').masked()</tt></td>
  <td>شکل متعارف یک شبکهٔ CIDR را با ماسک کردن بیت‌های خارج از پیشوند برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>cidr('192.168.0.0/24') == cidr('192.168.0.0/24').masked()</tt></td>
  <td>یک CIDR را با شکل متعارف آن مقایسه می‌کند (CIDR از قبل متعارف است).</td>
</tr>
<tr>
  <td><tt>cidr('192.168.0.1/24') == cidr('192.168.0.1/24').masked()</tt></td>
  <td>یک CIDR را با شکل متعارف آن مقایسه می‌کند (CIDR متعارف نیست).</td>
</tr>
<tr>
  <td><tt>cidr('192.168.0.0/16').prefixLength()</tt></td>
  <td>طول پیشوند یک CIDR از نوع IPv4 را برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>cidr('::1/128').prefixLength()</tt></td>
  <td>طول پیشوند یک CIDR از نوع IPv6 را برمی‌گرداند.</td>
</tr>
</tbody>
</table>

برای اطلاعات بیشتر، مستندات godoc [کتابخانهٔ CIDR کوبرنتیز](https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#CIDR) را ببینید.

### کتابخانهٔ مجوزدهندهٔ کوبرنتیز

در عبارت‌های CEL در API که متغیری از نوع `Authorizer` در دسترس است،
می‌توان از مجوزدهنده (authorizer) برای انجام بررسی‌های مجوز برای هویت درخواست‌دهنده (principal)،
یعنی کاربر احراز هویت‌شدهٔ درخواست، استفاده کرد.

بررسی‌های مجوز برای منابع API به این صورت انجام می‌شوند:

1. گروه و منبعی را که باید بررسی شود مشخص کنید: `Authorizer.group(string).resource(string) ResourceCheck`
1. در صورت نیاز، هر ترکیبی از توابع سازندهٔ زیر را فراخوانی کنید تا دامنهٔ بررسی مجوز محدودتر شود.
   توجه کنید که این توابع نوع گیرنده را برمی‌گردانند و می‌توان آن‌ها را به‌صورت زنجیره‌ای فراخوانی کرد:
   - `ResourceCheck.subresource(string) ResourceCheck`
   - `ResourceCheck.namespace(string) ResourceCheck`
   - `ResourceCheck.name(string) ResourceCheck`
1. برای انجام بررسی مجوز، `ResourceCheck.check(verb string) Decision` را فراخوانی کنید.
1. برای بررسی نتیجهٔ بررسی مجوز، `allowed() bool` یا `reason() string` را فراخوانی کنید.

بررسی‌های مجوز برای موارد غیرمنبعی به این صورت انجام می‌شوند:

1. فقط یک مسیر را مشخص کنید: `Authorizer.path(string) PathCheck`
1. برای انجام بررسی مجوز، `PathCheck.check(httpVerb string) Decision` را فراخوانی کنید.
1. برای بررسی نتیجهٔ بررسی مجوز، `allowed() bool` یا `reason() string` را فراخوانی کنید.

برای انجام بررسی مجوز برای یک حساب سرویس (service account):

- `Authorizer.serviceAccount(namespace string, name string) Authorizer`

<table>
<caption>نمونه‌هایی از عبارت‌های CEL که از توابع کتابخانهٔ URL استفاده می‌کنند</caption>
<thead>
<tr>
  <th>عبارت CEL</th>
  <th>هدف</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>authorizer.group('').resource('pods').namespace('default').check('create').allowed()</tt></td>
  <td>اگر هویت درخواست‌دهنده (کاربر یا حساب سرویس) مجاز به ایجاد پادها در فضای نام 'default' باشد، مقدار true برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>authorizer.path('/healthz').check('get').allowed()</tt></td>
  <td>بررسی می‌کند که آیا هویت درخواست‌دهنده (کاربر یا حساب سرویس) مجاز است درخواست‌های HTTP GET را به مسیر API ‏/healthz ارسال کند یا نه.</td>
</tr>
<tr>
  <td><tt>authorizer.serviceAccount('default', 'myserviceaccount').resource('deployments').check('delete').allowed()<tt></td>
  <td>بررسی می‌کند که آیا حساب سرویس مجاز به حذف Deploymentها است یا نه.</td>
</tr>
</tbody>
</table>

{{< feature-state feature_gate_name="AuthorizeWithSelectors" >}}

در عبارت‌های CEL در API که متغیری از نوع `Authorizer` در دسترس است،
می‌توان انتخابگرهای فیلد و برچسب را نیز در بررسی‌های مجوز گنجاند.

<table>
<caption>نمونه‌هایی از عبارت‌های CEL که از توابع مجوزدهی مبتنی بر انتخابگر استفاده می‌کنند</caption>
<thead>
<tr>
  <th>عبارت CEL</th>
  <th>هدف</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>authorizer.group('').resource('pods').fieldSelector('spec.nodeName=mynode').check('list').allowed()</tt></td>
  <td>
    اگر هویت درخواست‌دهنده (کاربر یا حساب سرویس) مجاز باشد پادها را
    با انتخابگر فیلد <tt>spec.nodeName=mynode</tt> فهرست کند، مقدار true برمی‌گرداند.
  </td>
</tr>
<tr>
  <td><tt>authorizer.group('').resource('pods').labelSelector('example.com/mylabel=myvalue').check('list').allowed()</tt></td>
  <td>
    اگر هویت درخواست‌دهنده (کاربر یا حساب سرویس) مجاز باشد پادها را
    با انتخابگر برچسب <tt>example.com/mylabel=myvalue</tt> فهرست کند، مقدار true برمی‌گرداند.
  </td>
</tr>
</tbody>
</table>

برای اطلاعات بیشتر، مستندات godoc [کتابخانهٔ Authz کوبرنتیز](https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz)
و [کتابخانهٔ AuthzSelectors کوبرنتیز](https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#AuthzSelectors)
را ببینید.

### کتابخانهٔ قالب کوبرنتیز

کتابخانهٔ `format` توابعی برای اعتبارسنجی قالب‌های رایج رشته در کوبرنتیز فراهم می‌کند.
این کتابخانه در `messageExpression` قواعد اعتبارسنجی کاربرد دارد و با آن می‌توان پیام‌های خطای دقیق‌تری ارائه کرد.

این کتابخانه برای هر قالب نام‌دار یک تابع `format()` و همچنین یک تابع عمومی `format.named()` فراهم می‌کند.

- تابع `format.named(string)` &rarr; `?Format`: اگر قالبی با نام داده‌شده وجود داشته باشد، آبجکت `Format` آن را برمی‌گرداند. در غیر این صورت، `optional.none` را برمی‌گرداند.
- تابع `format.<formatName>() -> Format`: توابع کمکی برای همهٔ قالب‌های نام‌دار نیز در دسترس هستند. برای مثال، `format.dns1123Label()` آبجکت `Format` مربوط به برچسب‌های DNS-1123 را برمی‌گرداند.
- تابع `<Format>.validate(string) -> list<string>?`: رشتهٔ داده‌شده را با قالب مقایسه و اعتبارسنجی می‌کند. اگر رشته معتبر باشد، `optional.none` را برمی‌گرداند؛ در غیر این صورت، یک مقدار اختیاری (optional) شامل فهرستی از رشته‌های خطای اعتبارسنجی برمی‌گرداند.

**قالب‌های موجود:**

نام‌های قالب زیر پشتیبانی می‌شوند:

<table>
<caption>قالب‌های موجود در کتابخانهٔ format</caption>
<thead>
<tr>
  <th>نام قالب</th>
  <th>توضیح</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>dns1123Label</tt></td>
  <td>بررسی می‌کند که آیا رشته یک برچسب DNS-1123 معتبر است.</td>
</tr>
<tr>
  <td><tt>dns1123Subdomain</tt></td>
  <td>بررسی می‌کند که آیا رشته یک زیردامنهٔ DNS-1123 معتبر است.</td>
</tr>
<tr>
  <td><tt>dns1035Label</tt></td>
  <td>بررسی می‌کند که آیا رشته یک برچسب DNS-1035 معتبر است.</td>
</tr>
<tr>
  <td><tt>qualifiedName</tt></td>
  <td>بررسی می‌کند که آیا رشته یک نام واجد شرایط (qualified name) معتبر است.</td>
</tr>
<tr>
  <td><tt>dns1123LabelPrefix</tt></td>
  <td>بررسی می‌کند که آیا رشته یک پیشوند برچسب DNS-1123 معتبر است.</td>
</tr>
<tr>
  <td><tt>dns1123SubdomainPrefix</tt></td>
  <td>بررسی می‌کند که آیا رشته یک پیشوند زیردامنهٔ DNS-1123 معتبر است.</td>
</tr>
<tr>
  <td><tt>dns1035LabelPrefix</tt></td>
  <td>بررسی می‌کند که آیا رشته یک پیشوند برچسب DNS-1035 معتبر است.</td>
</tr>
<tr>
  <td><tt>labelValue</tt></td>
  <td>بررسی می‌کند که آیا رشته یک مقدار برچسب معتبر است.</td>
</tr>
<tr>
  <td><tt>uri</tt></td>
  <td>بررسی می‌کند که آیا رشته یک URI معتبر است. این قالب از همان الگوی `isURL` استفاده می‌کند، اما فهرستی از خطاها برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>uuid</tt></td>
  <td>بررسی می‌کند که آیا رشته یک UUID معتبر است.</td>
</tr>
<tr>
  <td><tt>byte</tt></td>
  <td>بررسی می‌کند که آیا رشته یک رشتهٔ معتبر با کدگذاری base64 است.</td>
</tr>
<tr>
  <td><tt>date</tt></td>
  <td>بررسی می‌کند که آیا رشته یک تاریخ معتبر با قالب `YYYY-MM-DD` است.</td>
</tr>
<tr>
  <td><tt>datetime</tt></td>
  <td>بررسی می‌کند که آیا رشته یک تاریخ و زمان معتبر با قالب RFC3339 است.</td>
</tr>
</tbody>
</table>

**نمونه‌ها:**

<table>
<caption>نمونه‌هایی از عبارت‌های CEL که از توابع کتابخانهٔ format استفاده می‌کنند</caption>
<thead>
<tr>
  <th>عبارت CEL</th>
  <th>هدف</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>!format.dns1123Label().validate(self.metadata.name).hasValue()</tt></td>
  <td>یک قاعدهٔ اعتبارسنجی که بررسی می‌کند آیا نام یک آبجکت، برچسب DNS-1123 معتبری است یا نه.</td>
</tr>
<tr>
  <td><tt>format.dns1123Label().validate(self.metadata.name).orValue([]).join("\\n")</tt></td>
  <td>یک `messageExpression` که خطاهای اعتبارسنجی مشخص یک فیلد را برمی‌گرداند. اگر فیلد معتبر باشد، `validate` مقدار `optional.none` را برمی‌گرداند و `orValue` یک فهرست خالی فراهم می‌کند که نتیجهٔ آن یک رشتهٔ خالی است.</td>
</tr>
</tbody>
</table>

برای اطلاعات بیشتر، مستندات godoc [کتابخانهٔ Format کوبرنتیز](https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Format) را ببینید.

### کتابخانهٔ مقدار (quantity) کوبرنتیز

کوبرنتیز از نسخهٔ 1.28 از کار با رشته‌های مقدار (مانند 1.5G، 512k و 20Mi) پشتیبانی می‌کند.

- تابع `isQuantity(string)` بررسی می‌کند که آیا یک رشته بر اساس
  [resource.Quantity در کوبرنتیز](https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity) یک Quantity معتبر است یا نه.
- تابع `quantity(string) Quantity` یک رشته را به Quantity تبدیل می‌کند. اگر رشته
  مقدار معتبری نباشد، خطا رخ می‌دهد.

پس از تجزیهٔ رشته با تابع `quantity`، آبجکت Quantity حاصل
توابع عضو زیر را در اختیار می‌گذارد:

<table>
<caption>توابع عضو موجود برای Quantity</caption>
<thead>
<tr>
  <th>تابع عضو</th>
  <th>مقدار بازگشتی CEL</th>
  <th>توضیح</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>isInteger()</tt></td>
  <td>bool</td>
  <td>اگر و تنها اگر بتوان asInteger را بدون خطا فراخوانی کرد، مقدار true برمی‌گرداند</td>
</tr>
<tr>
  <td><tt>asInteger()</tt></td>
  <td>int</td>
  <td>
    در صورت امکان، نمایشی از مقدار فعلی را به‌صورت <tt>int64</tt> برمی‌گرداند.
    اگر این تبدیل به سرریز یا از دست رفتن دقت منجر شود، خطا رخ می‌دهد.
  </td>
</tr>
<tr>
  <td><tt>asApproximateFloat()</tt></td>
  <td>float</td>
  <td>
    نمایشی از مقدار را به‌صورت <tt>float64</tt> برمی‌گرداند که ممکن است با از دست رفتن دقت همراه باشد.
    اگر مقدار خارج از بازهٔ <tt>float64</tt> باشد،
    <tt>+Inf/-Inf</tt> برگردانده می‌شود.</td>
</tr>
<tr>
  <td><tt>sign()</tt></td>
  <td>int</td>
  <td>
    اگر مقدار مثبت باشد <tt>1</tt>، اگر منفی باشد <tt>-1</tt>
    و اگر صفر باشد <tt>0</tt> برمی‌گرداند.
  </td>
</tr>
<tr>
  <td><tt>add(&lt;Quantity&gt;)</tt></td>
  <td>Quantity</td>
  <td>مجموع دو مقدار را برمی‌گرداند</td>
</tr>
<tr>
  <td><tt>add(&lt;int&gt;)</tt></td>
  <td>Quantity</td>
  <td>مجموع یک مقدار و یک عدد صحیح را برمی‌گرداند</td>
  <td>
<tr>
  <td><tt>sub(&lt;Quantity&gt;)</tt></td>
  <td>Quantity</td>
  <td>تفاضل دو مقدار را برمی‌گرداند</td>
</tr>
<tr>
  <td><tt>sub(&lt;int&gt;)</tt></td>
  <td>Quantity</td>
  <td>تفاضل یک مقدار و یک عدد صحیح را برمی‌گرداند</td>
</tr>
<tr>
  <td><tt>isLessThan(&lt;Quantity&gt;)</tt></td>
  <td>bool</td>
  <td>اگر و تنها اگر گیرنده از عملوند کوچک‌تر باشد، مقدار true برمی‌گرداند</td>
</tr>
<tr>
  <td><tt>isGreaterThan(&lt;Quantity&gt;)</tt></td>
  <td>bool</td>
  <td>اگر و تنها اگر گیرنده از عملوند بزرگ‌تر باشد، مقدار true برمی‌گرداند</td>
</tr>
<tr>
  <td><tt>compareTo(&lt;Quantity&gt;)</tt></td>
  <td>int</td>
  <td>
    گیرنده را با عملوند مقایسه می‌کند و اگر برابر باشند 0،
    اگر گیرنده بزرگ‌تر باشد 1 و اگر گیرنده از عملوند کوچک‌تر باشد -1 برمی‌گرداند
  </td>
</tr>
</tbody>
</table>

نمونه‌ها:

<table>
<caption>نمونه‌هایی از عبارت‌های CEL که از توابع کتابخانهٔ URL استفاده می‌کنند</caption>
<thead>
<tr>
  <th>عبارت CEL</th>
  <th>هدف</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>quantity("500000G").isInteger()</tt></td>
  <td>بررسی اینکه آیا تبدیل به عدد صحیح خطا ایجاد می‌کند یا نه</td>
</tr>
<tr>
  <td><tt>quantity("50k").asInteger()</tt></td>
  <td>تبدیل دقیق به عدد صحیح</td>
</tr>
<tr>
  <td><tt>quantity("9999999999999999999999999999999999999G").asApproximateFloat()</tt></td>
  <td>تبدیل به عدد اعشاری همراه با از دست رفتن دقت</td>
</tr>
<tr>
  <td><tt>quantity("50k").add(quantity("20k"))</tt></td>
  <td>جمع دو مقدار</td>
</tr>
<tr>
  <td><tt>quantity("50k").sub(20000)</tt></td>
  <td>کم کردن یک عدد صحیح از یک مقدار</td>
</tr>
<tr>
  <td><tt>quantity("50k").add(20).sub(quantity("100k")).sub(-50000)</tt></td>
  <td>جمع و تفریق زنجیره‌ای اعداد صحیح و مقدارها</td>
</tr>
<tr>
  <td><tt>quantity("200M").compareTo(quantity("0.2G"))</tt></td>
  <td>مقایسهٔ دو مقدار</td>
</tr>
<tr>
  <td><tt>quantity("150Mi").isGreaterThan(quantity("100Mi"))</tt></td>
  <td>بررسی اینکه آیا یک مقدار از گیرنده بزرگ‌تر است یا نه</td>
</tr>
<tr>
  <td><tt>quantity("50M").isLessThan(quantity("100M"))</tt></td>
  <td>بررسی اینکه آیا یک مقدار از گیرنده کوچک‌تر است یا نه</td>
</tr>
</tbody>
</table>

### کتابخانهٔ semver کوبرنتیز

کوبرنتیز از نسخهٔ v1.34 امکان تجزیه و مقایسهٔ رشته‌هایی را فراهم می‌کند که از مشخصهٔ Semantic Versioning 2.0.0 پیروی می‌کنند.
برای آشنایی با الگوهای پذیرفته‌شده، به مستندات [semver.org](https://semver.org/) مراجعه کنید.

- تابع `isSemver(string)` بررسی می‌کند که آیا یک رشته، نسخهٔ معنایی معتبری است یا نه.
- تابع `semver(string)` یک رشته را به آبجکت Semver تبدیل می‌کند یا در غیر این صورت به خطا می‌انجامد.

می‌توان آرگومان بولی اختیاری `normalize` را به `isSemver` و `semver` داد. اگر مقدار آن `true` باشد، فرایند نرمال‌سازی هر پیشوند «v» را حذف می‌کند، برای نسخه‌هایی که فقط مؤلفهٔ major یا major.minor دارند، شماره‌های minor و patch را برابر 0 قرار می‌دهد و همهٔ صفرهای ابتدایی را حذف می‌کند.

پس از تجزیهٔ رشته با تابع `semver`، آبجکت Semver حاصل، کتابخانهٔ توابع عضو زیر را در اختیار می‌گذارد:

<table>
<caption>توابع عضو در دسترس برای یک آبجکت Semver</caption>
<thead>
<tr>
  <th>تابع عضو</th>
  <th>مقدار بازگشتی CEL</th>
  <th>توضیح</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>major()</tt></td>
  <td>int</td>
  <td>شمارهٔ نسخهٔ اصلی (major) را برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>minor()</tt></td>
  <td>int</td>
  <td>شمارهٔ نسخهٔ فرعی (minor) را برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>patch()</tt></td>
  <td>int</td>
  <td>شمارهٔ وصله (patch) را برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>isLessThan(&lt;Semver&gt;)</tt></td>
  <td>bool</td>
  <td>اگر و تنها اگر گیرنده از عملوند کوچک‌تر باشد، true برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>isGreaterThan(&lt;Semver&gt;)</tt></td>
  <td>bool</td>
  <td>اگر و تنها اگر گیرنده از عملوند بزرگ‌تر باشد، true برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>compareTo(&lt;Semver&gt;)</tt></td>
  <td>int</td>
  <td>
    گیرنده را با عملوند مقایسه می‌کند و اگر برابر باشند 0، اگر گیرنده بزرگ‌تر باشد 1
    و اگر گیرنده از عملوند کوچک‌تر باشد -1 برمی‌گرداند.
  </td>
</tr>
</tbody>
</table>

مثال‌ها:

<table>
<caption>نمونه‌هایی از عبارت‌های CEL که از توابع کتابخانهٔ semver استفاده می‌کنند</caption>
<thead>
<tr>
  <th>عبارت CEL</th>
  <th>هدف</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>isSemver('1.0.0')</tt></td>
  <td>برای یک رشتهٔ Semver معتبر، true برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>isSemver('v1.0', true)</tt></td>
  <td>برای یک رشتهٔ Semver قابل نرمال‌سازی، true برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>semver('1.2.3').major()</tt></td>
  <td>نسخهٔ اصلی یک Semver را برمی‌گرداند.</td>
</tr>
<tr>
  <td><tt>semver('1.2.3').compareTo(semver('2.0.0')) &lt; 0</tt></td>
  <td>دو رشتهٔ Semver را با هم مقایسه می‌کند.</td>
</tr>
</tbody>
</table>

برای اطلاعات بیشتر، godoc [کتابخانهٔ Semver کوبرنتیز](https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#SemverLib) را ببینید.

## بررسی نوع

زبان CEL یک [زبان با نوع‌دهی تدریجی](https://github.com/google/cel-spec/blob/master/doc/langdef.md#gradual-type-checking) است.

برخی از فیلدهای API کوبرنتیز حاوی عبارت‌های CEL هستند که نوع آن‌ها به‌طور کامل بررسی می‌شود. برای مثال،
[قواعد اعتبارسنجی CustomResourceDefinitions](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#validation-rules)
به‌طور کامل از نظر نوع بررسی می‌شوند.

برخی دیگر از فیلدهای API کوبرنتیز حاوی عبارت‌های CEL با بررسی نوع جزئی هستند. عبارتی با بررسی نوع جزئی،
عبارتی است که برخی از متغیرهای آن نوع ایستا و برخی دیگر نوع پویا دارند. برای مثال، در عبارت‌های CEL مربوط به
[ValidatingAdmissionPolicies](/docs/reference/access-authn-authz/validating-admission-policy/)
متغیر `request` نوع‌دار است، اما متغیر `object` نوع پویا دارد.
در نتیجه، عبارتی که شامل `request.namex` باشد در بررسی نوع رد می‌شود، زیرا فیلد `namex` تعریف نشده است.
اما `object.namex` حتی وقتی فیلد `namex` برای انواع منابعی که `object` به آن‌ها اشاره می‌کند تعریف نشده باشد،
از بررسی نوع عبور می‌کند، زیرا `object` نوع پویا دارد.

با ماکروی `has()` در عبارت‌های CEL می‌توان پیش از تلاش برای دسترسی به مقدار یک فیلد از متغیری با نوع پویا،
وجود آن فیلد را بررسی کرد. برای مثال:

```cel
has(object.namex) ? object.namex == 'special' : request.name == 'special'
```

از `has()` برای بررسی وجود فیلد استفاده کنید، اما برای بررسی اینکه یک map حاوی کلید معینی است یا نه، از آن
استفاده نکنید. برای مثال، عبارت
`has(object.metadata.labels['example.com/environment'])` را ننویسید. برای بررسی کلیدهای map،
به جای آن از عملگر `in` استفاده کنید. برای مثال:

```cel
has(object.metadata.labels) && 'example.com/environment' in object.metadata.labels
```

این عبارت پیش از بررسی اینکه map حاوی کلید `example.com/environment` است یا نه،
وجود `metadata.labels` را بررسی می‌کند.

## یکپارچگی با سیستم نوع

<table>
<caption>جدول رابطهٔ میان انواع OpenAPIv3 و انواع CEL</caption>
<thead>
<tr>
  <th>نوع OpenAPIv3</th>
  <th>نوع CEL</th>
</tr>
</thead>
<tbody>
<tr>
  <td>نوع 'object' دارای Properties</td>
  <td>
    نوع object / "message type"
    (حاصل ارزیابی <tt>type(&lt;object&gt;)</tt> برابر
     <tt>selfType&lt;uniqueNumber&gt;.path.to.object.from.self</tt> است)
  </td>
</tr>
<tr>
  <td>نوع 'object' دارای <tt>additionalProperties</tt></td>
  <td>map</td>
</tr>
<tr>
  <td>نوع 'object' دارای <tt>x-kubernetes-embedded-type</tt></td>
  <td>
    نوع object / "message type"؛ فیلدهای 'apiVersion'، 'kind'، 'metadata.name'
    و 'metadata.generateName' به‌طور ضمنی در طرح‌واره (schema) گنجانده می‌شوند
  </td>
</tr>
<tr>
  <td>نوع 'object' دارای x-kubernetes-preserve-unknown-fields</td>
  <td>نوع object / "message type"؛ فیلدهای ناشناخته در عبارت CEL به هیچ وجه در دسترس نیستند</td>
</tr>
<tr>
  <td><tt>x-kubernetes-int-or-string</tt></td>
  <td>
    اجتماع <tt>int</tt> یا <tt>string</tt>؛ عبارت
    <tt>self.intOrString < 100 | self.intOrString == '50%'</tt>
    برای هر دو مقدار <tt>50</tt> و <tt>"50%"</tt> به true ارزیابی می‌شود
  </td>
</tr>
<tr>
  <td>'array'</td>
  <td>list</td>
</tr>
<tr>
  <td>نوع 'array' دارای <tt>x-kubernetes-list-type=map</tt></td>
  <td>نوع list با برابری مبتنی بر map و تضمین یکتایی کلیدها</td>
</tr>
<tr>
  <td>نوع 'array' دارای <tt>x-kubernetes-list-type=set</tt></td>
  <td>نوع list با برابری مبتنی بر set و تضمین یکتایی عناصر</td>
</tr>
<tr>
  <td>'boolean'</td>
  <td>boolean</td>
</tr>
<tr>
  <td>نوع 'number' (همهٔ قالب‌ها)</td>
  <td>double</td>
</tr>
<tr>
  <td>نوع 'integer' (همهٔ قالب‌ها)</td>
  <td>int (64)</td>
</tr>
<tr>
  <td><i>معادلی ندارد</i></td>
  <td>uint (64)</td>
</tr>
<tr>
  <td>'null'</td>
  <td>null_type</td>
</tr>
<tr>
  <td>'string'</td>
  <td>string</td>
</tr>
<tr>
  <td>نوع 'string' با format=byte (کدگذاری‌شده با base64)</td>
  <td>bytes</td>
</tr>
<tr>
  <td>نوع 'string' با format=date</td>
  <td>timestamp (<tt>google.protobuf.Timestamp</tt>)</td>
</tr>
<tr>
  <td>نوع 'string' با format=datetime</td>
  <td>timestamp (<tt>google.protobuf.Timestamp</tt>)</td>
</tr>
<tr>
  <td>نوع 'string' با format=duration</td>
  <td>duration (<tt>google.protobuf.Duration</tt>)</td>
</tr>
</tbody>
</table>

همچنین ببینید: [انواع CEL](https://github.com/google/cel-spec/blob/v0.6.0/doc/langdef.md#values)،
[انواع OpenAPI](https://swagger.io/specification/#data-types)،
[طرح‌واره‌های ساختاری کوبرنتیز](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#specifying-a-structural-schema).

مقایسهٔ برابری برای آرایه‌هایی که `x-kubernetes-list-type` آن‌ها `set` یا `map` است، ترتیب عناصر را
نادیده می‌گیرد. برای مثال، اگر آرایه‌ها نمایانگر مقادیر `set` کوبرنتیز باشند، `[1, 2] == [2, 1]` برقرار است.

الحاق آرایه‌هایی که `x-kubernetes-list-type` دارند، از معناشناسی همان نوع لیست پیروی می‌کند:

`set`
: عملگر `X + Y` اجتماعی را انجام می‌دهد که در آن موقعیت همهٔ عناصر `X` در آرایه حفظ می‌شود
  و عناصر غیرمشترک `Y` با حفظ ترتیب جزئی‌شان به انتها افزوده می‌شوند.

`map`
: عملگر `X + Y` ادغامی را انجام می‌دهد که در آن موقعیت همهٔ کلیدهای `X` در آرایه حفظ می‌شود،
  اما هنگامی که مجموعه‌کلیدهای `X` و `Y` اشتراک داشته باشند، مقادیر با مقادیر `Y` بازنویسی می‌شوند.
  عناصری از `Y` که کلیدهای غیرمشترک دارند، با حفظ ترتیب جزئی‌شان به انتها افزوده می‌شوند.

## گریزدهی (Escaping)

فقط نام ویژگی‌هایی از منابع کوبرنتیز که به شکل
`[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` هستند، از CEL در دسترس‌اند. نام ویژگی‌های در دسترس،
هنگام دسترسی در عبارت، طبق قواعد زیر گریزدهی می‌شوند:

<table>
<caption>جدول قواعد گریزدهی شناسه‌های CEL</caption>
<thead>
<tr>
  <th>دنبالهٔ گریز</th>
  <th>نام ویژگی معادل</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>__underscores__</tt></td>
  <td><tt>__</tt></td>
</tr>
<tr>
  <td><tt>__dot__</tt></td>
  <td><tt>.</tt></td>
</tr>
<tr>
  <td><tt>__dash__</tt></td>
  <td><tt>-</tt></td>
</tr>
<tr>
  <td><tt>__slash__</tt></td>
  <td><tt>/</tt></td>
</tr>
<tr>
  <td><tt>__{keyword}__</tt></td>
  <td>
    <a href="https://github.com/google/cel-spec/blob/v0.6.0/doc/langdef.md#syntax">
      کلیدواژهٔ <b>رزروشدهٔ</b> CEL
    </a>
  </td>
</tr>
</tbody>
</table>

وقتی هر یک از کلیدواژه‌های **رزروشدهٔ** CEL را گریزدهی می‌کنید، برای استفاده از گریزدهی با زیرخط،
نام ویژگی باید دقیقاً با آن کلیدواژه مطابقت داشته باشد
(برای مثال، `int` در واژهٔ `sprint` گریزدهی نمی‌شود و نیازی هم به گریزدهی ندارد).

نمونه‌های گریزدهی:

<table>
<caption>نمونه‌هایی از شناسه‌های گریزدهی‌شدهٔ CEL</caption>
<thead>
<tr>
  <th>نام ویژگی</th>
  <th>قاعده با نام ویژگی گریزدهی‌شده</th>
</tr>
</thead>
<tbody>
<tr>
  <td><tt>namespace</tt></td>
  <td><tt>self.__namespace__ &gt; 0</tt></td>
</tr>
<tr>
  <td><tt>x-prop</tt></td>
  <td><tt>self.x__dash__prop &gt; 0</tt></td>
</tr>
<tr>
  <td><tt>redact_d</tt></td>
  <td><tt>self.redact__underscores__d &gt; 0</tt></td>
</tr>
<tr>
  <td><tt>string</tt></td>
  <td><tt>self.startsWith('kube')</tt></td>
</tr>
</tbody>
</table>

## محدودیت‌های منابع

زبان CEL تورینگ‌کامل نیست و سازوکارهای ایمنی گوناگونی برای محیط عملیاتی فراهم می‌کند تا زمان اجرا را محدود کند.
قابلیت‌های _محدودیت منابع_ در CEL دربارهٔ پیچیدگی عبارت‌ها به توسعه‌دهندگان بازخورد می‌دهند و به محافظت از
سرور API در برابر مصرف بیش از حد منابع هنگام ارزیابی کمک می‌کنند. از قابلیت‌های محدودیت منابع CEL برای
جلوگیری از مصرف بیش از حد منابع سرور API در فرایند ارزیابی CEL استفاده می‌شود.

یکی از عناصر کلیدی قابلیت‌های محدودیت منابع، _واحد هزینه_ است که CEL آن را برای ردیابی مصرف CPU تعریف می‌کند.
واحدهای هزینه مستقل از بار سیستم و سخت‌افزار هستند. این واحدها قطعی (deterministic) نیز هستند؛ یعنی برای
هر عبارت CEL و دادهٔ ورودی معین، ارزیابی آن عبارت در مفسر CEL همواره به هزینهٔ یکسانی می‌انجامد.

بسیاری از عملیات اصلی CEL هزینهٔ ثابتی دارند. ساده‌ترین عملیات، مانند مقایسه‌ها (برای مثال `<`)، هزینه‌ای
برابر 1 دارند. برخی از عملیات هزینهٔ ثابت بالاتری دارند؛ برای مثال، اعلان لیترال لیست هزینهٔ پایهٔ ثابتی
برابر 40 واحد هزینه دارد.

هزینهٔ فراخوانی توابعی که در کد بومی پیاده‌سازی شده‌اند، بر اساس پیچیدگی زمانی عملیات تخمین زده می‌شود.
برای مثال، هزینهٔ عملیاتی که از عبارات منظم استفاده می‌کنند، مانند `match` و `find`، با مقدار تقریبی
`length(regexString)*length(inputString)` تخمین زده می‌شود. این هزینهٔ تقریبی بازتاب‌دهندهٔ پیچیدگی زمانی
بدترین حالت در پیاده‌سازی RE2 زبان Go است.

### بودجهٔ هزینهٔ زمان اجرا

همهٔ عبارت‌های CEL که کوبرنتیز ارزیابی می‌کند، به یک بودجهٔ هزینهٔ زمان اجرا محدود هستند. بودجهٔ هزینهٔ
زمان اجرا تخمینی از مصرف واقعی CPU است که با افزایش یک شمارندهٔ واحد هزینه در حین تفسیر عبارت CEL
محاسبه می‌شود. اگر مفسر CEL دستورالعمل‌های بیش از حدی اجرا کند، از بودجهٔ هزینهٔ زمان اجرا فراتر می‌رود،
اجرای عبارت‌ها متوقف می‌شود و خطایی رخ می‌دهد.

برخی از منابع کوبرنتیز یک بودجهٔ هزینهٔ زمان اجرای اضافی تعریف می‌کنند که اجرای چند عبارت را محدود می‌کند.
اگر مجموع هزینهٔ عبارت‌ها از این بودجه فراتر رود، اجرای عبارت‌ها متوقف می‌شود و خطایی رخ می‌دهد.
برای مثال، اعتبارسنجی یک منبع سفارشی، بودجهٔ هزینهٔ زمان اجرای _به‌ازای هر اعتبارسنجی_ برای همهٔ
[قواعد اعتبارسنجی](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#validation-rules)
دارد که برای اعتبارسنجی آن منبع سفارشی ارزیابی می‌شوند.

### محدودیت‌های هزینهٔ تخمینی

برای برخی از منابع کوبرنتیز، سرور API ممکن است همچنین بررسی کند که آیا زمان اجرای تخمینی عبارت‌های CEL
در بدترین حالت، اجرای آن‌ها را بیش از حد پرهزینه می‌کند یا نه. در این صورت، سرور API با رد کردن عملیات
ایجاد یا به‌روزرسانی‌ای که آن عبارت CEL را در منابع API قرار می‌دهند، از نوشته شدن آن عبارت در منابع API
جلوگیری می‌کند. این قابلیت تضمین قوی‌تری فراهم می‌کند که عبارت‌های CEL نوشته‌شده در منبع API، در زمان اجرا
بدون فراتر رفتن از بودجهٔ هزینهٔ زمان اجرا ارزیابی شوند.
