---
title: دسترسی به کلاسترها با استفاده از API کوبرنتیز
content_type: task
weight: 60
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه می‌توان با استفاده از API کوبرنتیز به کلاسترها دسترسی پیدا کرد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

## دسترسی به API کوبرنتیز

### نخستین دسترسی با kubectl

هنگامی که برای نخستین بار به API کوبرنتیز دسترسی پیدا می‌کنید، از ابزار خط فرمان کوبرنتیز، یعنی `kubectl`، استفاده کنید.

برای دسترسی به یک کلاستر، باید محل کلاستر را بدانید و اعتبارنامه‌های (credentials) لازم برای دسترسی به آن را در اختیار داشته باشید. معمولاً وقتی یکی از [راهنماهای شروع به کار](/docs/setup/) را دنبال می‌کنید، این موارد به‌طور خودکار تنظیم می‌شوند؛ یا ممکن است شخص دیگری کلاستر را راه‌اندازی کرده و اعتبارنامه‌ها و محل کلاستر را در اختیار شما گذاشته باشد.

با این فرمان، محل و اعتبارنامه‌هایی را که kubectl از آن‌ها آگاه است بررسی کنید:

```shell
kubectl config view
```

بسیاری از [نمونه‌ها](https://github.com/kubernetes/examples/tree/master/) مقدمه‌ای بر استفاده از kubectl ارائه می‌دهند. مستندات کامل را می‌توانید در [راهنمای kubectl](/docs/reference/kubectl/) بیابید.

### دسترسی مستقیم به REST API

ابزار kubectl یافتن سرور API و احراز هویت در برابر آن را خودش انجام می‌دهد. اگر می‌خواهید با یک کلاینت http مانند `curl` یا `wget`، یا با یک مرورگر، مستقیماً به REST API دسترسی پیدا کنید، چند روش برای یافتن سرور API و احراز هویت در برابر آن وجود دارد:

1. kubectl را در حالت پراکسی اجرا کنید (توصیه‌شده). این روش توصیه می‌شود، زیرا از محل ذخیره‌شدهٔ سرور API استفاده می‌کند و هویت سرور API را با یک گواهی خودامضا (self-signed) تأیید می‌کند. با این روش، حملهٔ مرد میانی (MITM) امکان‌پذیر نیست.
1. به‌عنوان راه دیگر، می‌توانید محل و اعتبارنامه‌ها را مستقیماً در اختیار کلاینت http قرار دهید. این روش با کدهای کلاینتی که با پراکسی‌ها دچار مشکل می‌شوند کار می‌کند. برای محافظت در برابر حملات مرد میانی، باید یک گواهی ریشه را در مرورگر خود وارد کنید.

استفاده از کتابخانه‌های کلاینت Go یا Python، دسترسی از طریق kubectl در حالت پراکسی را فراهم می‌کند.

#### استفاده از kubectl proxy

فرمان زیر kubectl را در حالتی اجرا می‌کند که در آن به‌عنوان یک پراکسی معکوس (reverse proxy) عمل می‌کند. این فرمان یافتن سرور API و احراز هویت را انجام می‌دهد.

آن را به این صورت اجرا کنید:

```shell
kubectl proxy --port=8080 &
```

برای جزئیات بیشتر، [kubectl proxy](/docs/reference/generated/kubectl/kubectl-commands/#proxy) را ببینید.

سپس می‌توانید API را با curl، wget یا یک مرورگر بررسی کنید؛ به این صورت:

```shell
curl http://localhost:8080/api/
```

خروجی مشابه زیر است:

```json
{
  "versions": [
    "v1"
  ],
  "serverAddressByClientCIDRs": [
    {
      "clientCIDR": "0.0.0.0/0",
      "serverAddress": "10.0.1.149:443"
    }
  ]
}
```

#### بدون kubectl proxy

می‌توان با ارسال مستقیم یک توکن احراز هویت به سرور API، از به‌کارگیری kubectl proxy صرف‌نظر کرد؛ به این صورت:

با استفاده از روش `grep/cut`:

```shell
# Check all possible clusters, as your .KUBECONFIG may have multiple contexts:
kubectl config view -o jsonpath='{"Cluster name\tServer\n"}{range .clusters[*]}{.name}{"\t"}{.cluster.server}{"\n"}{end}'

# Select name of cluster you want to interact with from above output:
export CLUSTER_NAME="some_server_name"

# Point to the API server referring the cluster name
APISERVER=$(kubectl config view -o jsonpath="{.clusters[?(@.name==\"$CLUSTER_NAME\")].cluster.server}")

# Create a secret to hold a token for the default service account
kubectl apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: default-token
  annotations:
    kubernetes.io/service-account.name: default
type: kubernetes.io/service-account-token
EOF

# Wait for the token controller to populate the secret with a token:
while ! kubectl describe secret default-token | grep -E '^token' >/dev/null; do
  echo "waiting for token..." >&2
  sleep 1
done

# Get the token value
TOKEN=$(kubectl get secret default-token -o jsonpath='{.data.token}' | base64 --decode)

# Explore the API with TOKEN
curl -X GET $APISERVER/api --header "Authorization: Bearer $TOKEN" --insecure
```

خروجی مشابه زیر است:

```json
{
  "kind": "APIVersions",
  "versions": [
    "v1"
  ],
  "serverAddressByClientCIDRs": [
    {
      "clientCIDR": "0.0.0.0/0",
      "serverAddress": "10.0.1.149:443"
    }
  ]
}
```

نمونهٔ بالا از فلگ `--insecure` استفاده می‌کند و به همین دلیل در معرض حملات MITM قرار دارد. وقتی kubectl به کلاستر دسترسی پیدا می‌کند، برای دسترسی به سرور از یک گواهی ریشهٔ ذخیره‌شده و گواهی‌های کلاینت استفاده می‌کند. (این گواهی‌ها در دایرکتوری `~/.kube` نصب می‌شوند.) از آنجا که گواهی‌های کلاستر معمولاً خودامضا هستند، ممکن است برای اینکه کلاینت http شما از گواهی ریشه استفاده کند، به پیکربندی ویژه‌ای نیاز باشد.

در برخی کلاسترها، سرور API به احراز هویت نیاز ندارد؛ ممکن است فقط روی localhost سرویس دهد یا با یک فایروال محافظت شود. استاندارد مشخصی برای این موضوع وجود ندارد. صفحهٔ [کنترل دسترسی به API کوبرنتیز](/docs/concepts/security/controlling-access) توضیح می‌دهد که چگونه می‌توانید به‌عنوان مدیر کلاستر این موارد را پیکربندی کنید.

### دسترسی برنامه‌نویسی‌شده به API

کوبرنتیز به‌طور رسمی از کتابخانه‌های کلاینت برای [Go](#go-client)، [Python](#python-client)، [Java](#java-client)، [dotnet](#dotnet-client)، [JavaScript](#javascript-client) و [Haskell](#haskell-client) پشتیبانی می‌کند. کتابخانه‌های کلاینت دیگری نیز وجود دارند که نویسندگانشان، و نه تیم کوبرنتیز، آن‌ها را ارائه و نگهداری می‌کنند. برای دسترسی به API از زبان‌های دیگر و آشنایی با نحوهٔ احراز هویت آن‌ها، [کتابخانه‌های کلاینت](/docs/reference/using-api/client-libraries/) را ببینید.

#### کلاینت Go

* برای دریافت کتابخانه، فرمان زیر را اجرا کنید: `go get k8s.io/client-go@kubernetes-<kubernetes-version-number>`
  برای اطلاع از نسخه‌های پشتیبانی‌شده، [https://github.com/kubernetes/client-go/releases](https://github.com/kubernetes/client-go/releases) را ببینید.
* برنامه‌ای مبتنی بر کلاینت‌های client-go بنویسید.

{{< note >}}

کتابخانهٔ `client-go` آبجکت‌های API مخصوص به خود را تعریف می‌کند؛ بنابراین در صورت نیاز، تعریف‌های API را به‌جای مخزن اصلی، از client-go وارد (import) کنید. برای نمونه، `import "k8s.io/client-go/kubernetes"` درست است.

{{< /note >}}

کلاینت Go می‌تواند برای یافتن سرور API و احراز هویت در برابر آن، از همان [فایل kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) استفاده کند که kubectl CLI به کار می‌برد. این [نمونه](https://git.k8s.io/client-go/examples/out-of-cluster-client-configuration/main.go) را ببینید:

```golang
package main

import (
  "context"
  "fmt"
  "k8s.io/apimachinery/pkg/apis/meta/v1"
  "k8s.io/client-go/kubernetes"
  "k8s.io/client-go/tools/clientcmd"
)

func main() {
  // uses the current context in kubeconfig
  // path-to-kubeconfig -- for example, /root/.kube/config
  config, _ := clientcmd.BuildConfigFromFlags("", "<path-to-kubeconfig>")
  // creates the clientset
  clientset, _ := kubernetes.NewForConfig(config)
  // access the API to list pods
  pods, _ := clientset.CoreV1().Pods("").List(context.TODO(), v1.ListOptions{})
  fmt.Printf("There are %d pods in the cluster\n", len(pods.Items))
}
```

اگر برنامه به‌صورت یک Pod در کلاستر مستقر شده است، [دسترسی به API از درون یک Pod](/docs/tasks/access-application-cluster/access-cluster/#accessing-the-api-from-a-pod) را ببینید.

#### کلاینت Python

برای استفاده از [کلاینت Python](https://github.com/kubernetes-client/python)، فرمان زیر را اجرا کنید: `pip install kubernetes`. برای گزینه‌های بیشتر نصب، [صفحهٔ کتابخانهٔ کلاینت Python](https://github.com/kubernetes-client/python) را ببینید.

کلاینت Python می‌تواند برای یافتن سرور API و احراز هویت در برابر آن، از همان [فایل kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) استفاده کند که kubectl CLI به کار می‌برد. این [نمونه](https://github.com/kubernetes-client/python/blob/master/examples/out_of_cluster_config.py) را ببینید:

```python
from kubernetes import client, config

config.load_kube_config()

v1=client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
```

#### کلاینت Java

برای نصب [کلاینت Java](https://github.com/kubernetes-client/java)، این فرمان‌ها را اجرا کنید:

```shell
# Clone java library
git clone --recursive https://github.com/kubernetes-client/java

# Installing project artifacts, POM etc:
cd java
mvn install
```

برای اطلاع از نسخه‌های پشتیبانی‌شده، [https://github.com/kubernetes-client/java/releases](https://github.com/kubernetes-client/java/releases) را ببینید.

کلاینت Java می‌تواند برای یافتن سرور API و احراز هویت در برابر آن، از همان [فایل kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) استفاده کند که kubectl CLI به کار می‌برد. این [نمونه](https://github.com/kubernetes-client/java/blob/master/examples/examples-release-latest/src/main/java/io/kubernetes/client/examples/KubeConfigFileClientExample.java) را ببینید:

```java
package io.kubernetes.client.examples;

import io.kubernetes.client.ApiClient;
import io.kubernetes.client.ApiException;
import io.kubernetes.client.Configuration;
import io.kubernetes.client.apis.CoreV1Api;
import io.kubernetes.client.models.V1Pod;
import io.kubernetes.client.models.V1PodList;
import io.kubernetes.client.util.ClientBuilder;
import io.kubernetes.client.util.KubeConfig;
import java.io.FileReader;
import java.io.IOException;

/**
 * A simple example of how to use the Java API from an application outside a kubernetes cluster
 *
 * <p>Easiest way to run this: mvn exec:java
 * -Dexec.mainClass="io.kubernetes.client.examples.KubeConfigFileClientExample"
 *
 */
public class KubeConfigFileClientExample {
  public static void main(String[] args) throws IOException, ApiException {

    // file path to your KubeConfig
    String kubeConfigPath = "~/.kube/config";

    // loading the out-of-cluster config, a kubeconfig from file-system
    ApiClient client =
        ClientBuilder.kubeconfig(KubeConfig.loadKubeConfig(new FileReader(kubeConfigPath))).build();

    // set the global default api-client to the in-cluster one from above
    Configuration.setDefaultApiClient(client);

    // the CoreV1Api loads default api-client from global configuration.
    CoreV1Api api = new CoreV1Api();

    // invokes the CoreV1Api client
    V1PodList list = api.listPodForAllNamespaces(null, null, null, null, null, null, null, null, null);
    System.out.println("Listing all pods: ");
    for (V1Pod item : list.getItems()) {
      System.out.println(item.getMetadata().getName());
    }
  }
}
```

#### کلاینت dotnet

برای استفاده از [کلاینت dotnet](https://github.com/kubernetes-client/csharp)، فرمان زیر را اجرا کنید: `dotnet add package KubernetesClient --version 1.6.1`. برای گزینه‌های بیشتر نصب، [صفحهٔ کتابخانهٔ کلاینت dotnet](https://github.com/kubernetes-client/csharp) را ببینید. برای اطلاع از نسخه‌های پشتیبانی‌شده، [https://github.com/kubernetes-client/csharp/releases](https://github.com/kubernetes-client/csharp/releases) را ببینید.

کلاینت dotnet می‌تواند برای یافتن سرور API و احراز هویت در برابر آن، از همان [فایل kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) استفاده کند که kubectl CLI به کار می‌برد. این [نمونه](https://github.com/kubernetes-client/csharp/blob/master/examples/simple/PodList.cs) را ببینید:

```csharp
using System;
using k8s;

namespace simple
{
    internal class PodList
    {
        private static void Main(string[] args)
        {
            var config = KubernetesClientConfiguration.BuildDefaultConfig();
            IKubernetes client = new Kubernetes(config);
            Console.WriteLine("Starting Request!");

            var list = client.ListNamespacedPod("default");
            foreach (var item in list.Items)
            {
                Console.WriteLine(item.Metadata.Name);
            }
            if (list.Items.Count == 0)
            {
                Console.WriteLine("Empty!");
            }
        }
    }
}
```

#### کلاینت JavaScript

برای نصب [کلاینت JavaScript](https://github.com/kubernetes-client/javascript)، فرمان زیر را اجرا کنید: `npm install @kubernetes/client-node`. برای اطلاع از نسخه‌های پشتیبانی‌شده، [https://github.com/kubernetes-client/javascript/releases](https://github.com/kubernetes-client/javascript/releases) را ببینید.

کلاینت JavaScript می‌تواند برای یافتن سرور API و احراز هویت در برابر آن، از همان [فایل kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) استفاده کند که kubectl CLI به کار می‌برد. این [نمونه](https://github.com/kubernetes-client/javascript/blob/master/examples/example.js) را ببینید:

```javascript
const k8s = require('@kubernetes/client-node');

const kc = new k8s.KubeConfig();
kc.loadFromDefault();

const k8sApi = kc.makeApiClient(k8s.CoreV1Api);

k8sApi.listNamespacedPod({ namespace: 'default' }).then((res) => {
    console.log(res);
});
```

#### کلاینت Haskell

برای اطلاع از نسخه‌های پشتیبانی‌شده، [https://github.com/kubernetes-client/haskell/releases](https://github.com/kubernetes-client/haskell/releases) را ببینید.

[کلاینت Haskell](https://github.com/kubernetes-client/haskell) می‌تواند برای یافتن سرور API و احراز هویت در برابر آن، از همان [فایل kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) استفاده کند که kubectl CLI به کار می‌برد. این [نمونه](https://github.com/kubernetes-client/haskell/blob/master/kubernetes-client/example/App.hs) را ببینید:

```haskell
exampleWithKubeConfig :: IO ()
exampleWithKubeConfig = do
    oidcCache <- atomically $ newTVar $ Map.fromList []
    (mgr, kcfg) <- mkKubeClientConfig oidcCache $ KubeConfigFile "/path/to/kubeconfig"
    dispatchMime
            mgr
            kcfg
            (CoreV1.listPodForAllNamespaces (Accept MimeJSON))
        >>= print
```

## {{% heading "whatsnext" %}}

* [دسترسی به API کوبرنتیز از درون یک Pod](/docs/tasks/run-application/access-api-from-pod/)
