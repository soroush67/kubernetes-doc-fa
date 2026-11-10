---
title: تغییر سیاست بازپس‌گیری یک PersistentVolume
content_type: task
weight: 100
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه می‌توان سیاست بازپس‌گیری (reclaim policy) یک PersistentVolume در کوبرنتیز را تغییر داد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

## چرا سیاست بازپس‌گیری یک PersistentVolume را تغییر دهیم

هر PersistentVolume می‌تواند یکی از سیاست‌های بازپس‌گیری مختلف، از جمله «Retain»، «Recycle» و «Delete» را داشته باشد. سیاست بازپس‌گیری پیش‌فرض برای PersistentVolumeهایی که به‌صورت پویا تأمین (provision) می‌شوند، «Delete» است. یعنی وقتی کاربر PersistentVolumeClaim مربوط به یک حجم (volume) پویا‌تأمین‌شده را حذف کند، آن حجم نیز به‌طور خودکار حذف می‌شود. اگر حجم حاوی داده‌های ارزشمندی باشد، این رفتار خودکار ممکن است مناسب نباشد. در چنین حالتی بهتر است از سیاست «Retain» استفاده کنید. با سیاست «Retain»، اگر کاربر یک PersistentVolumeClaim را حذف کند، PersistentVolume متناظر با آن حذف نمی‌شود، بلکه به فاز Released منتقل می‌شود و همهٔ داده‌های آن را می‌توان به‌صورت دستی بازیابی کرد.

## تغییر سیاست بازپس‌گیری یک PersistentVolume

1. فهرست PersistentVolumeهای کلاستر خود را مشاهده کنید:

   ```shell
   kubectl get pv
   ```

   خروجی مشابه زیر است:

   ```none
   NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM             STORAGECLASS     REASON    AGE
   pvc-b6efd8da-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim1    manual                     10s
   pvc-b95650f8-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim2    manual                     6s
   pvc-bb3ca71d-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim3    manual                     3s
   ```

   این فهرست نام درخواست‌هایی (claim) را هم که به هر حجم متصل شده‌اند نشان می‌دهد تا حجم‌های پویا‌تأمین‌شده آسان‌تر شناسایی شوند.

1. یکی از PersistentVolumeهای خود را انتخاب کنید و سیاست بازپس‌گیری آن را تغییر دهید:

   ```shell
   kubectl patch pv <your-pv-name> -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
   ```

   در این دستور، `<your-pv-name>` نام PersistentVolume انتخاب‌شده است.

   {{< note >}}
   در ویندوز باید هر الگوی JSONPath را که شامل فاصله است، درون نقل‌قول _دوتایی_ قرار دهید (نه نقل‌قول تکی، آن‌طور که در بالا برای bash نشان داده شده است). در نتیجه، باید هر مقدار ثابت (literal) درون الگو را با نقل‌قول تکی یا نقل‌قول دوتایی escape‌شده مشخص کنید. برای مثال:

   ```cmd
   kubectl patch pv <your-pv-name> -p "{\"spec\":{\"persistentVolumeReclaimPolicy\":\"Retain\"}}"
   ```
   {{< /note >}}

1. بررسی کنید که PersistentVolume انتخاب‌شده سیاست درستی دارد:

   ```shell
   kubectl get pv
   ```

   خروجی مشابه زیر است:

   ```none
   NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM             STORAGECLASS     REASON    AGE
   pvc-b6efd8da-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim1    manual                     40s
   pvc-b95650f8-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim2    manual                     36s
   pvc-bb3ca71d-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Retain          Bound     default/claim3    manual                     33s
   ```

   در خروجی بالا می‌بینید که سیاست بازپس‌گیری حجمِ متصل به درخواست `default/claim3` برابر با `Retain` است. بنابراین وقتی کاربر درخواست `default/claim3` را حذف کند، این حجم به‌طور خودکار حذف نمی‌شود.

## {{% heading "whatsnext" %}}

* دربارهٔ [PersistentVolumeها](/docs/concepts/storage/persistent-volumes/) بیشتر بیاموزید.
* دربارهٔ [PersistentVolumeClaimها](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) بیشتر بیاموزید.

### مراجع {#reference}

* {{< api-reference page="core/persistent-volume-v1" >}}
  * به [فیلد](/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/#PersistentVolumeSpec)
    `.spec.persistentVolumeReclaimPolicy` در PersistentVolume توجه کنید.
* {{< api-reference page="core/persistent-volume-claim-v1" >}}
