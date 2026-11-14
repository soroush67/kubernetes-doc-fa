---
reviewers:
- verb
- soltysh
title: اشکال‌زدایی Podهای در حال اجرا
content_type: task
---

<!-- overview -->

این صفحه توضیح می‌دهد که چگونه Podهایی را که روی یک نود در حال اجرا هستند (یا از کار می‌افتند) اشکال‌زدایی کنید.


## {{% heading "prerequisites" %}}


* {{< glossary_tooltip text="Pod" term_id="pod" >}} شما باید از قبل زمان‌بندی شده و در حال اجرا باشد. اگر Pod شما هنوز اجرا نشده است، از [اشکال‌زدایی Podها](/docs/tasks/debug/debug-application/) شروع کنید.
* برای برخی از مراحل پیشرفته‌ی اشکال‌زدایی، باید بدانید Pod روی کدام نود اجرا می‌شود و برای اجرای دستورها روی آن نود به پوسته (shell) دسترسی داشته باشید. برای اجرای مراحل استاندارد اشکال‌زدایی که از `kubectl` استفاده می‌کنند، به چنین دسترسی‌ای نیازی ندارید.

## استفاده از `kubectl describe pod` برای دریافت جزئیات Podها

در این مثال، مانند مثال قبلی، با یک Deployment دو Pod ایجاد می‌کنیم.

{{% code_sample file="application/nginx-with-request.yaml" %}}

با اجرای دستور زیر، Deployment را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/nginx-with-request.yaml
```

```none
deployment.apps/nginx-deployment created
```

با دستور زیر وضعیت Podها را بررسی کنید:

```shell
kubectl get pods
```

```none
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-67d4bdd6f5-cx2nz   1/1     Running   0          13s
nginx-deployment-67d4bdd6f5-w6kd7   1/1     Running   0          13s
```

با `kubectl describe pod` می‌توانیم اطلاعات بسیار بیشتری درباره‌ی هر یک از این Podها به دست آوریم. برای مثال:

```shell
kubectl describe pod nginx-deployment-67d4bdd6f5-w6kd7
```

```none
Name:         nginx-deployment-67d4bdd6f5-w6kd7
Namespace:    default
Priority:     0
Node:         kube-worker-1/192.168.0.113
Start Time:   Thu, 17 Feb 2022 16:51:01 -0500
Labels:       app=nginx
              pod-template-hash=67d4bdd6f5
Annotations:  <none>
Status:       Running
IP:           10.88.0.3
IPs:
  IP:           10.88.0.3
  IP:           2001:db8::1
Controlled By:  ReplicaSet/nginx-deployment-67d4bdd6f5
Containers:
  nginx:
    Container ID:   containerd://5403af59a2b46ee5a23fb0ae4b1e077f7ca5c5fb7af16e1ab21c00e0e616462a
    Image:          nginx
    Image ID:       docker.io/library/nginx@sha256:2834dc507516af02784808c5f48b7cbe38b8ed5d0f4837f16e78d00deb7e7767
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Thu, 17 Feb 2022 16:51:05 -0500
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     500m
      memory:  128Mi
    Requests:
      cpu:        500m
      memory:     128Mi
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-bgsgp (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-bgsgp:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Guaranteed
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  34s   default-scheduler  Successfully assigned default/nginx-deployment-67d4bdd6f5-w6kd7 to kube-worker-1
  Normal  Pulling    31s   kubelet            Pulling image "nginx"
  Normal  Pulled     30s   kubelet            Successfully pulled image "nginx" in 1.146417389s
  Normal  Created    30s   kubelet            Created container nginx
  Normal  Started    30s   kubelet            Started container nginx
```

در این خروجی، هم اطلاعات پیکربندی کانتینر(ها) و Pod (برچسب‌ها، نیازمندی‌های منابع و غیره) و هم اطلاعات وضعیت کانتینر(ها) و Pod (حالت، آمادگی، تعداد راه‌اندازی مجدد، رویدادها و غیره) را می‌بینید.

حالت کانتینر یکی از مقادیر Waiting، Running یا Terminated است. بسته به این حالت، اطلاعات بیشتری نیز ارائه می‌شود؛ برای نمونه، در اینجا می‌بینید که برای کانتینری در حالت Running، سیستم زمان شروع به کار کانتینر را نشان می‌دهد.

فیلد Ready نشان می‌دهد که آیا کانتینر آخرین بررسی آمادگی (readiness probe) خود را با موفقیت گذرانده است یا نه. (در این مثال، هیچ بررسی آمادگی‌ای برای کانتینر پیکربندی نشده است؛ در چنین حالتی، کانتینر آماده فرض می‌شود.)

فیلد Restart Count نشان می‌دهد که کانتینر چند بار راه‌اندازی مجدد شده است. این اطلاعات برای تشخیص حلقه‌های از کار افتادن (crash loop) در کانتینرهایی که سیاست راه‌اندازی مجدد آن‌ها `Always` است، مفید است.

در حال حاضر تنها شرطی (Condition) که به یک Pod مربوط است، شرط دودویی Ready است. این شرط نشان می‌دهد که Pod می‌تواند به درخواست‌ها پاسخ دهد و باید به مخزن‌های توزیع بار همه‌ی Serviceهای منطبق اضافه شود.

در پایان، گزارشی از رویدادهای اخیر مربوط به Pod خود را می‌بینید. ستون «From» مؤلفه‌ای را نشان می‌دهد که رویداد را ثبت کرده است و ستون‌های «Reason» و «Message» توضیح می‌دهند که چه اتفاقی افتاده است.


## مثال: اشکال‌زدایی Podهای در وضعیت Pending

یکی از موقعیت‌های رایجی که با کمک رویدادها می‌توان تشخیص داد، زمانی است که Podی ایجاد کرده‌اید که روی هیچ نودی جا نمی‌شود. برای مثال، ممکن است Pod بیش از منابع آزاد هر نود درخواست کند، یا انتخابگر برچسبی (label selector) تعیین کرده باشد که با هیچ نودی منطبق نیست. فرض کنید Deployment قبلی را با ۵ رپلیکا (به جای ۲) و با درخواست ۶۰۰ میلی‌هسته به جای ۵۰۰ ایجاد کرده‌ایم، آن هم روی کلاستری چهارنودی که هر ماشین (مجازی) آن ۱ CPU دارد. در این حالت، یکی از Podها زمان‌بندی نخواهد شد. (توجه کنید که به دلیل Podهای افزونه‌ی کلاستر مانند fluentd، skydns و غیره که روی هر نود اجرا می‌شوند، اگر ۱۰۰۰ میلی‌هسته درخواست می‌کردیم، هیچ‌یک از Podها زمان‌بندی نمی‌شد.)

```shell
kubectl get pods
```

```none
NAME                                READY     STATUS    RESTARTS   AGE
nginx-deployment-1006230814-6winp   1/1       Running   0          7m
nginx-deployment-1006230814-fmgu3   1/1       Running   0          7m
nginx-deployment-1370807587-6ekbw   1/1       Running   0          1m
nginx-deployment-1370807587-fg172   0/1       Pending   0          1m
nginx-deployment-1370807587-fz9sd   0/1       Pending   0          1m
```

برای اینکه بفهمیم چرا Pod با نام nginx-deployment-1370807587-fz9sd اجرا نمی‌شود، می‌توانیم `kubectl describe pod` را روی این Pod در حالت Pending اجرا کنیم و رویدادهای آن را بررسی کنیم:

```shell
kubectl describe pod nginx-deployment-1370807587-fz9sd
```

```none
  Name:		nginx-deployment-1370807587-fz9sd
  Namespace:	default
  Node:		/
  Labels:		app=nginx,pod-template-hash=1370807587
  Status:		Pending
  IP:
  Controllers:	ReplicaSet/nginx-deployment-1370807587
  Containers:
    nginx:
      Image:	nginx
      Port:	80/TCP
      QoS Tier:
        memory:	Guaranteed
        cpu:	Guaranteed
      Limits:
        cpu:	1
        memory:	128Mi
      Requests:
        cpu:	1
        memory:	128Mi
      Environment Variables:
  Volumes:
    default-token-4bcbi:
      Type:	Secret (a volume populated by a Secret)
      SecretName:	default-token-4bcbi
  Events:
    FirstSeen	LastSeen	Count	From			        SubobjectPath	Type		Reason			    Message
    ---------	--------	-----	----			        -------------	--------	------			    -------
    1m		    48s		    7	    {default-scheduler }			        Warning		FailedScheduling	pod (nginx-deployment-1370807587-fz9sd) failed to fit in any node
  fit failure on node (kubernetes-node-6ta5): Node didn't have enough resource: CPU, requested: 1000, used: 1420, capacity: 2000
  fit failure on node (kubernetes-node-wul5): Node didn't have enough resource: CPU, requested: 1000, used: 1100, capacity: 2000
```

در اینجا رویدادی را می‌بینید که زمان‌بند ایجاد کرده است و نشان می‌دهد زمان‌بندی Pod به دلیل `FailedScheduling` (و احتمالاً دلایل دیگر) ناموفق بوده است. پیام این رویداد می‌گوید که روی هیچ‌یک از نودها منابع کافی برای Pod وجود نداشته است.

برای رفع این وضعیت، می‌توانید با `kubectl scale` تعداد رپلیکاهای Deployment خود را به چهار یا کمتر تغییر دهید. (همچنین می‌توانید آن یک Pod را در حالت Pending رها کنید؛ این کار ضرری ندارد.)

رویدادهایی مانند آنچه در انتهای خروجی `kubectl describe pod` دیدید، در etcd ذخیره می‌شوند و اطلاعاتی کلی درباره‌ی آنچه در کلاستر رخ می‌دهد ارائه می‌کنند. برای فهرست کردن همه‌ی رویدادها می‌توانید از دستور زیر استفاده کنید:

```shell
kubectl get events
```

اما به خاطر داشته باشید که رویدادها به فضای نام (namespace) وابسته‌اند. یعنی اگر به رویدادهای یک آبجکت وابسته به فضای نام علاقه دارید (برای مثال، اینکه چه اتفاقی برای Podهای فضای نام `my-namespace` افتاده است)، باید فضای نام را صراحتاً به دستور بدهید:

```shell
kubectl get events --namespace=my-namespace
```

برای دیدن رویدادهای همه‌ی فضاهای نام، می‌توانید از آرگومان `--all-namespaces` استفاده کنید.

علاوه بر `kubectl describe pod`، راه دیگری برای به دست آوردن اطلاعات بیشتر درباره‌ی یک Pod (فراتر از آنچه `kubectl get pod` ارائه می‌کند) این است که فلگ قالب خروجی `-o yaml` را به `kubectl get pod` بدهید. این کار اطلاعاتی حتی بیشتر از `kubectl describe pod` را در قالب YAML در اختیارتان می‌گذارد؛ در واقع تقریباً همه‌ی اطلاعاتی که سیستم درباره‌ی Pod دارد. در این خروجی مواردی مانند حاشیه‌نویسی‌ها (annotation) را می‌بینید، که فراداده‌هایی کلید-مقدار بدون محدودیت‌های برچسب هستند و مؤلفه‌های سیستمی کوبرنتیز به‌طور داخلی از آن‌ها استفاده می‌کنند. همچنین سیاست راه‌اندازی مجدد، پورت‌ها و حجم‌ها (volume) را نیز می‌بینید.

```shell
kubectl get pod nginx-deployment-1006230814-6winp -o yaml
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: "2022-02-17T21:51:01Z"
  generateName: nginx-deployment-67d4bdd6f5-
  labels:
    app: nginx
    pod-template-hash: 67d4bdd6f5
  name: nginx-deployment-67d4bdd6f5-w6kd7
  namespace: default
  ownerReferences:
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true
    kind: ReplicaSet
    name: nginx-deployment-67d4bdd6f5
    uid: 7d41dfd4-84c0-4be4-88ab-cedbe626ad82
  resourceVersion: "1364"
  uid: a6501da1-0447-4262-98eb-c03d4002222e
spec:
  containers:
  - image: nginx
    imagePullPolicy: Always
    name: nginx
    ports:
    - containerPort: 80
      protocol: TCP
    resources:
      limits:
        cpu: 500m
        memory: 128Mi
      requests:
        cpu: 500m
        memory: 128Mi
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-bgsgp
      readOnly: true
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  nodeName: kube-worker-1
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  restartPolicy: Always
  schedulerName: default-scheduler
  securityContext: {}
  serviceAccount: default
  serviceAccountName: default
  terminationGracePeriodSeconds: 30
  tolerations:
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  volumes:
  - name: kube-api-access-bgsgp
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          expirationSeconds: 3607
          path: token
      - configMap:
          items:
          - key: ca.crt
            path: ca.crt
          name: kube-root-ca.crt
      - downwardAPI:
          items:
          - fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
            path: namespace
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2022-02-17T21:51:01Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2022-02-17T21:51:06Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2022-02-17T21:51:06Z"
    status: "True"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2022-02-17T21:51:01Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: containerd://5403af59a2b46ee5a23fb0ae4b1e077f7ca5c5fb7af16e1ab21c00e0e616462a
    image: docker.io/library/nginx:latest
    imageID: docker.io/library/nginx@sha256:2834dc507516af02784808c5f48b7cbe38b8ed5d0f4837f16e78d00deb7e7767
    lastState: {}
    name: nginx
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2022-02-17T21:51:05Z"
  hostIP: 192.168.0.113
  phase: Running
  podIP: 10.88.0.3
  podIPs:
  - ip: 10.88.0.3
  - ip: 2001:db8::1
  qosClass: Guaranteed
  startTime: "2022-02-17T21:51:01Z"
```

## بررسی لاگ‌های Pod {#examine-pod-logs}

ابتدا لاگ‌های کانتینر مورد نظر را بررسی کنید:

```shell
kubectl logs ${POD_NAME} -c ${CONTAINER_NAME}
```

اگر کانتینر شما پیش‌تر از کار افتاده است، می‌توانید با دستور زیر به لاگ از کار افتادن کانتینر قبلی دسترسی پیدا کنید:

```shell
kubectl logs ${POD_NAME} -c ${CONTAINER_NAME} --previous
```

## اشکال‌زدایی با اجرای دستور در کانتینر {#container-exec}

اگر {{< glossary_tooltip text="ایمیج کانتینر" term_id="image" >}} ابزارهای اشکال‌زدایی را در خود داشته باشد، که در ایمیج‌های ساخته‌شده بر پایه‌ی ایمیج‌های پایه‌ی سیستم‌عامل‌های لینوکس و ویندوز چنین است، می‌توانید با `kubectl exec` دستورهایی را درون یک کانتینر مشخص اجرا کنید:

```shell
kubectl exec ${POD_NAME} -c ${CONTAINER_NAME} -- ${CMD} ${ARG1} ${ARG2} ... ${ARGN}
```

{{< note >}}
بخش `-c ${CONTAINER_NAME}` اختیاری است. برای Podهایی که فقط یک کانتینر دارند، می‌توانید آن را حذف کنید.
{{< /note >}}

برای نمونه، برای دیدن لاگ‌های یک Pod در حال اجرای Cassandra، می‌توانید دستور زیر را اجرا کنید:

```shell
kubectl exec cassandra -- cat /var/log/cassandra/system.log
```

با آرگومان‌های `-i` و `-t` در `kubectl exec` می‌توانید پوسته‌ای را اجرا کنید که به ترمینال شما متصل است؛ برای مثال:

```shell
kubectl exec -it cassandra -- sh
```

برای جزئیات بیشتر، [دسترسی به پوسته‌ی یک کانتینر در حال اجرا](
/docs/tasks/debug/debug-application/get-shell-running-container/) را ببینید.

## اشکال‌زدایی با یک کانتینر اشکال‌زدایی موقت {#ephemeral-container}

{{< feature-state state="stable" for_k8s_version="v1.25" >}}

{{< glossary_tooltip text="کانتینرهای موقت" term_id="ephemeral-container" >}}
برای عیب‌یابی تعاملی مفیدند، آن هم در شرایطی که `kubectl exec` کافی نیست؛ مثلاً وقتی کانتینری از کار افتاده است یا ایمیج کانتینر ابزارهای اشکال‌زدایی ندارد، مانند [ایمیج‌های distroless](
https://github.com/GoogleContainerTools/distroless).

### مجوزهای لازم برای کانتینرهای موقت {#ephemeral-container-permissions}

به دلایل امنیتی، افزودن یک کانتینر موقت به Pod در حال اجرا از زیرمنبع (subresource) `ephemeralcontainers` آن Pod استفاده می‌کند. در سطح API، این کار یک درخواست **update** روی `pods/ephemeralcontainers` است. داشتن مجوز **patch** روی یک Pod به‌تنهایی به کاربران اجازه نمی‌دهد کانتینرهای موقت را به آن Pod اضافه کنند.

زیرمنبع `pods/ephemeralcontainers` عمداً جزو
[ClusterRoleهای کاربرمحور](/docs/reference/access-authn-authz/rbac/#user-facing-roles)
پیش‌فرض `admin` و `edit` نیست. برای آشنایی با دلیل این تصمیم،
[کانتینرهای موقت: کنترل دسترسی](/docs/concepts/workloads/pods/ephemeral-containers/#access-control)
را ببینید.

اگر بدون داشتن مجوز لازم، `kubectl debug` را برای افزودن یک کانتینر موقت اجرا کنید، خطایی مشابه زیر می‌بینید:

```
Error from server (Forbidden): pods "example" is forbidden: User "alice" cannot
patch resource "pods/ephemeralcontainers" in API group "" in the namespace "example-ns"
```

اگر مدیریت دسترسی به کلاستر با شماست و کلاستر شما از [RBAC کوبرنتیز](/docs/reference/access-authn-authz/rbac/) استفاده می‌کند، می‌توانید این مجوز را به یکی از دو روش زیر اعطا کنید.

برای گسترش ClusterRoleهای داخلی `edit` و `admin` در کل کلاستر، یک ClusterRole تجمیعی ایجاد کنید که برچسب لازم برای
[تجمیع ClusterRole](/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles)
را داشته باشد. برچسب `aggregate-to-edit` کافی است، زیرا خود ClusterRole پیش‌فرض `edit` در `admin` تجمیع می‌شود:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: aggregate-ephemeralcontainers-edit
  labels:
    rbac.authorization.k8s.io/aggregate-to-edit: "true"
rules:
- apiGroups: [""]
  resources: ["pods/ephemeralcontainers"]
  verbs: ["patch", "update"]
```

برای اعطای این مجوز فقط به کاربران یا گروه‌های مشخص (برای مثال، یک گروه اختصاصی اشکال‌زدایی یا SRE)، یک ClusterRole محدودتر ایجاد کنید و آن را مستقیماً به آن‌ها متصل (bind) کنید:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: debug-ephemeralcontainers
rules:
- apiGroups: [""]
  resources: ["pods/ephemeralcontainers"]
  verbs: ["patch", "update"]
```

{{< note >}}
[پذیرش امنیت Pod](/docs/concepts/security/pod-security-admission/) کانتینرهای موقت را نیز بر اساس همان [استانداردهای امنیت Pod](/docs/concepts/security/pod-security-standards/) ارزیابی می‌کند که برای کانتینرهای عادی به کار می‌رود. هنگام اعطای مجوز افزودن کانتینرهای موقت به Podهایی که تحت سیاست `baseline` یا `restricted` هستند، یک [پروفایل اشکال‌زدایی](#debugging-profiles) متناسب، مانند `--profile=baseline` یا `--profile=restricted`، را همراه با `kubectl debug` انتخاب کنید.

همچنین ممکن است لازم باشد هر وب‌هوک پذیرش (admission webhook) یا سیاست پذیرشی در کلاستر شما که فیلد `ephemeralContainers` را ارزیابی نمی‌کند، به‌روزرسانی شود تا منبع `pods/ephemeralcontainers` را رهگیری کند و فیلد `ephemeralContainers` را در مشخصات (spec) Pod ارزیابی کند.
{{< /note >}}

### مثالی از اشکال‌زدایی با کانتینرهای موقت {#ephemeral-container-example}

با دستور `kubectl debug` می‌توانید کانتینرهای موقت را به یک Pod در حال اجرا اضافه کنید. ابتدا یک Pod برای این مثال ایجاد کنید:

```shell
kubectl run ephemeral-demo --image=registry.k8s.io/pause:3.1 --restart=Never
```

مثال‌های این بخش از ایمیج کانتینر `pause` استفاده می‌کنند، زیرا این ایمیج ابزارهای اشکال‌زدایی ندارد؛ اما این روش با همه‌ی ایمیج‌های کانتینر کار می‌کند.

اگر بخواهید با `kubectl exec` یک پوسته ایجاد کنید، با خطا روبه‌رو می‌شوید، زیرا این ایمیج کانتینر هیچ پوسته‌ای ندارد.

```shell
kubectl exec -it ephemeral-demo -- sh
```

```
OCI runtime exec failed: exec failed: container_linux.go:346: starting container process caused "exec: \"sh\": executable file not found in $PATH": unknown
```

در عوض می‌توانید با `kubectl debug` یک کانتینر اشکال‌زدایی اضافه کنید. اگر آرگومان `-i`/`--interactive` را مشخص کنید، `kubectl` به‌طور خودکار به کنسول کانتینر موقت متصل می‌شود.

```shell
kubectl debug -it ephemeral-demo --image=busybox:1.28 --target=ephemeral-demo
```

```
Defaulting debug container name to debugger-8xzrl.
If you don't see a command prompt, try pressing enter.
/ #
```

این دستور یک کانتینر busybox جدید اضافه می‌کند و به آن متصل می‌شود. پارامتر `--target` فضای نام پردازه‌ی (process namespace) کانتینر دیگری را هدف می‌گیرد. این پارامتر در اینجا لازم است، زیرا `kubectl run` در Podی که ایجاد می‌کند [اشتراک فضای نام پردازه](
/docs/tasks/configure-pod-container/share-process-namespace/) را فعال نمی‌کند.

{{< note >}}
{{< glossary_tooltip
text="محیط اجرای کانتینر" term_id="container-runtime" >}} باید از پارامتر `--target` پشتیبانی کند. در غیر این صورت، ممکن است کانتینر موقت اجرا نشود، یا با یک فضای نام پردازه‌ی جداگانه اجرا شود، به‌طوری که دستور `ps` پردازه‌های کانتینرهای دیگر را نشان ندهد.
{{< /note >}}

با `kubectl describe` می‌توانید وضعیت کانتینر موقتی را که تازه ایجاد شده است ببینید:

```shell
kubectl describe pod ephemeral-demo
```

```
...
Ephemeral Containers:
  debugger-8xzrl:
    Container ID:   docker://b888f9adfd15bd5739fefaa39e1df4dd3c617b9902082b1cfdc29c4028ffb2eb
    Image:          busybox
    Image ID:       docker-pullable://busybox@sha256:1828edd60c5efd34b2bf5dd3282ec0cc04d47b2ff9caa0b6d4f07a21d1c08084
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Wed, 12 Feb 2020 14:25:42 +0100
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:         <none>
...
```

پس از پایان کار، با `kubectl delete` آن Pod را حذف کنید:

```shell
kubectl delete pod ephemeral-demo
```

## اشکال‌زدایی با استفاده از یک نسخه‌ی کپی از Pod

گاهی گزینه‌های پیکربندی Pod عیب‌یابی را در برخی شرایط دشوار می‌کنند. برای مثال، اگر ایمیج کانتینر شما پوسته نداشته باشد یا برنامه‌ی شما هنگام راه‌اندازی از کار بیفتد، نمی‌توانید برای عیب‌یابی کانتینر از `kubectl exec` استفاده کنید. در چنین شرایطی می‌توانید با `kubectl debug` یک نسخه‌ی کپی از Pod بسازید که مقادیر پیکربندی آن برای کمک به اشکال‌زدایی تغییر کرده‌اند.

### کپی‌کردن یک Pod همراه با افزودن یک کانتینر جدید

افزودن یک کانتینر جدید زمانی مفید است که برنامه‌تان در حال اجراست، اما رفتار مورد انتظار را ندارد و می‌خواهید ابزارهای عیب‌یابی بیشتری به Pod اضافه کنید.

برای مثال، ممکن است ایمیج‌های کانتینر برنامه‌تان بر پایهٔ `busybox` ساخته شده باشند، اما به ابزارهای اشکال‌زدایی‌ای نیاز داشته باشید که در `busybox` وجود ندارند. می‌توانید این سناریو را با `kubectl run` شبیه‌سازی کنید:

```shell
kubectl run myapp --image=busybox:1.28 --restart=Never -- sleep 1d
```

این دستور را اجرا کنید تا یک کپی از `myapp` با نام `myapp-debug` ساخته شود که یک کانتینر جدید Ubuntu برای اشکال‌زدایی به آن اضافه می‌کند:

```shell
kubectl debug myapp -it --image=ubuntu --share-processes --copy-to=myapp-debug
```

```
Defaulting debug container name to debugger-w7xmf.
If you don't see a command prompt, try pressing enter.
root@myapp-debug:/#
```

{{< note >}}
* اگر با فلگ `--container` نامی برای کانتینر انتخاب نکنید، دستور `kubectl debug` به‌طور خودکار نامی برای آن تولید می‌کند.
* فلگ `-i` باعث می‌شود دستور `kubectl debug` به‌طور پیش‌فرض به کانتینر جدید متصل شود. می‌توانید با تعیین `--attach=false` از این کار جلوگیری کنید. اگر اتصال نشست شما قطع شد، می‌توانید با `kubectl attach` دوباره به آن متصل شوید.
* گزینهٔ `--share-processes` به کانتینرهای این Pod امکان می‌دهد فرایندهای سایر کانتینرهای Pod را ببینند. برای اطلاعات بیشتر دربارهٔ نحوهٔ کار این قابلیت، به [اشتراک‌گذاری فضای نام فرایند (process namespace) بین کانتینرهای یک Pod](
  /docs/tasks/configure-pod-container/share-process-namespace/) مراجعه کنید.
{{< /note >}}

فراموش نکنید که پس از پایان کار، Pod اشکال‌زدایی را پاک کنید:

```shell
kubectl delete pod myapp myapp-debug
```

### کپی‌کردن یک Pod همراه با تغییر دستور آن

گاهی تغییر دستور یک کانتینر مفید است؛ برای مثال برای افزودن یک فلگ اشکال‌زدایی، یا به این دلیل که برنامه از کار می‌افتد.

برای شبیه‌سازی برنامه‌ای که از کار می‌افتد، با `kubectl run` کانتینری بسازید که بلافاصله خارج می‌شود:

```
kubectl run --image=busybox:1.28 myapp -- false
```

با اجرای `kubectl describe pod myapp` می‌توانید ببینید که این کانتینر مدام از کار می‌افتد:

```
Containers:
  myapp:
    Image:         busybox
    ...
    Args:
      false
    State:          Waiting
      Reason:       CrashLoopBackOff
    Last State:     Terminated
      Reason:       Error
      Exit Code:    1
```

می‌توانید با `kubectl debug` یک کپی از این Pod بسازید که دستور آن به یک پوستهٔ تعاملی (interactive shell) تغییر کرده باشد:

```
kubectl debug myapp -it --copy-to=myapp-debug --container=myapp -- sh
```

```
If you don't see a command prompt, try pressing enter.
/ #
```

اکنون یک پوستهٔ تعاملی در اختیار دارید که می‌توانید با آن کارهایی مانند بررسی مسیرهای فایل‌سیستم یا اجرای دستی دستور کانتینر را انجام دهید.

{{< note >}}
* برای تغییر دستور یک کانتینر مشخص، باید نام آن را با `--container` تعیین کنید؛ در غیر این صورت، دستور `kubectl debug` به‌جای آن یک کانتینر جدید برای اجرای دستوری که مشخص کرده‌اید می‌سازد.
* فلگ `-i` باعث می‌شود دستور `kubectl debug` به‌طور پیش‌فرض به کانتینر متصل شود. می‌توانید با تعیین `--attach=false` از این کار جلوگیری کنید. اگر اتصال نشست شما قطع شد، می‌توانید با `kubectl attach` دوباره به آن متصل شوید.
{{< /note >}}

فراموش نکنید که پس از پایان کار، Pod اشکال‌زدایی را پاک کنید:

```shell
kubectl delete pod myapp myapp-debug
```

### کپی‌کردن یک Pod همراه با تغییر ایمیج‌های کانتینر

در برخی موقعیت‌ها ممکن است بخواهید ایمیج‌های کانتینر معمول محیط عملیاتی یک Pod معیوب را با ایمیجی جایگزین کنید که نسخهٔ اشکال‌زدایی یا ابزارهای اضافی را در خود دارد.

به‌عنوان مثال، با `kubectl run` یک Pod بسازید:

```
kubectl run myapp --image=busybox:1.28 --restart=Never -- sleep 1d
```

اکنون با `kubectl debug` یک کپی از آن بسازید و ایمیج کانتینر آن را به `ubuntu` تغییر دهید:

```
kubectl debug myapp --copy-to=myapp-debug --set-image=*=ubuntu
```

نحو `--set-image` همان نحو `container_name=image` در `kubectl set image` است. عبارت `*=ubuntu` یعنی ایمیج همهٔ کانتینرها به `ubuntu` تغییر کند.

فراموش نکنید که پس از پایان کار، Pod اشکال‌زدایی را پاک کنید:

```shell
kubectl delete pod myapp myapp-debug
```

## اشکال‌زدایی از طریق پوسته روی نود {#node-shell-session}

اگر هیچ‌یک از این روش‌ها کارساز نبود، می‌توانید نودی را که Pod روی آن اجرا می‌شود پیدا کنید و یک Pod روی همان نود بسازید. برای ایجاد یک پوستهٔ تعاملی روی یک نود با `kubectl debug`، این دستور را اجرا کنید:

```shell
kubectl debug node/mynode -it --image=ubuntu
```

```
Creating debugging pod node-debugger-mynode-pdx84 with container debugger on node mynode.
If you don't see a command prompt, try pressing enter.
root@ek8s:/#
```

هنگام ایجاد نشست اشکال‌زدایی روی یک نود، به نکات زیر توجه کنید:

* دستور `kubectl debug` نام Pod جدید را به‌طور خودکار بر اساس نام نود تولید می‌کند.
* فایل‌سیستم ریشهٔ نود در مسیر `/host` سوار (mount) می‌شود.
* کانتینر در فضاهای نام IPC، شبکه و PID میزبان اجرا می‌شود، اما Pod ممتاز (privileged) نیست؛ بنابراین ممکن است خواندن برخی اطلاعات فرایندها و نیز اجرای `chroot /host` با شکست مواجه شود.
* اگر به یک Pod ممتاز نیاز دارید، آن را به‌صورت دستی بسازید یا از فلگ `--profile=sysadmin` استفاده کنید.

فراموش نکنید که پس از پایان کار، Pod اشکال‌زدایی را پاک کنید:

```shell
kubectl delete pod node-debugger-mynode-pdx84
```

### ضبط و تحلیل ترافیک نود و Pod

هنگام اشکال‌زدایی مشکلات شبکه، ضبط و تحلیل ترافیک شبکهٔ نودها و Podها می‌تواند دید ارزشمندی دربارهٔ مشکلات اتصال، خطاهای تفکیک نام DNS یا رفتارهای غیرمنتظرهٔ شبکه به شما بدهد.

می‌توانید از `kubectl debug` همراه با فلگ `--profile=sysadmin` برای اجرای ابزارهای ضبط ترافیک شبکه روی یک نود استفاده کنید. ابتدا روی نودی که Pod شما در آن اجرا می‌شود یک نشست اشکال‌زدایی ایجاد کنید:

```shell
kubectl debug --profile=sysadmin node/${NODE_NAME} -it --image=ubuntu:latest
```

پس از ورود به کانتینر اشکال‌زدایی، ابزار tcpdump را نصب کنید و ترافیک رابط‌های شبکهٔ نود را ضبط کنید:

```shell
apt-get update && apt-get install -y tcpdump
tcpdump -i any -n
```

{{< note >}}
فراموش نکنید که پس از پایان کار، Pod اشکال‌زدایی را پاک کنید:

```shell
kubectl delete pod node-debugger-mynode-pdx84
```
{{< /note >}}

همچنین می‌توانید ترافیک یک Pod مشخص را ضبط کنید:

```shell
kubectl debug --profile=sysadmin pod/${POD_NAME} -n ${NAMESPACE} -it --image=ubuntu:latest
```

سپس همان دستور `tcpdump` را در کانتینر اشکال‌زدایی اجرا کنید تا ترافیک فضای نام شبکهٔ Pod ضبط شود.

## اشکال‌زدایی یک Pod یا نود همراه با اعمال یک پروفایل {#debugging-profiles}

هنگامی که با `kubectl debug` یک نود را از طریق یک Pod اشکال‌زدایی، یک Pod را از طریق یک کانتینر موقت (ephemeral container)، یا یک Pod کپی‌شده را اشکال‌زدایی می‌کنید، می‌توانید یک پروفایل روی آن‌ها اعمال کنید. با اعمال پروفایل، ویژگی‌های مشخصی مانند [securityContext](/docs/tasks/configure-pod-container/security-context/) تنظیم می‌شوند و به این ترتیب می‌توان آن‌ها را با سناریوهای گوناگون سازگار کرد. پروفایل‌ها دو نوع هستند: پروفایل ایستا و پروفایل سفارشی.

### اعمال پروفایل ایستا {#static-profile}

پروفایل ایستا مجموعه‌ای از ویژگی‌های ازپیش‌تعریف‌شده است که می‌توانید آن را با فلگ `--profile` اعمال کنید. پروفایل‌های موجود عبارت‌اند از:

| پروفایل      | توضیحات                                                     |
| ------------ | --------------------------------------------------------------- |
| legacy       | مجموعه‌ای از ویژگی‌ها برای سازگاری با رفتار نسخهٔ ۱.۲۲ |
| general      | مجموعه‌ای معقول از ویژگی‌های عمومی برای هر فرایند اشکال‌زدایی |
| baseline     | مجموعه‌ای از ویژگی‌های سازگار با [سیاست baseline در PodSecurityStandard](/docs/concepts/security/pod-security-standards/#baseline) |
| restricted   | مجموعه‌ای از ویژگی‌های سازگار با [سیاست restricted در PodSecurityStandard](/docs/concepts/security/pod-security-standards/#restricted) |
| netadmin     | مجموعه‌ای از ویژگی‌ها شامل امتیازات مدیر شبکه |
| sysadmin     | مجموعه‌ای از ویژگی‌ها شامل امتیازات مدیر سیستم (root) |


{{< note >}}
اگر `--profile` را مشخص نکنید، به‌طور پیش‌فرض از پروفایل `legacy` استفاده می‌شود، اما قرار است این پروفایل در آیندهٔ نزدیک منسوخ شود. بنابراین توصیه می‌شود از پروفایل‌های دیگری مانند `general` استفاده کنید.
{{< /note >}}


فرض کنید یک Pod می‌سازید و آن را اشکال‌زدایی می‌کنید. ابتدا به‌عنوان مثال یک Pod با نام `myapp` بسازید:

```shell
kubectl run myapp --image=busybox:1.28 --restart=Never -- sleep 1d
```

سپس Pod را با یک کانتینر موقت اشکال‌زدایی کنید. اگر کانتینر موقت به امتیاز ویژه نیاز دارد، می‌توانید از پروفایل `sysadmin` استفاده کنید:

```shell
kubectl debug -it myapp --image=busybox:1.28 --target=myapp --profile=sysadmin
```

```
Targeting container "myapp". If you don't see processes from this container it may be because the container runtime doesn't support this feature.
Defaulting debug container name to debugger-6kg4x.
If you don't see a command prompt, try pressing enter.
/ #
```

با اجرای دستور زیر در داخل کانتینر، قابلیت‌های (capabilities) فرایند کانتینر موقت را بررسی کنید:

```shell
/ # grep Cap /proc/$$/status
```

```
...
CapPrm:	000001ffffffffff
CapEff:	000001ffffffffff
...
```

این خروجی یعنی با اعمال پروفایل `sysadmin`، همهٔ قابلیت‌ها به فرایند کانتینر اعطا شده است، همانند یک کانتینر ممتاز. برای جزئیات بیشتر به [قابلیت‌ها](/docs/tasks/configure-pod-container/security-context/#set-capabilities-for-a-container) مراجعه کنید.

همچنین می‌توانید بررسی کنید که کانتینر موقت به‌صورت یک کانتینر ممتاز ساخته شده است:

```shell
kubectl get pod myapp -o jsonpath='{.spec.ephemeralContainers[0].securityContext}'
```

```
{"privileged":true}
```

پس از پایان کار، Pod را پاک کنید:

```shell
kubectl delete pod myapp
```

### اعمال پروفایل سفارشی {#custom-profile}

{{< feature-state for_k8s_version="v1.32" state="stable" >}}

می‌توانید بخشی از مشخصات (spec) کانتینر را برای اشکال‌زدایی، به‌صورت یک پروفایل سفارشی در قالب YAML یا JSON تعریف کنید و آن را با فلگ `--custom` اعمال کنید.

{{< note >}}
پروفایل سفارشی فقط از تغییر مشخصات کانتینر پشتیبانی می‌کند، اما تغییر فیلدهای `name`، `image`، `command`، `lifecycle` و `volumeDevices` در مشخصات کانتینر مجاز نیست. این پروفایل از تغییر مشخصات Pod پشتیبانی نمی‌کند.
{{< /note >}}

به‌عنوان مثال یک Pod با نام myapp بسازید:

```shell
kubectl run myapp --image=busybox:1.28 --restart=Never -- sleep 1d
```

یک پروفایل سفارشی در قالب YAML یا JSON بسازید. در اینجا یک فایل YAML با نام `custom-profile.yaml` ایجاد کنید:

```yaml
env:
- name: ENV_VAR_1
  value: value_1
- name: ENV_VAR_2
  value: value_2
securityContext:
  capabilities:
    add:
    - NET_ADMIN
    - SYS_TIME

```

این دستور را اجرا کنید تا Pod با یک کانتینر موقت و با اعمال پروفایل سفارشی اشکال‌زدایی شود:

```shell
kubectl debug -it myapp --image=busybox:1.28 --target=myapp --profile=general --custom=custom-profile.yaml
```

می‌توانید بررسی کنید که کانتینر موقت با پروفایل سفارشی اعمال‌شده به Pod هدف اضافه شده است:

```shell
kubectl get pod myapp -o jsonpath='{.spec.ephemeralContainers[0].env}'
```

```
[{"name":"ENV_VAR_1","value":"value_1"},{"name":"ENV_VAR_2","value":"value_2"}]
```

```shell
kubectl get pod myapp -o jsonpath='{.spec.ephemeralContainers[0].securityContext}'
```

```
{"capabilities":{"add":["NET_ADMIN","SYS_TIME"]}}
```

پس از پایان کار، Pod را پاک کنید:

```shell
kubectl delete pod myapp
```
