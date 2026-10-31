--- 
title: پشتیبانی از JSONPath
content_type: concept
weight: 40
math: true
---

<!-- overview -->
ابزار {{< glossary_tooltip term_id="kubectl" text="kubectl" >}} از قالب‌های JSONPath به‌عنوان یکی از قالب‌های خروجی پشتیبانی می‌کند.


<!-- body -->

هر _قالب JSONPath_ از عبارت‌های JSONPath تشکیل می‌شود که درون آکولاد، یعنی `{` و `}`، قرار می‌گیرند.
ابزار kubectl با استفاده از عبارت‌های JSONPath، فیلدهای مشخصی از آبجکت JSON را فیلتر می‌کند و خروجی را قالب‌بندی می‌کند.
علاوه بر نحو اصلی قالب JSONPath، توابع و نحو زیر نیز معتبر هستند:

1. برای قرار دادن متن درون عبارت‌های JSONPath از نقل‌قول دوتایی (double quotes) استفاده کنید.
2. برای پیمایش فهرست‌ها از عملگرهای `range` و `end` استفاده کنید.
3. برای حرکت رو به عقب در یک فهرست، از اندیس‌های منفی برش (slice) استفاده کنید.  
   اندیس‌های منفی از انتهای فهرست به ابتدای آن «برنمی‌گردند» و تا زمانی معتبر هستند که \\( ( - index + listLength ) \ge 0 \\) برقرار باشد.

{{< note >}}

- عملگر `$` اختیاری است، زیرا عبارت به‌طور پیش‌فرض همیشه از آبجکت ریشه آغاز می‌شود.

- آبجکت حاصل با استفاده از تابع `String()` آن چاپ می‌شود.

{{< /note >}}

## توابع در JSONPath کوبرنتیز {#functions}

با فرض ورودی JSON زیر:

```json
{
  "kind": "List",
  "items":[
    {
      "kind":"None",
      "metadata":{
        "name":"127.0.0.1",
        "labels":{
          "kubernetes.io/hostname":"127.0.0.1"
        }
      },
      "status":{
        "capacity":{"cpu":"4"},
        "addresses":[{"type": "LegacyHostIP", "address":"127.0.0.1"}]
      }
    },
    {
      "kind":"None",
      "metadata":{"name":"127.0.0.2"},
      "status":{
        "capacity":{"cpu":"8"},
        "addresses":[
          {"type": "LegacyHostIP", "address":"127.0.0.2"},
          {"type": "another", "address":"127.0.0.3"}
        ]
      }
    }
  ],
  "users":[
    {
      "name": "myself",
      "user": {}
    },
    {
      "name": "e2e",
      "user": {"username": "admin", "password": "secret"}
    }
  ]
}
```

{{< table caption="توابع، پارامترهای آن‌ها، نمونه‌ای از فراخوانی و نتیجه" >}}
تابع            | توضیح                  | مثال                                                         | نتیجه
--------------------|------------------------------|-----------------------------------------------------------------|------------------
`text`              | متن ساده               | `kind is {.kind}`                                               | `kind is List`
`@`                 | آبجکت جاری           | `{@}`                                                           | همان ورودی
`.` یا `[]`         | عملگر فرزند               | `{.kind}`، `{['kind']}` یا `{['name\.type']}`                   | `List`
`..`                | پیمایش بازگشتی (recursive descent)            | `{..name}`                                                      | `127.0.0.1 127.0.0.2 myself e2e`
`*`                 | نویسه عام (wildcard)؛ همه آبجکت‌ها را برمی‌گرداند    | `{.items[*].metadata.name}`                                     | `[127.0.0.1 127.0.0.2]`
`[start:end:step]` | عملگر اندیس           | `{.users[0].name}`                                              | `myself`
`[,]`               | عملگر اجتماع               | `{.items[*]['metadata.name', 'status.capacity']}`               | `127.0.0.1 127.0.0.2 map[cpu:4] map[cpu:8]`
`?()`               | فیلتر                       | `{.users[?(@.name=="e2e")].user.password}`                      | `secret`
`range`، `end`      | پیمایش فهرست                 | `{range .items[*]}[{.metadata.name}, {.status.capacity}] {end}` | `[127.0.0.1, map[cpu:4]] [127.0.0.2, map[cpu:8]]`
`''`                | نقل‌قول برای رشته تفسیرشده     | `{range .items[*]}{.metadata.name}{'\t'}{end}`                  | `127.0.0.1      127.0.0.2`
`\`                 | گریز از نویسه پایان‌دهنده | `{.items[0].metadata.labels.kubernetes\.io/hostname}`           | `127.0.0.1`
{{< /table >}}

## استفاده از عبارت‌های JSONPath با kubectl {#use-with-kubectl}

چند مثال از به‌کارگیری `kubectl` همراه با عبارت‌های JSONPath:

```shell
kubectl get pods -o json
kubectl get pods -o=jsonpath='{@}'
kubectl get pods -o=jsonpath='{.items[0]}'
kubectl get pods -o=jsonpath='{.items[0].metadata.name}'
kubectl get pods -o=jsonpath="{.items[*]['metadata.name', 'status.capacity']}"
kubectl get pods -o=jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.startTime}{"\n"}{end}'
kubectl get pods -o=jsonpath='{.items[0].metadata.labels.kubernetes\.io/hostname}'
```

یا با یک Pod به نام «my_pod» در فضای نام «my_namespace» (این نام‌ها را مطابق محیط خود تغییر دهید):

```shell
kubectl get pod/my_pod -n my_namespace -o=jsonpath='{@}'
kubectl get pod/my_pod -n my_namespace -o=jsonpath='{.metadata.name}'
kubectl get pod/my_pod -n my_namespace -o=jsonpath='{.status}'
```

{{< note >}}
در ویندوز، هر قالب JSONPath را که شامل فاصله باشد باید درون نقل‌قول _دوتایی_ قرار دهید (نه نقل‌قول تکی، آن‌گونه که در مثال‌های بالا برای bash نشان داده شد). در نتیجه، برای هر مقدار لفظی (literal) درون قالب باید از نقل‌قول تکی یا نقل‌قول دوتایی گریزداده‌شده استفاده کنید. برای مثال:

```cmd
kubectl get pods -o=jsonpath="{range .items[*]}{.metadata.name}{'\t'}{.status.startTime}{'\n'}{end}"
kubectl get pods -o=jsonpath="{range .items[*]}{.metadata.name}{\"\t\"}{.status.startTime}{\"\n\"}{end}"
```
{{< /note >}}

## عبارت‌های منظم در JSONPath

از عبارت‌های منظم (regular expressions) در JSONPath پشتیبانی نمی‌شود. اگر می‌خواهید تطبیق را با عبارت‌های منظم انجام دهید، می‌توانید از ابزاری مانند `jq` استفاده کنید.

```shell
# kubectl does not support regular expressions for JSONpath output
# The following command does not work
kubectl get pods -o jsonpath='{.items[?(@.metadata.name=~/^test$/)].metadata.name}'

# The following command achieves the desired result
kubectl get pods -o json | jq -r '.items[] | select(.metadata.name | test("test-")).metadata.name'
```
