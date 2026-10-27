---
title: مدیریت بارهای کاری
content_type: concept
reviewers:
- janetkuo
weight: 40
---

<!-- overview -->

برنامه خود را مستقر کرده‌اید و آن را از طریق یک Service در دسترس قرار داده‌اید. اکنون چه باید کرد؟ کوبرنتیز
ابزارهای متعددی برای کمک به مدیریت استقرار برنامه شما، از جمله مقیاس‌دهی و به‌روزرسانی، فراهم می‌کند.

<!-- body -->

## سازمان‌دهی پیکربندی‌های منابع

بسیاری از برنامه‌ها نیاز دارند چندین منبع ایجاد شود، مانند یک Deployment همراه با یک Service.
مدیریت چندین منبع را می‌توان با گروه‌بندی آن‌ها در یک فایل واحد
(که در YAML با `---` از هم جدا می‌شوند) ساده‌تر کرد. برای مثال:

{{% code_sample file="application/nginx-app.yaml" %}}

چندین منبع را می‌توان به همان روشی ایجاد کرد که یک منبع واحد ایجاد می‌شود:

```shell
kubectl apply -f https://k8s.io/examples/application/nginx-app.yaml
```

```none
service/my-nginx-svc created
deployment.apps/my-nginx created
```

منابع به همان ترتیبی که در مانیفست آمده‌اند ایجاد می‌شوند. بنابراین بهتر است
ابتدا Service را مشخص کنید، زیرا این کار تضمین می‌کند که زمان‌بند بتواند Podهای مرتبط
با Service را هنگامی که توسط کنترل‌کننده(ها)، مانند Deployment، ایجاد می‌شوند، توزیع کند.

`kubectl apply` چندین آرگومان `-f` را نیز می‌پذیرد:

```shell
kubectl apply -f https://k8s.io/examples/application/nginx/nginx-svc.yaml \
  -f https://k8s.io/examples/application/nginx/nginx-deployment.yaml
```


یک شیوه توصیه‌شده این است که منابع مرتبط با یک میکروسرویس یا لایه برنامه را
در یک فایل قرار دهید و همه فایل‌های مرتبط با برنامه خود را در یک
دایرکتوری گروه‌بندی کنید. اگر لایه‌های برنامه شما با استفاده از DNS به یکدیگر متصل می‌شوند، می‌توانید همه
مؤلفه‌های پشته (stack) خود را با هم مستقر کنید.

یک URL را نیز می‌توان به‌عنوان منبع پیکربندی مشخص کرد که برای استقرار مستقیم از
مانیفست‌های موجود در سیستم کنترل نسخه شما سودمند است:

```shell
kubectl apply -f https://k8s.io/examples/application/nginx/nginx-deployment.yaml
```

```none
deployment.apps/my-nginx created
```

اگر نیاز به تعریف مانیفست‌های بیشتری دارید، مانند افزودن یک ConfigMap، این کار را نیز می‌توانید انجام دهید.

### ابزارهای خارجی

این بخش تنها رایج‌ترین ابزارهایی را فهرست می‌کند که برای مدیریت بارهای کاری روی کوبرنتیز استفاده می‌شوند. برای دیدن فهرستی بزرگ‌تر، بخش
[Application definition and image build](https://landscape.cncf.io/guide#app-definition-and-development--application-definition-image-build)
را در Landscape مربوط به {{< glossary_tooltip text="CNCF" term_id="cncf" >}} ببینید.

#### Helm {#external-tool-helm}

{{% thirdparty-content single="true" %}}

[Helm](https://helm.sh/) ابزاری برای مدیریت بسته‌هایی از منابع از پیش پیکربندی‌شده
کوبرنتیز است. این بسته‌ها با نام _Helm chart_ شناخته می‌شوند.

#### Kustomize {#external-tool-kustomize}

[Kustomize](https://kustomize.io/) یک مانیفست کوبرنتیز را پیمایش می‌کند تا گزینه‌های پیکربندی را اضافه، حذف یا به‌روزرسانی کند.
این ابزار هم به‌صورت یک فایل اجرایی مستقل و هم به‌عنوان یک [قابلیت داخلی](/docs/tasks/manage-kubernetes-objects/kustomization/)
kubectl در دسترس است.

## عملیات انبوه در kubectl

ایجاد منابع تنها عملیاتی نیست که `kubectl` می‌تواند به‌صورت انبوه انجام دهد. این ابزار همچنین می‌تواند
نام منابع را از فایل‌های پیکربندی استخراج کند تا عملیات دیگری انجام دهد؛ به‌ویژه برای
حذف همان منابعی که ایجاد کرده‌اید:

```shell
kubectl delete -f https://k8s.io/examples/application/nginx-app.yaml
```

```none
deployment.apps "my-nginx" deleted
service "my-nginx-svc" deleted
```

در مورد دو منبع، می‌توانید هر دو منبع را با استفاده از نحو
resource/name در خط فرمان مشخص کنید:

```shell
kubectl delete deployments/my-nginx services/my-nginx-svc
```

برای تعداد بیشتری از منابع، ساده‌تر است که انتخابگر (پرس‌وجوی برچسب) را
با استفاده از `-l` یا `--selector` مشخص کنید تا منابع بر اساس برچسب‌هایشان فیلتر شوند:

```shell
kubectl delete deployment,services -l app=nginx
```

```none
deployment.apps "my-nginx" deleted
service "my-nginx-svc" deleted
```

### زنجیره‌سازی و فیلتر کردن

از آنجا که `kubectl` نام منابع را با همان نحوی که می‌پذیرد در خروجی چاپ می‌کند، می‌توانید عملیات را
با استفاده از `$()` یا `xargs` به هم زنجیر کنید:

```shell
kubectl get $(kubectl create -f docs/concepts/cluster-administration/nginx/ -o name | grep service/ )
kubectl create -f docs/concepts/cluster-administration/nginx/ -o name | grep service/ | xargs -i kubectl get '{}'
```

خروجی ممکن است مشابه زیر باشد:

```none
NAME           TYPE           CLUSTER-IP   EXTERNAL-IP   PORT(S)      AGE
my-nginx-svc   LoadBalancer   10.0.0.208   <pending>     80/TCP       0s
```

با فرمان‌های بالا، ابتدا منابعی را زیر `docs/concepts/cluster-administration/nginx/` ایجاد می‌کنید و
منابع ایجادشده را با قالب خروجی `-o name` چاپ می‌کنید (هر منبع به شکل resource/name چاپ می‌شود).
سپس تنها Service را با `grep` جدا می‌کنید و آن را با [`kubectl get`](/docs/reference/kubectl/generated/kubectl_get/) چاپ می‌کنید.

### عملیات بازگشتی روی فایل‌های محلی

اگر منابع خود را در چندین زیردایرکتوری درون یک دایرکتوری مشخص سازمان‌دهی کرده باشید،
می‌توانید با مشخص کردن `--recursive` یا `-R` در کنار آرگومان `--filename`/`-f`،
عملیات را به‌صورت بازگشتی روی زیردایرکتوری‌ها نیز انجام دهید.

برای نمونه، فرض کنید دایرکتوری `project/k8s/development` وجود دارد که همه
{{< glossary_tooltip text="مانیفست‌های" term_id="manifest" >}} لازم برای محیط توسعه را در خود دارد
و بر اساس نوع منبع سازمان‌دهی شده است:

```none
project/k8s/development
├── configmap
│   └── my-configmap.yaml
├── deployment
│   └── my-deployment.yaml
└── pvc
    └── my-pvc.yaml
```

به‌طور پیش‌فرض، انجام یک عملیات انبوه روی `project/k8s/development` در سطح اول
دایرکتوری متوقف می‌شود و هیچ زیردایرکتوری‌ای را پردازش نمی‌کند. اگر تلاش می‌کردید منابع این
دایرکتوری را با استفاده از فرمان زیر ایجاد کنید، با خطا مواجه می‌شدیم:

```shell
kubectl apply -f project/k8s/development
```

```none
error: you must provide one or more resources by argument or filename (.json|.yaml|.yml|stdin)
```

به‌جای آن، آرگومان خط فرمان `--recursive` یا `-R` را همراه با آرگومان `--filename`/`-f` مشخص کنید:

```shell
kubectl apply -f project/k8s/development --recursive
```

```none
configmap/my-config created
deployment.apps/my-deployment created
persistentvolumeclaim/my-pvc created
```

آرگومان `--recursive` با هر عملیاتی که آرگومان `--filename`/`-f` را می‌پذیرد کار می‌کند، مانند:
`kubectl create`، `kubectl get`، `kubectl delete`، `kubectl describe` یا حتی `kubectl rollout`.

آرگومان `--recursive` زمانی که چندین آرگومان `-f` ارائه شود نیز کار می‌کند:

```shell
kubectl apply -f project/k8s/namespaces -f project/k8s/development --recursive
```

```none
namespace/development created
namespace/staging created
configmap/my-config created
deployment.apps/my-deployment created
persistentvolumeclaim/my-pvc created
```

اگر علاقه‌مندید درباره `kubectl` بیشتر بدانید، بخش
[ابزار خط فرمان (kubectl)](/docs/reference/kubectl/) را بخوانید.

## به‌روزرسانی برنامه بدون قطعی

در مقطعی سرانجام نیاز خواهید داشت برنامه مستقرشده خود را به‌روزرسانی کنید؛ معمولاً با مشخص کردن
یک ایمیج یا تگ ایمیج جدید. `kubectl` از چندین عملیات به‌روزرسانی پشتیبانی می‌کند که هر کدام
برای سناریوهای متفاوتی کاربرد دارند.

می‌توانید چندین نسخه از برنامه خود را اجرا کنید و از یک _rollout_ برای انتقال تدریجی ترافیک به
Podهای سالم جدید استفاده کنید. در نهایت، همه Podهای در حال اجرا نرم‌افزار جدید را خواهند داشت.

این بخش از صفحه شما را در ایجاد و به‌روزرسانی برنامه‌ها با Deploymentها راهنمایی می‌کند.

فرض کنید نسخه 1.14.2 از nginx را اجرا می‌کردید:

```shell
kubectl create deployment my-nginx --image=nginx:1.14.2
```

```none
deployment.apps/my-nginx created
```

اطمینان حاصل کنید که 1 replica وجود دارد:

```shell
kubectl scale --replicas 1 deployments/my-nginx --subresource='scale' --type='merge' -p '{"spec":{"replicas": 1}}'
```

```none
deployment.apps/my-nginx scaled
```

و با تنظیم _حداکثر افزایش موقت (surge maximum)_ روی 100٪، به کوبرنتیز اجازه دهید در طول یک rollout،
replicaهای موقت بیشتری اضافه کند:

```shell
kubectl patch --type='merge' -p '{"spec":{"strategy":{"rollingUpdate":{"maxSurge": "100%" }}}}'
```

```none
deployment.apps/my-nginx patched
```

برای به‌روزرسانی به نسخه 1.16.1، مقدار `.spec.template.spec.containers[0].image` را با استفاده از `kubectl edit`
از `nginx:1.14.2` به `nginx:1.16.1` تغییر دهید:

```shell
kubectl edit deployment/my-nginx
# Change the manifest to use the newer container image, then save your changes
```

همین! Deployment به‌صورت اعلانی و در پس‌زمینه، برنامه nginx مستقرشده را به‌تدریج
به‌روزرسانی می‌کند. این کار تضمین می‌کند که تنها تعداد مشخصی از replicaهای قدیمی در حین به‌روزرسانی
از دسترس خارج شوند و تنها تعداد مشخصی از replicaهای جدید بیش از تعداد مطلوب
Podها ایجاد شوند. برای آشنایی با جزئیات بیشتر درباره نحوه انجام این کار،
به [Deployment](/docs/concepts/workloads/controllers/deployment/) مراجعه کنید.

می‌توانید از rolloutها با DaemonSetها، Deploymentها یا StatefulSetها استفاده کنید.

### مدیریت rolloutها

می‌توانید از [`kubectl rollout`](/docs/reference/kubectl/generated/kubectl_rollout/) برای مدیریت
به‌روزرسانی تدریجی یک برنامه موجود استفاده کنید.

برای مثال:

```shell
kubectl apply -f my-deployment.yaml

# wait for rollout to finish
kubectl rollout status deployment/my-deployment --timeout 10m # 10 minute timeout
```

یا

```shell
kubectl apply -f backing-stateful-component.yaml

# don't wait for rollout to finish, just check the status
kubectl rollout status statefulsets/backing-stateful-component --watch=false
```

همچنین می‌توانید یک rollout را متوقف، از سر گرفته یا لغو کنید.
برای اطلاعات بیشتر به [`kubectl rollout`](/docs/reference/kubectl/generated/kubectl_rollout/) مراجعه کنید.

## استقرارهای Canary

سناریوی دیگری که در آن به چندین برچسب نیاز است، تمایز قائل شدن میان استقرارهای نسخه‌های انتشار
یا پیکربندی‌های متفاوت یک مؤلفه است. رویه‌ای رایج است که یک *canary* از یک
نسخه انتشار جدید برنامه (که از طریق تگ ایمیج در قالب Pod مشخص می‌شود) در کنار
نسخه انتشار قبلی مستقر شود تا نسخه جدید بتواند پیش از rollout کامل،
ترافیک واقعی محیط عملیاتی را دریافت کند.

برای نمونه، می‌توانید از برچسب `track` برای تمایز میان نسخه‌های انتشار مختلف استفاده کنید.

نسخه انتشار اصلی و پایدار، برچسب `track` با مقدار `stable` خواهد داشت:

```none
name: frontend
replicas: 3
...
labels:
   app: guestbook
   tier: frontend
   track: stable
...
image: gb-frontend:v3
```

و سپس می‌توانید نسخه انتشار جدیدی از frontend برنامه guestbook ایجاد کنید که برچسب `track` را
با مقدار متفاوتی (یعنی `canary`) دارد، تا دو مجموعه Pod با هم هم‌پوشانی نداشته باشند:

```none
name: frontend-canary
replicas: 1
...
labels:
   app: guestbook
   tier: frontend
   track: canary
...
image: gb-frontend:v4
```

سرویس frontend با انتخاب زیرمجموعه مشترک برچسب‌های هر دو مجموعه replica
(یعنی حذف برچسب `track`)، هر دو مجموعه را پوشش می‌دهد تا ترافیک به هر دو
برنامه هدایت شود:

```yaml
selector:
   app: guestbook
   tier: frontend
```

می‌توانید تعداد replicaهای نسخه‌های انتشار پایدار و canary را تنظیم کنید تا نسبت
ترافیک واقعی محیط عملیاتی که هر نسخه دریافت می‌کند تعیین شود (در این مثال 3:1).
پس از اطمینان یافتن، می‌توانید مسیر پایدار را به نسخه انتشار جدید برنامه به‌روزرسانی کنید و
canary را حذف کنید.

برای آشنایی با مراحل کار، آموزش [استقرار یک نسخه انتشار با استفاده از Canary Deployment](/docs/tutorials/stateless-application/canary-deployment/) را دنبال کنید.

## به‌روزرسانی حاشیه‌نویسی‌ها

گاهی ممکن است بخواهید حاشیه‌نویسی‌هایی (annotation) به منابع متصل کنید. حاشیه‌نویسی‌ها فراداده‌های دلخواه و
غیرشناسایی‌کننده‌ای هستند که کلاینت‌های API مانند ابزارها یا کتابخانه‌ها آن‌ها را بازیابی می‌کنند.
این کار را می‌توان با `kubectl annotate` انجام داد. برای مثال:

```shell
kubectl annotate pods my-nginx-v4-9gw19 description='my frontend running nginx'
kubectl get pods my-nginx-v4-9gw19 -o yaml
```

```shell
apiVersion: v1
kind: pod
metadata:
  annotations:
    description: my frontend running nginx
...
```

برای اطلاعات بیشتر، به [حاشیه‌نویسی‌ها](/docs/concepts/overview/working-with-objects/annotations/)
و [kubectl annotate](/docs/reference/kubectl/generated/kubectl_annotate/) مراجعه کنید.

## مقیاس‌دهی برنامه

هنگامی که بار روی برنامه شما افزایش یا کاهش می‌یابد، از `kubectl` برای مقیاس‌دهی برنامه خود استفاده کنید.
برای نمونه، برای کاهش تعداد replicaهای nginx از 3 به 1، این فرمان را اجرا کنید:

```shell
kubectl scale deployment/my-nginx --replicas=1
```

```none
deployment.apps/my-nginx scaled
```

اکنون تنها یک Pod دارید که توسط deployment مدیریت می‌شود.

```shell
kubectl get pods -l app=my-nginx
```

```none
NAME                        READY     STATUS    RESTARTS   AGE
my-nginx-2035384211-j5fhi   1/1       Running   0          30m
```

برای اینکه سیستم به‌طور خودکار تعداد replicaهای nginx را بر حسب نیاز،
در بازه 1 تا 3، انتخاب کند، این فرمان را اجرا کنید:

```shell
# This requires an existing source of container and Pod metrics
kubectl autoscale deployment/my-nginx --min=1 --max=3
```

```none
horizontalpodautoscaler.autoscaling/my-nginx autoscaled
```

اکنون مقیاس replicaهای nginx شما به‌طور خودکار و بر حسب نیاز افزایش و کاهش می‌یابد.

برای اطلاعات بیشتر، لطفاً به مستندات [kubectl scale](/docs/reference/kubectl/generated/kubectl_scale/)،
[kubectl autoscale](/docs/reference/kubectl/generated/kubectl_autoscale/) و
[horizontal pod autoscaler](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) مراجعه کنید.

## به‌روزرسانی درجای منابع

گاهی لازم است به‌روزرسانی‌های محدود و بدون اختلال روی منابعی که ایجاد کرده‌اید انجام دهید.

### kubectl apply

پیشنهاد می‌شود مجموعه‌ای از فایل‌های پیکربندی را در سیستم کنترل نسخه نگهداری کنید
(به [پیکربندی به‌عنوان کد](https://martinfowler.com/bliki/InfrastructureAsCode.html) مراجعه کنید)،
تا بتوان آن‌ها را همراه با کد منابعی که پیکربندی می‌کنند نگهداری و نسخه‌بندی کرد.
سپس می‌توانید از [`kubectl apply`](/docs/reference/kubectl/generated/kubectl_apply/)
برای ارسال تغییرات پیکربندی خود به کلاستر استفاده کنید.

این فرمان نسخه پیکربندی‌ای را که ارسال می‌کنید با نسخه قبلی
مقایسه می‌کند و تغییراتی را که ایجاد کرده‌اید اعمال می‌کند، بدون آنکه تغییرات خودکار ویژگی‌هایی را
که مشخص نکرده‌اید بازنویسی کند.

```shell
kubectl apply -f https://k8s.io/examples/application/nginx/nginx-deployment.yaml
```

```none
deployment.apps/my-nginx configured
```

برای آشنایی بیشتر با سازوکار زیربنایی، [server-side apply](/docs/reference/using-api/server-side-apply/) را بخوانید.

### kubectl edit

به‌عنوان جایگزین، می‌توانید منابع را با [`kubectl edit`](/docs/reference/kubectl/generated/kubectl_edit/) نیز به‌روزرسانی کنید:

```shell
kubectl edit deployment/my-nginx
```

این کار معادل آن است که ابتدا منبع را با `get` دریافت کنید، آن را در ویرایشگر متن ویرایش کنید و سپس
منبع را با نسخه به‌روزشده `apply` کنید:

```shell
kubectl get deployment my-nginx -o yaml > /tmp/nginx.yaml
vi /tmp/nginx.yaml
# do some edit, and then save the file

kubectl apply -f /tmp/nginx.yaml
deployment.apps/my-nginx configured

rm /tmp/nginx.yaml
```

این روش به شما امکان می‌دهد تغییرات مهم‌تر را با سهولت بیشتری انجام دهید. توجه داشته باشید که می‌توانید ویرایشگر را
با متغیرهای محیطی `EDITOR` یا `KUBE_EDITOR` مشخص کنید.

برای اطلاعات بیشتر، لطفاً به [kubectl edit](/docs/reference/kubectl/generated/kubectl_edit/) مراجعه کنید.

### kubectl patch

می‌توانید از [`kubectl patch`](/docs/reference/kubectl/generated/kubectl_patch/) برای به‌روزرسانی درجای آبجکت‌های API استفاده کنید.
این زیرفرمان از JSON patch،
JSON merge patch و strategic merge patch پشتیبانی می‌کند.

برای جزئیات بیشتر، به
[به‌روزرسانی درجای آبجکت‌های API با استفاده از kubectl patch](/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/)
مراجعه کنید.

## به‌روزرسانی‌های مخرب

در برخی موارد ممکن است نیاز داشته باشید فیلدهایی از منبع را به‌روزرسانی کنید که پس از مقداردهی اولیه قابل به‌روزرسانی نیستند، یا
ممکن است بخواهید یک تغییر بازگشتی را بلافاصله اعمال کنید، مثلاً برای ترمیم Podهای معیوبی که توسط یک
Deployment ایجاد شده‌اند. برای تغییر چنین فیلدهایی، از `replace --force` استفاده کنید که منبع را حذف کرده و
دوباره ایجاد می‌کند. در این حالت، می‌توانید فایل پیکربندی اصلی خود را تغییر دهید:

```shell
kubectl replace -f https://k8s.io/examples/application/nginx/nginx-deployment.yaml --force
```

```none
deployment.apps/my-nginx deleted
deployment.apps/my-nginx replaced
```


## {{% heading "whatsnext" %}}

- با [نحوه استفاده از `kubectl` برای درون‌نگری و اشکال‌زدایی برنامه](/docs/tasks/debug/debug-application/debug-running-pod/) آشنا شوید.
