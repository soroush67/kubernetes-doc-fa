---
title: "مثال: استقرار WordPress و MySQL با حجم‌های پایدار"
reviewers:
- ahmetb
content_type: tutorial
weight: 20
card: 
  name: tutorials
  weight: 40
  title: "مثال Stateful: وردپرس با حجم‌های پایدار"
---

<!-- overview -->
این آموزش نشان می‌دهد که چگونه یک سایت WordPress و یک پایگاه داده MySQL را با استفاده از
Minikube مستقر کنید. هر دو برنامه برای ذخیره داده‌ها از PersistentVolume و PersistentVolumeClaim استفاده می‌کنند.

هر [PersistentVolume](/docs/concepts/storage/persistent-volumes/) (PV) بخشی از فضای ذخیره‌سازی
در کلاستر است که یا مدیر کلاستر آن را به‌صورت دستی تأمین کرده است، یا کوبرنتیز آن را با استفاده از یک
[StorageClass](/docs/concepts/storage/storage-classes) به‌صورت پویا تأمین می‌کند.
هر [PersistentVolumeClaim](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) (PVC)
درخواستی از سوی کاربر برای فضای ذخیره‌سازی است که یک PV می‌تواند به آن پاسخ دهد. چرخه عمر
PersistentVolumeها و PersistentVolumeClaimها مستقل از چرخه عمر Podها است و داده‌ها هنگام راه‌اندازی
مجدد، زمان‌بندی مجدد و حتی حذف Podها حفظ می‌شوند.

{{< alert color="danger" title="Warning" >}}
این استقرار برای محیط‌های عملیاتی (production) مناسب نیست، زیرا از Podهای تک‌نمونه‌ای WordPress
و MySQL استفاده می‌کند. برای استقرار WordPress در محیط عملیاتی، استفاده از
[چارت Helm وردپرس](https://github.com/bitnami/charts/tree/master/bitnami/wordpress)
را در نظر بگیرید.
{{< /alert >}}

{{< alert color="info" title="Note" >}}
فایل‌های ارائه‌شده در این آموزش از APIهای GA مربوط به Deployment استفاده می‌کنند و مختص
کوبرنتیز نسخه 1.9 و بالاتر هستند. اگر می‌خواهید این آموزش را با نسخه‌ای قدیمی‌تر از کوبرنتیز
به کار ببرید، نسخه API را متناسب با آن به‌روزرسانی کنید یا به نسخه‌های قدیمی‌تر این آموزش مراجعه کنید.
{{< /alert >}}

## {{% heading "objectives" %}}

* ایجاد PersistentVolumeClaimها و PersistentVolumeها
* ایجاد یک فایل `kustomization.yaml` شامل
  * یک مولد Secret
  * پیکربندی‌های منابع MySQL
  * پیکربندی‌های منابع WordPress
* اعمال پوشه kustomization با دستور `kubectl apply -k ./`
* پاک‌سازی

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

مثالی که در این صفحه نشان داده شده است با `kubectl` نسخه 1.27 و بالاتر کار می‌کند.

فایل‌های پیکربندی زیر را دانلود کنید:

1. [mysql-deployment.yaml](/examples/application/wordpress/mysql-deployment.yaml)

1. [wordpress-deployment.yaml](/examples/application/wordpress/wordpress-deployment.yaml)

<!-- lessoncontent -->

## ایجاد PersistentVolumeClaimها و PersistentVolumeها

هر یک از MySQL و WordPress برای ذخیره داده‌ها به یک PersistentVolume نیاز دارند.
PersistentVolumeClaimهای آن‌ها در مرحله استقرار ایجاد خواهند شد.

در بسیاری از محیط‌های کلاستر، یک StorageClass پیش‌فرض نصب شده است.
اگر در PersistentVolumeClaim هیچ StorageClassی مشخص نشده باشد،
از StorageClass پیش‌فرض کلاستر استفاده می‌شود.

هنگامی که یک PersistentVolumeClaim ایجاد می‌شود، یک PersistentVolume بر اساس پیکربندی
StorageClass به‌صورت پویا تأمین می‌شود.

{{< alert color="danger" title="Warning" >}}
در کلاسترهای محلی، StorageClass پیش‌فرض از تأمین‌کننده `hostPath` استفاده می‌کند.
حجم‌های `hostPath` فقط برای توسعه و آزمایش مناسب هستند. در حجم‌های `hostPath`،
داده‌های شما در مسیر `/tmp` روی نودی قرار می‌گیرند که Pod روی آن زمان‌بندی شده است و بین
نودها جابه‌جا نمی‌شوند. اگر Pod از کار بیفتد و روی نود دیگری در کلاستر زمان‌بندی شود، یا نود
راه‌اندازی مجدد شود، داده‌ها از دست می‌روند.
{{< /alert >}}

{{< alert color="info" title="Note" >}}
اگر کلاستری راه‌اندازی می‌کنید که باید از تأمین‌کننده `hostPath` استفاده کند،
باید فلگ `--enable-hostpath-provisioner` را در مؤلفه `controller-manager` تنظیم کنید.
{{< /alert >}}

{{< alert color="info" title="Note" >}}
اگر یک کلاستر کوبرنتیز دارید که روی Google Kubernetes Engine اجرا می‌شود،
[این راهنما](https://cloud.google.com/kubernetes-engine/docs/tutorials/persistent-disk) را دنبال کنید.
{{< /alert >}}

## ایجاد فایل kustomization.yaml

### افزودن یک مولد Secret

هر [Secret](/docs/concepts/configuration/secret/) آبجکتی است که بخشی از داده‌های حساس،
مانند گذرواژه یا کلید، را ذخیره می‌کند. از نسخه 1.14 به بعد، `kubectl` از مدیریت آبجکت‌های
کوبرنتیز با استفاده از فایل kustomization پشتیبانی می‌کند. می‌توانید با استفاده از مولدها در
`kustomization.yaml` یک Secret ایجاد کنید.

با دستور زیر، یک مولد Secret به `kustomization.yaml` اضافه کنید.
لازم است `YOUR_PASSWORD` را با گذرواژه‌ای که می‌خواهید استفاده کنید جایگزین کنید.

```shell
cat <<EOF >./kustomization.yaml
secretGenerator:
- name: mysql-pass
  literals:
  - password=YOUR_PASSWORD
EOF
```

## افزودن پیکربندی‌های منابع برای MySQL و WordPress

مانیفست زیر یک Deployment تک‌نمونه‌ای از MySQL را توصیف می‌کند. کانتینر MySQL،
PersistentVolume را در مسیر /var/lib/mysql متصل (mount) می‌کند. متغیر محیطی `MYSQL_ROOT_PASSWORD`
گذرواژه پایگاه داده را از Secret تنظیم می‌کند.

{{% code_sample file="application/wordpress/mysql-deployment.yaml" %}}

مانیفست زیر یک Deployment تک‌نمونه‌ای از WordPress را توصیف می‌کند. کانتینر WordPress،
PersistentVolume را برای فایل‌های داده وب‌سایت در مسیر `/var/www/html` متصل می‌کند. متغیر محیطی
`WORDPRESS_DB_HOST` نام Service مربوط به MySQL را که در بالا تعریف شد تنظیم می‌کند و WordPress
از طریق این Service به پایگاه داده دسترسی خواهد داشت. متغیر محیطی `WORDPRESS_DB_PASSWORD`
گذرواژه پایگاه داده را از Secretی که kustomize تولید کرده است تنظیم می‌کند.

{{% code_sample file="application/wordpress/wordpress-deployment.yaml" %}}

1. فایل پیکربندی استقرار MySQL را دانلود کنید.

   ```shell
   curl -LO https://k8s.io/examples/application/wordpress/mysql-deployment.yaml
   ```

2. فایل پیکربندی WordPress را دانلود کنید.

   ```shell
   curl -LO https://k8s.io/examples/application/wordpress/wordpress-deployment.yaml
   ```

3. آن‌ها را به فایل `kustomization.yaml` اضافه کنید.

   ```shell
   cat <<EOF >>./kustomization.yaml
   resources:
     - mysql-deployment.yaml
     - wordpress-deployment.yaml
   EOF
   ```

## اعمال و بررسی

فایل `kustomization.yaml` همه منابع لازم برای استقرار یک سایت WordPress و یک پایگاه داده
MySQL را در بر دارد. می‌توانید پوشه را با دستور زیر اعمال کنید:

```shell
kubectl apply -k ./
```

اکنون می‌توانید بررسی کنید که همه آبجکت‌ها وجود دارند.

1. با اجرای دستور زیر بررسی کنید که Secret وجود دارد:

   ```shell
   kubectl get secrets
   ```

   خروجی باید مشابه زیر باشد:

   ```
   NAME                    TYPE                                  DATA   AGE
   mysql-pass-c57bb4t7mf   Opaque                                1      9s
   ```

2. بررسی کنید که یک PersistentVolume به‌صورت پویا تأمین شده است.

   ```shell
   kubectl get pvc
   ```

   {{< alert color="info" title="Note" >}}
   ممکن است تأمین و اتصال (bind) PVها تا چند دقیقه طول بکشد.
   {{< /alert >}}

   خروجی باید مشابه زیر باشد:

   ```
   NAME             STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS       AGE
   mysql-pv-claim   Bound     pvc-8cbd7b2e-4044-11e9-b2bb-42010a800002   20Gi       RWO            standard           77s
   wp-pv-claim      Bound     pvc-8cd0df54-4044-11e9-b2bb-42010a800002   20Gi       RWO            standard           77s
   ```

3. با اجرای دستور زیر بررسی کنید که Pod در حال اجرا است:

   ```shell
   kubectl get pods
   ```

   {{< alert color="info" title="Note" >}}
   ممکن است تا چند دقیقه طول بکشد تا وضعیت Pod به `RUNNING` تغییر کند.
   {{< /alert >}}

   خروجی باید مشابه زیر باشد:

   ```
   NAME                               READY     STATUS    RESTARTS   AGE
   wordpress-mysql-1894417608-x5dzt   1/1       Running   0          40s
   ```

4. با اجرای دستور زیر بررسی کنید که Service در حال اجرا است:

   ```shell
   kubectl get services wordpress
   ```

   خروجی باید مشابه زیر باشد:

   ```
   NAME        TYPE            CLUSTER-IP   EXTERNAL-IP   PORT(S)        AGE
   wordpress   LoadBalancer    10.0.0.89    <pending>     80:32406/TCP   4m
   ```

   {{< alert color="info" title="Note" >}}
   در Minikube، Serviceها فقط از طریق `NodePort` در دسترس قرار می‌گیرند. مقدار EXTERNAL-IP همیشه در وضعیت pending است.
   {{< /alert >}}

5. برای دریافت نشانی IP مربوط به Service وردپرس، دستور زیر را اجرا کنید:

   ```shell
   minikube service wordpress --url
   ```

   خروجی باید مشابه زیر باشد:

   ```
   http://1.2.3.4:32406
   ```

6. نشانی IP را کپی کنید و برای مشاهده سایت خود، صفحه را در مرورگر باز کنید.

   باید صفحه راه‌اندازی WordPress را مشابه تصویر زیر ببینید.

   ![wordpress-init](/images/docs/tutorials/mysql-wordpress-persistent-volume/WordPress.png)

   {{< alert color="danger" title="Warning" >}}
   نصب WordPress را در همین صفحه رها نکنید. اگر کاربر دیگری آن را پیدا کند،
   می‌تواند روی نمونه شما یک وب‌سایت راه‌اندازی کند و از آن برای ارائه محتوای مخرب استفاده کند.<br/><br/>
   یا WordPress را با ایجاد نام کاربری و گذرواژه نصب کنید، یا نمونه خود را حذف کنید.
   {{< /alert >}}

## {{% heading "cleanup" %}}

1. برای حذف Secret، Deploymentها، Serviceها و PersistentVolumeClaimهای خود، دستور زیر را اجرا کنید:

   ```shell
   kubectl delete -k ./
   ```

## {{% heading "whatsnext" %}}

* درباره [بازرسی و اشکال‌زدایی](/docs/tasks/debug/debug-application/debug-running-pod/) بیشتر بیاموزید
* درباره [Jobها](/docs/concepts/workloads/controllers/job/) بیشتر بیاموزید
* درباره [هدایت پورت](/docs/tasks/access-application-cluster/port-forward-access-application-cluster/) بیشتر بیاموزید
* بیاموزید که چگونه [به شِل یک کانتینر دسترسی پیدا کنید](/docs/tasks/debug/debug-application/get-shell-running-container/)
