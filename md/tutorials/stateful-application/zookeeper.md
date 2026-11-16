---
reviewers:
- bprashanth
- enisoc
- erictune
- foxish
- janetkuo
- kow3ns
- smarterclayton
title: اجرای ZooKeeper، یک هماهنگ‌کنندهٔ سیستم‌های توزیع‌شده
content_type: tutorial
weight: 40
---

<!-- overview -->
این آموزش نحوهٔ اجرای [Apache Zookeeper](https://zookeeper.apache.org) را روی
کوبرنتیز با استفاده از [StatefulSetها](/docs/concepts/workloads/controllers/statefulset/)،
[PodDisruptionBudgetها](/docs/concepts/workloads/pods/disruptions/#pod-disruption-budget)
و [PodAntiAffinity](/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) نشان می‌دهد.

## {{% heading "prerequisites" %}}

پیش از شروع این آموزش، باید با مفاهیم زیر در کوبرنتیز آشنا باشید:

- [پادها (Pods)](/docs/concepts/workloads/pods/)
- [DNS کلاستر](/docs/concepts/services-networking/dns-pod-service/)
- [سرویس‌های Headless](/docs/concepts/services-networking/service/#headless-services)
- [PersistentVolumeها](/docs/concepts/storage/persistent-volumes/) 
- [StatefulSetها](/docs/concepts/workloads/controllers/statefulset/)
- [PodDisruptionBudgetها](/docs/concepts/workloads/pods/disruptions/#pod-disruption-budget)
- [PodAntiAffinity](/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)
- [رابط خط فرمان kubectl](/docs/reference/kubectl/kubectl/)

به کلاستری با دست‌کم چهار نود نیاز دارید و هر نود باید دست‌کم ۲ پردازندهٔ مجازی (CPU) و ۴ گیبی‌بایت حافظه داشته باشد. در این آموزش، نودهای کلاستر را cordon و drain می‌کنید. **این یعنی کلاستر همهٔ Podهای روی نودهایش را خاتمه می‌دهد و بیرون می‌راند (evict) و نودها به‌طور موقت زمان‌بندی‌ناپذیر می‌شوند.** بهتر است برای این آموزش از یک کلاستر اختصاصی استفاده کنید، یا مطمئن شوید که اختلالی که ایجاد می‌کنید در کار سایر مستأجران (tenants) تداخلی ایجاد نمی‌کند.

این آموزش فرض می‌کند که کلاستر خود را برای فراهم‌سازی پویای PersistentVolumeها
پیکربندی کرده‌اید. اگر کلاستر شما چنین پیکربندی‌ای ندارد، باید پیش از شروع این
آموزش، سه حجم (volume) ۲۰ گیبی‌بایتی را به‌صورت دستی فراهم کنید.

## {{% heading "objectives" %}}

پس از این آموزش، موارد زیر را خواهید آموخت:

- چگونه یک مجموعهٔ ZooKeeper (ensemble) را با استفاده از StatefulSet مستقر کنید.
- چگونه مجموعه را به‌شکلی یکنواخت پیکربندی کنید.
- چگونه استقرار سرورهای ZooKeeper را در مجموعه پخش کنید.
- چگونه با استفاده از PodDisruptionBudgetها، دسترس‌پذیری سرویس را در طول نگهداری‌های برنامه‌ریزی‌شده تضمین کنید.

<!-- lessoncontent -->

### ZooKeeper

[Apache ZooKeeper](https://zookeeper.apache.org/doc/current/) یک سرویس
هماهنگ‌سازی توزیع‌شده و متن‌باز برای برنامه‌های توزیع‌شده است.
با ZooKeeper می‌توانید داده‌ها را بخوانید، بنویسید و به‌روزرسانی‌های آن‌ها را مشاهده کنید.
داده‌ها در سلسله‌مراتبی شبیه به سیستم فایل سازمان‌دهی می‌شوند و روی همهٔ سرورهای
ZooKeeper در مجموعه (مجموعه‌ای از سرورهای ZooKeeper) تکثیر می‌شوند. همهٔ عملیات روی
داده‌ها اتمیک و به‌صورت ترتیبی سازگار هستند. ZooKeeper این ویژگی را با استفاده از
پروتکل اجماع [Zab](https://pdfs.semanticscholar.org/b02c/6b00bd5dbdbd951fddb00b906c82fa80f0b3.pdf)
تضمین می‌کند؛ این پروتکل یک ماشین حالت را روی همهٔ سرورهای مجموعه تکثیر می‌کند.

مجموعه از پروتکل Zab برای انتخاب رهبر استفاده می‌کند و تا زمانی که این انتخاب کامل نشود، نمی‌تواند داده بنویسد. پس از کامل شدن انتخاب، مجموعه با استفاده از Zab تضمین می‌کند که همهٔ نوشتن‌ها را پیش از تأیید و قابل‌مشاهده کردن آن‌ها برای کلاینت‌ها، روی یک حد نصاب (quorum) تکثیر کند. صرف‌نظر از حد نصاب‌های وزن‌دار، حد نصاب بخشی از مجموعه است که اکثریت را تشکیل می‌دهد و رهبر فعلی را در بر دارد. برای مثال، اگر مجموعه سه سرور داشته باشد، بخشی که شامل رهبر و یک سرور دیگر باشد، حد نصاب را تشکیل می‌دهد. اگر مجموعه نتواند به حد نصاب برسد، نمی‌تواند داده بنویسد.

سرورهای ZooKeeper کل ماشین حالت خود را در حافظه نگه می‌دارند و هر تغییر را در یک WAL (Write Ahead Log، گزارش پیش‌نویسی) ماندگار روی رسانهٔ ذخیره‌سازی می‌نویسند. وقتی سروری از کار می‌افتد، می‌تواند با بازپخش WAL، حالت قبلی خود را بازیابی کند. برای جلوگیری از رشد بی‌حد WAL، سرورهای ZooKeeper به‌طور دوره‌ای از حالت درون حافظهٔ خود یک تصویر لحظه‌ای (snapshot) روی رسانهٔ ذخیره‌سازی ثبت می‌کنند. این تصاویر لحظه‌ای را می‌توان مستقیماً در حافظه بارگذاری کرد و همهٔ ورودی‌های WAL که پیش از تصویر لحظه‌ای ثبت شده‌اند، قابل حذف هستند.

## ایجاد یک مجموعهٔ ZooKeeper

مانیفست زیر شامل یک
[سرویس Headless](/docs/concepts/services-networking/service/#headless-services)،
یک [Service](/docs/concepts/services-networking/service/)،
یک [PodDisruptionBudget](/docs/concepts/workloads/pods/disruptions/#pod-disruption-budgets)
و یک [StatefulSet](/docs/concepts/workloads/controllers/statefulset/) است.

{{% code_sample file="application/zookeeper/zookeeper.yaml" %}}

یک ترمینال باز کنید و با دستور
[`kubectl apply`](/docs/reference/generated/kubectl/kubectl-commands/#apply)
مانیفست را ایجاد کنید.

```shell
kubectl apply -f https://k8s.io/examples/application/zookeeper/zookeeper.yaml
```

این دستور سرویس Headless با نام `zk-hs`، سرویس `zk-cs`،
PodDisruptionBudget با نام `zk-pdb` و StatefulSet با نام `zk` را ایجاد می‌کند.

```
service/zk-hs created
service/zk-cs created
poddisruptionbudget.policy/zk-pdb created
statefulset.apps/zk created
```

با استفاده از [`kubectl get`](/docs/reference/generated/kubectl/kubectl-commands/#get)، ایجاد Podهای StatefulSet
به‌دست کنترل‌کنندهٔ StatefulSet را مشاهده کنید.

```shell
kubectl get pods -w -l app=zk
```

وقتی Pod با نام `zk-2` در وضعیت Running و Ready قرار گرفت، با `CTRL-C` اجرای kubectl را خاتمه دهید.

```
NAME      READY     STATUS    RESTARTS   AGE
zk-0      0/1       Pending   0          0s
zk-0      0/1       Pending   0         0s
zk-0      0/1       ContainerCreating   0         0s
zk-0      0/1       Running   0         19s
zk-0      1/1       Running   0         40s
zk-1      0/1       Pending   0         0s
zk-1      0/1       Pending   0         0s
zk-1      0/1       ContainerCreating   0         0s
zk-1      0/1       Running   0         18s
zk-1      1/1       Running   0         40s
zk-2      0/1       Pending   0         0s
zk-2      0/1       Pending   0         0s
zk-2      0/1       ContainerCreating   0         0s
zk-2      0/1       Running   0         19s
zk-2      1/1       Running   0         40s
```

کنترل‌کنندهٔ StatefulSet سه Pod ایجاد می‌کند و هر Pod یک کانتینر دارد که
یک سرور [ZooKeeper](https://archive.apache.org/dist/zookeeper/stable/) را اجرا می‌کند.

### تسهیل انتخاب رهبر

از آنجا که در یک شبکهٔ ناشناس هیچ الگوریتم پایان‌پذیری برای انتخاب رهبر وجود ندارد، پروتکل Zab برای انجام انتخاب رهبر به پیکربندی صریح اعضا نیاز دارد. هر سرور در مجموعه باید شناسهٔ یکتایی داشته باشد، همهٔ سرورها باید مجموعهٔ سراسری شناسه‌ها را بدانند و هر شناسه باید به یک نشانی شبکه مرتبط باشد.

با استفاده از [`kubectl exec`](/docs/reference/generated/kubectl/kubectl-commands/#exec)، نام میزبان (hostname)
Podهای StatefulSet با نام `zk` را به دست آورید.

```shell
for i in 0 1 2; do kubectl exec zk-$i -- hostname; done
```

کنترل‌کنندهٔ StatefulSet به هر Pod نام میزبان یکتایی بر اساس اندیس ترتیبی آن اختصاص می‌دهد. نام‌های میزبان به شکل `<statefulset name>-<ordinal index>` هستند. از آنجا که فیلد `replicas` در StatefulSet با نام `zk` روی `3` تنظیم شده است، کنترل‌کنندهٔ این مجموعه سه Pod با نام‌های میزبان `zk-0`، `zk-1` و
`zk-2` ایجاد می‌کند.

```
zk-0
zk-1
zk-2
```

سرورهای یک مجموعهٔ ZooKeeper از اعداد طبیعی به‌عنوان شناسهٔ یکتا استفاده می‌کنند و شناسهٔ هر سرور را در فایلی به نام `myid` در دایرکتوری داده‌های آن سرور ذخیره می‌کنند.

برای بررسی محتوای فایل `myid` هر سرور، از دستور زیر استفاده کنید.

```shell
for i in 0 1 2; do echo "myid zk-$i";kubectl exec zk-$i -- cat /var/lib/zookeeper/data/myid; done
```

از آنجا که شناسه‌ها اعداد طبیعی و اندیس‌های ترتیبی اعداد صحیح نامنفی هستند، می‌توانید با افزودن ۱ به اندیس ترتیبی، یک شناسه تولید کنید.

```
myid zk-0
1
myid zk-1
2
myid zk-2
3
```

برای به دست آوردن نام دامنهٔ کاملاً مشخص (FQDN) هر Pod در StatefulSet با نام `zk`، از دستور زیر استفاده کنید.

```shell
for i in 0 1 2; do kubectl exec zk-$i -- hostname -f; done
```

سرویس `zk-hs` برای همهٔ Podها دامنهٔ
`zk-hs.default.svc.cluster.local` را ایجاد می‌کند.

```
zk-0.zk-hs.default.svc.cluster.local
zk-1.zk-hs.default.svc.cluster.local
zk-2.zk-hs.default.svc.cluster.local
```

رکوردهای A در [DNS کوبرنتیز](/docs/concepts/services-networking/dns-pod-service/)، این FQDNها را به نشانی‌های IP پادها ترجمه می‌کنند. اگر کوبرنتیز Podها را دوباره زمان‌بندی کند، رکوردهای A را با نشانی‌های IP جدید Podها به‌روزرسانی می‌کند، اما نام رکوردهای A تغییر نمی‌کند.

ZooKeeper پیکربندی برنامهٔ خود را در فایلی به نام `zoo.cfg` ذخیره می‌کند. با استفاده از `kubectl exec`، محتوای فایل `zoo.cfg` را در Pod با نام `zk-0` مشاهده کنید.

```shell
kubectl exec zk-0 -- cat /opt/zookeeper/conf/zoo.cfg
```

در ویژگی‌های `server.1`، `server.2` و `server.3` در انتهای فایل،
اعداد `1`، `2` و `3` با شناسه‌های موجود در فایل‌های `myid` سرورهای
ZooKeeper متناظر هستند. این ویژگی‌ها روی FQDNهای Podهای StatefulSet با نام
`zk` تنظیم شده‌اند.

```
clientPort=2181
dataDir=/var/lib/zookeeper/data
dataLogDir=/var/lib/zookeeper/log
tickTime=2000
initLimit=10
syncLimit=2000
maxClientCnxns=60
minSessionTimeout= 4000
maxSessionTimeout= 40000
autopurge.snapRetainCount=3
autopurge.purgeInterval=0
server.1=zk-0.zk-hs.default.svc.cluster.local:2888:3888
server.2=zk-1.zk-hs.default.svc.cluster.local:2888:3888
server.3=zk-2.zk-hs.default.svc.cluster.local:2888:3888
```

### دستیابی به اجماع

پروتکل‌های اجماع نیاز دارند که شناسهٔ هر مشارکت‌کننده یکتا باشد. در پروتکل Zab هیچ دو مشارکت‌کننده‌ای نباید ادعای شناسهٔ یکتای یکسانی داشته باشند. این شرط لازم است تا فرایندهای سیستم بتوانند بر سر اینکه کدام فرایندها کدام داده‌ها را ثبت (commit) کرده‌اند، به توافق برسند. اگر دو Pod با اندیس ترتیبی یکسان راه‌اندازی شوند، دو سرور ZooKeeper هر دو خود را به‌عنوان یک سرور واحد معرفی می‌کنند.

```shell
kubectl get pods -w -l app=zk
```

```
NAME      READY     STATUS    RESTARTS   AGE
zk-0      0/1       Pending   0          0s
zk-0      0/1       Pending   0         0s
zk-0      0/1       ContainerCreating   0         0s
zk-0      0/1       Running   0         19s
zk-0      1/1       Running   0         40s
zk-1      0/1       Pending   0         0s
zk-1      0/1       Pending   0         0s
zk-1      0/1       ContainerCreating   0         0s
zk-1      0/1       Running   0         18s
zk-1      1/1       Running   0         40s
zk-2      0/1       Pending   0         0s
zk-2      0/1       Pending   0         0s
zk-2      0/1       ContainerCreating   0         0s
zk-2      0/1       Running   0         19s
zk-2      1/1       Running   0         40s
```

رکوردهای A هر Pod زمانی ثبت می‌شوند که آن Pod به وضعیت Ready برسد. بنابراین،
FQDN هر سرور ZooKeeper تنها به یک نقطهٔ پایانی (endpoint) ترجمه می‌شود و آن
نقطهٔ پایانی همان سرور یکتای ZooKeeper است که هویت پیکربندی‌شده در فایل `myid`
خود را اعلام می‌کند.

```
zk-0.zk-hs.default.svc.cluster.local
zk-1.zk-hs.default.svc.cluster.local
zk-2.zk-hs.default.svc.cluster.local
```

این امر تضمین می‌کند که ویژگی‌های `servers` در فایل‌های `zoo.cfg` سرورهای ZooKeeper،
نمایانگر مجموعه‌ای با پیکربندی درست باشند.

```
server.1=zk-0.zk-hs.default.svc.cluster.local:2888:3888
server.2=zk-1.zk-hs.default.svc.cluster.local:2888:3888
server.3=zk-2.zk-hs.default.svc.cluster.local:2888:3888
```

وقتی سرورها با استفاده از پروتکل Zab تلاش می‌کنند مقداری را ثبت کنند، یا به اجماع می‌رسند و مقدار را ثبت می‌کنند (اگر انتخاب رهبر موفقیت‌آمیز بوده و دست‌کم دو Pod در وضعیت Running و Ready باشند)، یا در این کار ناکام می‌مانند (اگر هر یک از این شرایط برقرار نباشد). هیچ‌گاه وضعیتی پیش نمی‌آید که در آن یک سرور، نوشتنی را از طرف سرور دیگری تأیید کند.

### آزمون سلامت مجموعه

ابتدایی‌ترین آزمون سلامت این است که داده‌ای را در یک سرور ZooKeeper بنویسید و
آن را از سرور دیگری بخوانید.

دستور زیر اسکریپت `zkCli.sh` را اجرا می‌کند تا مقدار `world` را در مسیر `/hello` روی Pod با نام `zk-0` در مجموعه بنویسد.

```shell
kubectl exec zk-0 -- zkCli.sh create /hello world
```

```
WATCHER::

WatchedEvent state:SyncConnected type:None path:null
Created /hello
```

برای دریافت داده از Pod با نام `zk-1`، از دستور زیر استفاده کنید.

```shell
kubectl exec zk-1 -- zkCli.sh get /hello
```

داده‌ای که روی `zk-0` ایجاد کردید، روی همهٔ سرورهای مجموعه در دسترس است.

```
WATCHER::

WatchedEvent state:SyncConnected type:None path:null
world
cZxid = 0x100000002
ctime = Thu Dec 08 15:13:30 UTC 2016
mZxid = 0x100000002
mtime = Thu Dec 08 15:13:30 UTC 2016
pZxid = 0x100000002
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 5
numChildren = 0
```

### فراهم کردن ذخیره‌سازی ماندگار

همان‌طور که در بخش [مبانی ZooKeeper](#zookeeper) گفته شد،
ZooKeeper همهٔ ورودی‌ها را در یک WAL ماندگار ثبت می‌کند و به‌طور دوره‌ای از حالت
درون حافظه، تصاویر لحظه‌ای روی رسانهٔ ذخیره‌سازی می‌نویسد. استفاده از WAL برای
تأمین ماندگاری، روشی رایج در برنامه‌هایی است که برای دستیابی به یک ماشین حالت
تکثیرشده از پروتکل‌های اجماع استفاده می‌کنند.

با دستور [`kubectl delete`](/docs/reference/generated/kubectl/kubectl-commands/#delete)،
StatefulSet با نام `zk` را حذف کنید.

```shell
kubectl delete statefulset zk
```

```
statefulset.apps "zk" deleted
```

خاتمه یافتن Podهای StatefulSet را مشاهده کنید.

```shell
kubectl get pods -w -l app=zk
```

وقتی `zk-0` به‌طور کامل خاتمه یافت، با `CTRL-C` اجرای kubectl را خاتمه دهید.

```
zk-2      1/1       Terminating   0         9m
zk-0      1/1       Terminating   0         11m
zk-1      1/1       Terminating   0         10m
zk-2      0/1       Terminating   0         9m
zk-2      0/1       Terminating   0         9m
zk-2      0/1       Terminating   0         9m
zk-1      0/1       Terminating   0         10m
zk-1      0/1       Terminating   0         10m
zk-1      0/1       Terminating   0         10m
zk-0      0/1       Terminating   0         11m
zk-0      0/1       Terminating   0         11m
zk-0      0/1       Terminating   0         11m
```

مانیفست موجود در `zookeeper.yaml` را دوباره اعمال کنید.

```shell
kubectl apply -f https://k8s.io/examples/application/zookeeper/zookeeper.yaml
```

این دستور آبجکت StatefulSet با نام `zk` را ایجاد می‌کند، اما سایر آبجکت‌های API موجود در مانیفست تغییری نمی‌کنند، زیرا از قبل وجود دارند.

بازسازی Podهای StatefulSet به‌دست کنترل‌کنندهٔ StatefulSet را مشاهده کنید.

```shell
kubectl get pods -w -l app=zk
```

وقتی Pod با نام `zk-2` در وضعیت Running و Ready قرار گرفت، با `CTRL-C` اجرای kubectl را خاتمه دهید.

```
NAME      READY     STATUS    RESTARTS   AGE
zk-0      0/1       Pending   0          0s
zk-0      0/1       Pending   0         0s
zk-0      0/1       ContainerCreating   0         0s
zk-0      0/1       Running   0         19s
zk-0      1/1       Running   0         40s
zk-1      0/1       Pending   0         0s
zk-1      0/1       Pending   0         0s
zk-1      0/1       ContainerCreating   0         0s
zk-1      0/1       Running   0         18s
zk-1      1/1       Running   0         40s
zk-2      0/1       Pending   0         0s
zk-2      0/1       Pending   0         0s
zk-2      0/1       ContainerCreating   0         0s
zk-2      0/1       Running   0         19s
zk-2      1/1       Running   0         40s
```

با دستور زیر، مقداری را که در طول [آزمون سلامت](#sanity-testing-the-ensemble) وارد کردید،
از Pod با نام `zk-2` دریافت کنید.

```shell
kubectl exec zk-2 zkCli.sh get /hello
```

با اینکه همهٔ Podهای StatefulSet با نام `zk` را خاتمه دادید و دوباره ایجاد کردید، مجموعه همچنان مقدار اولیه را ارائه می‌دهد.

```
WATCHER::

WatchedEvent state:SyncConnected type:None path:null
world
cZxid = 0x100000002
ctime = Thu Dec 08 15:13:30 UTC 2016
mZxid = 0x100000002
mtime = Thu Dec 08 15:13:30 UTC 2016
pZxid = 0x100000002
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 5
numChildren = 0
```

فیلد `volumeClaimTemplates` در `spec` مربوط به StatefulSet با نام `zk`، یک PersistentVolume را مشخص می‌کند که برای هر Pod فراهم می‌شود.

```yaml
volumeClaimTemplates:
  - metadata:
      name: datadir
      annotations:
        volume.alpha.kubernetes.io/storage-class: anything
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 20Gi
```

کنترل‌کنندهٔ `StatefulSet` برای هر Pod در `StatefulSet` یک
`PersistentVolumeClaim` تولید می‌کند.

برای دریافت `PersistentVolumeClaims` مربوط به `StatefulSet`، از دستور زیر استفاده کنید.

```shell
kubectl get pvc -l app=zk
```

وقتی `StatefulSet` پادهای خود را دوباره ایجاد کرد، PersistentVolumeهای Podها را دوباره متصل (mount) می‌کند.

```
NAME           STATUS    VOLUME                                     CAPACITY   ACCESSMODES   AGE
datadir-zk-0   Bound     pvc-bed742cd-bcb1-11e6-994f-42010a800002   20Gi       RWO           1h
datadir-zk-1   Bound     pvc-bedd27d2-bcb1-11e6-994f-42010a800002   20Gi       RWO           1h
datadir-zk-2   Bound     pvc-bee0817e-bcb1-11e6-994f-42010a800002   20Gi       RWO           1h
```

بخش `volumeMounts` در `template` کانتینر `StatefulSet`، این PersistentVolumeها را در دایرکتوری‌های داده‌های سرورهای ZooKeeper متصل می‌کند.

```yaml
volumeMounts:
- name: datadir
  mountPath: /var/lib/zookeeper
```

هر بار که یک Pod در `StatefulSet` با نام `zk` زمان‌بندی (یا دوباره زمان‌بندی) شود،
همیشه همان `PersistentVolume` به دایرکتوری داده‌های سرور ZooKeeper آن متصل می‌شود.
حتی وقتی Podها دوباره زمان‌بندی می‌شوند، همهٔ نوشتن‌هایی که در WAL سرورهای
ZooKeeper انجام شده و همهٔ تصاویر لحظه‌ای آن‌ها ماندگار باقی می‌مانند.

## تضمین پیکربندی یکنواخت

همان‌طور که در بخش‌های [تسهیل انتخاب رهبر](#facilitating-leader-election) و
[دستیابی به اجماع](#achieving-consensus) اشاره شد، سرورهای یک مجموعهٔ
ZooKeeper برای انتخاب رهبر و تشکیل حد نصاب به پیکربندی یکنواخت نیاز دارند.
همچنین برای اینکه پروتکل Zab به‌درستی روی شبکه کار کند، پیکربندی این پروتکل نیز
باید یکنواخت باشد. در مثال ما، پیکربندی یکنواخت با جاسازی مستقیم پیکربندی در
مانیفست به دست می‌آید.

StatefulSet با نام `zk` را دریافت کنید.

```shell
kubectl get sts zk -o yaml
```

```
…
command:
      - sh
      - -c
      - "start-zookeeper \
        --servers=3 \
        --data_dir=/var/lib/zookeeper/data \
        --data_log_dir=/var/lib/zookeeper/data/log \
        --conf_dir=/opt/zookeeper/conf \
        --client_port=2181 \
        --election_port=3888 \
        --server_port=2888 \
        --tick_time=2000 \
        --init_limit=10 \
        --sync_limit=5 \
        --heap=512M \
        --max_client_cnxns=60 \
        --snap_retain_count=3 \
        --purge_interval=12 \
        --max_session_timeout=40000 \
        --min_session_timeout=4000 \
        --log_level=INFO"
…
```

دستوری که برای راه‌اندازی سرورهای ZooKeeper استفاده شد، پیکربندی را به‌صورت پارامتر خط فرمان ارسال کرد. همچنین می‌توانید برای ارسال پیکربندی به مجموعه از متغیرهای محیطی استفاده کنید.

### پیکربندی لاگ‌گیری

یکی از فایل‌هایی که اسکریپت `zkGenConfig.sh` تولید می‌کند، لاگ‌گیری ZooKeeper را کنترل می‌کند. ZooKeeper از [Log4j](https://logging.apache.org/log4j/2.x/) استفاده می‌کند و به‌طور پیش‌فرض، در پیکربندی لاگ‌گیری خود یک ضمیمه‌گر فایل چرخشی (rolling file appender) مبتنی بر زمان و اندازه را به کار می‌برد.

با دستور زیر، پیکربندی لاگ‌گیری را از یکی از Podهای `StatefulSet` با نام `zk` دریافت کنید.

```shell
kubectl exec zk-0 cat /usr/etc/zookeeper/log4j.properties
```

پیکربندی لاگ‌گیری زیر باعث می‌شود فرایند ZooKeeper همهٔ لاگ‌های خود را در جریان فایل خروجی استاندارد بنویسد.

```
zookeeper.root.logger=CONSOLE
zookeeper.console.threshold=INFO
log4j.rootLogger=${zookeeper.root.logger}
log4j.appender.CONSOLE=org.apache.log4j.ConsoleAppender
log4j.appender.CONSOLE.Threshold=${zookeeper.console.threshold}
log4j.appender.CONSOLE.layout=org.apache.log4j.PatternLayout
log4j.appender.CONSOLE.layout.ConversionPattern=%d{ISO8601} [myid:%X{myid}] - %-5p [%t:%C{1}@%L] - %m%n
```

این ساده‌ترین روش ممکن برای لاگ‌گیری امن درون کانتینر است. از آنجا که برنامه‌ها لاگ‌ها را در خروجی استاندارد می‌نویسند، کوبرنتیز چرخش لاگ‌ها را برای شما انجام می‌دهد. کوبرنتیز همچنین یک سیاست نگهداری معقول پیاده‌سازی می‌کند که تضمین می‌کند لاگ‌های برنامه که در خروجی استاندارد و خطای استاندارد نوشته می‌شوند، رسانه‌های ذخیره‌سازی محلی را پر نکنند.

با دستور [`kubectl logs`](/docs/reference/generated/kubectl/kubectl-commands/#logs) بیست خط آخر لاگ را از یکی از Podها دریافت کنید.

```shell
kubectl logs zk-0 --tail 20
```

لاگ‌های برنامه را که در خروجی استاندارد یا خطای استاندارد نوشته شده‌اند، می‌توانید با `kubectl logs` و همچنین از طریق داشبورد کوبرنتیز مشاهده کنید.

```
2016-12-06 19:34:16,236 [myid:1] - INFO  [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@827] - Processing ruok command from /127.0.0.1:52740
2016-12-06 19:34:16,237 [myid:1] - INFO  [Thread-1136:NIOServerCnxn@1008] - Closed socket connection for client /127.0.0.1:52740 (no session established for client)
2016-12-06 19:34:26,155 [myid:1] - INFO  [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxnFactory@192] - Accepted socket connection from /127.0.0.1:52749
2016-12-06 19:34:26,155 [myid:1] - INFO  [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@827] - Processing ruok command from /127.0.0.1:52749
2016-12-06 19:34:26,156 [myid:1] - INFO  [Thread-1137:NIOServerCnxn@1008] - Closed socket connection for client /127.0.0.1:52749 (no session established for client)
2016-12-06 19:34:26,222 [myid:1] - INFO  [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxnFactory@192] - Accepted socket connection from /127.0.0.1:52750
2016-12-06 19:34:26,222 [myid:1] - INFO  [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@827] - Processing ruok command from /127.0.0.1:52750
2016-12-06 19:34:26,226 [myid:1] - INFO  [Thread-1138:NIOServerCnxn@1008] - Closed socket connection for client /127.0.0.1:52750 (no session established for client)
2016-12-06 19:34:36,151 [myid:1] - INFO  [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxnFactory@192] - Accepted socket connection from /127.0.0.1:52760
2016-12-06 19:34:36,152 [myid:1] - INFO  [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@827] - Processing ruok command from /127.0.0.1:52760
2016-12-06 19:34:36,152 [myid:1] - INFO  [Thread-1139:NIOServerCnxn@1008] - Closed socket connection for client /127.0.0.1:52760 (no session established for client)
2016-12-06 19:34:36,230 [myid:1] - INFO  [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxnFactory@192] - Accepted socket connection from /127.0.0.1:52761
2016-12-06 19:34:36,231 [myid:1] - INFO  [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@827] - Processing ruok command from /127.0.0.1:52761
2016-12-06 19:34:36,231 [myid:1] - INFO  [Thread-1140:NIOServerCnxn@1008] - Closed socket connection for client /127.0.0.1:52761 (no session established for client)
2016-12-06 19:34:46,149 [myid:1] - INFO  [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxnFactory@192] - Accepted socket connection from /127.0.0.1:52767
2016-12-06 19:34:46,149 [myid:1] - INFO  [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@827] - Processing ruok command from /127.0.0.1:52767
2016-12-06 19:34:46,149 [myid:1] - INFO  [Thread-1141:NIOServerCnxn@1008] - Closed socket connection for client /127.0.0.1:52767 (no session established for client)
2016-12-06 19:34:46,230 [myid:1] - INFO  [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxnFactory@192] - Accepted socket connection from /127.0.0.1:52768
2016-12-06 19:34:46,230 [myid:1] - INFO  [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2181:NIOServerCnxn@827] - Processing ruok command from /127.0.0.1:52768
2016-12-06 19:34:46,230 [myid:1] - INFO  [Thread-1142:NIOServerCnxn@1008] - Closed socket connection for client /127.0.0.1:52768 (no session established for client)
```

کوبرنتیز با راهکارهای لاگ‌گیری متعددی یکپارچه می‌شود. می‌توانید راهکاری را انتخاب کنید که با کلاستر و برنامه‌هایتان بهترین سازگاری را دارد. برای لاگ‌گیری و تجمیع لاگ‌ها در سطح کلاستر، استقرار یک [کانتینر کناری (sidecar)](/docs/concepts/cluster-administration/logging#sidecar-container-with-logging-agent) را برای چرخش و ارسال لاگ‌ها در نظر بگیرید.

### پیکربندی یک کاربر غیرممتاز

دربارهٔ بهترین شیوه‌ها برای اجازه دادن به اجرای یک برنامه با کاربر ممتاز درون کانتینر، دیدگاه‌های متفاوتی وجود دارد. اگر سازمان شما الزام می‌کند که برنامه‌ها با یک کاربر غیرممتاز اجرا شوند، می‌توانید با یک [SecurityContext](/docs/tasks/configure-pod-container/security-context/) کاربری را که نقطهٔ ورود با آن اجرا می‌شود، کنترل کنید.

قالب Pod (`template`) در `StatefulSet` با نام `zk` شامل یک `SecurityContext` است.

```yaml
securityContext:
  runAsUser: 1000
  fsGroup: 1000
```

در کانتینرهای Podها، شناسهٔ کاربری (UID) ۱۰۰۰ متناظر با کاربر zookeeper و شناسهٔ گروه (GID) ۱۰۰۰ متناظر با گروه zookeeper است.

اطلاعات فرایند ZooKeeper را از Pod با نام `zk-0` دریافت کنید.

```shell
kubectl exec zk-0 -- ps -elf
```

از آنجا که فیلد `runAsUser` در آبجکت `securityContext` روی ۱۰۰۰ تنظیم شده است، فرایند ZooKeeper به جای root با کاربر zookeeper اجرا می‌شود.

```
F S UID        PID  PPID  C PRI  NI ADDR SZ WCHAN  STIME TTY          TIME CMD
4 S zookeep+     1     0  0  80   0 -  1127 -      20:46 ?        00:00:00 sh -c zkGenConfig.sh && zkServer.sh start-foreground
0 S zookeep+    27     1  0  80   0 - 1155556 -    20:46 ?        00:00:19 /usr/lib/jvm/java-8-openjdk-amd64/bin/java -Dzookeeper.log.dir=/var/log/zookeeper -Dzookeeper.root.logger=INFO,CONSOLE -cp /usr/bin/../build/classes:/usr/bin/../build/lib/*.jar:/usr/bin/../share/zookeeper/zookeeper-3.4.9.jar:/usr/bin/../share/zookeeper/slf4j-log4j12-1.6.1.jar:/usr/bin/../share/zookeeper/slf4j-api-1.6.1.jar:/usr/bin/../share/zookeeper/netty-3.10.5.Final.jar:/usr/bin/../share/zookeeper/log4j-1.2.16.jar:/usr/bin/../share/zookeeper/jline-0.9.94.jar:/usr/bin/../src/java/lib/*.jar:/usr/bin/../etc/zookeeper: -Xmx2G -Xms2G -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.local.only=false org.apache.zookeeper.server.quorum.QuorumPeerMain /usr/bin/../etc/zookeeper/zoo.cfg
```

به‌طور پیش‌فرض، وقتی PersistentVolumeهای Pod در دایرکتوری داده‌های سرور ZooKeeper مانت می‌شوند، فقط کاربر root به آن‌ها دسترسی دارد. این پیکربندی مانع می‌شود که فرایند ZooKeeper در WAL خود بنویسد و اسنپ‌شات‌هایش را ذخیره کند.

با دستور زیر، مجوزهای فایل دایرکتوری داده‌های ZooKeeper را در Pod با نام `zk-0` دریافت کنید.

```shell
kubectl exec -ti zk-0 -- ls -ld /var/lib/zookeeper/data
```

از آنجا که فیلد `fsGroup` در آبجکت `securityContext` روی ۱۰۰۰ تنظیم شده است، مالکیت PersistentVolumeهای Podها به گروه zookeeper داده می‌شود و فرایند ZooKeeper می‌تواند داده‌های خود را بخواند و بنویسد.

```
drwxr-sr-x 3 zookeeper zookeeper 4096 Dec  5 20:45 /var/lib/zookeeper/data
```

## مدیریت فرایند ZooKeeper

در [مستندات ZooKeeper](https://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_supervision) آمده است: «بهتر است یک فرایند ناظر داشته باشید که هر یک از فرایندهای سرور ZooKeeper (JVM) شما را مدیریت کند.» استفاده از یک دیده‌بان (watchdog)، یعنی یک فرایند ناظر، برای راه‌اندازی مجدد فرایندهای ازکارافتاده در یک سیستم توزیع‌شده، الگویی رایج است. هنگام استقرار یک برنامه در کوبرنتیز، به جای استفاده از یک ابزار خارجی به‌عنوان فرایند ناظر، باید از خود کوبرنتیز به‌عنوان دیده‌بان برنامه‌تان استفاده کنید.

### به‌روزرسانی مجموعه (ensemble)

برای `StatefulSet` با نام `zk`، راهبرد به‌روزرسانی `RollingUpdate` پیکربندی شده است.

با `kubectl patch` می‌توانید تعداد `cpus` تخصیص‌یافته به سرورها را به‌روزرسانی کنید.

```shell
kubectl patch sts zk --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/resources/requests/cpu", "value":"0.3"}]'
```

```
statefulset.apps/zk patched
```

با `kubectl rollout status` وضعیت به‌روزرسانی را دنبال کنید.

```shell
kubectl rollout status sts/zk
```

```
waiting for statefulset rolling update to complete 0 pods at revision zk-5db4499664...
Waiting for 1 pods to be ready...
Waiting for 1 pods to be ready...
waiting for statefulset rolling update to complete 1 pods at revision zk-5db4499664...
Waiting for 1 pods to be ready...
Waiting for 1 pods to be ready...
waiting for statefulset rolling update to complete 2 pods at revision zk-5db4499664...
Waiting for 1 pods to be ready...
Waiting for 1 pods to be ready...
statefulset rolling update complete 3 pods at revision zk-5db4499664...
```

این کار Podها را یکی‌یکی و به ترتیب معکوس شمارهٔ ترتیبی خاتمه می‌دهد و آن‌ها را با پیکربندی جدید دوباره ایجاد می‌کند. به این ترتیب، حد نصاب (quorum) در طول به‌روزرسانی تدریجی حفظ می‌شود.

با دستور `kubectl rollout history` تاریخچه یا پیکربندی‌های قبلی را مشاهده کنید.

```shell
kubectl rollout history sts/zk
```

خروجی مشابه زیر است:

```
statefulsets "zk"
REVISION
1
2
```

با دستور `kubectl rollout undo` تغییر را بازگردانی کنید.

```shell
kubectl rollout undo sts/zk
```

خروجی مشابه زیر است:

```
statefulset.apps/zk rolled back
```

### مدیریت خرابی فرایند

[سیاست‌های راه‌اندازی مجدد](/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) تعیین می‌کنند که کوبرنتیز با خرابی فرایندِ نقطهٔ ورود کانتینر در یک Pod چگونه برخورد کند. برای Podهای یک `StatefulSet`، تنها مقدار مناسب برای `RestartPolicy` مقدار Always است که مقدار پیش‌فرض نیز هست. برای برنامه‌های دارای وضعیت (stateful) **هرگز** نباید سیاست پیش‌فرض را تغییر دهید.

با دستور زیر، درخت فرایندهای سرور ZooKeeper را که در Pod با نام `zk-0` اجرا می‌شود، بررسی کنید.

```shell
kubectl exec zk-0 -- ps -ef
```

دستوری که به‌عنوان نقطهٔ ورود کانتینر استفاده می‌شود، شناسهٔ فرایند (PID) ۱ را دارد و فرایند ZooKeeper، که فرزند نقطهٔ ورود است، شناسهٔ فرایند ۲۷ را دارد.

```
UID        PID  PPID  C STIME TTY          TIME CMD
zookeep+     1     0  0 15:03 ?        00:00:00 sh -c zkGenConfig.sh && zkServer.sh start-foreground
zookeep+    27     1  0 15:03 ?        00:00:03 /usr/lib/jvm/java-8-openjdk-amd64/bin/java -Dzookeeper.log.dir=/var/log/zookeeper -Dzookeeper.root.logger=INFO,CONSOLE -cp /usr/bin/../build/classes:/usr/bin/../build/lib/*.jar:/usr/bin/../share/zookeeper/zookeeper-3.4.9.jar:/usr/bin/../share/zookeeper/slf4j-log4j12-1.6.1.jar:/usr/bin/../share/zookeeper/slf4j-api-1.6.1.jar:/usr/bin/../share/zookeeper/netty-3.10.5.Final.jar:/usr/bin/../share/zookeeper/log4j-1.2.16.jar:/usr/bin/../share/zookeeper/jline-0.9.94.jar:/usr/bin/../src/java/lib/*.jar:/usr/bin/../etc/zookeeper: -Xmx2G -Xms2G -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.local.only=false org.apache.zookeeper.server.quorum.QuorumPeerMain /usr/bin/../etc/zookeeper/zoo.cfg
```

در یک ترمینال دیگر، با دستور زیر Podهای `StatefulSet` با نام `zk` را زیر نظر بگیرید.

```shell
kubectl get pod -w -l app=zk
```

در ترمینالی دیگر، با دستور زیر فرایند ZooKeeper را در Pod با نام `zk-0` خاتمه دهید.

```shell
kubectl exec zk-0 -- pkill java
```

خاتمهٔ فرایند ZooKeeper باعث خاتمهٔ فرایند والد آن شد. از آنجا که مقدار `RestartPolicy` کانتینر Always است، کانتینر فرایند والد را دوباره راه‌اندازی کرد.

```
NAME      READY     STATUS    RESTARTS   AGE
zk-0      1/1       Running   0          21m
zk-1      1/1       Running   0          20m
zk-2      1/1       Running   0          19m
NAME      READY     STATUS    RESTARTS   AGE
zk-0      0/1       Error     0          29m
zk-0      0/1       Running   1         29m
zk-0      1/1       Running   1         29m
```

اگر برنامهٔ شما برای اجرای فرایندی که منطق کسب‌وکار برنامه را پیاده‌سازی می‌کند از یک اسکریپت (مانند `zkServer.sh`) استفاده می‌کند، آن اسکریپت باید همراه با فرایند فرزند خاتمه یابد. به این ترتیب، هنگامی که فرایند پیاده‌سازی‌کنندهٔ منطق کسب‌وکار برنامه از کار بیفتد، کوبرنتیز کانتینر برنامه را دوباره راه‌اندازی خواهد کرد.

### آزمودن زنده بودن (liveness)

پیکربندی برنامه برای راه‌اندازی مجدد فرایندهای ازکارافتاده، برای سالم نگه داشتن یک سیستم توزیع‌شده کافی نیست. در برخی سناریوها، فرایندهای یک سیستم ممکن است زنده باشند اما پاسخ ندهند یا به شکل دیگری ناسالم باشند. باید از کاوشگرهای زنده بودن (liveness probe) استفاده کنید تا به کوبرنتیز اطلاع دهید که فرایندهای برنامه‌تان ناسالم هستند و باید آن‌ها را دوباره راه‌اندازی کند.

قالب Pod در `StatefulSet` با نام `zk` یک کاوشگر زنده بودن را مشخص می‌کند.

```yaml
  livenessProbe:
    exec:
      command:
      - sh
      - -c
      - "zookeeper-ready 2181"
    initialDelaySeconds: 15
    timeoutSeconds: 5
```

این کاوشگر یک اسکریپت bash را فراخوانی می‌کند که با استفاده از کلمهٔ چهارحرفی `ruok` در ZooKeeper، سلامت سرور را می‌آزماید.

```
OK=$(echo ruok | nc 127.0.0.1 $1)
if [ "$OK" == "imok" ]; then
    exit 0
else
    exit 1
fi
```

در یک پنجرهٔ ترمینال، با دستور زیر Podهای StatefulSet با نام `zk` را زیر نظر بگیرید.

```shell
kubectl get pod -w -l app=zk
```

در پنجره‌ای دیگر، با دستور زیر اسکریپت `zookeeper-ready` را از سیستم فایل Pod با نام `zk-0` حذف کنید.

```shell
kubectl exec zk-0 -- rm /opt/zookeeper/bin/zookeeper-ready
```

هنگامی که کاوشگر زنده بودن برای فرایند ZooKeeper ناموفق شود، کوبرنتیز به‌طور خودکار فرایند را برای شما دوباره راه‌اندازی می‌کند و به این ترتیب تضمین می‌شود که فرایندهای ناسالم در مجموعه دوباره راه‌اندازی شوند.

```shell
kubectl get pod -w -l app=zk
```

```
NAME      READY     STATUS    RESTARTS   AGE
zk-0      1/1       Running   0          1h
zk-1      1/1       Running   0          1h
zk-2      1/1       Running   0          1h
NAME      READY     STATUS    RESTARTS   AGE
zk-0      0/1       Running   0          1h
zk-0      0/1       Running   1         1h
zk-0      1/1       Running   1         1h
```

### آزمودن آمادگی (readiness)

آمادگی با زنده بودن یکسان نیست. اگر فرایندی زنده باشد، زمان‌بندی شده و سالم است. اگر فرایندی آماده باشد، می‌تواند ورودی را پردازش کند. زنده بودن شرط لازم برای آمادگی است، اما شرط کافی نیست. در مواردی، به‌ویژه هنگام راه‌اندازی اولیه و خاتمه، ممکن است فرایندی زنده باشد اما آماده نباشد.

اگر یک کاوشگر آمادگی (readiness probe) مشخص کنید، کوبرنتیز تضمین می‌کند که فرایندهای برنامهٔ شما تا زمانی که بررسی‌های آمادگی‌شان موفق نشده است، ترافیک شبکه دریافت نکنند.

برای یک سرور ZooKeeper، زنده بودن به معنای آمادگی است. بنابراین کاوشگر آمادگی در مانیفست `zookeeper.yaml` با کاوشگر زنده بودن یکسان است.

```yaml
  readinessProbe:
    exec:
      command:
      - sh
      - -c
      - "zookeeper-ready 2181"
    initialDelaySeconds: 15
    timeoutSeconds: 5
```

با اینکه کاوشگرهای زنده بودن و آمادگی یکسان هستند، مشخص کردن هر دو اهمیت دارد. این کار تضمین می‌کند که فقط سرورهای سالم در مجموعهٔ ZooKeeper ترافیک شبکه دریافت کنند.

## تحمل خرابی نود

ZooKeeper برای ثبت موفق تغییرات داده‌ها به حد نصابی از سرورها نیاز دارد. در یک مجموعهٔ سه‌سروری، برای موفقیت عملیات نوشتن باید دو سرور سالم باشند. در سیستم‌های مبتنی بر حد نصاب، اعضا در دامنه‌های خرابی (failure domain) مختلف مستقر می‌شوند تا دسترس‌پذیری تضمین شود. برای جلوگیری از قطعی در اثر از دست رفتن یک ماشین، بهترین شیوه‌ها قرار دادن چند نمونه از برنامه روی یک ماشین را مجاز نمی‌دانند.

کوبرنتیز به‌طور پیش‌فرض ممکن است Podهای یک `StatefulSet` را روی یک نود قرار دهد. در مجموعهٔ سه‌سروری‌ای که ایجاد کرده‌اید، اگر دو سرور روی یک نود باشند و آن نود از کار بیفتد، کلاینت‌های سرویس ZooKeeper شما تا زمانی که دست‌کم یکی از Podها دوباره زمان‌بندی شود، با قطعی مواجه خواهند شد.

همیشه باید ظرفیت اضافی فراهم کنید تا فرایندهای سیستم‌های حیاتی بتوانند در صورت خرابی نودها دوباره زمان‌بندی شوند. در این صورت، قطعی فقط تا زمانی ادامه می‌یابد که زمان‌بند کوبرنتیز یکی از سرورهای ZooKeeper را دوباره زمان‌بندی کند. اما اگر می‌خواهید سرویس شما خرابی نودها را بدون هیچ زمان ازکارافتادگی تحمل کند، باید `podAntiAffinity` را تنظیم کنید.

با دستور زیر، نودهای Podهای `StatefulSet` با نام `zk` را دریافت کنید.

```shell
for i in 0 1 2; do kubectl get pod zk-$i --template {{.spec.nodeName}}; echo ""; done
```

همهٔ Podهای `StatefulSet` با نام `zk` روی نودهای متفاوتی مستقر شده‌اند.

```
kubernetes-node-cxpk
kubernetes-node-a5aq
kubernetes-node-2g2d
```

دلیل این امر آن است که برای Podهای `StatefulSet` با نام `zk` یک `PodAntiAffinity` مشخص شده است.

```yaml
affinity:
  podAntiAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
            - key: "app"
              operator: In
              values:
                - zk
        topologyKey: "kubernetes.io/hostname"
```

فیلد `requiredDuringSchedulingIgnoredDuringExecution` به زمان‌بند کوبرنتیز می‌گوید که هرگز نباید دو Pod را که برچسب `app` آن‌ها برابر `zk` است، در دامنه‌ای که `topologyKey` تعریف می‌کند کنار هم قرار دهد. مقدار `kubernetes.io/hostname` برای `topologyKey` نشان می‌دهد که این دامنه یک نود منفرد است. با استفاده از قواعد، برچسب‌ها و انتخابگرهای (selector) متفاوت، می‌توانید این روش را گسترش دهید تا مجموعهٔ خود را در دامنه‌های خرابی فیزیکی، شبکه و برق پخش کنید.

## پایداری در زمان نگهداری

در این بخش، نودها را cordon و drain می‌کنید. اگر این آموزش را روی یک کلاستر مشترک اجرا می‌کنید، مطمئن شوید که این کار بر سایر کاربران کلاستر تأثیر منفی نمی‌گذارد.

در بخش قبل دیدید که چگونه Podها را میان نودها پخش کنید تا در برابر خرابی‌های برنامه‌ریزی‌نشدهٔ نودها پایدار بمانند. با این حال، باید برای از دسترس خارج شدن موقت نودها بر اثر نگهداری برنامه‌ریزی‌شده نیز آماده باشید.

با این دستور، فهرست نودهای کلاستر خود را دریافت کنید.

```shell
kubectl get nodes
```

این آموزش فرض می‌کند که کلاستر دست‌کم چهار نود دارد. اگر کلاستر بیش از چهار نود دارد، با [`kubectl cordon`](/docs/reference/generated/kubectl/kubectl-commands/#cordon) همهٔ نودها به‌جز چهار نود را cordon کنید. محدود کردن کلاستر به چهار نود تضمین می‌کند که کوبرنتیز هنگام زمان‌بندی Podهای zookeeper در شبیه‌سازی نگهداری که در ادامه می‌آید، با محدودیت‌های affinity و PodDisruptionBudget روبه‌رو شود.

```shell
kubectl cordon <node-name>
```

با این دستور، `PodDisruptionBudget` با نام `zk-pdb` را دریافت کنید.

```shell
kubectl get pdb zk-pdb
```

فیلد `max-unavailable` به کوبرنتیز اعلام می‌کند که در هر لحظه حداکثر یک Pod از `StatefulSet` با نام `zk` می‌تواند در دسترس نباشد.

```
NAME      MIN-AVAILABLE   MAX-UNAVAILABLE   ALLOWED-DISRUPTIONS   AGE
zk-pdb    N/A             1                 1
```

در یک ترمینال، با این دستور Podهای `StatefulSet` با نام `zk` را زیر نظر بگیرید.

```shell
kubectl get pods -w -l app=zk
```

در ترمینالی دیگر، با این دستور نودهایی را که Podها هم‌اکنون روی آن‌ها زمان‌بندی شده‌اند دریافت کنید.

```shell
for i in 0 1 2; do kubectl get pod zk-$i --template {{.spec.nodeName}}; echo ""; done
```

خروجی مشابه زیر است:

```
kubernetes-node-pb41
kubernetes-node-ixsl
kubernetes-node-i4c4
```

با [`kubectl drain`](/docs/reference/generated/kubectl/kubectl-commands/#drain)، نودی را که Pod با نام `zk-0` روی آن زمان‌بندی شده است cordon و drain کنید.

```shell
kubectl drain $(kubectl get pod zk-0 --template {{.spec.nodeName}}) --ignore-daemonsets --force --delete-emptydir-data
```

خروجی مشابه زیر است:

```
node "kubernetes-node-pb41" cordoned

WARNING: Deleting pods not managed by ReplicationController, ReplicaSet, Job, or DaemonSet: fluentd-cloud-logging-kubernetes-node-pb41, kube-proxy-kubernetes-node-pb41; Ignoring DaemonSet-managed pods: node-problem-detector-v0.1-o5elz
pod "zk-0" deleted
node "kubernetes-node-pb41" drained
```

از آنجا که کلاستر شما چهار نود دارد، دستور `kubectl drain` با موفقیت اجرا می‌شود و `zk-0` روی نود دیگری دوباره زمان‌بندی می‌شود.

```
NAME      READY     STATUS    RESTARTS   AGE
zk-0      1/1       Running   2          1h
zk-1      1/1       Running   0          1h
zk-2      1/1       Running   0          1h
NAME      READY     STATUS        RESTARTS   AGE
zk-0      1/1       Terminating   2          2h
zk-0      0/1       Terminating   2         2h
zk-0      0/1       Terminating   2         2h
zk-0      0/1       Terminating   2         2h
zk-0      0/1       Pending   0         0s
zk-0      0/1       Pending   0         0s
zk-0      0/1       ContainerCreating   0         0s
zk-0      0/1       Running   0         51s
zk-0      1/1       Running   0         1m
```

همچنان Podهای `StatefulSet` را در ترمینال اول زیر نظر داشته باشید و نودی را که `zk-1` روی آن زمان‌بندی شده است drain کنید.

```shell
kubectl drain $(kubectl get pod zk-1 --template {{.spec.nodeName}}) --ignore-daemonsets --force --delete-emptydir-data
```

خروجی مشابه زیر است:

```
"kubernetes-node-ixsl" cordoned
WARNING: Deleting pods not managed by ReplicationController, ReplicaSet, Job, or DaemonSet: fluentd-cloud-logging-kubernetes-node-ixsl, kube-proxy-kubernetes-node-ixsl; Ignoring DaemonSet-managed pods: node-problem-detector-v0.1-voc74
pod "zk-1" deleted
node "kubernetes-node-ixsl" drained
```


Pod با نام `zk-1` قابل زمان‌بندی نیست، زیرا `StatefulSet` با نام `zk` یک قاعدهٔ `PodAntiAffinity` دارد که از قرار گرفتن Podها روی یک نود مشترک جلوگیری می‌کند. از آنجا که فقط دو نود قابل زمان‌بندی هستند، این Pod در وضعیت Pending باقی می‌ماند.

```shell
kubectl get pods -w -l app=zk
```

خروجی مشابه زیر است:

```
NAME      READY     STATUS    RESTARTS   AGE
zk-0      1/1       Running   2          1h
zk-1      1/1       Running   0          1h
zk-2      1/1       Running   0          1h
NAME      READY     STATUS        RESTARTS   AGE
zk-0      1/1       Terminating   2          2h
zk-0      0/1       Terminating   2         2h
zk-0      0/1       Terminating   2         2h
zk-0      0/1       Terminating   2         2h
zk-0      0/1       Pending   0         0s
zk-0      0/1       Pending   0         0s
zk-0      0/1       ContainerCreating   0         0s
zk-0      0/1       Running   0         51s
zk-0      1/1       Running   0         1m
zk-1      1/1       Terminating   0         2h
zk-1      0/1       Terminating   0         2h
zk-1      0/1       Terminating   0         2h
zk-1      0/1       Terminating   0         2h
zk-1      0/1       Pending   0         0s
zk-1      0/1       Pending   0         0s
```

به زیر نظر گرفتن Podهای StatefulSet ادامه دهید و نودی را که `zk-2` روی آن زمان‌بندی شده است drain کنید.

```shell
kubectl drain $(kubectl get pod zk-2 --template {{.spec.nodeName}}) --ignore-daemonsets --force --delete-emptydir-data
```

خروجی مشابه زیر است:

```
node "kubernetes-node-i4c4" cordoned

WARNING: Deleting pods not managed by ReplicationController, ReplicaSet, Job, or DaemonSet: fluentd-cloud-logging-kubernetes-node-i4c4, kube-proxy-kubernetes-node-i4c4; Ignoring DaemonSet-managed pods: node-problem-detector-v0.1-dyrog
WARNING: Ignoring DaemonSet-managed pods: node-problem-detector-v0.1-dyrog; Deleting pods not managed by ReplicationController, ReplicaSet, Job, or DaemonSet: fluentd-cloud-logging-kubernetes-node-i4c4, kube-proxy-kubernetes-node-i4c4
There are pending pods when an error occurred: Cannot evict pod as it would violate the pod's disruption budget.
pod/zk-2
```

با فشردن `CTRL-C` اجرای kubectl را متوقف کنید.

نمی‌توانید نود سوم را drain کنید، زیرا بیرون راندن (evict) `zk-2` بودجهٔ `zk-budget` را نقض می‌کند. با این حال، این نود همچنان در حالت cordon باقی می‌ماند.

با `zkCli.sh` مقداری را که در آزمون سلامت وارد کرده بودید از `zk-0` بازیابی کنید.

```shell
kubectl exec zk-0 zkCli.sh get /hello
```

این سرویس همچنان در دسترس است، زیرا `PodDisruptionBudget` آن رعایت می‌شود.

```
WatchedEvent state:SyncConnected type:None path:null
world
cZxid = 0x200000002
ctime = Wed Dec 07 00:08:59 UTC 2016
mZxid = 0x200000002
mtime = Wed Dec 07 00:08:59 UTC 2016
pZxid = 0x200000002
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 5
numChildren = 0
```

با [`kubectl uncordon`](/docs/reference/generated/kubectl/kubectl-commands/#uncordon)، نود اول را از حالت cordon خارج کنید.

```shell
kubectl uncordon kubernetes-node-pb41
```

خروجی مشابه زیر است:

```
node "kubernetes-node-pb41" uncordoned
```

پاد `zk-1` روی این نود دوباره زمان‌بندی می‌شود. صبر کنید تا `zk-1` در وضعیت Running و Ready قرار گیرد.

```shell
kubectl get pods -w -l app=zk
```

خروجی مشابه زیر است:

```
NAME      READY     STATUS    RESTARTS   AGE
zk-0      1/1       Running   2          1h
zk-1      1/1       Running   0          1h
zk-2      1/1       Running   0          1h
NAME      READY     STATUS        RESTARTS   AGE
zk-0      1/1       Terminating   2          2h
zk-0      0/1       Terminating   2         2h
zk-0      0/1       Terminating   2         2h
zk-0      0/1       Terminating   2         2h
zk-0      0/1       Pending   0         0s
zk-0      0/1       Pending   0         0s
zk-0      0/1       ContainerCreating   0         0s
zk-0      0/1       Running   0         51s
zk-0      1/1       Running   0         1m
zk-1      1/1       Terminating   0         2h
zk-1      0/1       Terminating   0         2h
zk-1      0/1       Terminating   0         2h
zk-1      0/1       Terminating   0         2h
zk-1      0/1       Pending   0         0s
zk-1      0/1       Pending   0         0s
zk-1      0/1       Pending   0         12m
zk-1      0/1       ContainerCreating   0         12m
zk-1      0/1       Running   0         13m
zk-1      1/1       Running   0         13m
```

تلاش کنید نودی را که `zk-2` روی آن زمان‌بندی شده است drain کنید.

```shell
kubectl drain $(kubectl get pod zk-2 --template {{.spec.nodeName}}) --ignore-daemonsets --force --delete-emptydir-data
```

خروجی مشابه زیر است:

```
node "kubernetes-node-i4c4" already cordoned
WARNING: Deleting pods not managed by ReplicationController, ReplicaSet, Job, or DaemonSet: fluentd-cloud-logging-kubernetes-node-i4c4, kube-proxy-kubernetes-node-i4c4; Ignoring DaemonSet-managed pods: node-problem-detector-v0.1-dyrog
pod "heapster-v1.2.0-2604621511-wht1r" deleted
pod "zk-2" deleted
node "kubernetes-node-i4c4" drained
```

این بار دستور `kubectl drain` با موفقیت اجرا می‌شود.

نود دوم را از حالت cordon خارج کنید تا `zk-2` بتواند دوباره زمان‌بندی شود.

```shell
kubectl uncordon kubernetes-node-ixsl
```

خروجی مشابه زیر است:

```
node "kubernetes-node-ixsl" uncordoned
```

می‌توانید `kubectl drain` را همراه با `PodDisruptionBudgets` به کار ببرید تا مطمئن شوید سرویس‌هایتان در زمان نگهداری در دسترس باقی می‌مانند. اگر پیش از خارج کردن نود از مدار برای نگهداری، از drain برای cordon کردن نودها و بیرون راندن Podها استفاده شود، بودجهٔ اختلال سرویس‌هایی که چنین بودجه‌ای تعریف کرده‌اند رعایت خواهد شد. همیشه باید ظرفیت اضافی برای سرویس‌های حیاتی در نظر بگیرید تا Podهای آن‌ها بتوانند بی‌درنگ دوباره زمان‌بندی شوند.

## {{% heading "cleanup" %}}

- با `kubectl uncordon` همهٔ نودهای کلاستر خود را از حالت cordon خارج کنید.
- باید رسانه‌های ذخیره‌سازی پایدار مربوط به PersistentVolumeهایی را که در این آموزش استفاده شده‌اند حذف کنید. برای اطمینان از بازپس‌گیری کامل همهٔ فضای ذخیره‌سازی، گام‌های لازم را متناسب با محیط، پیکربندی ذخیره‌سازی و روش تأمین (provisioning) خود دنبال کنید.
