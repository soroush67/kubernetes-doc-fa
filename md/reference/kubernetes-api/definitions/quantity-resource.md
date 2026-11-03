---
api_metadata:
  apiVersion: "resource"
  import: "k8s.io/apimachinery/pkg/api/resource"
  kind: "Quantity"
content_type: "api_reference"
description: "Quantity is a fixed-point representation of a number. It provides convenient marshaling/unmarshaling in JSON and YAML, in addition to String() and AsInt64() accessors.\n\nThe serialization format is:\n\n``` &lt;quantity&gt;        ::= &lt;signedNumber&gt;&lt;suffix&gt;\n\n\t(Note that &lt;suffix&gt; may be empty, from the &#34;&#34; case in &lt;decimalSI&gt;.)\n\n&lt;digit&gt;           ::= 0 | 1 | ... | 9 &lt;digits&gt;          ::= &lt;digit&gt; | &lt;digit&gt;&lt;digits&gt; &lt;number&gt;          ::= &lt;digits&gt; | &lt;digits&gt;.&lt;digits&gt; | &lt;digits&gt;. | .&lt;digits&gt; &lt;sign&gt;            ::= &#34;+&#34; | &#34;-&#34; &lt;signedNumber&gt;    ::= &lt;number&gt; | &lt;sign&gt;&lt;number&gt; &lt;suffix&gt;          ::= &lt;binarySI&gt; | &lt;decimalExponent&gt; | &lt;decimalSI&gt; &lt;binarySI&gt;        ::= Ki | Mi | Gi | Ti | Pi | Ei\n\n\t(International System of units; See: http://physics.nist.gov/cuu/Units/binary.html)\n\n&lt;decimalSI&gt;       ::= m | &#34;&#34; | k | M | G | T | P | E\n\n\t(Note that 1024 = 1Ki but 1000 = 1k; I didn&#39;t choose the capitalization.)\n\n&lt;decimalExponent&gt; ::= &#34;e&#34; &lt;signedNumber&gt; | &#34;E&#34; &lt;signedNumber&gt; ```\n\nNo matter which of the three exponent forms is used, no quantity may represent a number greater than 2^63-1 in magnitude, nor may it have more than 3 decimal places. Numbers larger or more precise will be capped or rounded up. (E.g.: 0.1m will rounded up to 1m.) This may be extended in the future if we require larger or smaller quantities.\n\nWhen a Quantity is parsed from a string, it will remember the type of suffix it had, and will use the same type again when it is serialized.\n\nBefore serializing, Quantity will be put in &#34;canonical form&#34;. This means that Exponent/suffix will be adjusted up or down (with a corresponding increase or decrease in Mantissa) such that:\n\n- No precision is lost - No fractional digits will be emitted - The exponent (or suffix) is as large as possible.\n\nThe sign will be omitted unless the number is negative.\n\nExamples:\n\n- 1.5 will be serialized as &#34;1500m&#34; - 1.5Gi will be serialized as &#34;1536Mi&#34;\n\nNote that the quantity will NEVER be internally represented by a floating point number. That is the whole point of this exercise.\n\nNon-canonical values will still parse as long as they are well formed, but will be re-emitted in their canonical form. (So always use canonical form, or don&#39;t diff.)\n\nThis format is intended to make it difficult to use these numbers without writing some sort of special handling code in the hopes that that will cause implementors to also use a fixed point implementation."
title: "Quantity"
weight: 390
auto_generated: true
---

<!--
The file is auto-generated from the Go source code of the component using a generic
[generator](https://github.com/kubernetes-sigs/reference-docs/). To learn how
to generate the reference documentation, please read
[Contributing to the reference documentation](/docs/contribute/generate-ref-docs/).
To update the reference content, please follow the
[Contributing upstream](/docs/contribute/generate-ref-docs/contribute-upstream/)
guide. You can file document formatting bugs against the
[reference-docs](https://github.com/kubernetes-sigs/reference-docs/) project.
-->

`apiVersion: resource`

`import "k8s.io/apimachinery/pkg/api/resource"`


## Quantity {#Quantity}

Quantity نمایش اعشار ثابت (fixed-point) یک عدد است. این نوع، علاوه بر دسترسی‌دهنده‌های String() و AsInt64()، عملیات marshal و unmarshal را نیز به‌صورت مناسب در JSON و YAML فراهم می‌کند.

قالب سریال‌سازی به این صورت است:

``` &lt;quantity&gt;        ::= &lt;signedNumber&gt;&lt;suffix&gt;

	(Note that &lt;suffix&gt; may be empty, from the &#34;&#34; case in &lt;decimalSI&gt;.)

&lt;digit&gt;           ::= 0 | 1 | ... | 9 &lt;digits&gt;          ::= &lt;digit&gt; | &lt;digit&gt;&lt;digits&gt; &lt;number&gt;          ::= &lt;digits&gt; | &lt;digits&gt;.&lt;digits&gt; | &lt;digits&gt;. | .&lt;digits&gt; &lt;sign&gt;            ::= &#34;+&#34; | &#34;-&#34; &lt;signedNumber&gt;    ::= &lt;number&gt; | &lt;sign&gt;&lt;number&gt; &lt;suffix&gt;          ::= &lt;binarySI&gt; | &lt;decimalExponent&gt; | &lt;decimalSI&gt; &lt;binarySI&gt;        ::= Ki | Mi | Gi | Ti | Pi | Ei

	(International System of units; See: http://physics.nist.gov/cuu/Units/binary.html)

&lt;decimalSI&gt;       ::= m | &#34;&#34; | k | M | G | T | P | E

	(Note that 1024 = 1Ki but 1000 = 1k; I didn&#39;t choose the capitalization.)

&lt;decimalExponent&gt; ::= &#34;e&#34; &lt;signedNumber&gt; | &#34;E&#34; &lt;signedNumber&gt; ```

مهم نیست از کدام یک از سه شکل نمای توانی استفاده شود، هیچ quantity نمی‌تواند عددی با قدر مطلق بزرگ‌تر از 2^63-1 را نمایش دهد و نیز نمی‌تواند بیش از ۳ رقم اعشار داشته باشد. اعداد بزرگ‌تر یا دقیق‌تر محدود (cap) یا به سمت بالا گرد می‌شوند. (برای نمونه: 0.1m به 1m گرد می‌شود.) در صورتی که در آینده به quantityهای بزرگ‌تر یا کوچک‌تر نیاز باشد، این محدودیت‌ها ممکن است گسترش یابند.

وقتی یک Quantity از یک رشته تجزیه می‌شود، نوع پسوند آن را به خاطر می‌سپارد و هنگام سریال‌سازی دوباره از همان نوع استفاده می‌کند.

پیش از سریال‌سازی، Quantity به «شکل متعارف» (canonical form) درآورده می‌شود. این یعنی نما یا پسوند (Exponent/suffix) به‌گونه‌ای کاهش یا افزایش می‌یابد (و در مقابل، مانتیس (Mantissa) نیز متناسب با آن افزایش یا کاهش پیدا می‌کند) که:

- هیچ دقتی از دست نرود - هیچ رقم اعشاری تولید نشود - نما (یا پسوند) تا حد امکان بزرگ باشد.

علامت فقط زمانی نوشته می‌شود که عدد منفی باشد.

نمونه‌ها:

- 1.5 به‌صورت "1500m" سریال‌سازی می‌شود - 1.5Gi به‌صورت "1536Mi" سریال‌سازی می‌شود

توجه کنید که quantity هرگز در درون سیستم با عدد ممیز شناور نمایش داده نمی‌شود. هدف اصلی این طراحی همین است.

مقادیر غیرمتعارف تا زمانی که قالب درستی داشته باشند همچنان تجزیه می‌شوند، اما به شکل متعارف خود دوباره تولید می‌شوند. (بنابراین همیشه از شکل متعارف استفاده کنید، وگرنه diff نگیرید.)

هدف از این قالب آن است که استفاده از این اعداد بدون نوشتن نوعی کد مدیریت ویژه دشوار باشد، به این امید که پیاده‌سازان را نیز به استفاده از پیاده‌سازی اعشار ثابت وادار کند.

<hr>
