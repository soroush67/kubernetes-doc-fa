---
title: مهاجرت آبجکت‌های کوبرنتیز با استفاده از مهاجرت نسخهٔ ذخیره‌سازی
reviewers:
- deads2k
- jpbetz
- enj
- nilekhc
- michaelasp
content_type: task
min-kubernetes-server-version: v1.30
weight: 60
---

<!-- overview -->

{{< feature-state feature_gate_name="StorageVersionMigrator" >}}

کوبرنتیز برای پشتیبانی از برخی فعالیت‌های نگهداری مربوط به داده‌های ذخیره‌شده (at rest)، به بازنویسی فعال داده‌های API متکی است. دو نمونهٔ برجستهٔ این فعالیت‌ها عبارت‌اند از شِمای نسخه‌دار منابع ذخیره‌شده (یعنی تغییر شِمای ذخیره‌سازی ترجیحی یک منبع از v1 به v2) و رمزگذاری داده‌های ذخیره‌شده (یعنی بازنویسی داده‌های قدیمی بر اساس تغییری در نحوهٔ رمزگذاری داده‌ها).

با اجرای مهاجرت نسخهٔ ذخیره‌سازی (storage version migration) می‌توانید اطمینان پیدا کنید که همهٔ آبجکت‌های یک منبع از نسخهٔ ذخیره‌سازی قدیمی مهاجرت داده شده‌اند. پیش‌نیاز اجرای مهاجرت ذخیره‌سازی این است که منبع موردنظر یک نسخهٔ منبع (resource version) از نوع عدد صحیح داشته باشد. این ویژگی برای همهٔ منابع کوبرنتیز و CRDها تضمین شده است، اما اگر چنین نباشد، برای مثال در APIهای تجمیع‌شده (aggregated APIs)، مهاجرت با شکست مواجه می‌شود.

## {{% heading "prerequisites" %}}

[`kubectl`](/docs/tasks/tools/#kubectl) را نصب کنید.

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

[feature gate](/docs/reference/command-line-tools-reference/feature-gates/#StorageVersionMigrator) با نام `StorageVersionMigrator` و REST API با نام `storagemigration.k8s.io/v1` به‌طور پیش‌فرض در همهٔ کلاسترها فعال هستند.

<!-- steps -->

## رمزگذاری دوبارهٔ Secretهای کوبرنتیز با استفاده از مهاجرت نسخهٔ ذخیره‌سازی

- برای شروع، [ارائه‌دهندهٔ KMS را پیکربندی کنید](/docs/tasks/administer-cluster/kms-provider/) تا داده‌های ذخیره‌شده در etcd با پیکربندی رمزگذاری زیر رمزگذاری شوند.

  ```yaml
  kind: EncryptionConfiguration
  apiVersion: apiserver.config.k8s.io/v1
  resources:
  - resources:
    - secrets
    providers:
    - aescbc:
        keys:
        - name: key1
          secret: c2VjcmV0IGlzIHNlY3VyZQ==
  ```

  حتماً با تنظیم `--encryption-provider-config-automatic-reload` روی true، بارگذاری مجدد خودکار فایل پیکربندی رمزگذاری را فعال کنید.

- با استفاده از kubectl یک Secret ایجاد کنید.

  ```shell
  kubectl create secret generic my-secret --from-literal=key1=supersecret
  ```

- [بررسی کنید](/docs/tasks/administer-cluster/kms-provider/#verifying-that-the-data-is-encrypted) که داده‌های سریال‌شدهٔ آن آبجکت Secret با پیشوند `k8s:enc:aescbc:v1:key1` آغاز می‌شوند.

- برای چرخش کلید رمزگذاری، فایل پیکربندی رمزگذاری را به‌صورت زیر به‌روزرسانی کنید.

  ```yaml
  kind: EncryptionConfiguration
  apiVersion: apiserver.config.k8s.io/v1
  resources:
  - resources:
    - secrets
    providers:
    - aescbc:
        keys:
        - name: key2
          secret: c2VjcmV0IGlzIHNlY3VyZSwgaXMgaXQ/
    - aescbc:
        keys:
        - name: key1
          secret: c2VjcmV0IGlzIHNlY3VyZQ==
  ```

- برای اطمینان از اینکه Secret ایجادشدهٔ قبلی، یعنی `my-secret`، با کلید جدید `key2` دوباره رمزگذاری شود، از _مهاجرت نسخهٔ ذخیره‌سازی_ استفاده خواهید کرد.

- یک مانیفست StorageVersionMigration با نام `migrate-secret.yaml` به‌صورت زیر ایجاد کنید:

  ```yaml
  kind: StorageVersionMigration
  apiVersion: storagemigration.k8s.io/v1
  metadata:
    name: secrets-migration
  spec:
    resource:
      group: ""
      resource: secrets
  ```

  آبجکت را با استفاده از `kubectl` به‌صورت زیر ایجاد کنید:

  ```shell
  kubectl apply -f migrate-secret.yaml
  ```

- با بررسی `.status` آبجکت StorageVersionMigration، روند مهاجرت Secretها را پایش کنید. در یک مهاجرت موفق، شرط `Succeeded` باید روی true تنظیم شده باشد. آبجکت StorageVersionMigration را به‌صورت زیر دریافت کنید:

  ```shell
  kubectl wait --for=condition=Succeeded storageversionmigration.storagemigration.k8s.io/secrets-migration
  ```

  خروجی مشابه زیر است:

  ```yaml
  kind: StorageVersionMigration
  apiVersion: storagemigration.k8s.io/v1
  metadata:
    name: secrets-migration
    uid: 628f6922-a9cb-4514-b076-12d3c178967c
    resourceVersion: "90"
    creationTimestamp: "2024-03-12T20:29:45Z"
  spec:
    resource:
      group: ""
      resource: secrets
  status:
    conditions:
    - type: Running
      status: "False"
      lastUpdateTime: "2024-03-12T20:29:46Z"
      reason: StorageVersionMigrationInProgress
    - type: Succeeded
      status: "True"
      lastUpdateTime: "2024-03-12T20:29:46Z"
      reason: StorageVersionMigrationSucceeded
    resourceVersion: "84"
  ```

- [بررسی کنید](/docs/tasks/administer-cluster/kms-provider/#verifying-that-the-data-is-encrypted) که Secret ذخیره‌شده اکنون با پیشوند `k8s:enc:aescbc:v1:key2` آغاز می‌شود.

## به‌روزرسانی شِمای ذخیره‌سازی ترجیحی یک CRD

سناریویی را در نظر بگیرید که در آن یک {{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinition" >}} (CRD) برای ارائهٔ منابع سفارشی (CR) ایجاد شده و به‌عنوان شِمای ذخیره‌سازی ترجیحی تنظیم شده است. هنگامی که زمان معرفی نسخهٔ v2 این CRD فرا می‌رسد، می‌توان آن را فقط برای ارائه (serving) و همراه با یک وب‌هوک تبدیل (conversion webhook) اضافه کرد. این کار گذاری روان‌تر را ممکن می‌سازد؛ به این صورت که کاربران می‌توانند CRها را با شِمای v1 یا v2 ایجاد کنند و وب‌هوک تبدیل‌های لازم میان این دو شِما را انجام می‌دهد. پیش از تنظیم v2 به‌عنوان نسخهٔ ترجیحی شِمای ذخیره‌سازی، مهم است اطمینان حاصل کنید که همهٔ CRهای موجودِ ذخیره‌شده با نسخهٔ v1 به v2 مهاجرت داده شده‌اند. این مهاجرت را می‌توان با _مهاجرت نسخهٔ ذخیره‌سازی_ انجام داد تا همهٔ CRها از v1 به v2 منتقل شوند.

- یک مانیفست برای CRD با نام `test-crd.yaml` به‌صورت زیر ایجاد کنید:

  ```yaml
  apiVersion: apiextensions.k8s.io/v1
  kind: CustomResourceDefinition
  metadata:
    name: selfierequests.example.com
  spec:
    group: example.com
    names:
      plural: selfierequests
      singular: selfierequest
      kind: SelfieRequest
      listKind: SelfieRequestList
    scope: Namespaced
    versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            hostPort:
              type: string
    conversion:
      strategy: Webhook
      webhook:
        clientConfig:
          url: "https://127.0.0.1:9443/crdconvert"
          caBundle: <CABundle info>
      conversionReviewVersions:
      - v1
      - v2
  ```

  در این مرحله نسخهٔ ذخیره‌شده باید `v1` باشد؛ برای تأیید این موضوع دستور زیر را اجرا کنید:
  ```shell
  kubectl get crd selfierequests.example.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}'
  ```

  CRD را با استفاده از kubectl ایجاد کنید:

  ```shell
  kubectl apply -f test-crd.yaml
  ```

- یک مانیفست برای یک testcrd نمونه ایجاد کنید. نام مانیفست را `cr1.yaml` بگذارید و محتوای زیر را در آن قرار دهید:

  ```yaml
  apiVersion: example.com/v1
  kind: SelfieRequest
  metadata:
    name: cr1
    namespace: default
  ```

  CR را با استفاده از kubectl ایجاد کنید:

  ```shell
  kubectl apply -f cr1.yaml
  ```

- با دریافت آبجکت از etcd، بررسی کنید که CR با نسخهٔ v1 نوشته و ذخیره شده است.

  ```shell
  ETCDCTL_API=3 etcdctl get /kubernetes.io/example.com/testcrds/default/cr1 [...] | hexdump -C
  ```

  در اینجا `[...]` شامل آرگومان‌های اضافی برای اتصال به سرور etcd است.

- فایل CRD یعنی `test-crd.yaml` را به‌صورت زیر به‌روزرسانی کنید تا نسخهٔ v2 هم برای ارائه و هم برای ذخیره‌سازی، و نسخهٔ v1 فقط برای ارائه تعریف شود:

  ```yaml
  apiVersion: apiextensions.k8s.io/v1
  kind: CustomResourceDefinition
  metadata:
  name: selfierequests.example.com
  spec:
    group: example.com
    names:
      plural: selfierequests
      singular: selfierequest
      kind: SelfieRequest
      listKind: SelfieRequestList
    scope: Namespaced
    versions:
      - name: v2
        served: true
        storage: true
        schema:
          openAPIV3Schema:
            type: object
            properties:
              host:
                type: string
              port:
                type: string
      - name: v1
        served: true
        storage: false
        schema:
          openAPIV3Schema:
            type: object
            properties:
              hostPort:
                type: string
    conversion:
      strategy: Webhook
      webhook:
        clientConfig:
          url: "https://127.0.0.1:9443/crdconvert"
          caBundle: <CABundle info>
        conversionReviewVersions:
          - v1
          - v2
  ```

  اکنون نسخهٔ ذخیره‌شده باید `v2` باشد؛ این موضوع را تأیید کنید:
  ```shell
  kubectl get crd selfierequests.example.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}'
  ```

  CRD را با استفاده از kubectl به‌روزرسانی کنید:

  ```shell
  kubectl apply -f test-crd.yaml
  ```

- فایل منبع CR را با نام `cr2.yaml` به‌صورت زیر ایجاد کنید:

  ```yaml
  apiVersion: example.com/v2
  kind: SelfieRequest
  metadata:
    name: cr2
    namespace: default
  ```

- CR را با استفاده از kubectl ایجاد کنید:

  ```shell
  kubectl apply -f cr2.yaml
  ```

- با دریافت آبجکت از etcd، بررسی کنید که CR با نسخهٔ v2 نوشته و ذخیره شده است.

  ```shell
  ETCDCTL_API=3 etcdctl get /kubernetes.io/example.com/testcrds/default/cr2 [...] | hexdump -C
  ```

  در اینجا `[...]` شامل آرگومان‌های اضافی برای اتصال به سرور etcd است.

- یک مانیفست StorageVersionMigration با نام `migrate-crd.yaml` و با محتوای زیر ایجاد کنید:

  ```yaml
  kind: StorageVersionMigration
  apiVersion: storagemigration.k8s.io/v1
  metadata:
    name: crdsvm
  spec:
    resource:
      group: example.com
      resource: selfierequests
  ```

  آبجکت را با استفاده از _kubectl_ به‌صورت زیر ایجاد کنید:

  ```shell
  kubectl apply -f migrate-crd.yaml
  ```

- روند مهاجرت Secretها را با استفاده از وضعیت (status) پایش کنید. در یک مهاجرت موفق، شرط `Succeeded` در فیلد status باید روی "True" تنظیم شده باشد. منبع مهاجرت را به‌صورت زیر دریافت کنید:

  ```shell
  kubectl get storageversionmigration.storagemigration.k8s.io/crdsvm -o yaml
  ```

  خروجی مشابه زیر است:

  ```yaml
  kind: StorageVersionMigration
  apiVersion: storagemigration.k8s.io/v1
  metadata:
    name: crdsvm
    uid: 13062fe4-32d7-47cc-9528-5067fa0c6ac8
    resourceVersion: "111"
    creationTimestamp: "2024-03-12T22:40:01Z"
  spec:
    resource:
      group: example.com
      resource: testcrds
  status:
    conditions:
      - type: Running
        status: "False"
        lastUpdateTime: "2024-03-12T22:40:03Z"
        reason: StorageVersionMigrationInProgress
      - type: Succeeded
        status: "True"
        lastUpdateTime: "2024-03-12T22:40:03Z"
        reason: StorageVersionMigrationSucceeded
    resourceVersion: "106"
  ```

- با دریافت آبجکت از etcd، بررسی کنید که cr1 ایجادشدهٔ قبلی اکنون با نسخهٔ v2 نوشته و ذخیره شده است.

  ```shell
  ETCDCTL_API=3 etcdctl get /kubernetes.io/example.com/testcrds/default/cr1 [...] | hexdump -C
  ```

  در اینجا `[...]` شامل آرگومان‌های اضافی برای اتصال به سرور etcd است.

- همچنین بررسی کنید که وضعیت نسخه‌های ذخیره‌شدهٔ CRD اکنون فقط شامل v2 است:

  ```shell
  kubectl get crd testcrds.example.com -o yaml
  ```

  خروجی مشابه زیر است:

  ```yaml
  kind: CustomResourceDefinition
  apiVersion: apiextensions.k8s.io/v1
  metadata:
    name: testcrds.example.com
  spec:
    group: example.com
    names:
      kind: TestCRD
      plural: testcrds
    scope: Namespaced
    versions:
      - name: v1
        served: true
        storage: false
      - name: v2
        served: true
        storage: true
  status:
    acceptedNames:
      kind: TestCRD
      plural: testcrds
    conditions:
      - type: Established
        status: "True"
    storedVersions:
      - v2
  ```
