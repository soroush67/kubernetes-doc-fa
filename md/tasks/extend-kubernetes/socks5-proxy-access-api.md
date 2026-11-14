---
title: استفاده از پراکسی SOCKS5 برای دسترسی به API کوبرنتیز
content_type: task
weight: 42
min-kubernetes-server-version: v1.24
---
<!-- overview -->

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

این صفحه نشان می‌دهد که چگونه با یک پراکسی SOCKS5 به API یک کلاستر کوبرنتیز راه دور دسترسی پیدا کنید.
این روش زمانی مفید است که کلاستر موردنظر، API خود را مستقیماً روی اینترنت عمومی در دسترس قرار نداده باشد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

به نرم‌افزار کلاینت SSH (ابزار `ssh`) و یک سرویس SSH در حال اجرا روی سرور راه دور نیاز دارید.
همچنین باید بتوانید به سرویس SSH روی سرور راه دور وارد شوید.

<!-- steps -->

## زمینهٔ کار

{{< note >}}
در این مثال، ترافیک از طریق SSH تونل می‌شود و کلاینت و سرور SSH نقش پراکسی SOCKS را ایفا می‌کنند.
به‌جای آن می‌توانید از هر نوع دیگری از پراکسی‌های [SOCKS5](https://en.wikipedia.org/wiki/SOCKS#SOCKS5) استفاده کنید.
{{</ note >}}

شکل ۱ آنچه را که در این کار به آن دست خواهید یافت نشان می‌دهد.

* یک رایانهٔ کلاینت دارید که در مراحل بعد «محلی» نامیده می‌شود و از آن برای ارسال درخواست به API کوبرنتیز استفاده خواهید کرد.
* سرور یا API کوبرنتیز روی یک سرور راه دور میزبانی می‌شود.
* با استفاده از نرم‌افزار کلاینت و سرور SSH، یک تونل امن SOCKS5 میان رایانهٔ محلی و سرور راه دور ایجاد
  خواهید کرد. ترافیک HTTPS میان کلاینت و API کوبرنتیز از درون تونل SOCKS5 عبور می‌کند و این تونل
  نیز خود از طریق SSH تونل می‌شود.

{{< mermaid >}}
graph LR;

  subgraph local[Local client machine]
  client([client])-. local <br> traffic .->  local_ssh[Local SSH <br> SOCKS5 proxy];
  end
  local_ssh[SSH <br>SOCKS5 <br> proxy]-- SSH Tunnel -->sshd
  
  subgraph remote[Remote server]
  sshd[SSH <br> server]-- local traffic -->service1;
  end
  client([client])-. proxied HTTPs traffic <br> going through the proxy .->service1[Kubernetes API];

  classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
  classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
  classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
  class ingress,service1,service2,pod1,pod2,pod3,pod4 k8s;
  class client plain;
  class cluster cluster;
{{</ mermaid >}}
شکل ۱. اجزای آموزش SOCKS5

## استفاده از ssh برای ایجاد پراکسی SOCKS5

فرمان زیر یک پراکسی SOCKS5 میان رایانهٔ کلاینت شما و سرور SOCKS راه دور راه‌اندازی می‌کند:

```shell
# The SSH tunnel continues running in the foreground after you run this
ssh -D 1080 -q -N username@kubernetes-remote-server.example
```

پراکسی SOCKS5 با پیکربندی زیر امکان اتصال به سرور API کلاستر را برای شما فراهم می‌کند:
* گزینهٔ `-D 1080`: یک پراکسی SOCKS روی پورت محلی ‎:1080 باز می‌کند.
* گزینهٔ `-q`: حالت بی‌صدا؛ باعث می‌شود بیشتر پیام‌های هشدار و عیب‌یابی نمایش داده نشوند.
* گزینهٔ `-N`: هیچ فرمانی را در سمت راه دور اجرا نمی‌کند. این گزینه برای زمانی مفید است که فقط می‌خواهید پورت‌ها را هدایت (forward) کنید.
* مقدار `username@kubernetes-remote-server.example`: سرور SSH راه دوری است که کلاستر کوبرنتیز پشت آن
  اجرا می‌شود (برای مثال، یک میزبان bastion).

## پیکربندی کلاینت

برای دسترسی به سرور API کوبرنتیز از طریق پراکسی، باید به `kubectl` اعلام کنید که درخواست‌ها را از طریق
پراکسی `SOCKS` که پیش‌تر ایجاد کردیم ارسال کند. این کار را می‌توانید یا با تنظیم متغیر محیطی مناسب
و یا با استفاده از ویژگی `proxy-url` در فایل kubeconfig انجام دهید. استفاده از متغیر محیطی:

```shell
export HTTPS_PROXY=socks5://localhost:1080
```

برای اینکه این تنظیم همواره در یک context مشخص از `kubectl` به کار رود، ویژگی `proxy-url` را در مدخل
`cluster` مربوطه در فایل `~/.kube/config` مشخص کنید. برای مثال:

```yaml
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LRMEMMW2 # shortened for readability 
    server: https://<API_SERVER_IP_ADDRESS>:6443  # the "Kubernetes API" server, in other words the IP address of kubernetes-remote-server.example
    proxy-url: socks5://localhost:1080   # the "SSH SOCKS5 proxy" in the diagram above
  name: default
contexts:
- context:
    cluster: default
    user: default
  name: default
current-context: default
kind: Config
preferences: {}
users:
- name: default
  user:
    client-certificate-data: LS0tLS1CR== # shortened for readability
    client-key-data: LS0tLS1CRUdJT=      # shortened for readability
```

پس از آنکه تونل را با فرمان ssh که پیش‌تر گفته شد ایجاد کردید و متغیر محیطی یا ویژگی `proxy-url` را
تعریف کردید، می‌توانید از طریق این پراکسی با کلاستر خود تعامل داشته باشید. برای مثال:

```shell
kubectl get pods
```

```console
NAMESPACE     NAME                                     READY   STATUS      RESTARTS   AGE
kube-system   coredns-85cb69466-klwq8                  1/1     Running     0          5m46s
```

{{< note >}}
- پیش از نسخهٔ 1.24 ابزار `kubectl`، بیشتر فرمان‌های `kubectl` هنگام استفاده از پراکسی socks کار می‌کردند، به‌جز `kubectl exec`.
- ابزار `kubectl` از هر دو متغیر محیطی `HTTPS_PROXY` و `https_proxy` پشتیبانی می‌کند. این متغیرها را
  برنامه‌های دیگری که از SOCKS پشتیبانی می‌کنند، مانند `curl`، نیز به کار می‌برند. بنابراین در برخی موارد
  بهتر است متغیر محیطی را در همان خط فرمان تعریف کنید:
  ```shell
  HTTPS_PROXY=socks5://localhost:1080 kubectl get pods
  ```
- هنگام استفاده از `proxy-url`، پراکسی فقط برای context مربوطه در `kubectl` به کار می‌رود،
  در حالی که متغیر محیطی بر همهٔ contextها اثر می‌گذارد.
- برای محافظت بیشتر از نام میزبان سرور API کوبرنتیز در برابر نشت DNS، می‌توانید به‌جای پروتکل رایج‌تر `socks5`
  که در بالا نشان داده شد، از نام پروتکل `socks5h` استفاده کنید. در این حالت، `kubectl` به‌جای آنکه نام دامنهٔ
  سرور API کوبرنتیز را روی سیستمی که `kubectl` را اجرا می‌کند resolve کند، این کار را از سرور پراکسی (مانند یک
  bastion مبتنی بر ssh) می‌خواهد. همچنین توجه کنید که با `socks5h`، نشانی سرور API کوبرنتیز مانند `https://localhost:6443/api`
  به رایانهٔ کلاینت محلی شما اشاره نمی‌کند، بلکه به `localhost` از دید سرور پراکسی (مثلاً همان bastion مبتنی بر ssh) اشاره دارد.
{{</ note >}}


## پاک‌سازی

فرایند هدایت پورت ssh را با فشردن `CTRL+C` در ترمینالی که در آن اجرا می‌شود متوقف کنید.

برای توقف هدایت ترافیک http از طریق پراکسی، در یک ترمینال فرمان `unset https_proxy` را وارد کنید.

## مطالعهٔ بیشتر

* [کلاینت ورود از راه دور OpenSSH](https://man.openbsd.org/ssh)
