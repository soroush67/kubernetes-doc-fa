---
title: نصب درایورها و تخصیص دستگاه‌ها با DRA
content_type: tutorial
weight: 60
min-kubernetes-server-version: v1.34
---
<!-- FUTURE MAINTAINERS: 
The original point of this doc was for people (mainly cluster administrators) to
understand the importance of the DRA driver and its interaction with the DRA
APIs. As a result it was a requirement of this tutorial to not use Helm and to
be more direct with all the component installation procedures. While much of
this content is also useful to workload authors, I see the primary audience of
_this_ tutorial as cluster administrators, who I feel also need to understand
how the DRA APIs interact with the driver to maintain them well. If I had to
choose which audience to focus on in this doc, I would choose cluster
administrators. If the prose gets too muddied by considering both of them, I'd
rather make a second tutorial for the workload authors that doesn't go into the
driver at all (since IMHO that is more representative of what we think their
experience should be like) and also potentially goes into much more detailed/ ✨
fun ✨ use cases. 
-->

{{< feature-state feature_gate_name="DynamicResourceAllocation" >}}


<!-- overview -->
این آموزش نشان می‌دهد که چگونه درایورهای
{{< glossary_tooltip term_id="dra" text="تخصیص پویای منابع (DRA)" >}}
را در کلاستر خود نصب کنید و چگونه از آن‌ها همراه با APIهای DRA برای تخصیص
{{< glossary_tooltip text="دستگاه‌ها" term_id="device" >}} به Podها استفاده کنید.
مخاطب این صفحه مدیران کلاستر هستند.

با {{< glossary_tooltip text="تخصیص پویای منابع (DRA)" term_id="dra" >}}،
کلاستر می‌تواند در دسترس بودن و تخصیص منابع سخت‌افزاری را مدیریت کند تا
درخواست‌های مبتنی بر Pod برای نیازمندی‌ها و ترجیحات سخت‌افزاری برآورده شوند. برای
پشتیبانی از این قابلیت، ترکیبی از مؤلفه‌های داخلی کوبرنتیز (مانند زمان‌بند
کوبرنتیز، kubelet و kube-controller-manager) و درایورهای شخص ثالثی که
مالکان دستگاه‌ها ارائه می‌کنند (و درایورهای DRA نامیده می‌شوند)، مسئولیت اعلام،
تخصیص، آماده‌سازی، اتصال (mount)، بررسی سلامت، لغو آماده‌سازی و پاک‌سازی منابع را
در سراسر چرخه عمر Pod به‌طور مشترک بر عهده دارند. این مؤلفه‌ها از طریق مجموعه‌ای
از APIهای مخصوص DRA در گروه API `resource.k8s.io` اطلاعات را با یکدیگر به اشتراک
می‌گذارند. این APIها شامل
{{< glossary_tooltip text="DeviceClassها" term_id="deviceclass" >}}،
{{< glossary_tooltip text="ResourceSliceها" term_id="resourceslice" >}} و
{{< glossary_tooltip text="ResourceClaimها" term_id="resourceclaim" >}} و همچنین
فیلدهای جدیدی در خودِ spec مربوط به Pod هستند.

<!-- objectives -->

### {{% heading "objectives" %}}
* استقرار یک درایور DRA نمونه
* استقرار یک Pod که با استفاده از APIهای DRA یک درخواست سخت‌افزاری (claim) ثبت می‌کند
* حذف Podای که درخواست دارد

<!-- prerequisites -->
## {{% heading "prerequisites" %}}

کلاستر شما باید از [RBAC](/docs/reference/access-authn-authz/rbac/) پشتیبانی کند.
می‌توانید این آموزش را روی کلاستری با سازوکار مجوزدهی دیگری نیز امتحان کنید، اما
در آن صورت باید مراحل مربوط به تعریف نقش‌ها و مجوزها را با آن سازوکار تطبیق دهید.

{{< include "task-tutorial-prereqs.md" >}}

این آموزش روی نودهای لینوکسی آزموده شده است، هرچند ممکن است روی انواع دیگر
نودها نیز کار کند.

{{< version-check >}}

اگر کلاستر شما در حال حاضر کوبرنتیز {{< skew currentVersion >}} را اجرا نمی‌کند،
لطفاً مستندات نسخه‌ای از کوبرنتیز را که قصد استفاده از آن را دارید بررسی کنید.

<!-- lessoncontent -->

## بررسی وضعیت اولیه کلاستر {#explore-initial-state}

می‌توانید کمی زمان بگذارید و وضعیت اولیه کلاستری را که DRA در آن فعال است
مشاهده کنید، به‌ویژه اگر پیش‌تر از این APIها زیاد استفاده نکرده‌اید. اگر برای
این آموزش کلاستر جدیدی راه‌اندازی کرده‌اید که هیچ درایوری روی آن نصب نشده و هنوز
هیچ درخواست Pod برای برآورده شدن ندارد، خروجی این دستورها هیچ منبعی را نشان
نخواهد داد.

1.  فهرست {{< glossary_tooltip text="DeviceClassها" term_id="deviceclass" >}} را دریافت کنید:

    ```shell
    kubectl get deviceclasses
    ```
    خروجی مشابه زیر است:
    ```
    No resources found
    ```

1.  فهرست {{< glossary_tooltip text="ResourceSliceها" term_id="resourceslice" >}} را دریافت کنید:

    ```shell
    kubectl get resourceslices
    ```
    خروجی مشابه زیر است:
    ```
    No resources found
    ```

1.  فهرست {{< glossary_tooltip text="ResourceClaimها" term_id="resourceclaim" >}} و
    {{< glossary_tooltip text="ResourceClaimTemplateها" term_id="resourceclaimtemplate" >}} را دریافت کنید.

    ```shell
    kubectl get resourceclaims -A
    kubectl get resourceclaimtemplates -A
    ```
    خروجی مشابه زیر است:
    ```
    No resources found
    No resources found
    ```

تا اینجا تأیید کرده‌اید که DRA در کلاستر فعال است و به‌درستی پیکربندی شده است و
هنوز هیچ درایور DRA منبعی را به APIهای DRA اعلام نکرده است.

## نصب یک درایور DRA نمونه {#install-example-driver}  

درایورهای DRA برنامه‌های شخص ثالثی هستند که روی هر نود کلاستر شما اجرا می‌شوند تا
میان سخت‌افزار آن نود و مؤلفه‌های داخلی DRA در کوبرنتیز ارتباط برقرار کنند. روند
نصب به درایوری که انتخاب می‌کنید بستگی دارد، اما به احتمال زیاد درایور به‌صورت یک
{{< glossary_tooltip term_id="daemonset" >}} روی همه نودهای کلاستر یا گروهی از آن‌ها
(با استفاده از {{< glossary_tooltip text="انتخابگرها" term_id="selector" >}}
یا سازوکارهای مشابه) مستقر می‌شود.

برای دستورالعمل‌های دقیق نصب، مستندات درایور خود را بررسی کنید. این دستورالعمل‌ها
ممکن است شامل یک Helm chart، مجموعه‌ای از مانیفست‌ها یا ابزارهای استقرار دیگر باشند.

این آموزش برای نمایش نحوه نصب درایور از یک درایور نمونه استفاده می‌کند که در مخزن
[kubernetes-sigs/dra-example-driver](https://github.com/kubernetes-sigs/dra-example-driver)
قرار دارد. این درایور نمونه، GPUهای شبیه‌سازی‌شده‌ای را به کوبرنتیز اعلام می‌کند
تا Podهای شما بتوانند با آن‌ها کار کنند.

### آماده‌سازی کلاستر برای نصب درایور {#prepare-cluster-driver}

برای ساده‌تر شدن پاک‌سازی، یک فضای نام (namespace) با نام dra-tutorial بسازید:

1.  فضای نام را ایجاد کنید:

    ```shell
    kubectl create namespace dra-tutorial 
    ```

    در محیط عملیاتی، به احتمال زیاد از ایمیجی استفاده می‌کنید که پیش‌تر توسط
    سازنده درایور یا سازمان خودتان منتشر یا تأیید شده است، و نودهای شما باید به
    رجیستری ایمیجی که ایمیج درایور در آن میزبانی می‌شود دسترسی داشته باشند. در این
    آموزش، برای شبیه‌سازی دسترسی به ایمیج یک درایور DRA، از ایمیج عمومیِ منتشرشده
    dra-example-driver استفاده می‌کنید.


1.  با اجرای دستور زیر از داخل یکی از نودهای کلاستر، تأیید کنید که نودهای شما به
    این ایمیج دسترسی دارند:

    ```shell
    docker pull registry.k8s.io/dra-example-driver/dra-example-driver:v0.2.0
    ```

### استقرار مؤلفه‌های درایور DRA

در این آموزش، مؤلفه‌های حیاتی درایور منبع نمونه را یکی‌یکی با `kubectl` نصب
می‌کنید.

1.  یک DeviceClass بسازید که نمایانگر انواع دستگاه‌هایی باشد که این درایور DRA
    پشتیبانی می‌کند:

    {{% code_sample language="yaml" file="dra/driver-install/deviceclass.yaml" %}}

    ```shell
    kubectl apply --server-side -f https://k8s.io/examples/dra/driver-install/deviceclass.yaml
    ```

1.  آبجکت‌های ServiceAccount، ClusterRole و ClusterRoleBinding را بسازید. درایور
    از این آبجکت‌ها برای کسب مجوز تعامل با API کوبرنتیز در این کلاستر استفاده
    می‌کند:

    1.  ServiceAccount را بسازید: 

        {{% code_sample language="yaml" file="dra/driver-install/serviceaccount.yaml" %}}

        ```shell
        kubectl apply --server-side -f https://k8s.io/examples/dra/driver-install/serviceaccount.yaml
        ```

    1.  ClusterRole را بسازید: 

        {{% code_sample language="yaml" file="dra/driver-install/clusterrole.yaml" %}}

        ```shell
        kubectl apply --server-side -f https://k8s.io/examples/dra/driver-install/clusterrole.yaml
        ```

    1.  ClusterRoleBinding را بسازید:

        {{% code_sample language="yaml" file="dra/driver-install/clusterrolebinding.yaml" %}}

        ```shell
        kubectl apply --server-side -f https://k8s.io/examples/dra/driver-install/clusterrolebinding.yaml
        ```

1.  یک {{< glossary_tooltip term_id="priority-class" >}} برای درایور DRA بسازید.
    این PriorityClass از پیش‌دستی (preemption) روی مؤلفه درایور DRA جلوگیری
    می‌کند؛ مؤلفه‌ای که مسئول عملیات مهم چرخه عمر Podهای دارای درخواست است.
    [درباره اولویت و پیش‌دستی Pod اینجا بیشتر
    بخوانید](/docs/concepts/scheduling-eviction/pod-priority-preemption/).

    {{% code_sample language="yaml" file="dra/driver-install/priorityclass.yaml" %}}

    ```shell
    kubectl apply --server-side -f https://k8s.io/examples/dra/driver-install/priorityclass.yaml
    ```

1.  خودِ درایور DRA را به‌صورت یک DaemonSet مستقر کنید که برای اجرای فایل اجرایی
    درایور نمونه با مجوزهای فراهم‌شده در مراحل بالا پیکربندی شده است. این DaemonSet
    مجوزهایی را دارد که در مراحل قبل به ServiceAccount اعطا کردید.

    {{% code_sample language="yaml" file="dra/driver-install/daemonset.yaml" %}}

    ```shell
    kubectl apply --server-side -f https://k8s.io/examples/dra/driver-install/daemonset.yaml
    ```

    این DaemonSet با اتصال‌های حجم (volume mount) لازم پیکربندی شده است تا بتواند
    با دایرکتوری زیربنایی رابط دستگاه کانتینر (Container Device Interface یا CDI)
    تعامل کند و سوکت خود را از طریق دایرکتوری `kubelet/plugins` در اختیار `kubelet`
    قرار دهد.

### بررسی نصب درایور DRA {#verify-driver-install}

1.  فهرست Podهای DaemonSet درایور DRA را روی همه نودهای کارگر دریافت کنید:

    ```shell
    kubectl get pod -l app.kubernetes.io/name=dra-example-driver -n dra-tutorial
    ```
    خروجی مشابه زیر است:
    ```
    NAME                                     READY   STATUS    RESTARTS   AGE
    dra-example-driver-kubeletplugin-4sk2x   1/1     Running   0          13s
    dra-example-driver-kubeletplugin-cttr2   1/1     Running   0          13s
    ```


1.  نخستین وظیفه درایور DRA محلی در هر نود این است که با انتشار فراداده‌های خود در
    API مربوط به ResourceSliceها، کلاستر را از دستگاه‌هایی که در آن نود برای Podها
    در دسترس هستند آگاه کند. می‌توانید این API را بررسی کنید تا ببینید هر نودی که
    درایور دارد، کلاس دستگاهی را که نمایندگی می‌کند اعلام کرده است.

    ResourceSliceهای در دسترس را بررسی کنید:

    ```shell
    kubectl get resourceslices
    ```
    خروجی مشابه زیر است:
    ```
    NAME                                 NODE           DRIVER            POOL           AGE
    kind-worker-gpu.example.com-k69gd    kind-worker    gpu.example.com   kind-worker    19s
    kind-worker2-gpu.example.com-qdgpn   kind-worker2   gpu.example.com   kind-worker2   19s
    ```

تا اینجا درایور DRA نمونه را با موفقیت نصب کرده‌اید و پیکربندی اولیه آن را تأیید
کرده‌اید. اکنون آماده‌اید تا از DRA برای زمان‌بندی Podها استفاده کنید.

## درخواست منابع و استقرار یک Pod {#claim-resources-pod}

برای درخواست منابع با استفاده از DRA، ResourceClaimها یا ResourceClaimTemplateهایی
می‌سازید که منابع مورد نیاز Podهای شما را تعریف می‌کنند. در درایور نمونه، یک ویژگی
ظرفیت حافظه برای دستگاه‌های GPU ساختگی ارائه شده است. این بخش نشان می‌دهد چگونه
با استفاده از {{< glossary_tooltip term_id="cel" >}} نیازمندی‌های خود را در یک
ResourceClaim بیان کنید، آن ResourceClaim را در مشخصات یک Pod انتخاب کنید و
تخصیص منبع را مشاهده کنید.

این آموزش تنها یک نمونه ساده از ResourceClaim در DRA را نشان می‌دهد. برای آشنایی
بیشتر با ResourceClaimها، صفحه
[تخصیص پویای منابع](/docs/concepts/resource-management/dynamic-resource-allocation/)
را بخوانید.

### ساخت ResourceClaim

در این بخش، یک ResourceClaim می‌سازید و در یک Pod به آن ارجاع می‌دهید. درخواست هر
چه باشد، فیلد `deviceClassName` الزامی است و دامنه درخواست را به یک کلاس دستگاه
مشخص محدود می‌کند. خودِ درخواست می‌تواند شامل یک عبارت
{{< glossary_tooltip term_id="cel" >}} باشد که به ویژگی‌هایی ارجاع می‌دهد که ممکن
است درایورِ مدیریت‌کننده آن کلاس دستگاه اعلام کرده باشد.

در این مثال، درخواستی برای هر GPU‌ای می‌سازید که ظرفیت حافظه‌ای بیش از 10Gi اعلام
کرده باشد. ویژگی‌ای که درایور نمونه ظرفیت را با آن ارائه می‌کند، به شکل
`device.capacity['gpu.example.com'].memory` است. همچنین توجه کنید که نام این
درخواست `some-gpu` تعیین شده است.

{{% code_sample language="yaml" file="dra/driver-install/example/resourceclaim.yaml" %}}

```shell
kubectl apply --server-side -f https://k8s.io/examples/dra/driver-install/example/resourceclaim.yaml
```

### ساخت Podای که به آن ResourceClaim ارجاع می‌دهد

در ادامه، مانیفست Podای آمده است که در فیلد `spec.resourceClaims.resourceClaimName`
به ResourceClaimی که همین حالا ساختید، یعنی `some-gpu`، ارجاع می‌دهد. سپس نام
محلی این درخواست، یعنی `gpu`، در فیلد `spec.containers.resources.claims.name`
به کار می‌رود تا درخواست به کانتینر زیربنایی Pod تخصیص یابد.

{{% code_sample language="yaml" file="dra/driver-install/example/pod.yaml" %}}

```shell
kubectl apply --server-side -f https://k8s.io/examples/dra/driver-install/example/pod.yaml
```

تأیید کنید که Pod مستقر شده است:

```shell
kubectl get pod pod0 -n dra-tutorial
```

خروجی مشابه زیر است:

```
NAME   READY   STATUS    RESTARTS   AGE
pod0   1/1     Running   0          9s
```

### بررسی وضعیت DRA

پس از ساخت Pod، کلاستر تلاش می‌کند آن Pod را روی نودی زمان‌بندی کند که کوبرنتیز
بتواند ResourceClaim را در آن برآورده کند. در این آموزش، درایور DRA روی همه نودها
مستقر شده است و روی همه آن‌ها GPUهای ساختگی اعلام می‌کند و همه این GPUها ظرفیت
کافی برای برآورده کردن درخواست Pod اعلام کرده‌اند. بنابراین کوبرنتیز می‌تواند این
Pod را روی هر نودی زمان‌بندی کند و هر یک از GPUهای ساختگی آن نود را تخصیص دهد.

وقتی کوبرنتیز یک GPU ساختگی را به یک Pod تخصیص می‌دهد، درایور نمونه در هر کانتینری
که GPU به آن تخصیص یافته، متغیرهای محیطی اضافه می‌کند. این متغیرها نشان می‌دهند
که یک درایور منبع واقعی _کدام_ GPUها را به آن کانتینرها تزریق می‌کرد و آن‌ها را
چگونه پیکربندی می‌کرد. به این ترتیب می‌توانید با بررسی این متغیرهای محیطی ببینید
سیستم Podها را چگونه مدیریت کرده است.

1.  لاگ‌های Pod را بررسی کنید که نام GPU ساختگیِ تخصیص‌یافته را گزارش می‌کنند:

    ```shell
    kubectl logs pod0 -c ctr0 -n dra-tutorial | grep -E "GPU_DEVICE_[0-9]+=" | grep -v "RESOURCE_CLAIM"
    ```

    خروجی مشابه زیر است:
    ```
    declare -x GPU_DEVICE_0="gpu-0"
    ```

1.  وضعیت آبجکت ResourceClaim را بررسی کنید:

    ```shell
    kubectl get resourceclaims -n dra-tutorial
    ```

    خروجی مشابه زیر است:

    ```
    NAME       STATE                AGE
    some-gpu   allocated,reserved   34s
    ```

    در این خروجی، ستون `STATE` نشان می‌دهد که ResourceClaim تخصیص یافته و رزرو
    شده است.

1.  جزئیات ResourceClaim با نام `some-gpu` را بررسی کنید. بخش `status` در
    ResourceClaim اطلاعاتی درباره دستگاه تخصیص‌یافته و Podای که دستگاه برای آن
    رزرو شده است در بر دارد:

    ```shell
    kubectl get resourceclaim some-gpu -n dra-tutorial -o yaml
    ```

    خروجی مشابه زیر است:

    {{< highlight yaml "linenos=inline, hl_lines=27-30 38-41, style=emacs" >}}
    apiVersion: resource.k8s.io/v1
    kind: ResourceClaim
    metadata:
      creationTimestamp: "2025-08-20T18:17:31Z"
      finalizers:
      - resource.kubernetes.io/delete-protection
      name: some-gpu
      namespace: dra-tutorial
      resourceVersion: "2326"
      uid: d3e48dbf-40da-47c3-a7b9-f7d54d1051c3
    spec:
      devices:
        requests:
        - exactly:
            allocationMode: ExactCount
            count: 1
            deviceClassName: gpu.example.com
            selectors:
            - cel:
                expression: device.capacity['gpu.example.com'].memory.compareTo(quantity('10Gi'))
                >= 0
          name: some-gpu
    status:
      allocation:
        devices:
          results:
          - device: gpu-0
            driver: gpu.example.com
            pool: kind-worker
            request: some-gpu
        nodeSelector:
          nodeSelectorTerms:
          - matchFields:
            - key: metadata.name
              operator: In
              values:
              - kind-worker
      reservedFor:
      - name: pod0
        resource: pods
        uid: c4dadf20-392a-474d-a47b-ab82080c8bd7
    {{< /highlight >}}

1.  برای اینکه ببینید درایور تخصیص دستگاه را چگونه انجام داده است، لاگ‌های
    Podهای DaemonSet درایور را دریافت کنید:

    ```shell
    kubectl logs -l app.kubernetes.io/name=dra-example-driver -n dra-tutorial
    ```

    خروجی مشابه زیر است:
    ```
    I0820 18:17:44.131324       1 driver.go:106] PrepareResourceClaims is called: number of claims: 1
    I0820 18:17:44.135056       1 driver.go:133] Returning newly prepared devices for claim 'd3e48dbf-40da-47c3-a7b9-f7d54d1051c3': [{[some-gpu] kind-worker gpu-0 [k8s.gpu.example.com/gpu=common k8s.gpu.example.com/gpu=d3e48dbf-40da-47c3-a7b9-f7d54d1051c3-gpu-0]}]
    ```

اکنون Podای را که با استفاده از DRA دستگاه درخواست می‌کند با موفقیت مستقر کرده‌اید،
تأیید کرده‌اید که Pod روی نود مناسبی زمان‌بندی شده است و دیدید که انواع API مرتبط
با DRA با وضعیت تخصیص به‌روزرسانی شده‌اند.

## حذف Podای که درخواست دارد {#delete-pod-claim}

وقتی Podای که درخواست دارد حذف می‌شود، درایور DRA تخصیص منبع را آزاد می‌کند تا
منبع برای زمان‌بندی‌های آینده در دسترس باشد. برای بررسی این رفتار، Podای را که در
مراحل قبل ساختید حذف کنید و تغییرات متناظر را در ResourceClaim و درایور مشاهده کنید.

Pod با نام `pod0` را حذف کنید:

```shell
kubectl delete pod pod0 -n dra-tutorial
```

خروجی مشابه زیر است:

```
pod "pod0" deleted
```

### مشاهده وضعیت DRA

وقتی Pod حذف می‌شود، درایور تخصیص دستگاه را از ResourceClaim آزاد می‌کند و منبع
ResourceClaim را در API کوبرنتیز به‌روزرسانی می‌کند. این ResourceClaim تا زمانی
که در یک Pod جدید به آن ارجاع داده شود، در وضعیت `pending` باقی می‌ماند.

1.  وضعیت ResourceClaim با نام `some-gpu` را بررسی کنید:

    ```shell
    kubectl get resourceclaims -n dra-tutorial
    ```

    خروجی مشابه زیر است:
    ```
    NAME       STATE     AGE
    some-gpu   pending   76s
    ```

1.  با بررسی لاگ‌های درایور، تأیید کنید که درایور لغو آماده‌سازی دستگاه را برای
    این درخواست انجام داده است:

    ```shell
    kubectl logs -l app.kubernetes.io/name=dra-example-driver -n dra-tutorial
    ```
    خروجی مشابه زیر است:
    ```
    I0820 18:22:15.629376       1 driver.go:138] UnprepareResourceClaims is called: number of claims: 1
    ```

اکنون Podای را که درخواست داشت حذف کرده‌اید و مشاهده کردید که درایور، آماده‌سازی
منبع سخت‌افزاری زیربنایی را لغو کرد و APIهای DRA را به‌روزرسانی کرد تا نشان دهد
منبع دوباره برای زمان‌بندی‌های آینده در دسترس است.

## {{% heading "cleanup" %}}

برای پاک‌سازی منابعی که در این آموزش ساختید، مراحل زیر را دنبال کنید:

```shell
kubectl delete namespace dra-tutorial
kubectl delete deviceclass gpu.example.com
kubectl delete clusterrole dra-example-driver-role
kubectl delete clusterrolebinding dra-example-driver-role-binding
kubectl delete priorityclass dra-driver-high-priority
```

## {{% heading "whatsnext" %}}

* [درباره DRA بیشتر بدانید](/docs/concepts/resource-management/dynamic-resource-allocation/)
* [تخصیص دستگاه‌ها به بارهای کاری با DRA](/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra)
