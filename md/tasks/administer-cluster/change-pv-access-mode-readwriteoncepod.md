---
title: تغییر حالت دسترسی یک PersistentVolume به ReadWriteOncePod
content_type: task
weight: 90
min-kubernetes-server-version: v1.22
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان حالت دسترسی (access mode) یک PersistentVolume موجود را به `ReadWriteOncePod` تغییر داد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

{{< note >}}
حالت دسترسی `ReadWriteOncePod` در نسخهٔ v1.29 کوبرنتیز به وضعیت پایدار رسید. اگر از نسخه‌ای قدیمی‌تر از v1.29 کوبرنتیز استفاده می‌کنید، ممکن است لازم باشد یک feature gate را فعال کنید. برای این کار، مستندات نسخهٔ کوبرنتیز خود را بررسی کنید.
{{< /note >}}

{{< note >}}
حالت دسترسی `ReadWriteOncePod` فقط برای حجم‌های (volume)
{{< glossary_tooltip text="CSI" term_id="csi" >}} پشتیبانی می‌شود.
برای استفاده از این حالت دسترسی، باید
[sidecarهای CSI](https://kubernetes-csi.github.io/docs/sidecar-containers.html)
زیر را به این نسخه‌ها یا نسخه‌های بالاتر به‌روزرسانی کنید:

* [csi-provisioner:v3.0.0+](https://github.com/kubernetes-csi/external-provisioner/releases/tag/v3.0.0)
* [csi-attacher:v3.3.0+](https://github.com/kubernetes-csi/external-attacher/releases/tag/v3.3.0)
* [csi-resizer:v1.3.0+](https://github.com/kubernetes-csi/external-resizer/releases/tag/v1.3.0)
{{< /note >}}

## چرا باید از `ReadWriteOncePod` استفاده کنم؟

پیش از نسخهٔ v1.22 کوبرنتیز، معمولاً از حالت دسترسی `ReadWriteOnce` برای محدود کردن دسترسی به PersistentVolume در بارهای کاری (workload) استفاده می‌شد که به دسترسی تک‌نویسنده به فضای ذخیره‌سازی نیاز داشتند. با این حال، این حالت دسترسی یک محدودیت داشت: دسترسی به حجم را به یک *نود* محدود می‌کرد و در نتیجه چند پاد روی همان نود می‌توانستند هم‌زمان از یک حجم بخوانند و در آن بنویسند. این وضعیت می‌توانست برای برنامه‌هایی که برای حفظ ایمنی داده‌ها به دسترسی سخت‌گیرانهٔ تک‌نویسنده نیاز دارند، خطرساز باشد.

اگر تضمین دسترسی تک‌نویسنده برای بارهای کاری شما حیاتی است، مهاجرت حجم‌های خود به `ReadWriteOncePod` را در نظر بگیرید.

<!-- steps -->

## مهاجرت PersistentVolumeهای موجود

اگر PersistentVolumeهایی از قبل دارید، می‌توانید آن‌ها را برای استفاده از `ReadWriteOncePod` مهاجرت دهید. فقط مهاجرت از `ReadWriteOnce` به `ReadWriteOncePod` پشتیبانی می‌شود.

در این مثال، از قبل یک PersistentVolumeClaim با حالت `ReadWriteOnce` به نام "cat-pictures-pvc" وجود دارد که به یک PersistentVolume به نام "cat-pictures-pv" متصل (bound) شده است، و همچنین یک Deployment به نام "cat-pictures-writer" از این PersistentVolumeClaim استفاده می‌کند.

{{< note >}}
اگر افزونهٔ ذخیره‌سازی شما از
[تأمین پویا](/docs/concepts/storage/dynamic-provisioning/)
پشتیبانی کند، "cat-pictures-pv" برای شما ایجاد می‌شود، اما ممکن است نام آن متفاوت باشد. برای دریافت نام PersistentVolume خود، دستور زیر را اجرا کنید:

```shell
kubectl get pvc cat-pictures-pvc -o jsonpath='{.spec.volumeName}'
```
{{< /note >}}

پیش از اعمال تغییرات نیز می‌توانید PVC را مشاهده کنید. برای این کار، یا مانیفست را به‌صورت محلی ببینید، یا دستور `kubectl get pvc <name-of-pvc> -o yaml` را اجرا کنید. خروجی مشابه زیر است:

```yaml
# cat-pictures-pvc.yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: cat-pictures-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

در ادامه، نمونه‌ای از یک Deployment آمده است که به آن PersistentVolumeClaim وابسته است:

```yaml
# cat-pictures-writer-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cat-pictures-writer
spec:
  replicas: 3
  selector:
    matchLabels:
      app: cat-pictures-writer
  template:
    metadata:
      labels:
        app: cat-pictures-writer
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
        volumeMounts:
        - name: cat-pictures
          mountPath: /mnt
      volumes:
      - name: cat-pictures
        persistentVolumeClaim:
          claimName: cat-pictures-pvc
          readOnly: false
```

در گام نخست، باید فیلد `spec.persistentVolumeReclaimPolicy` در PersistentVolume خود را ویرایش کنید و مقدار آن را `Retain` قرار دهید. با این کار مطمئن می‌شوید که هنگام حذف PersistentVolumeClaim متناظر، PersistentVolume شما حذف نمی‌شود:

```shell
kubectl patch pv cat-pictures-pv -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
```

سپس باید همهٔ بارهای کاری‌ای را که از PersistentVolumeClaim متصل به PersistentVolume موردنظر برای مهاجرت استفاده می‌کنند متوقف کنید و پس از آن، PersistentVolumeClaim را حذف کنید. تا پایان مهاجرت، از اعمال هرگونه تغییر دیگر در PersistentVolumeClaim، مانند تغییر اندازهٔ حجم، خودداری کنید.

پس از انجام این کار، باید فیلد `spec.claimRef.uid` در PersistentVolume خود را پاک کنید تا مطمئن شوید که PersistentVolumeClaimها پس از ایجاد دوباره می‌توانند به آن متصل شوند:

```shell
kubectl scale --replicas=0 deployment cat-pictures-writer
kubectl delete pvc cat-pictures-pvc
kubectl patch pv cat-pictures-pv -p '{"spec":{"claimRef":{"uid":""}}}'
```

پس از آن، فهرست حالت‌های دسترسی معتبر PersistentVolume را طوری جایگزین کنید که (فقط) شامل `ReadWriteOncePod` باشد:

```shell
kubectl patch pv cat-pictures-pv -p '{"spec":{"accessModes":["ReadWriteOncePod"]}}'
```

{{< note >}}
حالت دسترسی `ReadWriteOncePod` را نمی‌توان با حالت‌های دسترسی دیگر ترکیب کرد. هنگام به‌روزرسانی، مطمئن شوید که `ReadWriteOncePod` تنها حالت دسترسی روی PersistentVolume است؛ در غیر این صورت، درخواست با شکست مواجه می‌شود.
{{< /note >}}

سپس باید PersistentVolumeClaim خود را طوری تغییر دهید که `ReadWriteOncePod` تنها حالت دسترسی آن باشد. همچنین باید فیلد `spec.volumeName` در PersistentVolumeClaim را برابر نام PersistentVolume خود قرار دهید تا مطمئن شوید که به همین PersistentVolume مشخص متصل می‌شود.

پس از انجام این کار، می‌توانید PersistentVolumeClaim خود را دوباره ایجاد کنید و بارهای کاری خود را راه‌اندازی کنید:

```shell
# IMPORTANT: Make sure to edit your PVC in cat-pictures-pvc.yaml before applying. You need to:
# - Set ReadWriteOncePod as the only access mode
# - Set spec.volumeName to "cat-pictures-pv"

kubectl apply -f cat-pictures-pvc.yaml
kubectl apply -f cat-pictures-writer-deployment.yaml
```

در پایان، اگر پیش‌تر فیلد `spec.persistentVolumeReclaimPolicy` در PersistentVolume خود را تغییر داده‌اید، می‌توانید آن را ویرایش کنید و مقدارش را دوباره به `Delete` برگردانید.

```shell
kubectl patch pv cat-pictures-pv -p '{"spec":{"persistentVolumeReclaimPolicy":"Delete"}}'
```

## {{% heading "whatsnext" %}}

* دربارهٔ [PersistentVolumeها](/docs/concepts/storage/persistent-volumes/) بیشتر بیاموزید.
* دربارهٔ [PersistentVolumeClaimها](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) بیشتر بیاموزید.
* دربارهٔ [پیکربندی یک Pod برای استفاده از PersistentVolume جهت ذخیره‌سازی](/docs/tutorials/configuration/configure-persistent-volume-storage/) بیشتر بیاموزید.
