---
reviewers:
- janetkuo
title: Deploymentها
api_metadata:
- apiVersion: "apps/v1"
  kind: "Deployment"
feature:
  title: rolloutها و بازگشت‌های خودکار
  description: >
    کوبرنتیز تغییرات برنامه یا پیکربندی آن را به‌تدریج rollout می‌کند و در همان حال سلامت برنامه را پایش می‌کند تا اطمینان حاصل شود که همه‌ی نمونه‌های شما را هم‌زمان از بین نمی‌برد. اگر مشکلی پیش بیاید، کوبرنتیز تغییر را برای شما بازمی‌گرداند. از اکوسیستم رو به رشد راهکارهای استقرار بهره ببرید.
description: >-
  یک Deployment مجموعه‌ای از Podها را برای اجرای بار کاری یک برنامه مدیریت می‌کند؛ معمولاً برنامه‌ای که حالت (state) نگه نمی‌دارد.
content_type: concept
weight: 10
hide_summary: true # Listed separately in section index
---

<!-- overview -->

یک _Deployment_ به‌روزرسانی‌های اعلانی را برای {{< glossary_tooltip text="Podها" term_id="pod" >}} و
{{< glossary_tooltip term_id="replica-set" text="ReplicaSetها" >}} فراهم می‌کند.

شما یک _وضعیت مطلوب_ را در یک Deployment توصیف می‌کنید و {{< glossary_tooltip term_id="controller" >}} مربوط به Deployment وضعیت واقعی را با نرخی کنترل‌شده به وضعیت مطلوب تغییر می‌دهد. می‌توانید Deploymentها را طوری تعریف کنید که ReplicaSetهای جدید ایجاد کنند، یا Deploymentهای موجود را حذف کنند و همه‌ی منابع آن‌ها را با Deploymentهای جدید به فرزندی بپذیرند.

{{< note >}}
ReplicaSetهایی را که در مالکیت یک Deployment هستند مدیریت نکنید. اگر مورد استفاده‌ی شما در ادامه پوشش داده نشده است، باز کردن یک issue در مخزن اصلی کوبرنتیز را در نظر بگیرید.
{{< /note >}}

<!-- body -->

## مورد استفاده

موارد زیر کاربردهای معمول Deploymentها هستند:

* [یک Deployment ایجاد کنید تا یک ReplicaSet را rollout کند](#creating-a-deployment). ReplicaSet در پس‌زمینه Podها را ایجاد می‌کند. وضعیت rollout را بررسی کنید تا ببینید موفق بوده است یا نه.
* با به‌روزرسانی PodTemplateSpec مربوط به Deployment، [وضعیت جدید Podها را اعلام کنید](#updating-a-deployment). یک ReplicaSet جدید ایجاد می‌شود و Deployment به‌تدریج مقیاس آن را افزایش می‌دهد و هم‌زمان مقیاس ReplicaSet قدیمی را کاهش می‌دهد و بدین ترتیب اطمینان حاصل می‌کند که Podها با نرخی کنترل‌شده جایگزین می‌شوند. هر ReplicaSet جدید، revision (بازنگری) مربوط به Deployment را به‌روزرسانی می‌کند.
* اگر وضعیت فعلی Deployment پایدار نیست، [به یک revision قبلی Deployment بازگردید](#rolling-back-a-deployment). هر بازگشت، revision مربوط به Deployment را به‌روزرسانی می‌کند.
* [مقیاس Deployment را افزایش دهید تا بار بیشتری را پشتیبانی کند](#scaling-a-deployment).
* [rollout یک Deployment را متوقف کنید](#pausing-and-resuming-a-deployment) تا چندین اصلاح را روی PodTemplateSpec آن اعمال کنید و سپس آن را از سر بگیرید تا یک rollout جدید آغاز شود.
* [از وضعیت Deployment](#deployment-status) به‌عنوان نشانگری برای گیر کردن یک rollout استفاده کنید.
* [ReplicaSetهای قدیمی‌تری را پاک‌سازی کنید](#clean-up-policy) که دیگر به آن‌ها نیاز ندارید.

## ایجاد یک Deployment

نمونه‌ی زیر مثالی از یک Deployment است. این Deployment یک ReplicaSet ایجاد می‌کند تا سه Pod `nginx` را راه‌اندازی کند:

{{% code_sample file="controllers/nginx-deployment.yaml" %}}

در این مثال:

* یک Deployment با نام `nginx-deployment` ایجاد می‌شود که با
  فیلد `.metadata.name` مشخص شده است. این نام مبنای ReplicaSetها
  و Podهایی خواهد بود که بعداً ایجاد می‌شوند. برای جزئیات بیشتر، به [نوشتن spec یک Deployment](#writing-a-deployment-spec)
  مراجعه کنید.
* Deployment یک ReplicaSet ایجاد می‌کند که سه Pod تکثیرشده را ایجاد می‌کند؛ این تعداد با فیلد `.spec.replicas` مشخص شده است.
* فیلد `.spec.selector` تعریف می‌کند که ReplicaSet ایجادشده چگونه Podهایی را که باید مدیریت کند پیدا کند.
  در این حالت، برچسبی را انتخاب می‌کنید که در قالب Pod تعریف شده است (`app: nginx`).
  با این حال، قواعد انتخاب پیچیده‌تری نیز امکان‌پذیر است،
  به شرط آنکه خود قالب Pod آن قاعده را برآورده کند.

  {{< note >}}
  فیلد `.spec.selector.matchLabels` نگاشتی از زوج‌های {key,value} است.
  یک {key,value} منفرد در نگاشت `matchLabels` معادل عنصری از `matchExpressions` است
  که فیلد `key` آن برابر "key"، `operator` آن برابر "In"، و آرایه‌ی `values` آن فقط شامل "value" است.
  برای مطابقت، همه‌ی الزامات، هم از `matchLabels` و هم از `matchExpressions`، باید برآورده شوند.
  {{< /note >}}

* فیلد `.spec.template` شامل زیرفیلدهای زیر است:
  * Podها با استفاده از فیلد `.metadata.labels` با برچسب `app: nginx` برچسب‌گذاری می‌شوند.
  * مشخصات قالب Pod، یا فیلد `.spec`، نشان می‌دهد که
    Podها یک کانتینر به نام `nginx` اجرا می‌کنند که ایمیج `nginx` از
    [Docker Hub](https://hub.docker.com/) را در نسخه‌ی 1.14.2 اجرا می‌کند.
  * با استفاده از فیلد `.spec.containers[0].name` یک کانتینر ایجاد کنید و نام آن را `nginx` بگذارید.

پیش از شروع، مطمئن شوید که کلاستر کوبرنتیز شما راه‌اندازی شده و در حال اجراست.
گام‌های زیر را برای ایجاد Deployment بالا دنبال کنید:

1. Deployment را با اجرای فرمان زیر ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/controllers/nginx-deployment.yaml
   ```

2. `kubectl get deployments` را اجرا کنید تا بررسی کنید که Deployment ایجاد شده است یا نه.

   اگر Deployment هنوز در حال ایجاد باشد، خروجی مشابه زیر است:
   ```
   NAME               READY   UP-TO-DATE   AVAILABLE   AGE
   nginx-deployment   0/3     0            0           1s
   ```
   هنگامی که Deploymentهای کلاستر خود را بررسی می‌کنید، فیلدهای زیر نمایش داده می‌شوند:
   * `NAME` نام Deploymentهای موجود در فضای نام را فهرست می‌کند.
   * `READY` نشان می‌دهد چه تعداد از رپلیکاهای برنامه برای کاربران شما در دسترس هستند. این فیلد از الگوی ready/desired پیروی می‌کند.
   * `UP-TO-DATE` تعداد رپلیکاهایی را نشان می‌دهد که برای رسیدن به وضعیت مطلوب به‌روزرسانی شده‌اند.
   * `AVAILABLE` نشان می‌دهد چه تعداد از رپلیکاهای برنامه برای کاربران شما در دسترس هستند.
   * `AGE` مدت زمانی را نشان می‌دهد که برنامه در حال اجرا بوده است.

   توجه کنید که تعداد رپلیکاهای مطلوب طبق فیلد `.spec.replicas` برابر ۳ است.

3. برای مشاهده‌ی وضعیت rollout مربوط به Deployment، `kubectl rollout status deployment/nginx-deployment` را اجرا کنید.

   خروجی مشابه زیر است:
   ```
   Waiting for rollout to finish: 2 out of 3 new replicas have been updated...
   deployment "nginx-deployment" successfully rolled out
   ```

4. چند ثانیه بعد دوباره `kubectl get deployments` را اجرا کنید.
   خروجی مشابه زیر است:
   ```
   NAME               READY   UP-TO-DATE   AVAILABLE   AGE
   nginx-deployment   3/3     3            3           18s
   ```
   توجه کنید که Deployment هر سه رپلیکا را ایجاد کرده است و همه‌ی رپلیکاها به‌روز (شامل جدیدترین قالب Pod) و در دسترس هستند.

5. برای مشاهده‌ی ReplicaSet (`rs`) ایجادشده توسط Deployment، `kubectl get rs` را اجرا کنید. خروجی مشابه زیر است:
   ```
   NAME                          DESIRED   CURRENT   READY   AGE
   nginx-deployment-75675f5897   3         3         3       18s
   ```
   خروجی ReplicaSet فیلدهای زیر را نشان می‌دهد:

   * `NAME` نام ReplicaSetهای موجود در فضای نام را فهرست می‌کند.
   * `DESIRED` تعداد مطلوب _رپلیکاهای_ برنامه را نشان می‌دهد که هنگام ایجاد Deployment تعریف می‌کنید. این همان _وضعیت مطلوب_ است.
   * `CURRENT` نشان می‌دهد در حال حاضر چه تعداد رپلیکا در حال اجرا هستند.
   * `READY` نشان می‌دهد چه تعداد از رپلیکاهای برنامه برای کاربران شما در دسترس هستند.
   * `AGE` مدت زمانی را نشان می‌دهد که برنامه در حال اجرا بوده است.

   توجه کنید که نام ReplicaSet همواره به قالب
   `[DEPLOYMENT-NAME]-[HASH]` است. این نام مبنای Podهایی خواهد بود
   که ایجاد می‌شوند.

   رشته‌ی `HASH` همان برچسب `pod-template-hash` روی ReplicaSet است.

6. برای مشاهده‌ی برچسب‌هایی که به‌طور خودکار برای هر Pod تولید شده‌اند، `kubectl get pods --show-labels` را اجرا کنید.
   خروجی مشابه زیر است:
   ```
   NAME                                READY     STATUS    RESTARTS   AGE       LABELS
   nginx-deployment-75675f5897-7ci7o   1/1       Running   0          18s       app=nginx,pod-template-hash=75675f5897
   nginx-deployment-75675f5897-kzszj   1/1       Running   0          18s       app=nginx,pod-template-hash=75675f5897
   nginx-deployment-75675f5897-qqcnn   1/1       Running   0          18s       app=nginx,pod-template-hash=75675f5897
   ```
   ReplicaSet ایجادشده اطمینان حاصل می‌کند که سه Pod `nginx` وجود داشته باشد.

{{< note >}}
باید یک انتخابگر و برچسب‌های قالب Pod مناسب را در یک Deployment مشخص کنید
(در این حالت، `app: nginx`).

برچسب‌ها یا انتخابگرها را با سایر کنترل‌کننده‌ها (از جمله سایر Deploymentها و StatefulSetها) هم‌پوشان نکنید. کوبرنتیز مانع هم‌پوشانی نمی‌شود و اگر چند کنترل‌کننده انتخابگرهای هم‌پوشان داشته باشند، ممکن است آن کنترل‌کننده‌ها با یکدیگر تداخل پیدا کنند و رفتار غیرمنتظره‌ای داشته باشند.
{{< /note >}}

### برچسب pod-template-hash

{{< caution >}}
این برچسب را تغییر ندهید.
{{< /caution >}}

برچسب `pod-template-hash` توسط کنترل‌کننده‌ی Deployment به هر ReplicaSetای که یک Deployment ایجاد می‌کند یا به فرزندی می‌پذیرد اضافه می‌شود.

این برچسب اطمینان حاصل می‌کند که ReplicaSetهای فرزند یک Deployment با یکدیگر هم‌پوشانی نداشته باشند. این برچسب با هش کردن `PodTemplate` مربوط به ReplicaSet و استفاده از هش حاصل به‌عنوان مقدار برچسبی تولید می‌شود که به انتخابگر ReplicaSet، برچسب‌های قالب Pod،
و هر Pod موجودی که ReplicaSet ممکن است داشته باشد اضافه می‌شود.

## به‌روزرسانی یک Deployment

{{< note >}}
rollout یک Deployment تنها و تنها در صورتی آغاز می‌شود که قالب Pod مربوط به Deployment (یعنی `.spec.template`)
تغییر کند، برای مثال اگر برچسب‌ها یا ایمیج‌های کانتینر قالب به‌روزرسانی شوند. سایر به‌روزرسانی‌ها، مانند مقیاس‌دهی Deployment، rollout را آغاز نمی‌کنند.
{{< /note >}}

گام‌های زیر را برای به‌روزرسانی Deployment خود دنبال کنید:

1. بیایید Podهای nginx را طوری به‌روزرسانی کنیم که به‌جای ایمیج `nginx:1.14.2` از ایمیج `nginx:1.16.1` استفاده کنند.

   ```shell
   kubectl set image deployment.v1.apps/nginx-deployment nginx=nginx:1.16.1
   ```

   یا از فرمان زیر استفاده کنید:

   ```shell
   kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1
   ```
   که در آن `deployment/nginx-deployment` نشان‌دهنده‌ی Deployment،
   `nginx` نشان‌دهنده‌ی کانتینری که به‌روزرسانی روی آن انجام می‌شود، و
   `nginx:1.16.1` نشان‌دهنده‌ی ایمیج جدید و تگ آن است.


   خروجی مشابه زیر است:

   ```
   deployment.apps/nginx-deployment image updated
   ```

   به‌عنوان جایگزین، می‌توانید Deployment را `edit` کنید و `.spec.template.spec.containers[0].image` را از `nginx:1.14.2` به `nginx:1.16.1` تغییر دهید:

   ```shell
   kubectl edit deployment/nginx-deployment
   ```

   خروجی مشابه زیر است:

   ```
   deployment.apps/nginx-deployment edited
   ```

2. برای مشاهده‌ی وضعیت rollout، فرمان زیر را اجرا کنید:

   ```shell
   kubectl rollout status deployment/nginx-deployment
   ```

   خروجی مشابه زیر است:

   ```
   Waiting for rollout to finish: 2 out of 3 new replicas have been updated...
   ```

   یا

   ```
   deployment "nginx-deployment" successfully rolled out
   ```

جزئیات بیشتری درباره‌ی Deployment به‌روزشده‌ی خود به دست آورید:

* پس از موفقیت rollout، می‌توانید Deployment را با اجرای `kubectl get deployments` مشاهده کنید.
  خروجی مشابه زیر است:

  ```
  NAME               READY   UP-TO-DATE   AVAILABLE   AGE
  nginx-deployment   3/3     3            3           36s
  ```

* `kubectl get rs` را اجرا کنید تا ببینید که Deployment، Podها را با ایجاد یک ReplicaSet جدید و افزایش مقیاس آن
تا ۳ رپلیکا، و همچنین کاهش مقیاس ReplicaSet قدیمی به ۰ رپلیکا، به‌روزرسانی کرده است.

  ```shell
  kubectl get rs
  ```

  خروجی مشابه زیر است:
  ```
  NAME                          DESIRED   CURRENT   READY   AGE
  nginx-deployment-1564180365   3         3         3       6s
  nginx-deployment-2035384211   0         0         0       36s
  ```

* اجرای `get pods` اکنون باید فقط Podهای جدید را نشان دهد:

  ```shell
  kubectl get pods
  ```

  خروجی مشابه زیر است:
  ```
  NAME                                READY     STATUS    RESTARTS   AGE
  nginx-deployment-1564180365-khku8   1/1       Running   0          14s
  nginx-deployment-1564180365-nacti   1/1       Running   0          14s
  nginx-deployment-1564180365-z9gth   1/1       Running   0          14s
  ```

  دفعه‌ی بعد که بخواهید این Podها را به‌روزرسانی کنید، فقط کافی است دوباره قالب Pod مربوط به Deployment را به‌روزرسانی کنید.

  Deployment اطمینان حاصل می‌کند که در هنگام به‌روزرسانی Podها، فقط تعداد مشخصی از آن‌ها از دسترس خارج باشند. به‌طور پیش‌فرض،
  اطمینان حاصل می‌کند که دست‌کم ۷۵٪ از تعداد مطلوب Podها در حال اجرا باشند (حداکثر ۲۵٪ غیرقابل دسترس).

  Deployment همچنین اطمینان حاصل می‌کند که فقط تعداد مشخصی Pod بیش از تعداد مطلوب Podها ایجاد شود.
  به‌طور پیش‌فرض، اطمینان حاصل می‌کند که حداکثر ۱۲۵٪ از تعداد مطلوب Podها در حال اجرا باشند (حداکثر ۲۵٪ مازاد).

  برای مثال، اگر به Deployment بالا دقیق نگاه کنید، می‌بینید که ابتدا یک Pod جدید ایجاد می‌کند،
  سپس یک Pod قدیمی را حذف می‌کند و یک Pod جدید دیگر ایجاد می‌کند. این Deployment تا زمانی که تعداد کافی از
  Podهای جدید راه‌اندازی نشده باشند Podهای قدیمی را از بین نمی‌برد، و تا زمانی که تعداد کافی از Podهای قدیمی از بین نرفته باشند Podهای جدید ایجاد نمی‌کند.
  این Deployment اطمینان حاصل می‌کند که دست‌کم ۳ Pod در دسترس باشند و در مجموع حداکثر ۴ Pod در دسترس باشند. در مورد
  یک Deployment با ۴ رپلیکا، تعداد Podها میان ۳ و ۵ خواهد بود.

* جزئیات Deployment خود را به دست آورید:
  ```shell
  kubectl describe deployments
  ```
  خروجی مشابه زیر است:
  ```
  Name:                   nginx-deployment
  Namespace:              default
  CreationTimestamp:      Thu, 30 Nov 2017 10:56:25 +0000
  Labels:                 app=nginx
  Annotations:            deployment.kubernetes.io/revision=2
  Selector:               app=nginx
  Replicas:               3 desired | 3 updated | 3 total | 3 available | 0 unavailable
  StrategyType:           RollingUpdate
  MinReadySeconds:        0
  RollingUpdateStrategy:  25% max unavailable, 25% max surge
  Pod Template:
    Labels:  app=nginx
     Containers:
      nginx:
        Image:        nginx:1.16.1
        Port:         80/TCP
        Environment:  <none>
        Mounts:       <none>
      Volumes:        <none>
    Conditions:
      Type           Status  Reason
      ----           ------  ------
      Available      True    MinimumReplicasAvailable
      Progressing    True    NewReplicaSetAvailable
    OldReplicaSets:  <none>
    NewReplicaSet:   nginx-deployment-1564180365 (3/3 replicas created)
    Events:
      Type    Reason             Age   From                   Message
      ----    ------             ----  ----                   -------
      Normal  ScalingReplicaSet  2m    deployment-controller  Scaled up replica set nginx-deployment-2035384211 to 3
      Normal  ScalingReplicaSet  24s   deployment-controller  Scaled up replica set nginx-deployment-1564180365 to 1
      Normal  ScalingReplicaSet  22s   deployment-controller  Scaled down replica set nginx-deployment-2035384211 to 2
      Normal  ScalingReplicaSet  22s   deployment-controller  Scaled up replica set nginx-deployment-1564180365 to 2
      Normal  ScalingReplicaSet  19s   deployment-controller  Scaled down replica set nginx-deployment-2035384211 to 1
      Normal  ScalingReplicaSet  19s   deployment-controller  Scaled up replica set nginx-deployment-1564180365 to 3
      Normal  ScalingReplicaSet  14s   deployment-controller  Scaled down replica set nginx-deployment-2035384211 to 0
  ```
  در اینجا می‌بینید که هنگامی که Deployment را برای نخستین بار ایجاد کردید، یک ReplicaSet (nginx-deployment-2035384211) ایجاد کرد
  و مقیاس آن را مستقیماً تا ۳ رپلیکا افزایش داد. هنگامی که Deployment را به‌روزرسانی کردید، یک ReplicaSet جدید
  (nginx-deployment-1564180365) ایجاد کرد و مقیاس آن را تا ۱ افزایش داد و منتظر ماند تا راه‌اندازی شود. سپس مقیاس ReplicaSet قدیمی را
  به ۲ کاهش داد و مقیاس ReplicaSet جدید را به ۲ افزایش داد، به‌طوری که در همه‌ی زمان‌ها دست‌کم ۳ Pod در دسترس و حداکثر ۴ Pod ایجاد شده باشند.
  سپس با همان راهبرد به‌روزرسانی تدریجی، به افزایش و کاهش مقیاس ReplicaSet جدید و قدیمی ادامه داد.
  در نهایت، ۳ رپلیکای در دسترس در ReplicaSet جدید خواهید داشت و مقیاس ReplicaSet قدیمی به ۰ کاهش می‌یابد.

{{< note >}}
کوبرنتیز هنگام محاسبه‌ی تعداد `availableReplicas`، که باید میان
`replicas - maxUnavailable` و `replicas + maxSurge` باشد، Podهای در حال خاتمه را به حساب نمی‌آورد. در نتیجه، ممکن است متوجه شوید که در طول یک rollout تعداد Podها بیشتر از
حد انتظار است و مجموع منابع مصرف‌شده توسط Deployment بیشتر از `replicas + maxSurge` است،
تا زمانی که `terminationGracePeriodSeconds` مربوط به Podهای در حال خاتمه به پایان برسد.
{{< /note >}}

### Rollover (یا چند به‌روزرسانی هم‌زمان در جریان)

هر بار که کنترل‌کننده‌ی Deployment یک Deployment جدید را مشاهده می‌کند، یک ReplicaSet برای راه‌اندازی
Podهای مطلوب ایجاد می‌شود. اگر Deployment به‌روزرسانی شود، ReplicaSet موجودی که Podهایی را کنترل می‌کند که برچسب‌هایشان
با `.spec.selector` مطابقت دارد اما قالبشان با `.spec.template` مطابقت ندارد، کاهش مقیاس می‌یابد. در نهایت، مقیاس ReplicaSet
جدید به `.spec.replicas` می‌رسد و مقیاس همه‌ی ReplicaSetهای قدیمی به ۰ کاهش می‌یابد.

اگر یک Deployment را در حالی به‌روزرسانی کنید که یک rollout موجود در حال انجام است، Deployment طبق به‌روزرسانی یک ReplicaSet جدید
ایجاد می‌کند و شروع به افزایش مقیاس آن می‌کند، و ReplicaSetای را که پیش‌تر در حال افزایش مقیاس آن بود rollover می‌کند
-- آن را به فهرست ReplicaSetهای قدیمی خود اضافه می‌کند و شروع به کاهش مقیاس آن می‌کند.

برای مثال، فرض کنید یک Deployment ایجاد می‌کنید تا ۵ رپلیکا از `nginx:1.14.2` ایجاد کند،
اما سپس، هنگامی که فقط ۳ رپلیکا از `nginx:1.14.2` ایجاد شده‌اند، Deployment را به‌روزرسانی می‌کنید تا ۵ رپلیکا از `nginx:1.16.1` ایجاد کند.
در این حالت، Deployment بلافاصله شروع به
از بین بردن ۳ Pod `nginx:1.14.2` که ایجاد کرده بود می‌کند و شروع به ایجاد
Podهای `nginx:1.16.1` می‌کند. این Deployment پیش از تغییر مسیر منتظر ایجاد ۵ رپلیکای `nginx:1.14.2`
نمی‌ماند.

### به‌روزرسانی‌های انتخابگر برچسب

به‌طور کلی انجام به‌روزرسانی‌های انتخابگر برچسب توصیه نمی‌شود و پیشنهاد می‌شود انتخابگرهای خود را از ابتدا برنامه‌ریزی کنید.
انتخابگر برچسب یک Deployment پس از ایجاد **تغییرناپذیر** است؛
نمی‌توان آن را از طریق `kubectl patch`، `kubectl edit`، `kubectl apply` یا ابزارهایی مانند `helm upgrade` به‌روزرسانی کرد.

اگر ناگزیر به تغییر انتخابگر هستید، باید Deployment را حذف کنید و دوباره ایجاد کنید.
به‌طور پیش‌فرض، حذف Deployment، Podهای در حال اجرای آن را نیز حذف می‌کند و باعث قطعی سرویس می‌شود؛ اگر
لازم است آن Podها در حین بازسازی Deployment به اجرای خود ادامه دهند، از `--cascade=orphan` استفاده کنید
(پیامدهای آن را در ادامه ببینید).
نهایت احتیاط را به خرج دهید و مطمئن شوید که پیامدهای زیر را درک می‌کنید:

* **افزودن‌ها:** هنگامی که یک Deployment جدید با انتخابگری محدودتر ایجاد می‌کنید، Deployment جدید **باید** یک قالب Pod مناسب نیز داشته باشد.
  اگر یک مانیفست موجود دارید و آن را برای محدودتر کردن انتخابگر ویرایش می‌کنید، باید فراداده‌ی قالب Pod درون آن Deployment را نیز ویرایش کنید و
  برچسب‌های جدید را برای مطابقت
  اضافه کنید، در غیر این صورت سرور API یک خطای اعتبارسنجی برمی‌گرداند. این یک تغییر _بدون هم‌پوشانی_ است:
  Deployment جدید Podهای قدیمی (که فاقد برچسب جدید هستند) را «نمی‌بیند» و این باعث می‌شود ReplicaSet
  قدیمی **یتیم** شود و یک ReplicaSet کاملاً جدید ایجاد شود.
* **به‌روزرسانی مقدار:** تغییر مقدار موجود در یک کلید انتخابگر (برای مثال، از `v1` به `v2`)
  به همان رفتار افزودن‌ها (یتیم شدن و بازسازی) منجر می‌شود.
* **حذف‌ها:** حذف یک کلید موجود از انتخابگر Deployment به هیچ تغییری
  در برچسب‌های قالب Pod نیاز ندارد. این یک تغییر _هم‌پوشان_ است: انتخابگر جدید و گسترده‌تر
  با Podهای قدیمی مطابقت خواهد داشت. ReplicaSetهای موجود یتیم نمی‌شوند و ReplicaSet جدیدی ایجاد نمی‌شود،
  اما توجه داشته باشید که برچسب حذف‌شده همچنان در Podها و ReplicaSetهای موجود وجود دارد.
  می‌توانید با آغاز یک rollout برای Deployment آن را پاک‌سازی کنید.

## بازگرداندن یک Deployment

گاهی ممکن است بخواهید یک Deployment را بازگردانید (rollback)؛ برای مثال، هنگامی که Deployment پایدار نیست، مانند حالت crash looping.
به‌طور پیش‌فرض، کل سابقه‌ی rollout مربوط به Deployment در سیستم نگه داشته می‌شود تا هر زمان که بخواهید بتوانید آن را بازگردانید
(می‌توانید این رفتار را با تغییر محدودیت سابقه‌ی revisionها تغییر دهید).

{{< note >}}
revision یک Deployment هنگامی ایجاد می‌شود که rollout آن Deployment آغاز شود. این بدان معناست که
revision جدید تنها و تنها در صورتی ایجاد می‌شود که قالب Pod مربوط به Deployment (`.spec.template`) تغییر کند،
برای مثال اگر برچسب‌ها یا ایمیج‌های کانتینر قالب را به‌روزرسانی کنید. سایر به‌روزرسانی‌ها، مانند مقیاس‌دهی Deployment،
revision جدیدی برای Deployment ایجاد نمی‌کنند تا بتوانید مقیاس‌دهی دستی یا خودکار هم‌زمان را تسهیل کنید.
این بدان معناست که هنگامی که به یک revision قبلی بازمی‌گردید، فقط بخش قالب Pod مربوط به Deployment
بازگردانده می‌شود.
{{< /note >}}

* فرض کنید هنگام به‌روزرسانی Deployment یک اشتباه تایپی مرتکب شده‌اید و نام ایمیج را به‌جای `nginx:1.16.1` به‌صورت `nginx:1.161` وارد کرده‌اید:

  ```shell
  kubectl set image deployment/nginx-deployment nginx=nginx:1.161
  ```

  خروجی مشابه زیر است:
  ```
  deployment.apps/nginx-deployment image updated
  ```

* rollout گیر می‌کند. می‌توانید این را با بررسی وضعیت rollout تأیید کنید:

  ```shell
  kubectl rollout status deployment/nginx-deployment
  ```

  خروجی مشابه زیر است:
  ```
  Waiting for rollout to finish: 1 out of 3 new replicas have been updated...
  ```

* برای متوقف کردن پایش وضعیت rollout بالا، Ctrl-C را فشار دهید. برای اطلاعات بیشتر درباره‌ی rolloutهای گیرکرده،
[اینجا بیشتر بخوانید](#deployment-status).

* می‌بینید که تعداد رپلیکاهای قدیمی (با جمع تعداد رپلیکاهای
  `nginx-deployment-1564180365` و `nginx-deployment-2035384211`) برابر ۳ و تعداد
  رپلیکاهای جدید (از `nginx-deployment-3066724191`) برابر ۱ است.

  ```shell
  kubectl get rs
  ```

  خروجی مشابه زیر است:
  ```
  NAME                          DESIRED   CURRENT   READY   AGE
  nginx-deployment-1564180365   3         3         3       25s
  nginx-deployment-2035384211   0         0         0       36s
  nginx-deployment-3066724191   1         1         0       6s
  ```

* با نگاه به Podهای ایجادشده، می‌بینید که ۱ Pod ایجادشده توسط ReplicaSet جدید در یک حلقه‌ی دریافت ایمیج (image pull) گیر کرده است.

  ```shell
  kubectl get pods
  ```

  خروجی مشابه زیر است:
  ```
  NAME                                READY     STATUS             RESTARTS   AGE
  nginx-deployment-1564180365-70iae   1/1       Running            0          25s
  nginx-deployment-1564180365-jbqqo   1/1       Running            0          25s
  nginx-deployment-1564180365-hysrc   1/1       Running            0          25s
  nginx-deployment-3066724191-08mng   0/1       ImagePullBackOff   0          6s
  ```

  {{< note >}}
  کنترل‌کننده‌ی Deployment، rollout معیوب را به‌طور خودکار متوقف می‌کند و افزایش مقیاس ReplicaSet جدید را متوقف می‌کند. این به پارامترهای rollingUpdate (به‌طور مشخص `maxUnavailable`) که مشخص کرده‌اید بستگی دارد. کوبرنتیز به‌طور پیش‌فرض این مقدار را روی ۲۵٪ تنظیم می‌کند.
  {{< /note >}}

* توضیحات Deployment را به دست آورید:
  ```shell
  kubectl describe deployment
  ```

  خروجی مشابه زیر است:
  ```
  Name:           nginx-deployment
  Namespace:      default
  CreationTimestamp:  Tue, 15 Mar 2016 14:48:04 -0700
  Labels:         app=nginx
  Selector:       app=nginx
  Replicas:       3 desired | 1 updated | 4 total | 3 available | 1 unavailable
  StrategyType:       RollingUpdate
  MinReadySeconds:    0
  RollingUpdateStrategy:  25% max unavailable, 25% max surge
  Pod Template:
    Labels:  app=nginx
    Containers:
     nginx:
      Image:        nginx:1.161
      Port:         80/TCP
      Host Port:    0/TCP
      Environment:  <none>
      Mounts:       <none>
    Volumes:        <none>
  Conditions:
    Type           Status  Reason
    ----           ------  ------
    Available      True    MinimumReplicasAvailable
    Progressing    True    ReplicaSetUpdated
  OldReplicaSets:     nginx-deployment-1564180365 (3/3 replicas created)
  NewReplicaSet:      nginx-deployment-3066724191 (1/1 replicas created)
  Events:
    FirstSeen LastSeen    Count   From                    SubObjectPath   Type        Reason              Message
    --------- --------    -----   ----                    -------------   --------    ------              -------
    1m        1m          1       {deployment-controller }                Normal      ScalingReplicaSet   Scaled up replica set nginx-deployment-2035384211 to 3
    22s       22s         1       {deployment-controller }                Normal      ScalingReplicaSet   Scaled up replica set nginx-deployment-1564180365 to 1
    22s       22s         1       {deployment-controller }                Normal      ScalingReplicaSet   Scaled down replica set nginx-deployment-2035384211 to 2
    22s       22s         1       {deployment-controller }                Normal      ScalingReplicaSet   Scaled up replica set nginx-deployment-1564180365 to 2
    21s       21s         1       {deployment-controller }                Normal      ScalingReplicaSet   Scaled down replica set nginx-deployment-2035384211 to 1
    21s       21s         1       {deployment-controller }                Normal      ScalingReplicaSet   Scaled up replica set nginx-deployment-1564180365 to 3
    13s       13s         1       {deployment-controller }                Normal      ScalingReplicaSet   Scaled down replica set nginx-deployment-2035384211 to 0
    13s       13s         1       {deployment-controller }                Normal      ScalingReplicaSet   Scaled up replica set nginx-deployment-3066724191 to 1
  ```

  برای رفع این مشکل، باید به یک revision قبلی و پایدار از Deployment بازگردید.

### بررسی سابقه‌ی rollout یک Deployment

گام‌های زیر را برای بررسی سابقه‌ی rollout دنبال کنید:

1. ابتدا، revisionهای این Deployment را بررسی کنید:
   ```shell
   kubectl rollout history deployment/nginx-deployment
   ```
   خروجی مشابه زیر است:
   ```
   deployments "nginx-deployment"
   REVISION    CHANGE-CAUSE
   1           <none>
   2           <none>
   3           <none>
   ```

   `CHANGE-CAUSE` در هنگام ایجاد revisionها از حاشیه‌نویسی `kubernetes.io/change-cause` مربوط به Deployment در آن‌ها کپی می‌شود. می‌توانید پیام `CHANGE-CAUSE` را به این روش‌ها مشخص کنید:

   * حاشیه‌نویسی Deployment با `kubectl annotate deployment/nginx-deployment kubernetes.io/change-cause="image updated to 1.16.1"`
   * ویرایش دستی مانیفست منبع.
   * استفاده از ابزارهایی که حاشیه‌نویسی را به‌طور خودکار تنظیم می‌کنند.

   {{< note >}}
   در نسخه‌های قدیمی‌تر کوبرنتیز، می‌توانستید از flag `--record` همراه با فرمان‌های kubectl برای مقداردهی خودکار فیلد `CHANGE-CAUSE` استفاده کنید. این flag منسوخ شده است و در نسخه‌ای در آینده حذف خواهد شد.
   {{< /note >}}

2. برای مشاهده‌ی جزئیات هر revision، فرمان زیر را اجرا کنید:
   ```shell
   kubectl rollout history deployment/nginx-deployment --revision=2
   ```

   خروجی مشابه زیر است:
   ```
   deployments "nginx-deployment" revision 2
     Labels:       app=nginx
             pod-template-hash=1159050644
     Containers:
      nginx:
       Image:      nginx:1.16.1
       Port:       80/TCP
        QoS Tier:
           cpu:      BestEffort
           memory:   BestEffort
       Environment Variables:      <none>
     No volumes.
   ```

### بازگشت به یک revision قبلی
گام‌های زیر را برای بازگرداندن Deployment از نسخه‌ی فعلی به نسخه‌ی قبلی، یعنی نسخه‌ی ۲، دنبال کنید.

1. اکنون تصمیم گرفته‌اید rollout فعلی را لغو کنید و به revision قبلی بازگردید:
   ```shell
   kubectl rollout undo deployment/nginx-deployment
   ```

   خروجی مشابه زیر است:
   ```
   deployment.apps/nginx-deployment rolled back
   ```
   به‌عنوان جایگزین، می‌توانید با مشخص کردن یک revision خاص با `--to-revision` به آن بازگردید:

   ```shell
   kubectl rollout undo deployment/nginx-deployment --to-revision=2
   ```

   خروجی مشابه زیر است:
   ```
   deployment.apps/nginx-deployment rolled back
   ```

   برای جزئیات بیشتر درباره‌ی فرمان‌های مرتبط با rollout، [`kubectl rollout`](/docs/reference/generated/kubectl/kubectl-commands#rollout) را بخوانید.

   اکنون Deployment به یک revision پایدار قبلی بازگردانده شده است. همان‌طور که می‌بینید، یک رویداد `DeploymentRollback`
   برای بازگشت به revision ۲ توسط کنترل‌کننده‌ی Deployment تولید می‌شود.

2. برای بررسی اینکه بازگشت موفق بوده و Deployment طبق انتظار در حال اجراست، فرمان زیر را اجرا کنید:
   ```shell
   kubectl get deployment nginx-deployment
   ```

   خروجی مشابه زیر است:
   ```
   NAME               READY   UP-TO-DATE   AVAILABLE   AGE
   nginx-deployment   3/3     3            3           30m
   ```
3. توضیحات Deployment را به دست آورید:
   ```shell
   kubectl describe deployment nginx-deployment
   ```
   خروجی مشابه زیر است:
   ```
   Name:                   nginx-deployment
   Namespace:              default
   CreationTimestamp:      Sun, 02 Sep 2018 18:17:55 -0500
   Labels:                 app=nginx
   Annotations:            deployment.kubernetes.io/revision=4
   Selector:               app=nginx
   Replicas:               3 desired | 3 updated | 3 total | 3 available | 0 unavailable
   StrategyType:           RollingUpdate
   MinReadySeconds:        0
   RollingUpdateStrategy:  25% max unavailable, 25% max surge
   Pod Template:
     Labels:  app=nginx
     Containers:
      nginx:
       Image:        nginx:1.16.1
       Port:         80/TCP
       Host Port:    0/TCP
       Environment:  <none>
       Mounts:       <none>
     Volumes:        <none>
   Conditions:
     Type           Status  Reason
     ----           ------  ------
     Available      True    MinimumReplicasAvailable
     Progressing    True    NewReplicaSetAvailable
   OldReplicaSets:  <none>
   NewReplicaSet:   nginx-deployment-c4747d96c (3/3 replicas created)
   Events:
     Type    Reason              Age   From                   Message
     ----    ------              ----  ----                   -------
     Normal  ScalingReplicaSet   12m   deployment-controller  Scaled up replica set nginx-deployment-75675f5897 to 3
     Normal  ScalingReplicaSet   11m   deployment-controller  Scaled up replica set nginx-deployment-c4747d96c to 1
     Normal  ScalingReplicaSet   11m   deployment-controller  Scaled down replica set nginx-deployment-75675f5897 to 2
     Normal  ScalingReplicaSet   11m   deployment-controller  Scaled up replica set nginx-deployment-c4747d96c to 2
     Normal  ScalingReplicaSet   11m   deployment-controller  Scaled down replica set nginx-deployment-75675f5897 to 1
     Normal  ScalingReplicaSet   11m   deployment-controller  Scaled up replica set nginx-deployment-c4747d96c to 3
     Normal  ScalingReplicaSet   11m   deployment-controller  Scaled down replica set nginx-deployment-75675f5897 to 0
     Normal  ScalingReplicaSet   11m   deployment-controller  Scaled up replica set nginx-deployment-595696685f to 1
     Normal  DeploymentRollback  15s   deployment-controller  Rolled back deployment "nginx-deployment" to revision 2
     Normal  ScalingReplicaSet   15s   deployment-controller  Scaled down replica set nginx-deployment-595696685f to 0
   ```

## مقیاس‌دهی یک Deployment

می‌توانید یک Deployment را با استفاده از فرمان زیر مقیاس‌دهی کنید:

```shell
kubectl scale deployment/nginx-deployment --replicas=10
```
خروجی مشابه زیر است:
```
deployment.apps/nginx-deployment scaled
```

با فرض اینکه [مقیاس‌دهی خودکار افقی Pod](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) در کلاستر شما فعال باشد،
می‌توانید یک مقیاس‌دهنده‌ی خودکار برای Deployment خود راه‌اندازی کنید و حداقل و حداکثر تعداد
Podهایی را که می‌خواهید اجرا شوند، بر اساس میزان استفاده از CPU توسط Podهای موجود، انتخاب کنید.

```shell
kubectl autoscale deployment/nginx-deployment --min=10 --max=15 --cpu-percent=80%
```
خروجی مشابه زیر است:
```
deployment.apps/nginx-deployment scaled
```

### مقیاس‌دهی متناسب

Deploymentهای RollingUpdate از اجرای هم‌زمان چند نسخه از یک برنامه پشتیبانی می‌کنند. هنگامی که شما
یا یک مقیاس‌دهنده‌ی خودکار، یک Deployment از نوع RollingUpdate را که در میانه‌ی یک rollout است (چه در حال انجام
و چه متوقف‌شده) مقیاس‌دهی می‌کنید، کنترل‌کننده‌ی Deployment رپلیکاهای اضافی را میان ReplicaSetهای فعال
موجود (ReplicaSetهایی که Pod دارند) متوازن می‌کند تا ریسک کاهش یابد. این کار *مقیاس‌دهی متناسب* نامیده می‌شود.

برای مثال، شما یک Deployment با ۱۰ رپلیکا، [maxSurge](#max-surge)=3 و [maxUnavailable](#max-unavailable)=2 اجرا می‌کنید.

* مطمئن شوید که ۱۰ رپلیکای Deployment شما در حال اجرا هستند.
  ```shell
  kubectl get deploy
  ```
  خروجی مشابه زیر است:

  ```
  NAME                 DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
  nginx-deployment     10        10        10           10          50s
  ```

* به ایمیج جدیدی به‌روزرسانی می‌کنید که اتفاقاً از درون کلاستر قابل resolve نیست.
  ```shell
  kubectl set image deployment/nginx-deployment nginx=nginx:sometag
  ```

  خروجی مشابه زیر است:
  ```
  deployment.apps/nginx-deployment image updated
  ```

* به‌روزرسانی ایمیج یک rollout جدید با ReplicaSet nginx-deployment-1989198191 آغاز می‌کند، اما به دلیل
الزام `maxUnavailable` که در بالا ذکر کردید مسدود می‌شود. وضعیت rollout را بررسی کنید:
  ```shell
  kubectl get rs
  ```
  خروجی مشابه زیر است:
  ```
  NAME                          DESIRED   CURRENT   READY     AGE
  nginx-deployment-1989198191   5         5         0         9s
  nginx-deployment-618515232    8         8         8         1m
  ```

* سپس یک درخواست مقیاس‌دهی جدید برای Deployment می‌رسد. مقیاس‌دهنده‌ی خودکار تعداد رپلیکاهای Deployment را
به ۱۵ افزایش می‌دهد. کنترل‌کننده‌ی Deployment باید تصمیم بگیرد این ۵ رپلیکای جدید را کجا اضافه کند. اگر از
مقیاس‌دهی متناسب استفاده نمی‌کردید، هر ۵ رپلیکا به ReplicaSet جدید اضافه می‌شدند. با مقیاس‌دهی متناسب،
رپلیکاهای اضافی را میان همه‌ی ReplicaSetها پخش می‌کنید. سهم‌های بزرگ‌تر به ReplicaSetهایی که
بیشترین رپلیکا را دارند و سهم‌های کوچک‌تر به ReplicaSetهایی با رپلیکای کمتر می‌رسد. هر باقی‌مانده‌ای به
ReplicaSetای که بیشترین رپلیکا را دارد اضافه می‌شود. مقیاس ReplicaSetهایی که صفر رپلیکا دارند افزایش نمی‌یابد.

در مثال بالا، ۳ رپلیکا به ReplicaSet قدیمی و ۲ رپلیکا به
ReplicaSet جدید اضافه می‌شوند. فرایند rollout در نهایت باید همه‌ی رپلیکاها را به ReplicaSet جدید منتقل کند، با این فرض
که رپلیکاهای جدید سالم شوند. برای تأیید این موضوع، فرمان زیر را اجرا کنید:

```shell
kubectl get deploy
```

خروجی مشابه زیر است:
```
NAME                 DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment     15        18        7            8           7m
```
وضعیت rollout تأیید می‌کند که رپلیکاها چگونه به هر ReplicaSet اضافه شده‌اند.
```shell
kubectl get rs
```

خروجی مشابه زیر است:
```
NAME                          DESIRED   CURRENT   READY     AGE
nginx-deployment-1989198191   7         7         0         7m
nginx-deployment-618515232    11        11        11        7m
```

## توقف و از سرگیری rollout یک Deployment {#pausing-and-resuming-a-deployment}

هنگامی که یک Deployment را به‌روزرسانی می‌کنید یا قصد آن را دارید، می‌توانید rolloutهای
آن Deployment را پیش از آغاز یک یا چند به‌روزرسانی متوقف کنید. هنگامی
که برای اعمال آن تغییرات آماده شدید، rolloutهای
Deployment را از سر می‌گیرید. این رویکرد به شما امکان می‌دهد
چندین اصلاح را در فاصله‌ی میان توقف و از سرگیری اعمال کنید، بدون آنکه rolloutهای غیرضروری آغاز شوند.

* برای مثال، با یک Deployment که ایجاد شده است:

  جزئیات Deployment را به دست آورید:
  ```shell
  kubectl get deploy
  ```
  خروجی مشابه زیر است:
  ```
  NAME      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
  nginx     3         3         3            3           1m
  ```
  وضعیت rollout را به دست آورید:
  ```shell
  kubectl get rs
  ```
  خروجی مشابه زیر است:
  ```
  NAME               DESIRED   CURRENT   READY     AGE
  nginx-2142116321   3         3         3         1m
  ```

* با اجرای فرمان زیر آن را متوقف کنید:
  ```shell
  kubectl rollout pause deployment/nginx-deployment
  ```

  خروجی مشابه زیر است:
  ```
  deployment.apps/nginx-deployment paused
  ```

* سپس ایمیج Deployment را به‌روزرسانی کنید:
  ```shell
  kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1
  ```

  خروجی مشابه زیر است:
  ```
  deployment.apps/nginx-deployment image updated
  ```

* توجه کنید که هیچ rollout جدیدی آغاز نشده است:
  ```shell
  kubectl rollout history deployment/nginx-deployment
  ```

  خروجی مشابه زیر است:
  ```
  deployments "nginx"
  REVISION  CHANGE-CAUSE
  1   <none>
  ```
* وضعیت rollout را به دست آورید تا تأیید کنید که ReplicaSet موجود تغییری نکرده است:
  ```shell
  kubectl get rs
  ```

  خروجی مشابه زیر است:
  ```
  NAME               DESIRED   CURRENT   READY     AGE
  nginx-2142116321   3         3         3         2m
  ```

* می‌توانید هر تعداد به‌روزرسانی که می‌خواهید انجام دهید؛ برای مثال، منابعی را که استفاده خواهند شد به‌روزرسانی کنید:
  ```shell
  kubectl set resources deployment/nginx-deployment -c=nginx --limits=cpu=200m,memory=512Mi
  ```

  خروجی مشابه زیر است:
  ```
  deployment.apps/nginx-deployment resource requirements updated
  ```

  وضعیت اولیه‌ی Deployment پیش از توقف rollout آن به کار خود ادامه می‌دهد، اما به‌روزرسانی‌های جدید
  Deployment تا زمانی که rollout آن متوقف است هیچ اثری نخواهند داشت.

* در نهایت، rollout مربوط به Deployment را از سر بگیرید و ببینید که یک ReplicaSet جدید با همه‌ی به‌روزرسانی‌های جدید راه‌اندازی می‌شود:
  ```shell
  kubectl rollout resume deployment/nginx-deployment
  ```

  خروجی مشابه زیر است:
  ```
  deployment.apps/nginx-deployment resumed
  ```
* وضعیت rollout را تا پایان آن {{< glossary_tooltip text="زیر نظر بگیرید (watch)" term_id="watch" >}}.
  ```shell
  kubectl get rs --watch
  ```

  خروجی مشابه زیر است:
  ```
  NAME               DESIRED   CURRENT   READY     AGE
  nginx-2142116321   2         2         2         2m
  nginx-3926361531   2         2         0         6s
  nginx-3926361531   2         2         1         18s
  nginx-2142116321   1         2         2         2m
  nginx-2142116321   1         2         2         2m
  nginx-3926361531   3         2         1         18s
  nginx-3926361531   3         2         1         18s
  nginx-2142116321   1         1         1         2m
  nginx-3926361531   3         3         1         18s
  nginx-3926361531   3         3         2         19s
  nginx-2142116321   0         1         1         2m
  nginx-2142116321   0         1         1         2m
  nginx-2142116321   0         0         0         2m
  nginx-3926361531   3         3         3         20s
  ```
* وضعیت آخرین rollout را به دست آورید:
  ```shell
  kubectl get rs
  ```

  خروجی مشابه زیر است:
  ```
  NAME               DESIRED   CURRENT   READY     AGE
  nginx-2142116321   0         0         0         2m
  nginx-3926361531   3         3         3         28s
  ```
{{< note >}}
نمی‌توانید یک Deployment متوقف‌شده را تا زمانی که آن را از سر نگرفته‌اید بازگردانید.
{{< /note >}}

## وضعیت Deployment

یک Deployment در طول چرخه‌ی حیات خود وارد وضعیت‌های مختلفی می‌شود. ممکن است در حین
rollout یک ReplicaSet جدید [در حال پیشرفت](#progressing-deployment) باشد، ممکن است [کامل](#complete-deployment) باشد، یا ممکن است [در پیشرفت ناکام بماند](#failed-deployment).

### Deployment در حال پیشرفت

کوبرنتیز یک Deployment را هنگامی به‌عنوان _در حال پیشرفت_ علامت‌گذاری می‌کند که یکی از کارهای زیر انجام شود:

* Deployment یک ReplicaSet جدید ایجاد می‌کند.
* Deployment در حال افزایش مقیاس جدیدترین ReplicaSet خود است.
* Deployment در حال کاهش مقیاس ReplicaSet(های) قدیمی‌تر خود است.
* Podهای جدید آماده یا در دسترس می‌شوند (دست‌کم به مدت [MinReadySeconds](#min-ready-seconds) آماده باشند).

هنگامی که rollout «در حال پیشرفت» می‌شود، کنترل‌کننده‌ی Deployment یک condition با ویژگی‌های
زیر به `.status.conditions` مربوط به Deployment اضافه می‌کند:

* `type: Progressing`
* `status: "True"`
* `reason: NewReplicaSetCreated` | `reason: FoundNewReplicaSet` | `reason: ReplicaSetUpdated`

می‌توانید پیشرفت یک Deployment را با استفاده از `kubectl rollout status` پایش کنید.

### Deployment کامل

کوبرنتیز یک Deployment را هنگامی به‌عنوان _کامل_ علامت‌گذاری می‌کند که ویژگی‌های زیر را داشته باشد:

* همه‌ی رپلیکاهای مرتبط با Deployment به جدیدترین نسخه‌ای که مشخص کرده‌اید به‌روزرسانی شده باشند، یعنی همه‌ی
به‌روزرسانی‌هایی که درخواست کرده‌اید تکمیل شده باشند.
* همه‌ی رپلیکاهای مرتبط با Deployment در دسترس باشند.
* هیچ رپلیکای قدیمی‌ای از Deployment در حال اجرا نباشد.

هنگامی که rollout «کامل» می‌شود، کنترل‌کننده‌ی Deployment یک condition با ویژگی‌های
زیر در `.status.conditions` مربوط به Deployment تنظیم می‌کند:

* `type: Progressing`
* `status: "True"`
* `reason: NewReplicaSetAvailable`

این condition `Progressing` تا زمانی که یک rollout جدید آغاز شود مقدار وضعیت `"True"` را حفظ می‌کند.
این condition حتی هنگامی که دسترس‌پذیری رپلیکاها تغییر کند (که در عوض
بر condition `Available` اثر می‌گذارد) برقرار می‌ماند.

می‌توانید با استفاده از `kubectl rollout status` بررسی کنید که آیا یک Deployment کامل شده است یا نه. اگر rollout
با موفقیت کامل شده باشد، `kubectl rollout status` کد خروج صفر برمی‌گرداند.

```shell
kubectl rollout status deployment/nginx-deployment
```
خروجی مشابه زیر است:
```
Waiting for rollout to finish: 2 of 3 updated replicas are available...
deployment "nginx-deployment" successfully rolled out
```
و وضعیت خروج `kubectl rollout` برابر 0 (موفقیت) است:
```shell
echo $?
```
```
0
```

### Deployment ناموفق

ممکن است Deployment شما در تلاش برای استقرار جدیدترین ReplicaSet خود گیر کند و هرگز کامل نشود. این وضعیت ممکن است
به دلیل برخی از عوامل زیر رخ دهد:

* سهمیه‌ی (quota) ناکافی
* شکست‌های readiness probe
* خطاهای دریافت ایمیج
* مجوزهای ناکافی
* محدوده‌های محدودیت (limit ranges)
* پیکربندی نادرست زمان اجرای برنامه

یکی از راه‌های تشخیص این وضعیت، مشخص کردن یک پارامتر مهلت در spec مربوط به Deployment است:
([`.spec.progressDeadlineSeconds`](#progress-deadline-seconds)). `.spec.progressDeadlineSeconds` نشان‌دهنده‌ی
تعداد ثانیه‌هایی است که کنترل‌کننده‌ی Deployment پیش از اعلام (در وضعیت Deployment) اینکه
پیشرفت Deployment متوقف شده است منتظر می‌ماند.

فرمان `kubectl` زیر spec را با `progressDeadlineSeconds` تنظیم می‌کند تا کنترل‌کننده
پس از ۱۰ دقیقه عدم پیشرفت rollout یک Deployment را گزارش کند:

```shell
kubectl patch deployment/nginx-deployment -p '{"spec":{"progressDeadlineSeconds":600}}'
```
خروجی مشابه زیر است:
```
deployment.apps/nginx-deployment patched
```
پس از گذشتن مهلت، کنترل‌کننده‌ی Deployment یک DeploymentCondition با ویژگی‌های
زیر به `.status.conditions` مربوط به Deployment اضافه می‌کند:

* `type: Progressing`
* `status: "False"`
* `reason: ProgressDeadlineExceeded`

این condition همچنین ممکن است زودتر شکست بخورد و در این صورت به دلایلی مانند `ReplicaSetCreateError` روی مقدار وضعیت `"False"` تنظیم شود.
همچنین، پس از تکمیل rollout مربوط به Deployment، مهلت دیگر در نظر گرفته نمی‌شود.

برای اطلاعات بیشتر درباره‌ی status conditionها، به [قراردادهای API کوبرنتیز](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#typical-status-properties) مراجعه کنید.

{{< note >}}
کوبرنتیز روی یک Deployment متوقف‌مانده هیچ اقدامی جز گزارش یک status condition با
`reason: ProgressDeadlineExceeded` انجام نمی‌دهد. هماهنگ‌کننده‌های سطح بالاتر می‌توانند از آن بهره ببرند و بر اساس آن اقدام کنند؛ برای
مثال، Deployment را به نسخه‌ی قبلی آن بازگردانند.
{{< /note >}}

{{< note >}}
اگر rollout یک Deployment را متوقف کنید، کوبرنتیز پیشرفت را در برابر مهلت مشخص‌شده‌ی شما بررسی نمی‌کند.
می‌توانید با خیال آسوده rollout یک Deployment را در میانه‌ی آن متوقف کنید و از سر بگیرید، بدون آنکه
condition مربوط به گذشتن از مهلت فعال شود.
{{< /note >}}

ممکن است با Deploymentهای خود خطاهای گذرا تجربه کنید، چه به دلیل timeout پایینی که تنظیم کرده‌اید و چه
به دلیل هر نوع خطای دیگری که بتوان آن را گذرا تلقی کرد. برای مثال، فرض کنید
سهمیه‌ی ناکافی دارید. اگر Deployment را describe کنید، متوجه بخش زیر خواهید شد:

```shell
kubectl describe deployment nginx-deployment
```
خروجی مشابه زیر است:
```
<...>
Conditions:
  Type            Status  Reason
  ----            ------  ------
  Available       True    MinimumReplicasAvailable
  Progressing     True    ReplicaSetUpdated
  ReplicaFailure  True    FailedCreate
<...>
```

اگر `kubectl get deployment nginx-deployment -o yaml` را اجرا کنید، وضعیت Deployment مشابه زیر است:

```
status:
  availableReplicas: 2
  conditions:
  - lastTransitionTime: 2016-10-04T12:25:39Z
    lastUpdateTime: 2016-10-04T12:25:39Z
    message: Replica set "nginx-deployment-4262182780" is progressing.
    reason: ReplicaSetUpdated
    status: "True"
    type: Progressing
  - lastTransitionTime: 2016-10-04T12:25:42Z
    lastUpdateTime: 2016-10-04T12:25:42Z
    message: Deployment has minimum availability.
    reason: MinimumReplicasAvailable
    status: "True"
    type: Available
  - lastTransitionTime: 2016-10-04T12:25:39Z
    lastUpdateTime: 2016-10-04T12:25:39Z
    message: 'Error creating: pods "nginx-deployment-4262182780-" is forbidden: exceeded quota:
      object-counts, requested: pods=1, used: pods=3, limited: pods=2'
    reason: FailedCreate
    status: "True"
    type: ReplicaFailure
  observedGeneration: 3
  replicas: 2
  unavailableReplicas: 2
```

در نهایت، هنگامی که مهلت پیشرفت Deployment سپری شود، کوبرنتیز وضعیت و
دلیل condition Progressing را به‌روزرسانی می‌کند:

```
Conditions:
  Type            Status  Reason
  ----            ------  ------
  Available       True    MinimumReplicasAvailable
  Progressing     False   ProgressDeadlineExceeded
  ReplicaFailure  True    FailedCreate
```

می‌توانید مشکل سهمیه‌ی ناکافی را با کاهش مقیاس Deployment، با کاهش مقیاس سایر
کنترل‌کننده‌هایی که ممکن است در حال اجرا داشته باشید، یا با افزایش سهمیه در فضای نام خود برطرف کنید. اگر شرایط سهمیه را
برآورده کنید و سپس کنترل‌کننده‌ی Deployment، rollout مربوط به Deployment را تکمیل کند، خواهید دید که
وضعیت Deployment با یک condition موفق (`status: "True"` و `reason: NewReplicaSetAvailable`) به‌روزرسانی می‌شود.

```
Conditions:
  Type          Status  Reason
  ----          ------  ------
  Available     True    MinimumReplicasAvailable
  Progressing   True    NewReplicaSetAvailable
```

`type: Available` با `status: "True"` به این معناست که Deployment شما حداقل دسترس‌پذیری را دارد. حداقل دسترس‌پذیری
توسط پارامترهای مشخص‌شده در راهبرد استقرار تعیین می‌شود. `type: Progressing` با `status: "True"` به این معناست که Deployment شما
یا در میانه‌ی یک rollout و در حال پیشرفت است، یا پیشرفت خود را با موفقیت کامل کرده است و حداقل
رپلیکاهای جدید موردنیاز در دسترس هستند (برای جزئیات، Reason مربوط به condition را ببینید - در مثال ما
`reason: NewReplicaSetAvailable` به این معناست که Deployment کامل است).

می‌توانید با استفاده از `kubectl rollout status` بررسی کنید که آیا یک Deployment در پیشرفت ناکام مانده است یا نه. اگر Deployment از مهلت پیشرفت فراتر رفته باشد،
`kubectl rollout status` یک کد خروج غیرصفر برمی‌گرداند.

```shell
kubectl rollout status deployment/nginx-deployment
```
خروجی مشابه زیر است:
```
Waiting for rollout to finish: 2 out of 3 new replicas have been updated...
error: deployment "nginx" exceeded its progress deadline
```
و وضعیت خروج `kubectl rollout` برابر 1 (نشان‌دهنده‌ی خطا) است:
```shell
echo $?
```
```
1
```

### کار با یک Deployment ناموفق

همه‌ی اقداماتی که برای یک Deployment کامل کاربرد دارند، برای یک Deployment ناموفق نیز کاربرد دارند. می‌توانید مقیاس آن را افزایش/کاهش دهید، آن را
به یک revision قبلی بازگردانید، یا حتی اگر لازم است چند تنظیم را در قالب Pod مربوط به Deployment اعمال کنید، آن را متوقف کنید.

## سیاست پاک‌سازی

می‌توانید فیلد `.spec.revisionHistoryLimit` را در یک Deployment تنظیم کنید تا مشخص کنید چه تعداد ReplicaSet قدیمی
برای این Deployment می‌خواهید نگه دارید. بقیه در پس‌زمینه توسط جمع‌آوری زباله حذف می‌شوند. به‌طور پیش‌فرض،
این مقدار ۱۰ است.

{{< note >}}
تنظیم صریح این فیلد روی 0 باعث پاک‌سازی کل سابقه‌ی Deployment شما می‌شود
و بنابراین آن Deployment قادر به بازگشت نخواهد بود.
{{< /note >}}

پاک‌سازی فقط **پس از** آنکه یک Deployment به
[وضعیت کامل](/docs/concepts/workloads/controllers/deployment/#complete-deployment) برسد آغاز می‌شود.
اگر `.spec.revisionHistoryLimit` را روی 0 تنظیم کنید، هر rollout با این حال پیش از آنکه کوبرنتیز ReplicaSet قدیمی را حذف کند،
ایجاد یک ReplicaSet جدید را آغاز می‌کند.

حتی با یک محدودیت سابقه‌ی revision غیرصفر، ممکن است تعداد ReplicaSetهای شما بیشتر از محدودیتی باشد
که پیکربندی کرده‌اید. برای مثال، اگر Podها در حالت crash looping باشند و در طول زمان چندین رویداد به‌روزرسانی تدریجی
آغاز شود، ممکن است در نهایت تعداد ReplicaSetها از
`.spec.revisionHistoryLimit` بیشتر شود، زیرا Deployment هرگز به وضعیت کامل نمی‌رسد.

## استقرارهای Canary

اگر می‌خواهید با استفاده از Deployment، نسخه‌ها را برای زیرمجموعه‌ای از کاربران یا سرورها rollout کنید،
می‌توانید چند Deployment ایجاد کنید، یکی برای هر نسخه، و از الگوی canary توصیف‌شده در
[مدیریت منابع](/docs/concepts/workloads/management/#canary-deployments) پیروی کنید.

برای آشنایی با جزئیات کار، آموزش [استقرار یک نسخه با استفاده از استقرار Canary](/docs/tutorials/stateless-application/canary-deployment/) را دنبال کنید.

## نوشتن spec یک Deployment

همانند همه‌ی پیکربندی‌های دیگر کوبرنتیز، یک Deployment به فیلدهای `.apiVersion`، `.kind` و `.metadata` نیاز دارد.
برای اطلاعات کلی درباره‌ی کار با فایل‌های پیکربندی، به مستندات
[استقرار برنامه‌ها](/docs/tasks/run-application/run-stateless-application-deployment/)،
پیکربندی کانتینرها و [استفاده از kubectl برای مدیریت منابع](/docs/concepts/overview/working-with-objects/object-management/) مراجعه کنید.

هنگامی که control plane برای یک Deployment، Podهای جدید ایجاد می‌کند، `.metadata.name` مربوط به
Deployment بخشی از مبنای نام‌گذاری آن Podها است. نام یک Deployment باید یک مقدار معتبر
[زیردامنه‌ی DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names)
باشد، اما این ممکن است برای hostnameهای Pod نتایج غیرمنتظره‌ای ایجاد کند. برای بهترین سازگاری،
نام باید از قواعد سخت‌گیرانه‌تر یک
[برچسب DNS](/docs/concepts/overview/working-with-objects/names#dns-label-names) پیروی کند.

یک Deployment همچنین به یک [بخش `.spec`](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status) نیاز دارد.

### قالب Pod

`.spec.template` و `.spec.selector` تنها فیلدهای الزامی `.spec` هستند.

`.spec.template` یک [قالب Pod](/docs/concepts/workloads/pods/#pod-templates) است. این قالب دقیقاً همان شِمای یک {{< glossary_tooltip text="Pod" term_id="pod" >}} را دارد، با این تفاوت که تودرتو است و `apiVersion` یا `kind` ندارد.

علاوه بر فیلدهای الزامی یک Pod، قالب Pod در یک Deployment باید برچسب‌های مناسب
و یک سیاست راه‌اندازی مجدد مناسب مشخص کند. در مورد برچسب‌ها، مطمئن شوید که با سایر کنترل‌کننده‌ها هم‌پوشانی ندارند. به [انتخابگر](#selector) مراجعه کنید.

فقط [`.spec.template.spec.restartPolicy`](/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) برابر با `Always`
مجاز است که در صورت مشخص نشدن، مقدار پیش‌فرض نیز همین است.

### رپلیکاها

`.spec.replicas` یک فیلد اختیاری است که تعداد Podهای مطلوب را مشخص می‌کند. مقدار پیش‌فرض آن 1 است.

اگر یک Deployment را به‌صورت دستی مقیاس‌دهی کنید، برای مثال از طریق `kubectl scale deployment
deployment --replicas=X`، و سپس آن Deployment را بر اساس یک مانیفست به‌روزرسانی کنید
(برای مثال: با اجرای `kubectl apply -f deployment.yaml`)،
اعمال آن مانیفست مقیاس‌دهی دستی‌ای را که پیش‌تر انجام داده‌اید بازنویسی می‌کند.

اگر یک [HorizontalPodAutoscaler](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) (یا هر
API مشابهی برای مقیاس‌دهی افقی) مقیاس‌دهی یک Deployment را مدیریت می‌کند، `.spec.replicas` را تنظیم نکنید.

در عوض، اجازه دهید
{{< glossary_tooltip text="control plane" term_id="control-plane" >}} کوبرنتیز فیلد
`.spec.replicas` را به‌طور خودکار مدیریت کند.

### انتخابگر

`.spec.selector` یک فیلد الزامی است که یک [انتخابگر برچسب](/docs/concepts/overview/working-with-objects/labels/)
برای Podهایی که این Deployment هدف قرار می‌دهد مشخص می‌کند.

`.spec.selector` باید با `.spec.template.metadata.labels` مطابقت داشته باشد، در غیر این صورت توسط API رد می‌شود.

در نسخه‌ی API `apps/v1`، اگر `.spec.selector` و `.metadata.labels` تنظیم نشده باشند، به‌طور پیش‌فرض مقدار `.spec.template.metadata.labels` را نمی‌گیرند. بنابراین باید به‌صورت صریح تنظیم شوند. همچنین توجه داشته باشید که `.spec.selector` در `apps/v1` پس از ایجاد Deployment تغییرناپذیر است.

یک Deployment ممکن است Podهایی را که برچسب‌هایشان با انتخابگر مطابقت دارد خاتمه دهد، در صورتی که قالب آن‌ها
با `.spec.template` متفاوت باشد یا تعداد کل چنین Podهایی از `.spec.replicas` فراتر رود. اگر تعداد Podها کمتر از تعداد مطلوب باشد،
Podهای جدیدی با `.spec.template` راه‌اندازی می‌کند.

{{< note >}}
نباید Podهای دیگری ایجاد کنید که برچسب‌هایشان با این انتخابگر مطابقت داشته باشد؛ چه به‌طور مستقیم، چه با ایجاد
یک Deployment دیگر، و چه با ایجاد کنترل‌کننده‌ی دیگری مانند ReplicaSet یا ReplicationController. اگر
چنین کنید، Deployment نخست تصور می‌کند که این Podهای دیگر را خودش ایجاد کرده است. کوبرنتیز مانع انجام این کار نمی‌شود.
{{< /note >}}

اگر چند کنترل‌کننده با انتخابگرهای هم‌پوشان داشته باشید، کنترل‌کننده‌ها با یکدیگر
درگیر می‌شوند و به‌درستی رفتار نخواهند کرد.

### راهبرد

`.spec.strategy` راهبردی را مشخص می‌کند که برای جایگزینی Podهای قدیمی با Podهای جدید استفاده می‌شود.
`.spec.strategy.type` می‌تواند "Recreate" یا "RollingUpdate" باشد. "RollingUpdate"
مقدار پیش‌فرض است.

#### Deployment با راهبرد Recreate

هنگامی که `.spec.strategy.type==Recreate` باشد، همه‌ی Podهای موجود پیش از ایجاد Podهای جدید از بین برده می‌شوند.

{{< note >}}
این راهبرد فقط برای ارتقاها تضمین می‌کند که خاتمه‌ی Pod پیش از ایجاد رخ دهد. اگر یک Deployment را ارتقا دهید، همه‌ی Podهای
revision قدیمی بلافاصله خاتمه می‌یابند. پیش از ایجاد هر Pod از revision
جدید، منتظر حذف موفق آن‌ها می‌ماند. اگر یک Pod را به‌صورت دستی حذف کنید، چرخه‌ی حیات توسط ReplicaSet کنترل می‌شود و
جایگزین بلافاصله ایجاد می‌شود (حتی اگر Pod قدیمی هنوز در وضعیت Terminating باشد). اگر به
تضمین «حداکثر» برای Podهای خود نیاز دارید، باید استفاده از
[StatefulSet](/docs/concepts/workloads/controllers/statefulset/) را در نظر بگیرید.
{{< /note >}}

#### Deployment با به‌روزرسانی تدریجی

هنگامی که `.spec.strategy.type==RollingUpdate` باشد، Deployment، Podها را به شیوه‌ی به‌روزرسانی تدریجی
(کاهش تدریجی مقیاس ReplicaSetهای قدیمی و افزایش مقیاس ReplicaSet جدید) به‌روزرسانی می‌کند. می‌توانید `maxUnavailable` و `maxSurge` را برای کنترل
فرایند به‌روزرسانی تدریجی مشخص کنید.

##### حداکثر غیرقابل دسترس (Max Unavailable)

`.spec.strategy.rollingUpdate.maxUnavailable` یک فیلد اختیاری است که حداکثر تعداد
Podهایی را مشخص می‌کند که می‌توانند در طول فرایند به‌روزرسانی غیرقابل دسترس باشند. این مقدار می‌تواند یک عدد مطلق (برای مثال، ۵)
یا درصدی از Podهای مطلوب (برای مثال، ۱۰٪) باشد. عدد مطلق از روی درصد با
گرد کردن رو به پایین محاسبه می‌شود. اگر `.spec.strategy.rollingUpdate.maxSurge` برابر 0 باشد، این مقدار نمی‌تواند 0 باشد. مقدار پیش‌فرض ۲۵٪ است.

برای مثال، هنگامی که این مقدار روی ۳۰٪ تنظیم شده باشد، ReplicaSet قدیمی می‌تواند بلافاصله پس از آغاز به‌روزرسانی تدریجی به ۷۰٪ از Podهای
مطلوب کاهش مقیاس یابد. پس از آماده شدن Podهای جدید، ReplicaSet قدیمی می‌تواند
بیشتر کاهش مقیاس یابد و به دنبال آن ReplicaSet جدید افزایش مقیاس یابد، به‌طوری که اطمینان حاصل شود تعداد کل Podهای در دسترس
در همه‌ی زمان‌ها در طول به‌روزرسانی دست‌کم ۷۰٪ از Podهای مطلوب است.

##### حداکثر مازاد (Max Surge)

`.spec.strategy.rollingUpdate.maxSurge` یک فیلد اختیاری است که حداکثر تعداد Podهایی را مشخص می‌کند
که می‌توانند بیش از تعداد مطلوب Podها ایجاد شوند. این مقدار می‌تواند یک عدد مطلق (برای مثال، ۵) یا
درصدی از Podهای مطلوب (برای مثال، ۱۰٪) باشد. اگر `maxUnavailable` برابر 0 باشد، این مقدار نمی‌تواند 0 باشد. عدد مطلق
از روی درصد با گرد کردن رو به بالا محاسبه می‌شود. مقدار پیش‌فرض ۲۵٪ است.

برای مثال، هنگامی که این مقدار روی ۳۰٪ تنظیم شده باشد، ReplicaSet جدید می‌تواند بلافاصله پس از
آغاز به‌روزرسانی تدریجی افزایش مقیاس یابد، به‌طوری که مجموع Podهای قدیمی و جدید از ۱۳۰٪ Podهای مطلوب
فراتر نرود. پس از از بین رفتن Podهای قدیمی، ReplicaSet جدید می‌تواند بیشتر افزایش مقیاس یابد، به‌طوری که اطمینان حاصل شود
تعداد کل Podهای در حال اجرا در هر زمان در طول به‌روزرسانی حداکثر ۱۳۰٪ از Podهای مطلوب است.

در اینجا چند مثال از Deployment با به‌روزرسانی تدریجی آمده است که از `maxUnavailable` و `maxSurge` استفاده می‌کنند:

{{< tabs name="tab_with_md" >}}
{{% tab name="حداکثر غیرقابل دسترس" %}}

 ```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
 ```

{{% /tab %}}
{{% tab name="حداکثر مازاد" %}}

 ```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
 ```

{{% /tab %}}
{{% tab name="ترکیبی" %}}

 ```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
 ```

{{% /tab %}}
{{< /tabs >}}

### مهلت پیشرفت بر حسب ثانیه (Progress Deadline Seconds)

`.spec.progressDeadlineSeconds` یک فیلد اختیاری است که تعداد ثانیه‌هایی را مشخص می‌کند که می‌خواهید
برای پیشرفت Deployment خود منتظر بمانید، پیش از آنکه سیستم گزارش دهد Deployment
[در پیشرفت ناکام مانده است](#failed-deployment) - که به‌صورت یک condition با `type: Progressing`، `status: "False"`
و `reason: ProgressDeadlineExceeded` در وضعیت منبع نمایان می‌شود. کنترل‌کننده‌ی Deployment
به تلاش مجدد برای Deployment ادامه خواهد داد. مقدار پیش‌فرض آن ۶۰۰ است.

در صورت مشخص شدن، این فیلد باید بزرگ‌تر از `.spec.minReadySeconds` باشد.

### حداقل ثانیه‌های آمادگی (Min Ready Seconds)

`.spec.minReadySeconds` یک فیلد اختیاری است که حداقل تعداد ثانیه‌هایی را مشخص می‌کند که یک Pod تازه
ایجادشده باید بدون از کار افتادن هیچ‌یک از کانتینرهایش آماده باشد تا در دسترس تلقی شود.
مقدار پیش‌فرض آن 0 است (Pod به‌محض آماده شدن در دسترس تلقی می‌شود). برای آشنایی بیشتر با اینکه
یک Pod چه زمانی آماده تلقی می‌شود، به [Probeهای کانتینر](/docs/concepts/workloads/pods/pod-lifecycle/#container-probes) مراجعه کنید.

### Podهای در حال خاتمه

{{< feature-state feature_gate_name="DeploymentReplicaSetTerminatingReplicas" >}}

فقط در صورتی می‌توانید Podهای در حال خاتمه را ببینید که
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) `DeploymentReplicaSetTerminatingReplicas`
روی [سرور API](/docs/reference/command-line-tools-reference/kube-apiserver/)
و روی [kube-controller-manager](/docs/reference/command-line-tools-reference/kube-controller-manager/) فعال باشد.

Podهایی که به دلیل حذف یا کاهش مقیاس در حال خاتمه قرار می‌گیرند ممکن است خاتمه‌شان زمان زیادی طول بکشد و
در طول آن دوره منابع اضافی مصرف کنند. در نتیجه، تعداد کل همه‌ی Podها می‌تواند به‌طور موقت از
`.spec.replicas` فراتر رود. Podهای در حال خاتمه را می‌توان با استفاده از فیلد `.status.terminatingReplicas` مربوط به Deployment ردیابی کرد.

### محدودیت سابقه‌ی revision

سابقه‌ی revisionهای یک Deployment در ReplicaSetهایی که کنترل می‌کند ذخیره می‌شود.

`.spec.revisionHistoryLimit` یک فیلد اختیاری است که تعداد ReplicaSetهای قدیمی‌ای را که برای امکان بازگشت باید نگه داشته شوند
مشخص می‌کند. این ReplicaSetهای قدیمی منابعی را در `etcd` مصرف می‌کنند و خروجی `kubectl get rs` را شلوغ می‌کنند. پیکربندی هر revision از Deployment در ReplicaSetهای آن ذخیره می‌شود؛ بنابراین، پس از حذف یک ReplicaSet قدیمی، امکان بازگشت به آن revision از Deployment را از دست می‌دهید. به‌طور پیش‌فرض، ۱۰ ReplicaSet قدیمی نگه داشته می‌شوند، اما مقدار ایدئال آن به تناوب و پایداری Deploymentهای جدید بستگی دارد.

به‌طور مشخص‌تر، تنظیم این فیلد روی صفر به این معناست که همه‌ی ReplicaSetهای قدیمی با 0 رپلیکا پاک‌سازی می‌شوند.
در این حالت، rollout جدید یک Deployment را نمی‌توان لغو کرد، زیرا سابقه‌ی revisionهای آن پاک‌سازی شده است.

### متوقف‌شده (Paused)

`.spec.paused` یک فیلد بولی اختیاری برای توقف و از سرگیری یک Deployment است. تنها تفاوت میان
یک Deployment متوقف‌شده و Deploymentای که متوقف نشده، این است که هرگونه تغییر در PodTemplateSpec مربوط به
Deployment متوقف‌شده، تا زمانی که متوقف است، rolloutهای جدیدی آغاز نمی‌کند. یک Deployment به‌طور پیش‌فرض هنگام
ایجاد متوقف نیست.

## {{% heading "whatsnext" %}}

* درباره‌ی [Podها](/docs/concepts/workloads/pods) بیشتر بیاموزید.
* [یک برنامه‌ی بی‌حالت را با استفاده از یک Deployment اجرا کنید](/docs/tasks/run-application/run-stateless-application-deployment/).
* برای درک API مربوط به Deployment، {{< api-reference page="apps/deployment-v1" >}} را بخوانید.
* درباره‌ی [PodDisruptionBudget](/docs/concepts/workloads/pods/disruptions/) و اینکه
  چگونه می‌توانید از آن برای مدیریت دسترس‌پذیری برنامه در هنگام اختلال‌ها استفاده کنید بخوانید.
* از kubectl برای [ایجاد یک Deployment](/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/) استفاده کنید.
