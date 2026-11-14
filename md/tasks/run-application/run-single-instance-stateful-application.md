---
title: اجرای یک برنامهٔ حالت‌مند تک‌نمونه‌ای
content_type: tutorial
weight: 20
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توانید با استفاده از یک PersistentVolume و یک Deployment، یک برنامهٔ حالت‌مند (stateful) تک‌نمونه‌ای را در کوبرنتیز اجرا کنید. برنامهٔ مورد نظر MySQL است.

## {{% heading "objectives" %}}

- یک PersistentVolume بسازید که به یک دیسک در محیط شما ارجاع دهد.
- یک Deployment برای MySQL بسازید.
- MySQL را با یک نام DNS مشخص در دسترس سایر Podهای کلاستر قرار دهید.

## {{% heading "prerequisites" %}}

- {{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

- {{< include "default-storage-class-prereqs.md" >}}

<!-- lessoncontent -->

## استقرار MySQL

برای اجرای یک برنامهٔ حالت‌مند می‌توانید یک Deployment در کوبرنتیز بسازید و آن را با استفاده از یک PersistentVolumeClaim به یک PersistentVolume موجود متصل کنید. برای نمونه، فایل YAML زیر یک Deployment را توصیف می‌کند که MySQL را اجرا می‌کند و به PersistentVolumeClaim ارجاع می‌دهد. این فایل یک محل اتصال حجم (volume mount) برای ‎/var/lib/mysql تعریف می‌کند و سپس یک PersistentVolumeClaim می‌سازد که به دنبال یک حجم (volume) ‎20G است. این درخواست را هر حجم موجودی که الزامات آن را برآورده کند، یا یک تأمین‌کنندهٔ پویا (dynamic provisioner)، پاسخ می‌دهد.

نکته: گذرواژه در فایل پیکربندی YAML تعریف شده است و این کار امن نیست. برای یک راه‌حل امن، به [Secretها در کوبرنتیز](/docs/concepts/configuration/secret/) مراجعه کنید.

{{% code_sample file="application/mysql/mysql-deployment.yaml" %}}
{{% code_sample file="application/mysql/mysql-pv.yaml" %}}

1. PV و PVC تعریف‌شده در فایل YAML را مستقر کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/mysql/mysql-pv.yaml
   ```

1. محتوای فایل YAML را مستقر کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/mysql/mysql-deployment.yaml
   ```

1. اطلاعات Deployment را نمایش دهید:

   ```shell
   kubectl describe deployment mysql
   ```

   خروجی مشابه زیر است:

   ```
   Name:                 mysql
   Namespace:            default
   CreationTimestamp:    Tue, 01 Nov 2016 11:18:45 -0700
   Labels:               app=mysql
   Annotations:          deployment.kubernetes.io/revision=1
   Selector:             app=mysql
   Replicas:             1 desired | 1 updated | 1 total | 0 available | 1 unavailable
   StrategyType:         Recreate
   MinReadySeconds:      0
   Pod Template:
     Labels:       app=mysql
     Containers:
       mysql:
       Image:      mysql:9
       Port:       3306/TCP
       Environment:
         MYSQL_ROOT_PASSWORD:      password
       Mounts:
         /var/lib/mysql from mysql-persistent-storage (rw)
     Volumes:
       mysql-persistent-storage:
       Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
       ClaimName:  mysql-pv-claim
       ReadOnly:   false
   Conditions:
     Type          Status  Reason
     ----          ------  ------
     Available     False   MinimumReplicasUnavailable
     Progressing   True    ReplicaSetUpdated
   OldReplicaSets:       <none>
   NewReplicaSet:        mysql-63082529 (1/1 replicas created)
   Events:
     FirstSeen    LastSeen    Count    From                SubobjectPath    Type        Reason            Message
     ---------    --------    -----    ----                -------------    --------    ------            -------
     33s          33s         1        {deployment-controller }             Normal      ScalingReplicaSet Scaled up replica set mysql-63082529 to 1
   ```

1. فهرست Podهایی را که Deployment ساخته است نمایش دهید:

   ```shell
   kubectl get pods -l app=mysql
   ```

   خروجی مشابه زیر است:

   ```
   NAME                   READY     STATUS    RESTARTS   AGE
   mysql-63082529-2z3ki   1/1       Running   0          3m
   ```

1. PersistentVolumeClaim را بررسی کنید:

   ```shell
   kubectl describe pvc mysql-pv-claim
   ```

   خروجی مشابه زیر است:

   ```
   Name:         mysql-pv-claim
   Namespace:    default
   StorageClass:
   Status:       Bound
   Volume:       mysql-pv-volume
   Labels:       <none>
   Annotations:    pv.kubernetes.io/bind-completed=yes
                   pv.kubernetes.io/bound-by-controller=yes
   Capacity:     20Gi
   Access Modes: RWO
   Events:       <none>
   ```

## دسترسی به نمونهٔ MySQL

فایل YAML پیشین یک Service می‌سازد که به سایر Podهای کلاستر امکان دسترسی به پایگاه داده را می‌دهد. گزینهٔ `clusterIP: None` در Service باعث می‌شود نام DNS سرویس مستقیماً به نشانی IP مربوط به Pod ترجمه شود. این روش زمانی بهینه است که تنها یک Pod پشت Service دارید و قصد ندارید تعداد Podها را افزایش دهید.

برای اتصال به سرور، یک کلاینت MySQL اجرا کنید:

```shell
kubectl run -it --rm --image=mysql:9 --restart=Never mysql-client -- mysql -h mysql -ppassword
```

این فرمان یک Pod جدید در کلاستر می‌سازد که یک کلاینت MySQL را اجرا می‌کند و آن را از طریق Service به سرور متصل می‌کند. اگر اتصال برقرار شود، مطمئن می‌شوید که پایگاه دادهٔ حالت‌مند MySQL شما راه‌اندازی شده و در حال اجراست.

```
Waiting for pod default/mysql-client-274442439-zyp6i to be running, status is Pending, pod ready: false
If you don't see a command prompt, try pressing enter.

mysql>
```

## به‌روزرسانی

ایمیج یا هر بخش دیگری از Deployment را می‌توان طبق روال معمول با فرمان `kubectl apply` به‌روزرسانی کرد. در ادامه چند نکتهٔ احتیاطی آمده است که مختص برنامه‌های حالت‌مند است:

- برنامه را مقیاس‌دهی نکنید. این پیکربندی فقط برای برنامه‌های تک‌نمونه‌ای است. PersistentVolume زیربنایی تنها می‌تواند به یک Pod متصل شود. برای برنامه‌های حالت‌مند خوشه‌ای، به [مستندات StatefulSet](/docs/concepts/workloads/controllers/statefulset/) مراجعه کنید.
- در فایل YAML پیکربندی Deployment از `strategy:` `type: Recreate` استفاده کنید. این تنظیم به کوبرنتیز دستور می‌دهد که از به‌روزرسانی‌های تدریجی (rolling updates) استفاده _نکند_. به‌روزرسانی تدریجی در این حالت کار نمی‌کند، زیرا نمی‌توانید بیش از یک Pod را هم‌زمان در حال اجرا داشته باشید. راهبرد `Recreate` پیش از ساختن Pod جدید با پیکربندی به‌روزشده، Pod نخست را متوقف می‌کند.

## حذف یک Deployment

آبجکت‌های مستقرشده را با نامشان حذف کنید:

```shell
kubectl delete deployment,svc mysql
kubectl delete pvc mysql-pv-claim
kubectl delete pv mysql-pv-volume
```

اگر PersistentVolume را به‌صورت دستی تأمین کرده‌اید، باید آن را نیز به‌صورت دستی حذف کنید و منبع زیربنایی را هم آزاد کنید. اگر از یک تأمین‌کنندهٔ پویا استفاده کرده‌اید، این تأمین‌کننده با مشاهدهٔ حذف PersistentVolumeClaim، PersistentVolume را به‌طور خودکار حذف می‌کند. برخی تأمین‌کننده‌های پویا (مانند تأمین‌کننده‌های EBS و PD) هنگام حذف PersistentVolume، منبع زیربنایی را نیز آزاد می‌کنند.

## {{% heading "whatsnext" %}}

- دربارهٔ [آبجکت‌های Deployment](/docs/concepts/workloads/controllers/deployment/) بیشتر بیاموزید.

- دربارهٔ [استقرار برنامه‌ها](/docs/tasks/run-application/run-stateless-application-deployment/) بیشتر بیاموزید.

- [مستندات kubectl run](/docs/reference/generated/kubectl/kubectl-commands/#run)

- [حجم‌ها](/docs/concepts/storage/volumes/) و [حجم‌های پایدار](/docs/concepts/storage/persistent-volumes/)
