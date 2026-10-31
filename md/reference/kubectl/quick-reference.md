---
title: مرجع سریع kubectl
reviewers:
- erictune
- krousey
- clove
content_type: concept
weight: 10 # highlight it
card:
  name: tasks
  weight: 10
---

<!-- overview -->

این صفحه فهرستی از دستورها و فلگ‌های پرکاربرد `kubectl` را در بر دارد.

{{< note >}}
این دستورالعمل‌ها برای کوبرنتیز نسخهٔ v{{< skew currentVersion >}} نوشته شده‌اند. برای بررسی نسخه، از دستور `kubectl version` استفاده کنید.
{{< /note >}}
<!-- body -->

## تکمیل خودکار kubectl

### BASH

```bash
source <(kubectl completion bash) # set up autocomplete in bash into the current shell, bash-completion package should be installed first.
echo "source <(kubectl completion bash)" >> ~/.bashrc # add autocomplete permanently to your bash shell.
```

همچنین می‌توانید برای `kubectl` یک نام مستعار (alias) کوتاه تعریف کنید که با تکمیل خودکار نیز کار کند:

```bash
alias k=kubectl
complete -o default -F __start_kubectl k
```

### ZSH

```bash
source <(kubectl completion zsh)  # set up autocomplete in zsh into the current shell
echo '[[ $commands[kubectl] ]] && source <(kubectl completion zsh)' >> ~/.zshrc # add autocomplete permanently to your zsh shell
```

### FISH

{{< note >}}
به kubectl نسخهٔ 1.23 یا بالاتر نیاز دارد.
{{< /note >}}

```bash
echo 'kubectl completion fish | source' > ~/.config/fish/completions/kubectl.fish && source ~/.config/fish/completions/kubectl.fish
```

### نکته‌ای دربارهٔ `--all-namespaces`

افزودن `--all-namespaces` به فرمان‌ها آن‌قدر رایج است که بهتر است شکل کوتاه آن را بشناسید:

```kubectl -A```

## زمینه (context) و پیکربندی kubectl

با این فرمان‌ها مشخص می‌کنید که `kubectl` با کدام کلاستر کوبرنتیز ارتباط برقرار کند و اطلاعات پیکربندی را تغییر می‌دهید. برای آشنایی دقیق با فایل پیکربندی، مستند [احراز هویت در چند کلاستر با kubeconfig](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) را ببینید.

```bash
kubectl config view # Show Merged kubeconfig settings.

# use multiple kubeconfig files at the same time and view merged config
KUBECONFIG=~/.kube/config:~/.kube/kubconfig2

kubectl config view

# Show merged kubeconfig settings and raw certificate data and exposed secrets
kubectl config view --raw

# get the password for the e2e user
kubectl config view -o jsonpath='{.users[?(@.name == "e2e")].user.password}'

# get the certificate for the e2e user
kubectl config view --raw -o jsonpath='{.users[?(.name == "e2e")].user.client-certificate-data}' | base64 -d

kubectl config view -o jsonpath='{.users[].name}'    # display the first user
kubectl config view -o jsonpath='{.users[*].name}'   # get a list of users
kubectl config get-contexts                          # display list of contexts
kubectl config get-contexts -o name                  # get all context names
kubectl config current-context                       # display the current-context
kubectl config use-context my-cluster-name           # set the default context to my-cluster-name

kubectl config set-cluster my-cluster-name           # set a cluster entry in the kubeconfig

# configure the URL to a proxy server to use for requests made by this client in the kubeconfig
kubectl config set-cluster my-cluster-name --proxy-url=my-proxy-url

# add a new user to your kubeconf that supports basic auth
kubectl config set-credentials kubeuser/foo.kubernetes.com --username=kubeuser --password=kubepassword

# permanently save the namespace for all subsequent kubectl commands in that context.
kubectl config set-context --current --namespace=ggckad-s2

# set a context utilizing a specific username and namespace.
kubectl config set-context gce --user=cluster-admin --namespace=foo \
  && kubectl config use-context gce

kubectl config unset users.foo                       # delete user foo

# short alias to set/show context/namespace (only works for bash and bash-compatible shells, current context to be set before using kn to set namespace)
alias kx='f() { [ "$1" ] && kubectl config use-context $1 || kubectl config current-context ; } ; f'
alias kn='f() { [ "$1" ] && kubectl config set-context --current --namespace $1 || kubectl config view --minify | grep namespace | cut -d" " -f6 ; } ; f'
```

## فرمان kubectl apply

فرمان `apply` برنامه‌ها را از طریق فایل‌هایی مدیریت می‌کند که منابع کوبرنتیز را تعریف می‌کنند. با اجرای `kubectl apply`، منابع در کلاستر ایجاد و به‌روزرسانی می‌شوند. این روش توصیه‌شده برای مدیریت برنامه‌های کوبرنتیز در محیط عملیاتی است. برای اطلاعات بیشتر، [کتاب Kubectl](https://kubectl.docs.kubernetes.io) را ببینید.

## ایجاد آبجکت‌ها

مانیفست‌های کوبرنتیز را می‌توان در قالب YAML یا JSON تعریف کرد. پسوندهای `.yaml`، `.yml` و `.json` برای این فایل‌ها قابل استفاده‌اند.

```bash
kubectl apply -f ./my-manifest.yaml                 # create resource(s)
kubectl apply -f ./my1.yaml -f ./my2.yaml           # create from multiple files
kubectl apply -f ./dir                              # create resource(s) in all manifest files in dir
kubectl apply -f https://example.com/manifest.yaml  # create resource(s) from url (Note: this is an example domain and does not contain a valid manifest)
kubectl create deployment nginx --image=nginx       # start a single instance of nginx

# create a Job which prints "Hello World"
kubectl create job hello --image=busybox:1.28 -- echo "Hello World"

# create a CronJob that prints "Hello World" every minute
kubectl create cronjob hello --image=busybox:1.28   --schedule="*/1 * * * *" -- echo "Hello World"

kubectl explain pods                           # get the documentation for pod manifests

# Create multiple YAML objects from stdin
kubectl apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: busybox-sleep
spec:
  containers:
  - name: busybox
    image: busybox:1.28
    args:
    - sleep
    - "1000000"
---
apiVersion: v1
kind: Pod
metadata:
  name: busybox-sleep-less
spec:
  containers:
  - name: busybox
    image: busybox:1.28
    args:
    - sleep
    - "1000"
EOF

# Create a secret with several keys
kubectl apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  password: $(echo -n "s33msi4" | base64 -w0)
  username: $(echo -n "jane" | base64 -w0)
EOF

```

## مشاهده و یافتن منابع

```bash
# Get commands with basic output
kubectl get services                          # List all services in the namespace
kubectl get pods --all-namespaces             # List all pods in all namespaces
kubectl get pods -o wide                      # List all pods in the current namespace, with more details
kubectl get deployment my-dep                 # List a particular deployment
kubectl get pods                              # List all pods in the namespace
kubectl get pod my-pod -o yaml                # Get a pod's YAML

# Describe commands with verbose output
kubectl describe nodes my-node
kubectl describe pods my-pod

# List Services Sorted by Name
kubectl get services --sort-by=.metadata.name

# List pods Sorted by Restart Count
kubectl get pods --sort-by='.status.containerStatuses[0].restartCount'

# List PersistentVolumes sorted by capacity
kubectl get pv --sort-by=.spec.capacity.storage

# Get the version label of all pods with label app=cassandra
kubectl get pods --selector=app=cassandra -o \
  jsonpath='{.items[*].metadata.labels.version}'

# Retrieve the value of a key with dots, e.g. 'ca.crt'
kubectl get configmap myconfig \
  -o jsonpath='{.data.ca\.crt}'

# Retrieve a base64 encoded value with dashes instead of underscores.
kubectl get secret my-secret --template='{{index .data "key-name-with-dashes"}}'

# Get all worker nodes (use a selector to exclude results that have a label
# named 'node-role.kubernetes.io/control-plane')
kubectl get node --selector='!node-role.kubernetes.io/control-plane'

# Get all running pods in the namespace
kubectl get pods --field-selector=status.phase=Running

# Get ExternalIPs of all nodes
kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="ExternalIP")].address}'

# List Names of Pods that belong to Particular RC
# "jq" command useful for transformations that are too complex for jsonpath, it can be found at https://jqlang.github.io/jq/
sel=${$(kubectl get rc my-rc --output=json | jq -j '.spec.selector | to_entries | .[] | "\(.key)=\(.value),"')%?}
echo $(kubectl get pods --selector=$sel --output=jsonpath={.items..metadata.name})

# Show labels for all pods (or any other Kubernetes object that supports labelling)
kubectl get pods --show-labels

# Check which nodes are ready
JSONPATH='{range .items[*]}{@.metadata.name}:{range @.status.conditions[*]}{@.type}={@.status};{end}{end}' \
 && kubectl get nodes -o jsonpath="$JSONPATH" | grep "Ready=True"

# Check which nodes are ready with custom-columns
kubectl get node -o custom-columns='NODE_NAME:.metadata.name,STATUS:.status.conditions[?(@.type=="Ready")].status'

# Output decoded secrets without external tools
kubectl get secret my-secret -o go-template='{{range $k,$v := .data}}{{"### "}}{{$k}}{{"\n"}}{{$v|base64decode}}{{"\n\n"}}{{end}}'

# List all Secrets currently in use by a pod
kubectl get pods -o json | jq '.items[].spec.containers[].env[]?.valueFrom.secretKeyRef.name' | grep -v null | sort | uniq

# List all containerIDs of initContainer of all pods
# Helpful when cleaning up stopped containers, while avoiding removal of initContainers.
kubectl get pods --all-namespaces -o jsonpath='{range .items[*].status.initContainerStatuses[*]}{.containerID}{"\n"}{end}' | cut -d/ -f3

# List Events sorted by timestamp
kubectl get events --sort-by=.metadata.creationTimestamp

# List all warning events
kubectl events --types=Warning

# Compares the current state of the cluster against the state that the cluster would be in if the manifest was applied.
kubectl diff -f ./my-manifest.yaml

# Produce a period-delimited tree of all keys returned for nodes
# Helpful when locating a key within a complex nested JSON structure
kubectl get nodes -o json | jq -c 'paths|join(".")'

# Produce a period-delimited tree of all keys returned for pods, etc
kubectl get pods -o json | jq -c 'paths|join(".")'

# Produce ENV for all pods, assuming you have a default container for the pods, default namespace and the `env` command is supported.
# Helpful when running any supported command across all pods, not just `env`
for pod in $(kubectl get po --output=jsonpath={.items..metadata.name}); do echo $pod && kubectl exec -it $pod -- env; done

# Get a deployment's status subresource
kubectl get deployment nginx-deployment --subresource=status
```

## به‌روزرسانی منابع

```bash
kubectl set image deployment/frontend www=image:v2               # Rolling update "www" containers of "frontend" deployment, updating the image
kubectl rollout history deployment/frontend                      # Check the history of deployments including the revision
kubectl rollout undo deployment/frontend                         # Rollback to the previous deployment
kubectl rollout undo deployment/frontend --to-revision=2         # Rollback to a specific revision
kubectl rollout status -w deployment/frontend                    # Watch rolling update status of "frontend" deployment until completion
kubectl rollout restart deployment/frontend                      # Rolling restart of the "frontend" deployment


cat pod.json | kubectl replace -f -                              # Replace a pod based on the JSON passed into stdin

# Force replace, delete and then re-create the resource. Will cause a service outage.
kubectl replace --force -f ./pod.json

# Create a service for a replicated nginx, which serves on port 80 and connects to the containers on port 8000
kubectl expose rc nginx --port=80 --target-port=8000

# Update a single-container pod's image version (tag) to v4
kubectl get pod mypod -o yaml | sed 's/\(image: myimage\):.*$/\1:v4/' | kubectl replace -f -

kubectl label pods my-pod new-label=awesome                      # Add a Label
kubectl label pods my-pod new-label-                             # Remove a label
kubectl label pods my-pod new-label=new-value --overwrite        # Overwrite an existing value
kubectl annotate pods my-pod icon-url=http://goo.gl/XXBTWq       # Add an annotation
kubectl annotate pods my-pod icon-url-                           # Remove annotation
kubectl autoscale deployment foo --min=2 --max=10                # Auto scale a deployment "foo"
```

## وصله‌کردن (patch) منابع

```bash
# Partially update a node
kubectl patch node k8s-node-1 -p '{"spec":{"unschedulable":true}}'

# Update a container's image; spec.containers[*].name is required because it's a merge key
kubectl patch pod valid-pod -p '{"spec":{"containers":[{"name":"kubernetes-serve-hostname","image":"new image"}]}}'

# Update a container's image using a json patch with positional arrays
kubectl patch pod valid-pod --type='json' -p='[{"op": "replace", "path": "/spec/containers/0/image", "value":"new image"}]'

# Disable a deployment livenessProbe using a json patch with positional arrays
kubectl patch deployment valid-deployment  --type json   -p='[{"op": "remove", "path": "/spec/template/spec/containers/0/livenessProbe"}]'

# Add a new element to a positional array
kubectl patch sa default --type='json' -p='[{"op": "add", "path": "/secrets/1", "value": {"name": "whatever" } }]'

# Update a deployment's replica count by patching its scale subresource
kubectl patch deployment nginx-deployment --subresource='scale' --type='merge' -p '{"spec":{"replicas":2}}'
```

## ویرایش منابع

هر منبع API را می‌توانید در ویرایشگر دلخواه خود ویرایش کنید.

```bash
kubectl edit svc/docker-registry                      # Edit the service named docker-registry
KUBE_EDITOR="nano" kubectl edit svc/docker-registry   # Use an alternative editor
```

## مقیاس‌دهی منابع

```bash
kubectl scale --replicas=3 rs/foo                                 # Scale a replicaset named 'foo' to 3
kubectl scale --replicas=3 -f foo.yaml                            # Scale a resource specified in "foo.yaml" to 3
kubectl scale --current-replicas=2 --replicas=3 deployment/mysql  # If the deployment named mysql's current size is 2, scale mysql to 3
kubectl scale --replicas=5 rc/foo rc/bar rc/baz                   # Scale multiple replication controllers
```

## حذف منابع

```bash
kubectl delete -f ./pod.json                                      # Delete a pod using the type and name specified in pod.json
kubectl delete pod unwanted --now                                 # Delete a pod with no grace period
kubectl delete pod,service baz foo                                # Delete pods and services with same names "baz" and "foo"
kubectl delete pods,services -l name=myLabel                      # Delete pods and services with label name=myLabel
kubectl -n my-ns delete pod,svc --all                             # Delete all pods and services in namespace my-ns,
# Delete all pods matching the awk pattern1 or pattern2
kubectl get pods  -n mynamespace --no-headers=true | awk '/pattern1|pattern2/{print $1}' | xargs  kubectl delete -n mynamespace pod
```

## تعامل با Podهای در حال اجرا

```bash
kubectl logs my-pod                                 # dump pod logs (stdout)
kubectl logs -l name=myLabel                        # dump pod logs, with label name=myLabel (stdout)
kubectl logs my-pod --previous                      # dump pod logs (stdout) for a previous instantiation of a container
kubectl logs my-pod -c my-container                 # dump pod container logs (stdout, multi-container case)
kubectl logs -l name=myLabel -c my-container        # dump pod container logs, with label name=myLabel (stdout)
kubectl logs my-pod -c my-container --previous      # dump pod container logs (stdout, multi-container case) for a previous instantiation of a container
kubectl logs -f my-pod                              # stream pod logs (stdout)
kubectl logs -f my-pod -c my-container              # stream pod container logs (stdout, multi-container case)
kubectl logs -f -l name=myLabel --all-containers    # stream all pods logs with label name=myLabel (stdout)
kubectl run -i --tty busybox --image=busybox:1.28 -- sh  # Run pod as interactive shell
kubectl run nginx --image=nginx -n mynamespace      # Start a single instance of nginx pod in the namespace of mynamespace
kubectl run nginx --image=nginx --dry-run=client -o yaml > pod.yaml
                                                    # Generate spec for running pod nginx and write it into a file called pod.yaml
kubectl attach my-pod -i                            # Attach to Running Container
kubectl port-forward my-pod 5000:6000               # Listen on port 5000 on the local machine and forward to port 6000 on my-pod
kubectl exec my-pod -- ls /                         # Run command in existing pod (1 container case)
kubectl exec --stdin --tty my-pod -- /bin/sh        # Interactive shell access to a running pod (1 container case)
kubectl exec my-pod -c my-container -- ls /         # Run command in existing pod (multi-container case)
kubectl debug my-pod -it --image=busybox:1.28       # Create an interactive debugging session within existing pod and immediately attach to it
kubectl debug node/my-node -it --image=busybox:1.28 # Create an interactive debugging session on a node and immediately attach to it
kubectl top pod                                     # Show metrics for all pods in the default namespace
kubectl top pod POD_NAME --containers               # Show metrics for a given pod and its containers
kubectl top pod POD_NAME --sort-by=cpu              # Show metrics for a given pod and sort it by 'cpu' or 'memory'
```
## کپی فایل‌ها و دایرکتوری‌ها به کانتینرها و از کانتینرها

```bash
kubectl cp /tmp/foo_dir my-pod:/tmp/bar_dir            # Copy /tmp/foo_dir local directory to /tmp/bar_dir in a remote pod in the current namespace
kubectl cp /tmp/foo my-pod:/tmp/bar -c my-container    # Copy /tmp/foo local file to /tmp/bar in a remote pod in a specific container
kubectl cp /tmp/foo my-namespace/my-pod:/tmp/bar       # Copy /tmp/foo local file to /tmp/bar in a remote pod in namespace my-namespace
kubectl cp my-namespace/my-pod:/tmp/foo /tmp/bar       # Copy /tmp/foo from a remote pod to /tmp/bar locally
```
{{< note >}}
فرمان `kubectl cp` به وجود فایل اجرایی 'tar' در ایمیج کانتینر نیاز دارد. اگر 'tar' در ایمیج وجود نداشته باشد، `kubectl cp` با خطا مواجه می‌شود.
برای کاربردهای پیشرفته‌تر، مانند پیوندهای نمادین (symlink)، گسترش نویسه‌های عام (wildcard) یا حفظ مجوزهای فایل، استفاده از `kubectl exec` را در نظر بگیرید.
{{< /note >}}

```bash
tar cf - /tmp/foo | kubectl exec -i -n my-namespace my-pod -- tar xf - -C /tmp/bar           # Copy /tmp/foo local file to /tmp/bar in a remote pod in namespace my-namespace
kubectl exec -n my-namespace my-pod -- tar cf - /tmp/foo | tar xf - -C /tmp/bar    # Copy /tmp/foo from a remote pod to /tmp/bar locally
```


## تعامل با Deploymentها و Serviceها
```bash
kubectl logs deploy/my-deployment                         # dump Pod logs for a Deployment (single-container case)
kubectl logs deploy/my-deployment -c my-container         # dump Pod logs for a Deployment (multi-container case)

kubectl port-forward svc/my-service 5000                  # listen on local port 5000 and forward to port 5000 on Service backend
kubectl port-forward svc/my-service 5000:my-service-port  # listen on local port 5000 and forward to Service target port with name <my-service-port>

kubectl port-forward deploy/my-deployment 5000:6000       # listen on local port 5000 and forward to port 6000 on a Pod created by <my-deployment>
kubectl exec deploy/my-deployment -- ls                   # run command in first Pod and first container in Deployment (single- or multi-container cases)
```

## تعامل با نودها و کلاستر

```bash
kubectl cordon my-node                                                # Mark my-node as unschedulable
kubectl drain my-node                                                 # Drain my-node in preparation for maintenance
kubectl uncordon my-node                                              # Mark my-node as schedulable
kubectl top node                                                      # Show metrics for all nodes
kubectl top node my-node                                              # Show metrics for a given node
kubectl cluster-info                                                  # Display addresses of the master and services
kubectl cluster-info dump                                             # Dump current cluster state to stdout
kubectl cluster-info dump --output-directory=/path/to/cluster-state   # Dump current cluster state to /path/to/cluster-state

# View existing taints on which exist on current nodes.
kubectl get nodes -o='custom-columns=NodeName:.metadata.name,TaintKey:.spec.taints[*].key,TaintValue:.spec.taints[*].value,TaintEffect:.spec.taints[*].effect'

# If a taint with that key and effect already exists, its value is replaced as specified.
kubectl taint nodes foo dedicated=special-user:NoSchedule
```

### انواع منابع

با فرمان زیر، فهرست همهٔ انواع منابع پشتیبانی‌شده را همراه با نام‌های کوتاه، [گروه API](/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning)، [وابستگی یا عدم وابستگی به فضای نام](/docs/concepts/overview/working-with-objects/namespaces) و [نوع (kind)](/docs/concepts/overview/working-with-objects/) آن‌ها مشاهده کنید:

```bash
kubectl api-resources
```

عملیات دیگر برای بررسی منابع API:

```bash
kubectl api-resources --namespaced=true      # All namespaced resources
kubectl api-resources --namespaced=false     # All non-namespaced resources
kubectl api-resources -o name                # All resources with simple output (only the resource name)
kubectl api-resources -o wide                # All resources with expanded (aka "wide") output
kubectl api-resources --verbs=list,get       # All resources that support the "list" and "get" request verbs
kubectl api-resources --api-group=extensions # All resources in the "extensions" API group
```

### قالب‌بندی خروجی

برای نمایش جزئیات در پنجرهٔ ترمینال با قالبی مشخص، فلگ `-o` (یا `--output`) را به یکی از فرمان‌های پشتیبانی‌شدهٔ `kubectl` اضافه کنید.

قالب خروجی | توضیح
--------------| -----------
`-o=custom-columns=<spec>` | جدولی را با استفاده از فهرستی از ستون‌های سفارشی که با کاما از هم جدا شده‌اند چاپ می‌کند
`-o=custom-columns-file=<filename>` | جدولی را با استفاده از الگوی ستون‌های سفارشی موجود در فایل `<filename>` چاپ می‌کند
`-o=go-template=<template>`     | فیلدهای تعریف‌شده در یک [الگوی golang](https://pkg.go.dev/text/template) را چاپ می‌کند
`-o=go-template-file=<filename>` | فیلدهای تعریف‌شده در [الگوی golang](https://pkg.go.dev/text/template) موجود در فایل `<filename>` را چاپ می‌کند
`-o=json`     | یک آبجکت API را در قالب JSON نمایش می‌دهد
`-o=jsonpath=<template>` | فیلدهای تعریف‌شده در یک عبارت [jsonpath](/docs/reference/kubectl/jsonpath) را چاپ می‌کند
`-o=jsonpath-file=<filename>` | فیلدهای تعریف‌شده در عبارت [jsonpath](/docs/reference/kubectl/jsonpath) موجود در فایل `<filename>` را چاپ می‌کند
`-o=kyaml`    | یک آبجکت API را در قالب [KYAML](/docs/reference/encodings/kyaml) نمایش می‌دهد. KYAML گویشی از YAML مخصوص کوبرنتیز است و می‌توان آن را به‌عنوان YAML تجزیه کرد.
`-o=name`     | فقط نام منبع را چاپ می‌کند و هیچ چیز دیگری را نمایش نمی‌دهد
`-o=wide`     | خروجی را در قالب متن ساده همراه با اطلاعات تکمیلی نمایش می‌دهد و برای Podها نام نود را نیز درج می‌کند
`-o=yaml`     | یک آبجکت API را در قالب YAML نمایش می‌دهد

نمونه‌هایی از کاربرد `-o=custom-columns`:

```bash
# All images running in a cluster
kubectl get pods -A -o=custom-columns='DATA:spec.containers[*].image'

# All images running in namespace: default, grouped by Pod
kubectl get pods --namespace default --output=custom-columns="NAME:.metadata.name,IMAGE:.spec.containers[*].image"

 # All images excluding "registry.k8s.io/coredns:1.6.2"
kubectl get pods -A -o=custom-columns='DATA:spec.containers[?(@.image!="registry.k8s.io/coredns:1.6.2")].image'

# All fields under metadata regardless of name
kubectl get pods -A -o=custom-columns='DATA:metadata.*'
```

نمونه‌های بیشتر را می‌توانید در [مستندات مرجع](/docs/reference/kubectl/#custom-columns) kubectl ببینید.

### میزان جزئیات خروجی kubectl و اشکال‌زدایی

میزان جزئیات (verbosity) خروجی kubectl با پرچم `-v` یا `--v` و یک عدد صحیح پس از آن تعیین می‌شود که سطح لاگ را نشان می‌دهد. قراردادهای کلی لاگ‌نویسی در کوبرنتیز و سطوح لاگ مربوط به آن‌ها [در اینجا](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-instrumentation/logging.md) شرح داده شده‌اند.

میزان جزئیات | توضیحات
--------------| -----------
`--v=0` | معمولاً مفید است که این سطح *همیشه* برای اپراتور کلاستر قابل مشاهده باشد.
`--v=1` | اگر به جزئیات زیاد نیاز ندارید، سطح لاگ پیش‌فرض مناسبی است.
`--v=2` | اطلاعات مفیدی درباره وضعیت پایدار سرویس و پیام‌های لاگ مهمی ارائه می‌دهد که ممکن است با تغییرات قابل‌توجه در سیستم مرتبط باشند. این سطح، سطح لاگ پیش‌فرض توصیه‌شده برای بیشتر سیستم‌هاست.
`--v=3` | اطلاعات گسترده‌تری درباره تغییرات نمایش می‌دهد.
`--v=4` | جزئیات در سطح اشکال‌زدایی (debug).
`--v=5` | جزئیات در سطح ردیابی (trace).
`--v=6` | منابع درخواست‌شده را نمایش می‌دهد.
`--v=7` | سرآیندهای درخواست HTTP را نمایش می‌دهد.
`--v=8` | محتوای درخواست HTTP را نمایش می‌دهد.
`--v=9` | محتوای درخواست HTTP را بدون کوتاه‌سازی نمایش می‌دهد.

## {{% heading "whatsnext" %}}

* با [نمای کلی kubectl](/docs/concepts/overview/kubectl/) و نقش آن در اکوسیستم کوبرنتیز آشنا شوید.
* [مرجع kubectl](/docs/reference/kubectl/) را بخوانید و با [JsonPath](/docs/reference/kubectl/jsonpath) آشنا شوید.

* گزینه‌های [kubectl](/docs/reference/kubectl/kubectl/) را ببینید.

* گزینه‌های [kuberc](/docs/reference/kubectl/kuberc) را ببینید.

* همچنین [قراردادهای استفاده از kubectl](/docs/reference/kubectl/conventions/) را بخوانید تا با نحوه استفاده از kubectl در اسکریپت‌های قابل استفاده مجدد آشنا شوید.

* [برگه‌های تقلب kubectl](https://github.com/dennyzhang/cheatsheet-kubernetes-A4) بیشتری را که جامعه کاربری تهیه کرده است ببینید.
