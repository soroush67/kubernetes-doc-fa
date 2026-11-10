---
title: کتابخانه‌های کلاینت
reviewers:
- ahmetb
content_type: concept
weight: 30
---

<!-- overview -->
این صفحه مروری بر کتابخانه‌های کلاینت (client libraries) ارائه می‌دهد که برای استفاده از API کوبرنتیز در زبان‌های برنامه‌نویسی گوناگون در دسترس هستند.


<!-- body -->
برای نوشتن برنامه‌هایی که از [REST API کوبرنتیز](/docs/reference/using-api/) استفاده می‌کنند، لازم نیست فراخوانی‌های API و انواع درخواست و پاسخ را خودتان پیاده‌سازی کنید. می‌توانید از یک کتابخانهٔ کلاینت برای زبان برنامه‌نویسی موردنظرتان استفاده کنید.

کتابخانه‌های کلاینت معمولاً کارهای رایجی مانند احراز هویت را برای شما انجام می‌دهند. اگر کلاینت API درون کلاستر کوبرنتیز اجرا شود، بیشتر کتابخانه‌های کلاینت می‌توانند Service Account کوبرنتیز را شناسایی کنند و از آن برای احراز هویت بهره بگیرند. همچنین می‌توانند قالب [فایل kubeconfig](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) را تفسیر کنند تا اعتبارنامه‌ها و نشانی API Server را از آن بخوانند.

## کتابخانه‌های کلاینت کوبرنتیز با پشتیبانی رسمی

نگهداری کتابخانه‌های کلاینت زیر به‌طور رسمی بر عهدهٔ [Kubernetes SIG API Machinery](https://github.com/kubernetes/community/tree/main/sig-api-machinery) است.


| زبان   | کتابخانهٔ کلاینت | برنامه‌های نمونه |
|------------|----------------|-----------------|
| C          | [github.com/kubernetes-client/c](https://github.com/kubernetes-client/c/) | [مشاهده](https://github.com/kubernetes-client/c/tree/master/examples)
| dotnet     | [github.com/kubernetes-client/csharp](https://github.com/kubernetes-client/csharp) | [مشاهده](https://github.com/kubernetes-client/csharp/tree/master/examples)
| Go         | [github.com/kubernetes/client-go/](https://github.com/kubernetes/client-go/) | [مشاهده](https://github.com/kubernetes/client-go/tree/master/examples)
| Haskell    | [github.com/kubernetes-client/haskell](https://github.com/kubernetes-client/haskell) | [مشاهده](https://github.com/kubernetes-client/haskell/tree/master/kubernetes-client/example)
| Java       | [github.com/kubernetes-client/java](https://github.com/kubernetes-client/java/) | [مشاهده](https://github.com/kubernetes-client/java/tree/master/examples)
| JavaScript | [github.com/kubernetes-client/javascript](https://github.com/kubernetes-client/javascript) | [مشاهده](https://github.com/kubernetes-client/javascript/tree/master/examples)
| Perl       | [github.com/kubernetes-client/perl/](https://github.com/kubernetes-client/perl/) | [مشاهده](https://github.com/kubernetes-client/perl/tree/master/examples)
| Python     | [github.com/kubernetes-client/python/](https://github.com/kubernetes-client/python/) | [مشاهده](https://github.com/kubernetes-client/python/tree/master/examples)
| Ruby       | [github.com/kubernetes-client/ruby/](https://github.com/kubernetes-client/ruby/) | [مشاهده](https://github.com/kubernetes-client/ruby/tree/master/examples)

## کتابخانه‌های کلاینت نگهداری‌شده به‌دست جامعه

{{% thirdparty-content %}}

کتابخانه‌های کلاینت API کوبرنتیز که در ادامه آمده‌اند، به‌دست نویسندگانشان ارائه و نگهداری می‌شوند، نه تیم کوبرنتیز.

| زبان             | کتابخانهٔ کلاینت                           |
| -------------------- | ---------------------------------------- |
| Clojure              | [github.com/yanatan16/clj-kubernetes-api](https://github.com/yanatan16/clj-kubernetes-api) |
| DotNet               | [github.com/tonnyeremin/kubernetes_gen](https://github.com/tonnyeremin/kubernetes_gen) |
| DotNet (RestSharp)   | [github.com/masroorhasan/Kubernetes.DotNet](https://github.com/masroorhasan/Kubernetes.DotNet) |
| Elixir               | [github.com/obmarg/kazan](https://github.com/obmarg/kazan/) |
| Elixir               | [github.com/coryodaniel/k8s](https://github.com/coryodaniel/k8s) |
| Java (OSGi)          | [bitbucket.org/amdatulabs/amdatu-kubernetes](https://bitbucket.org/amdatulabs/amdatu-kubernetes) |
| Java (Fabric8, OSGi) | [github.com/fabric8io/kubernetes-client](https://github.com/fabric8io/kubernetes-client) |
| Java                 | [github.com/manusa/yakc](https://github.com/manusa/yakc) |
| Lisp                 | [github.com/brendandburns/cl-k8s](https://github.com/brendandburns/cl-k8s) |
| Lisp                 | [github.com/xh4/cube](https://github.com/xh4/cube) |
| Node.js (TypeScript) | [github.com/Goyoo/node-k8s-client](https://github.com/Goyoo/node-k8s-client) |
| Node.js              | [github.com/ajpauwels/easy-k8s](https://github.com/ajpauwels/easy-k8s)
| Node.js              | [github.com/godaddy/kubernetes-client](https://github.com/godaddy/kubernetes-client) |
| Node.js              | [github.com/tenxcloud/node-kubernetes-client](https://github.com/tenxcloud/node-kubernetes-client) |
| Perl                 | [metacpan.org/pod/Net::Kubernetes](https://metacpan.org/pod/Net::Kubernetes) |
| PHP                  | [github.com/allansun/kubernetes-php-client](https://github.com/allansun/kubernetes-php-client) |
| PHP                  | [github.com/maclof/kubernetes-client](https://github.com/maclof/kubernetes-client) |
| PHP                  | [github.com/travisghansen/kubernetes-client-php](https://github.com/travisghansen/kubernetes-client-php) |
| PHP                  | [github.com/renoki-co/php-k8s](https://github.com/renoki-co/php-k8s) |
| Python               | [github.com/cloudcoil/cloudcoil](https://github.com/cloudcoil/cloudcoil) |
| Python               | [github.com/fiaas/k8s](https://github.com/fiaas/k8s) |
| Python               | [github.com/gtsystem/lightkube](https://github.com/gtsystem/lightkube) |
| Python               | [github.com/kr8s-org/kr8s](https://github.com/kr8s-org/kr8s) |
| Python               | [github.com/mnubo/kubernetes-py](https://github.com/mnubo/kubernetes-py) |
| Python               | [github.com/puzl-cloud/kubesdk](https://github.com/puzl-cloud/kubesdk) |
| Python               | [github.com/tomplus/kubernetes_asyncio](https://github.com/tomplus/kubernetes_asyncio) |
| Python               | [github.com/Frankkkkk/pykorm](https://github.com/Frankkkkk/pykorm) |
| Ruby                 | [github.com/abonas/kubeclient](https://github.com/abonas/kubeclient) |
| Ruby                 | [github.com/k8s-ruby/k8s-ruby](https://github.com/k8s-ruby/k8s-ruby) |
| Ruby                 | [github.com/kontena/k8s-client](https://github.com/kontena/k8s-client) |
| Rust                 | [github.com/kube-rs/kube](https://github.com/kube-rs/kube) |
| Rust                 | [github.com/ynqa/kubernetes-rust](https://github.com/ynqa/kubernetes-rust) |
| Scala                | [github.com/hagay3/skuber](https://github.com/hagay3/skuber) |
| Scala                | [github.com/hnaderi/scala-k8s](https://github.com/hnaderi/scala-k8s) |
| Scala                | [github.com/joan38/kubernetes-client](https://github.com/joan38/kubernetes-client) |
| Swift                | [github.com/swiftkube/client](https://github.com/swiftkube/client) |
