---
title: تأیید آرتیفکت‌های امضاشدهٔ کوبرنتیز
content_type: task
min-kubernetes-server-version: v1.26
weight: 420
---

<!-- overview -->

{{< feature-state state="beta" for_k8s_version="v1.26" >}}

## {{% heading "prerequisites" %}}

باید ابزارهای زیر را نصب کرده باشید:

- `cosign` ([راهنمای نصب](https://docs.sigstore.dev/cosign/system_config/installation/))
- `curl` (که معمولاً سیستم‌عامل شما آن را فراهم می‌کند)
- `jq` ([دانلود jq](https://jqlang.github.io/jq/download/))

## تأیید امضای فایل‌های باینری

فرایند انتشار کوبرنتیز همهٔ آرتیفکت‌های باینری (فایل‌های tarball، فایل‌های SPDX و باینری‌های مستقل) را با روش امضای بدون کلید (keyless signing) ابزار cosign امضا می‌کند. برای تأیید یک باینری مشخص، آن را همراه با امضا و گواهی‌اش دریافت کنید:

```bash
URL=https://dl.k8s.io/release/v{{< skew currentPatchVersion >}}/bin/linux/amd64
BINARY=kubectl

FILES=(
    "$BINARY"
    "$BINARY.sig"
    "$BINARY.cert"
)

for FILE in "${FILES[@]}"; do
    curl -sSfL --retry 3 --retry-delay 3 "$URL/$FILE" -o "$FILE"
done
```

سپس با دستور `cosign verify-blob` فایل دریافت‌شده را تأیید کنید:

```shell
cosign verify-blob "$BINARY" \
  --signature "$BINARY".sig \
  --certificate "$BINARY".cert \
  --certificate-identity krel-staging@k8s-releng-prod.iam.gserviceaccount.com \
  --certificate-oidc-issuer https://accounts.google.com
```

{{< note >}}
نسخهٔ 2.0 ابزار Cosign به گزینه‌های `--certificate-identity` و `--certificate-oidc-issuer` نیاز دارد.

برای آشنایی بیشتر با امضای بدون کلید، به [امضاهای بدون کلید](https://docs.sigstore.dev/cosign/signing/overview/) مراجعه کنید.

در نسخه‌های قبلی Cosign لازم بود متغیر `COSIGN_EXPERIMENTAL=1` را تنظیم کنید.

برای اطلاعات بیشتر، به [وبلاگ sigstore](https://blog.sigstore.dev/cosign-2-0-released/) مراجعه کنید.
{{< /note >}}

## تأیید امضای ایمیج‌ها

برای مشاهدهٔ فهرست کامل ایمیج‌های امضاشده، به صفحهٔ [انتشارها](/releases/download/) مراجعه کنید.

یکی از ایمیج‌های این فهرست را انتخاب کنید و امضای آن را با دستور `cosign verify` تأیید کنید:

```shell
cosign verify registry.k8s.io/kube-apiserver-amd64:v{{< skew currentPatchVersion >}} \
  --certificate-identity krel-trust@k8s-releng-prod.iam.gserviceaccount.com \
  --certificate-oidc-issuer https://accounts.google.com \
  | jq .
```

### تأیید ایمیج‌های همهٔ مؤلفه‌های control plane

برای تأیید همهٔ ایمیج‌های امضاشدهٔ control plane در آخرین نسخهٔ پایدار (v{{< skew currentPatchVersion >}})، دستورهای زیر را اجرا کنید:

```shell
curl -Ls "https://sbom.k8s.io/$(curl -Ls https://dl.k8s.io/release/stable.txt)/release" \
  | grep "SPDXID: SPDXRef-Package-registry.k8s.io" \
  | grep -v sha256 | cut -d- -f3- | sed 's/-/\//' | sed 's/-v1/:v1/' \
  | sort > images.txt
input=images.txt
while IFS= read -r image
do
  cosign verify "$image" \
    --certificate-identity krel-trust@k8s-releng-prod.iam.gserviceaccount.com \
    --certificate-oidc-issuer https://accounts.google.com \
    | jq .
done < "$input"
```

پس از تأیید یک ایمیج، می‌توانید مانند مثال زیر آن را با digest خودش در مانیفست‌های Pod مشخص کنید:

```console
registry-url/image-name@sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2
```

برای اطلاعات بیشتر، به بخش [سیاست دریافت ایمیج](/docs/concepts/containers/images/#image-pull-policy) مراجعه کنید.

## تأیید امضای ایمیج‌ها با کنترل‌کنندهٔ پذیرش

امضای ایمیج‌هایی که به control plane تعلق ندارند (برای مثال [ایمیج انطباق‌پذیری](https://github.com/kubernetes/kubernetes/blob/master/test/conformance/image/README.md)) را نیز می‌توان هنگام استقرار با کنترل‌کنندهٔ پذیرش (admission controller) [sigstore policy-controller](https://docs.sigstore.dev/policy-controller/overview) تأیید کرد.

منابع مفید زیر برای شروع کار با `policy-controller` در دسترس هستند:

- [نصب](https://github.com/sigstore/helm-charts/tree/main/charts/policy-controller)
- [گزینه‌های پیکربندی](https://github.com/sigstore/policy-controller/tree/main/config)

## تأیید فهرست اجزای نرم‌افزار

فهرست اجزای نرم‌افزار (SBOM) کوبرنتیز را می‌توانید با گواهی و امضای sigstore، یا با فایل‌های SHA متناظر تأیید کنید:

```shell
# Retrieve the latest available Kubernetes release version
VERSION=$(curl -Ls https://dl.k8s.io/release/stable.txt)

# Verify the SHA512 sum
curl -Ls "https://sbom.k8s.io/$VERSION/release" -o "$VERSION.spdx"
echo "$(curl -Ls "https://sbom.k8s.io/$VERSION/release.sha512") $VERSION.spdx" | sha512sum --check

# Verify the SHA256 sum
echo "$(curl -Ls "https://sbom.k8s.io/$VERSION/release.sha256") $VERSION.spdx" | sha256sum --check

# Retrieve sigstore signature and certificate
curl -Ls "https://sbom.k8s.io/$VERSION/release.sig" -o "$VERSION.spdx.sig"
curl -Ls "https://sbom.k8s.io/$VERSION/release.cert" -o "$VERSION.spdx.cert"

# Verify the sigstore signature
cosign verify-blob \
    --certificate "$VERSION.spdx.cert" \
    --signature "$VERSION.spdx.sig" \
    --certificate-identity krel-staging@k8s-releng-prod.iam.gserviceaccount.com \
    --certificate-oidc-issuer https://accounts.google.com \
    "$VERSION.spdx"
```
