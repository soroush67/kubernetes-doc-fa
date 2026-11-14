---
title: مدیریت اعلانی آبجکت‌های کوبرنتیز با استفاده از Kustomize
content_type: task
weight: 20
---

<!-- overview -->

ابزار [Kustomize](https://github.com/kubernetes-sigs/kustomize) ابزاری مستقل برای سفارشی‌سازی آبجکت‌های کوبرنتیز از طریق یک [فایل kustomization](https://kubectl.docs.kubernetes.io/references/kustomize/glossary/#kustomization) است.

از نسخهٔ 1.14 به بعد، kubectl نیز از مدیریت آبجکت‌های کوبرنتیز با استفاده از فایل kustomization پشتیبانی می‌کند.
برای مشاهدهٔ منابع موجود در دایرکتوری‌ای که فایل kustomization دارد، دستور زیر را اجرا کنید:

```shell
kubectl kustomize <kustomization_directory>
```

برای اعمال این منابع، دستور `kubectl apply` را با فلگ `--kustomize` یا `-k` اجرا کنید:

```shell
kubectl apply -k <kustomization_directory>
```

## {{% heading "prerequisites" %}}

ابزار [`kubectl`](/docs/tasks/tools/) را نصب کنید.

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

## مروری بر Kustomize

ابزار Kustomize برای سفارشی‌سازی پیکربندی‌های کوبرنتیز به کار می‌رود و برای مدیریت فایل‌های پیکربندی برنامه، ویژگی‌های زیر را دارد:

* تولید منابع از منشأهای دیگر
* تنظیم فیلدهای مشترک (cross-cutting) برای منابع
* ترکیب و سفارشی‌سازی مجموعه‌هایی از منابع

### تولید منابع

آبجکت‌های ConfigMap و Secret داده‌های پیکربندی یا داده‌های حساسی را نگه می‌دارند که آبجکت‌های دیگر کوبرنتیز، مانند Podها، از آن‌ها استفاده می‌کنند. مرجع اصلی (source of truth) این داده‌ها معمولاً بیرون از کلاستر قرار دارد؛ برای نمونه، یک فایل `.properties` یا یک فایل کلید SSH.
ابزار Kustomize دو مولد `secretGenerator` و `configMapGenerator` دارد که Secret و ConfigMap را از فایل‌ها یا مقادیر لیترال تولید می‌کنند.

#### configMapGenerator

برای تولید یک ConfigMap از یک فایل، یک مدخل به فهرست `files` در `configMapGenerator` اضافه کنید.
در مثال زیر، یک ConfigMap با یک آیتم داده از یک فایل `.properties` تولید می‌شود:

```shell
# Create a application.properties file
cat <<EOF >application.properties
FOO=Bar
EOF

cat <<EOF >./kustomization.yaml
configMapGenerator:
- name: example-configmap-1
  files:
  - application.properties
EOF
```

با دستور زیر می‌توانید ConfigMap تولیدشده را بررسی کنید:

```shell
kubectl kustomize ./
```

آبجکت ConfigMap تولیدشده به این صورت است:

```yaml
apiVersion: v1
data:
  application.properties: |
    FOO=Bar
kind: ConfigMap
metadata:
  name: example-configmap-1-8mbdf7882g
```

برای تولید یک ConfigMap از یک فایل env، یک مدخل به فهرست `envs` در `configMapGenerator` اضافه کنید.
در مثال زیر، یک ConfigMap با یک آیتم داده از یک فایل `.env` تولید می‌شود:

```shell
# Create a .env file
cat <<EOF >.env
FOO=Bar
EOF

cat <<EOF >./kustomization.yaml
configMapGenerator:
- name: example-configmap-1
  envs:
  - .env
EOF
```

با دستور زیر می‌توانید ConfigMap تولیدشده را بررسی کنید:

```shell
kubectl kustomize ./
```

آبجکت ConfigMap تولیدشده به این صورت است:

```yaml
apiVersion: v1
data:
  FOO: Bar
kind: ConfigMap
metadata:
  name: example-configmap-1-42cfbf598f
```

{{< note >}}
هر متغیر در فایل `.env` به یک کلید جداگانه در ConfigMap تولیدشده تبدیل می‌شود.
این رفتار با مثال قبلی متفاوت است؛ در آن مثال، فایلی به نام `application.properties` (همراه با همهٔ مدخل‌هایش) به‌عنوان مقدارِ یک کلید واحد جاسازی می‌شد.
{{< /note >}}

همچنین می‌توان ConfigMapها را از جفت‌های کلید-مقدار لیترال تولید کرد. برای تولید یک ConfigMap از یک جفت کلید-مقدار لیترال، یک مدخل به فهرست `literals` در configMapGenerator اضافه کنید.
در مثال زیر، یک ConfigMap با یک آیتم داده از یک جفت کلید-مقدار تولید می‌شود:

```shell
cat <<EOF >./kustomization.yaml
configMapGenerator:
- name: example-configmap-2
  literals:
  - FOO=Bar
EOF
```

با دستور زیر می‌توانید ConfigMap تولیدشده را بررسی کنید:

```shell
kubectl kustomize ./
```

آبجکت ConfigMap تولیدشده به این صورت است:

```yaml
apiVersion: v1
data:
  FOO: Bar
kind: ConfigMap
metadata:
  name: example-configmap-2-g2hdhfc6tk
```

برای استفاده از یک ConfigMap تولیدشده در یک Deployment، با نامی که در configMapGenerator تعریف شده است به آن ارجاع دهید.
ابزار Kustomize این نام را به‌طور خودکار با نام تولیدشده جایگزین می‌کند.

در ادامه، نمونه‌ای از یک Deployment آمده است که از یک ConfigMap تولیدشده استفاده می‌کند:

```yaml
# Create an application.properties file
cat <<EOF >application.properties
FOO=Bar
EOF

cat <<EOF >deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  labels:
    app: my-app
spec:
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: my-app
        volumeMounts:
        - name: config
          mountPath: /config
      volumes:
      - name: config
        configMap:
          name: example-configmap-1
EOF

cat <<EOF >./kustomization.yaml
resources:
- deployment.yaml
configMapGenerator:
- name: example-configmap-1
  files:
  - application.properties
EOF
```

آبجکت‌های ConfigMap و Deployment را تولید کنید:

```shell
kubectl kustomize ./
```

آبجکت Deployment تولیدشده با نام به ConfigMap تولیدشده ارجاع می‌دهد:

```yaml
apiVersion: v1
data:
  application.properties: |
    FOO=Bar
kind: ConfigMap
metadata:
  name: example-configmap-1-g4hk9g2ff8
---
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: my-app
  name: my-app
spec:
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - image: my-app
        name: app
        volumeMounts:
        - mountPath: /config
          name: config
      volumes:
      - configMap:
          name: example-configmap-1-g4hk9g2ff8
        name: config
```

#### secretGenerator

می‌توانید Secretها را از فایل‌ها یا جفت‌های کلید-مقدار لیترال تولید کنید.
برای تولید یک Secret از یک فایل، یک مدخل به فهرست `files` در `secretGenerator` اضافه کنید.
در مثال زیر، یک Secret با یک آیتم داده از یک فایل تولید می‌شود:

```shell
# Create a password.txt file
cat <<EOF >./password.txt
username=admin
password=secret
EOF

cat <<EOF >./kustomization.yaml
secretGenerator:
- name: example-secret-1
  files:
  - password.txt
EOF
```

آبجکت Secret تولیدشده به این صورت است:

```yaml
apiVersion: v1
data:
  password.txt: dXNlcm5hbWU9YWRtaW4KcGFzc3dvcmQ9c2VjcmV0Cg==
kind: Secret
metadata:
  name: example-secret-1-t2kt65hgtb
type: Opaque
```

برای تولید یک Secret از یک جفت کلید-مقدار لیترال، یک مدخل به فهرست `literals` در `secretGenerator` اضافه کنید. در مثال زیر، یک Secret با یک آیتم داده از یک جفت کلید-مقدار تولید می‌شود:

```shell
cat <<EOF >./kustomization.yaml
secretGenerator:
- name: example-secret-2
  literals:
  - username=admin
  - password=secret
EOF
```

آبجکت Secret تولیدشده به این صورت است:

```yaml
apiVersion: v1
data:
  password: c2VjcmV0
  username: YWRtaW4=
kind: Secret
metadata:
  name: example-secret-2-t52t6g96d8
type: Opaque
```

همانند ConfigMapها، می‌توان Secretهای تولیدشده را با ارجاع به نام تعریف‌شده در secretGenerator در Deploymentها به کار برد:

```shell
# Create a password.txt file
cat <<EOF >./password.txt
username=admin
password=secret
EOF

cat <<EOF >deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  labels:
    app: my-app
spec:
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: my-app
        volumeMounts:
        - name: password
          mountPath: /secrets
      volumes:
      - name: password
        secret:
          secretName: example-secret-1
EOF

cat <<EOF >./kustomization.yaml
resources:
- deployment.yaml
secretGenerator:
- name: example-secret-1
  files:
  - password.txt
EOF
```

#### generatorOptions

به نام ConfigMapها و Secretهای تولیدشده یک پسوند حاوی هش محتوا افزوده می‌شود. این کار تضمین می‌کند که با تغییر محتوا، یک ConfigMap یا Secret جدید تولید شود. برای غیرفعال کردن افزودن این پسوند، می‌توانید از `generatorOptions` استفاده کنید. افزون بر این، با آن می‌توان گزینه‌های مشترکی را برای ConfigMapها و Secretهای تولیدشده تعیین کرد.

```shell
cat <<EOF >./kustomization.yaml
configMapGenerator:
- name: example-configmap-3
  literals:
  - FOO=Bar
generatorOptions:
  disableNameSuffixHash: true
  labels:
    type: generated
  annotations:
    note: generated
EOF
```

برای مشاهدهٔ ConfigMap تولیدشده، دستور `kubectl kustomize ./` را اجرا کنید:

```yaml
apiVersion: v1
data:
  FOO: Bar
kind: ConfigMap
metadata:
  annotations:
    note: generated
  labels:
    type: generated
  name: example-configmap-3
```

### تنظیم فیلدهای مشترک

تنظیم فیلدهای مشترک برای همهٔ منابع کوبرنتیز در یک پروژه بسیار رایج است.
برخی از کاربردهای تنظیم فیلدهای مشترک عبارت‌اند از:

* تعیین فضای نام (namespace) یکسان برای همهٔ منابع
* افزودن پیشوند یا پسوند یکسان به نام‌ها
* افزودن مجموعهٔ یکسانی از برچسب‌ها
* افزودن مجموعهٔ یکسانی از حاشیه‌نویسی‌ها (annotation)

به مثال زیر توجه کنید:

```shell
# Create a deployment.yaml
cat <<EOF >./deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
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
        image: nginx
EOF

cat <<EOF >./kustomization.yaml
namespace: my-namespace
namePrefix: dev-
nameSuffix: "-001"
labels:
  - pairs:
      app: bingo
    includeSelectors: true 
commonAnnotations:
  oncallPager: 800-555-1212
resources:
- deployment.yaml
EOF
```

برای اینکه ببینید همهٔ این فیلدها در منبع Deployment تنظیم شده‌اند، دستور `kubectl kustomize ./` را اجرا کنید:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    oncallPager: 800-555-1212
  labels:
    app: bingo
  name: dev-nginx-deployment-001
  namespace: my-namespace
spec:
  selector:
    matchLabels:
      app: bingo
  template:
    metadata:
      annotations:
        oncallPager: 800-555-1212
      labels:
        app: bingo
    spec:
      containers:
      - image: nginx
        name: nginx
```

### ترکیب و سفارشی‌سازی منابع

معمولاً مجموعه‌ای از منابع یک پروژه را با هم ترکیب می‌کنند و آن‌ها را در یک فایل یا دایرکتوری مدیریت می‌کنند.
ابزار Kustomize امکان ترکیب منابع از فایل‌های مختلف و اعمال وصله‌ها (patch) یا سفارشی‌سازی‌های دیگر روی آن‌ها را فراهم می‌کند.

#### ترکیب

ابزار Kustomize از ترکیب منابع مختلف پشتیبانی می‌کند. فیلد `resources` در فایل `kustomization.yaml` فهرست منابعی را تعیین می‌کند که باید در پیکربندی گنجانده شوند. مسیر فایل پیکربندی هر منبع را در فهرست `resources` قرار دهید.
در مثال زیر، یک برنامهٔ NGINX از یک Deployment و یک Service تشکیل شده است:

```shell
# Create a deployment.yaml file
cat <<EOF > deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  selector:
    matchLabels:
      run: my-nginx
  replicas: 2
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - name: my-nginx
        image: nginx
        ports:
        - containerPort: 80
EOF

# Create a service.yaml file
cat <<EOF > service.yaml
apiVersion: v1
kind: Service
metadata:
  name: my-nginx
  labels:
    run: my-nginx
spec:
  ports:
  - port: 80
    protocol: TCP
  selector:
    run: my-nginx
EOF

# Create a kustomization.yaml composing them
cat <<EOF >./kustomization.yaml
resources:
- deployment.yaml
- service.yaml
EOF
```

منابع حاصل از اجرای `kubectl kustomize ./` شامل هر دو آبجکت Deployment و Service است.

#### سفارشی‌سازی

با وصله‌ها می‌توان سفارشی‌سازی‌های گوناگونی را روی منابع اعمال کرد. ابزار Kustomize از طریق فیلد `patches` از سازوکارهای مختلف وصله‌گذاری، یعنی `StrategicMerge` و `Json6902`، پشتیبانی می‌کند. هر وصله در `patches` می‌تواند یک فایل یا یک رشتهٔ درون‌خطی باشد و یک یا چند منبع را هدف بگیرد.

فیلد `patches` فهرستی از وصله‌ها را در بر دارد که به همان ترتیبی که مشخص شده‌اند اعمال می‌شوند. هدف هر وصله، منابع را بر اساس `group`، `version`، `kind`، `name`، `namespace`، `labelSelector` و `annotationSelector` انتخاب می‌کند.

توصیه می‌شود از وصله‌های کوچکی استفاده کنید که هر کدام فقط یک کار انجام می‌دهند. برای مثال، یک وصله برای افزایش تعداد رپلیکاهای Deployment و وصلهٔ دیگری برای تعیین محدودیت حافظه بسازید. منبع هدف با استفاده از فیلدهای `group`، `version`، `kind` و `name` در فایل وصله تطبیق داده می‌شود.

```shell
# Create a deployment.yaml file
cat <<EOF > deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  selector:
    matchLabels:
      run: my-nginx
  replicas: 2
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - name: my-nginx
        image: nginx
        ports:
        - containerPort: 80
EOF

# Create a patch increase_replicas.yaml
cat <<EOF > increase_replicas.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  replicas: 3
EOF

# Create another patch set_memory.yaml
cat <<EOF > set_memory.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  template:
    spec:
      containers:
      - name: my-nginx
        resources:
          limits:
            memory: 512Mi
EOF

cat <<EOF >./kustomization.yaml
resources:
- deployment.yaml
patches:
  - path: increase_replicas.yaml
  - path: set_memory.yaml
EOF
```

برای مشاهدهٔ Deployment، دستور `kubectl kustomize ./` را اجرا کنید:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      run: my-nginx
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - image: nginx
        name: my-nginx
        ports:
        - containerPort: 80
        resources:
          limits:
            memory: 512Mi
```

همهٔ منابع یا فیلدها از وصله‌های `strategicMerge` پشتیبانی نمی‌کنند. برای اینکه بتوان هر فیلدی را در هر منبعی تغییر داد، ابزار Kustomize امکان اعمال [وصلهٔ JSON](https://tools.ietf.org/html/rfc6902) را از طریق `Json6902` فراهم می‌کند.
برای یافتن منبع درست برای یک وصلهٔ `Json6902`، تعیین فیلد `target` در `kustomization.yaml` الزامی است.

برای مثال، افزایش تعداد رپلیکاهای یک آبجکت Deployment را می‌توان با یک وصلهٔ `Json6902` نیز انجام داد. منبع هدف با استفاده از `group`، `version`، `kind` و `name` در فیلد `target` تطبیق داده می‌شود.

```shell
# Create a deployment.yaml file
cat <<EOF > deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  selector:
    matchLabels:
      run: my-nginx
  replicas: 2
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - name: my-nginx
        image: nginx
        ports:
        - containerPort: 80
EOF

# Create a json patch
cat <<EOF > patch.yaml
- op: replace
  path: /spec/replicas
  value: 3
EOF

# Create a kustomization.yaml
cat <<EOF >./kustomization.yaml
resources:
- deployment.yaml

patches:
- target:
    group: apps
    version: v1
    kind: Deployment
    name: my-nginx
  path: patch.yaml
EOF
```

برای اینکه ببینید فیلد `replicas` به‌روزرسانی شده است، دستور `kubectl kustomize ./` را اجرا کنید:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      run: my-nginx
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - image: nginx
        name: my-nginx
        ports:
        - containerPort: 80
```

افزون بر وصله‌ها، ابزار Kustomize امکان سفارشی‌سازی ایمیج‌های کانتینر یا تزریق مقادیر فیلدها از آبجکت‌های دیگر به کانتینرها را بدون ساختن وصله نیز فراهم می‌کند. برای مثال، می‌توانید با تعیین ایمیج جدید در فیلد `images` در `kustomization.yaml`، ایمیجی را که درون کانتینرها استفاده می‌شود تغییر دهید.

```shell
cat <<EOF > deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  selector:
    matchLabels:
      run: my-nginx
  replicas: 2
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - name: my-nginx
        image: nginx
        ports:
        - containerPort: 80
EOF

cat <<EOF >./kustomization.yaml
resources:
- deployment.yaml
images:
- name: nginx
  newName: my.image.registry/nginx
  newTag: "1.4.0"
EOF
```

برای اینکه ببینید ایمیج استفاده‌شده به‌روزرسانی شده است، دستور `kubectl kustomize ./` را اجرا کنید:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      run: my-nginx
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - image: my.image.registry/nginx:1.4.0
        name: my-nginx
        ports:
        - containerPort: 80
```

گاهی برنامه‌ای که در یک Pod اجرا می‌شود باید از مقادیر پیکربندی آبجکت‌های دیگر استفاده کند. برای مثال، یک Pod متعلق به یک آبجکت Deployment باید نام Service متناظر را از متغیرهای محیطی (Env) یا به‌صورت آرگومان فرمان بخواند.
از آنجا که با افزودن `namePrefix` یا `nameSuffix` در فایل `kustomization.yaml` ممکن است نام Service تغییر کند، توصیه نمی‌شود نام Service را به‌صورت ثابت (hard code) در آرگومان فرمان بنویسید. برای این کاربرد، ابزار Kustomize می‌تواند نام Service را از طریق `replacements` به کانتینرها تزریق کند.

```shell
# Create a deployment.yaml file (quoting the here doc delimiter)
cat <<'EOF' > deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  selector:
    matchLabels:
      run: my-nginx
  replicas: 2
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - name: my-nginx
        image: nginx
        command: ["start", "--host", "MY_SERVICE_NAME_PLACEHOLDER"]
EOF

# Create a service.yaml file
cat <<EOF > service.yaml
apiVersion: v1
kind: Service
metadata:
  name: my-nginx
  labels:
    run: my-nginx
spec:
  ports:
  - port: 80
    protocol: TCP
  selector:
    run: my-nginx
EOF

cat <<EOF >./kustomization.yaml
namePrefix: dev-
nameSuffix: "-001"

resources:
- deployment.yaml
- service.yaml

replacements:
- source:
    kind: Service
    name: my-nginx
    fieldPath: metadata.name
  targets:
  - select:
      kind: Deployment
      name: my-nginx
    fieldPaths:
    - spec.template.spec.containers.0.command.2
EOF
```

برای اینکه ببینید نام Service تزریق‌شده به کانتینرها `dev-my-nginx-001` است، دستور `kubectl kustomize ./` را اجرا کنید:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dev-my-nginx-001
spec:
  replicas: 2
  selector:
    matchLabels:
      run: my-nginx
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - command:
        - start
        - --host
        - dev-my-nginx-001
        image: nginx
        name: my-nginx
```

## پایه‌ها و لایه‌های رویی

ابزار Kustomize دو مفهوم **پایه** (base) و **لایهٔ رویی** (overlay) دارد. **پایه** دایرکتوری‌ای است که یک فایل `kustomization.yaml` دارد و شامل مجموعه‌ای از منابع و سفارشی‌سازی‌های مرتبط با آن‌هاست. پایه می‌تواند یک دایرکتوری محلی یا دایرکتوری‌ای در یک مخزن راه دور باشد، به شرطی که فایل `kustomization.yaml` درون آن وجود داشته باشد. **لایهٔ رویی** دایرکتوری‌ای با یک فایل `kustomization.yaml` است که به دایرکتوری‌های kustomization دیگر به‌عنوان `bases` خود ارجاع می‌دهد. **پایه** هیچ اطلاعی از لایهٔ رویی ندارد و می‌توان از آن در چندین لایهٔ رویی استفاده کرد.

فایل `kustomization.yaml` در دایرکتوری یک **لایهٔ رویی** می‌تواند به چندین `bases` ارجاع دهد و همهٔ منابع تعریف‌شده در این پایه‌ها را در قالب یک پیکربندی یکپارچه ترکیب کند. افزون بر این، می‌تواند برای برآوردن نیازهای خاص، سفارشی‌سازی‌هایی را روی این منابع اعمال کند.

در ادامه، نمونه‌ای از یک پایه آمده است:

```shell
# Create a directory to hold the base
mkdir base
# Create a base/deployment.yaml
cat <<EOF > base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  selector:
    matchLabels:
      run: my-nginx
  replicas: 2
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - name: my-nginx
        image: nginx
EOF

# Create a base/service.yaml file
cat <<EOF > base/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: my-nginx
  labels:
    run: my-nginx
spec:
  ports:
  - port: 80
    protocol: TCP
  selector:
    run: my-nginx
EOF
# Create a base/kustomization.yaml
cat <<EOF > base/kustomization.yaml
resources:
- deployment.yaml
- service.yaml
EOF
```

از این پایه می‌توان در چندین لایهٔ رویی استفاده کرد. می‌توانید در لایه‌های رویی مختلف، `namePrefix` متفاوت یا فیلدهای مشترک دیگری اضافه کنید. در ادامه، دو لایهٔ رویی آمده است که از یک پایهٔ یکسان استفاده می‌کنند.

```shell
mkdir dev
cat <<EOF > dev/kustomization.yaml
resources:
- ../base
namePrefix: dev-
EOF

mkdir prod
cat <<EOF > prod/kustomization.yaml
resources:
- ../base
namePrefix: prod-
EOF
```

## نحوهٔ اعمال، مشاهده و حذف آبجکت‌ها با Kustomize

برای شناسایی منابعی که با `kustomization.yaml` مدیریت می‌شوند، در دستورهای `kubectl` از `--kustomize` یا `-k` استفاده کنید.
توجه کنید که `-k` باید به یک دایرکتوری kustomization اشاره کند؛ برای نمونه:

```shell
kubectl apply -k <kustomization directory>/
```

فایل `kustomization.yaml` زیر را در نظر بگیرید:

```shell
# Create a deployment.yaml file
cat <<EOF > deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  selector:
    matchLabels:
      run: my-nginx
  replicas: 2
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - name: my-nginx
        image: nginx
        ports:
        - containerPort: 80
EOF

# Create a kustomization.yaml
cat <<EOF >./kustomization.yaml
namePrefix: dev-
labels:
  - pairs:
      app: my-nginx
    includeSelectors: true 
resources:
- deployment.yaml
EOF
```

برای اعمال آبجکت Deployment با نام `dev-my-nginx`، دستور زیر را اجرا کنید:

```shell
> kubectl apply -k ./
deployment.apps/dev-my-nginx created
```

برای مشاهدهٔ آبجکت Deployment با نام `dev-my-nginx`، یکی از دستورهای زیر را اجرا کنید:

```shell
kubectl get -k ./
```

```shell
kubectl describe -k ./
```

برای مقایسهٔ آبجکت Deployment با نام `dev-my-nginx` با وضعیتی که کلاستر در صورت اعمال مانیفست پیدا می‌کرد، دستور زیر را اجرا کنید:

```shell
kubectl diff -k ./
```

برای حذف آبجکت Deployment با نام `dev-my-nginx`، دستور زیر را اجرا کنید:

```shell
> kubectl delete -k ./
deployment.apps "dev-my-nginx" deleted
```

## فهرست قابلیت‌های Kustomize

| فیلد | نوع | توضیح |
|-------|------|-------------|
| bases | []string | هر مدخل این فهرست باید به دایرکتوری‌ای اشاره کند که یک فایل kustomization.yaml دارد |
| commonAnnotations | map[string]string | حاشیه‌نویسی‌هایی که به همهٔ منابع افزوده می‌شوند |
| commonLabels | map[string]string | برچسب‌هایی که به همهٔ منابع و انتخابگرها افزوده می‌شوند |
| configMapGenerator | [][ConfigMapArgs](https://github.com/kubernetes-sigs/kustomize/blob/master/api/types/configmapargs.go#L7) | هر مدخل این فهرست یک ConfigMap تولید می‌کند |
| configurations | []string | هر مدخل این فهرست باید به فایلی اشاره کند که [پیکربندی‌های transformer در Kustomize](https://github.com/kubernetes-sigs/kustomize/tree/master/examples/transformerconfigs) را در خود دارد |
| crds | []string | هر مدخل این فهرست باید به یک فایل تعریف OpenAPI برای نوع‌های کوبرنتیز اشاره کند |
| generatorOptions | [GeneratorOptions](https://github.com/kubernetes-sigs/kustomize/blob/master/api/types/generatoroptions.go#L7) | رفتار همهٔ مولدهای ConfigMap و Secret را تغییر می‌دهد |
| images | [][Image](https://github.com/kubernetes-sigs/kustomize/blob/master/api/types/image.go#L8) | هر مدخل، نام، تگ‌ها و/یا digest یک ایمیج را بدون ایجاد patch تغییر می‌دهد |
| labels | map[string]string | برچسب‌ها را بدون تزریق خودکار انتخابگرهای متناظر اضافه می‌کند |
| namePrefix | string | مقدار این فیلد به ابتدای نام همهٔ منابع افزوده می‌شود |
| nameSuffix | string | مقدار این فیلد به انتهای نام همهٔ منابع افزوده می‌شود |
| patchesJson6902 | [][Patch](https://github.com/kubernetes-sigs/kustomize/blob/master/api/types/patch.go#L10) | هر مدخل این فهرست باید به یک آبجکت کوبرنتیز و یک JSON Patch اشاره کند |
| patchesStrategicMerge | []string | هر مدخل این فهرست باید به یک strategic merge patch از یک آبجکت کوبرنتیز اشاره کند |
| replacements | [][Replacements](https://github.com/kubernetes-sigs/kustomize/blob/master/api/types/replacement.go#L15) | مقدار یک فیلد از یک منبع را در هر تعداد مقصد مشخص‌شده کپی می‌کند. |
| resources | []string | هر مدخل این فهرست باید به یک فایل پیکربندی منبعِ موجود اشاره کند |
| secretGenerator | [][SecretArgs](https://github.com/kubernetes-sigs/kustomize/blob/master/api/types/secretargs.go#L7) | هر مدخل این فهرست یک Secret تولید می‌کند |
| vars | [][Var](https://github.com/kubernetes-sigs/kustomize/blob/master/api/types/var.go#L19) | هر مدخل، متنی را از فیلدِ یک منبع استخراج می‌کند |

## {{% heading "whatsnext" %}}

* [Kustomize](https://github.com/kubernetes-sigs/kustomize)
* [کتاب Kubectl](https://kubectl.docs.kubernetes.io)
* [مرجع دستورهای Kubectl](/docs/reference/generated/kubectl/kubectl-commands/)
* [مرجع API کوبرنتیز](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/)
