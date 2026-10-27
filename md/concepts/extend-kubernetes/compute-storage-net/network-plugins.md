---
reviewers:
- dcbw
- freehan
- thockin
title: افزونه‌های شبکه
content_type: concept
weight: 10
---


<!-- overview -->

کوبرنتیز (از نسخهٔ 1.3 تا آخرین نسخه، یعنی {{< skew latestVersion >}}، و احتمالاً پس از آن) به شما اجازه می‌دهد
از افزونه‌های [رابط شبکهٔ کانتینر](https://github.com/containernetworking/cni)
(CNI) برای شبکهٔ کلاستر استفاده کنید. باید از افزونهٔ CNI‌ای استفاده کنید که با
کلاستر شما سازگار باشد و با نیازهای شما تناسب داشته باشد. افزونه‌های مختلفی (هم متن‌باز و هم متن‌بسته)
در اکوسیستم گسترده‌تر کوبرنتیز در دسترس هستند.

برای پیاده‌سازی
[مدل شبکهٔ کوبرنتیز](/docs/concepts/services-networking/#the-kubernetes-network-model) به یک افزونهٔ CNI نیاز است. 

باید از افزونهٔ CNI‌ای استفاده کنید که با نسخهٔ
[v0.4.0](https://github.com/containernetworking/cni/blob/spec-v0.4.0/SPEC.md) یا نسخه‌های بعدی
مشخصات CNI سازگار باشد. پروژهٔ کوبرنتیز استفاده از افزونه‌ای را توصیه می‌کند که با
مشخصات CNI نسخهٔ [v1.0.0](https://github.com/containernetworking/cni/blob/spec-v1.0.0/SPEC.md)
سازگار باشد (افزونه‌ها می‌توانند با چند نسخه از مشخصات سازگار باشند).

<!-- body -->

## نصب

یک Container Runtime (محیط اجرای کانتینر)، در زمینهٔ شبکه، دیمنی روی یک نود است که برای ارائهٔ
سرویس‌های CRI به kubelet پیکربندی شده است. به‌طور خاص، Container Runtime باید طوری پیکربندی شود که
افزونه‌های CNI لازم برای پیاده‌سازی مدل شبکهٔ کوبرنتیز را بارگذاری کند.

{{< note >}}
پیش از کوبرنتیز 1.24، افزونه‌های CNI را همچنین می‌شد توسط kubelet و با استفاده از
پارامترهای خط فرمان `cni-bin-dir` و `network-plugin` مدیریت کرد.
این پارامترهای خط فرمان در کوبرنتیز 1.24 حذف شدند و مدیریت CNI دیگر
در حوزهٔ مسئولیت kubelet نیست.

اگر پس از حذف dockershim با مشکلاتی روبه‌رو هستید، به
[عیب‌یابی خطاهای مرتبط با افزونهٔ CNI](/docs/tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors/)
مراجعه کنید.
{{< /note >}}

برای اطلاعات مشخص دربارهٔ نحوهٔ مدیریت افزونه‌های CNI توسط یک Container Runtime، به
مستندات آن Container Runtime مراجعه کنید، برای مثال:

- [containerd](https://github.com/containerd/containerd/blob/main/script/setup/install-cni)
- [CRI-O](https://github.com/cri-o/cri-o/blob/main/contrib/cni/README.md)

برای اطلاعات مشخص دربارهٔ نحوهٔ نصب و مدیریت یک افزونهٔ CNI، به مستندات آن
افزونه یا [ارائه‌دهندهٔ شبکه](/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-network-model) مراجعه کنید.

## الزامات افزونهٔ شبکه

### CNI مربوط به Loopback

کوبرنتیز علاوه بر افزونهٔ CNI نصب‌شده روی نودها برای پیاده‌سازی مدل شبکهٔ
کوبرنتیز، از محیط‌های اجرای کانتینر می‌خواهد یک رابط loopback با نام `lo` فراهم کنند که
برای هر sandbox (sandboxهای پاد، sandboxهای ماشین مجازی و ...) استفاده می‌شود.
پیاده‌سازی رابط loopback را می‌توان با استفادهٔ مجدد از
[افزونهٔ loopback در CNI.](https://github.com/containernetworking/plugins/blob/master/plugins/main/loopback/loopback.go)
یا با توسعهٔ کد اختصاصی خود برای این منظور انجام داد (به
[این مثال از CRI-O](https://github.com/cri-o/ocicni/blob/release-1.24/pkg/ocicni/util_linux.go#L91) مراجعه کنید).

### پشتیبانی از hostPort

افزونهٔ شبکهٔ CNI از `hostPort` پشتیبانی می‌کند. می‌توانید از افزونهٔ رسمی
[portmap](https://github.com/containernetworking/plugins/tree/master/plugins/meta/portmap)
که تیم افزونه‌های CNI ارائه می‌دهد استفاده کنید یا از افزونهٔ اختصاصی خود با قابلیت portMapping بهره ببرید.

اگر می‌خواهید پشتیبانی از `hostPort` را فعال کنید، باید `portMappings capability` را در
`cni-conf-dir` خود مشخص کنید. برای مثال:

```json
{
  "name": "k8s-pod-network",
  "cniVersion": "0.4.0",
  "plugins": [
    {
      "type": "calico",
      "log_level": "info",
      "datastore_type": "kubernetes",
      "nodename": "127.0.0.1",
      "ipam": {
        "type": "host-local",
        "subnet": "usePodCidr"
      },
      "policy": {
        "type": "k8s"
      },
      "kubernetes": {
        "kubeconfig": "/etc/cni/net.d/calico-kubeconfig"
      }
    },
    {
      "type": "portmap",
      "capabilities": {"portMappings": true},
      "externalSetMarkChain": "KUBE-MARK-MASQ"
    }
  ]
}
```

### پشتیبانی از شکل‌دهی ترافیک

**قابلیت آزمایشی**

افزونهٔ شبکهٔ CNI همچنین از شکل‌دهی ترافیک ورودی و خروجی پاد پشتیبانی می‌کند. می‌توانید از
افزونهٔ رسمی [bandwidth](https://github.com/containernetworking/plugins/tree/master/plugins/meta/bandwidth)
که تیم افزونه‌های CNI ارائه می‌دهد استفاده کنید یا از افزونهٔ اختصاصی خود با قابلیت کنترل پهنای باند بهره ببرید.

اگر می‌خواهید پشتیبانی از شکل‌دهی ترافیک را فعال کنید، باید افزونهٔ `bandwidth` را به فایل پیکربندی CNI
خود (به‌طور پیش‌فرض `/etc/cni/net.d`) اضافه کنید و اطمینان حاصل کنید که فایل باینری آن در دایرکتوری bin مربوط به CNI
(به‌طور پیش‌فرض `/opt/cni/bin`) قرار دارد.

```json
{
  "name": "k8s-pod-network",
  "cniVersion": "0.4.0",
  "plugins": [
    {
      "type": "calico",
      "log_level": "info",
      "datastore_type": "kubernetes",
      "nodename": "127.0.0.1",
      "ipam": {
        "type": "host-local",
        "subnet": "usePodCidr"
      },
      "policy": {
        "type": "k8s"
      },
      "kubernetes": {
        "kubeconfig": "/etc/cni/net.d/calico-kubeconfig"
      }
    },
    {
      "type": "bandwidth",
      "capabilities": {"bandwidth": true}
    }
  ]
}
```

اکنون می‌توانید حاشیه‌نویسی‌های `kubernetes.io/ingress-bandwidth` و `kubernetes.io/egress-bandwidth`
را به Pod خود اضافه کنید. برای مثال:

```yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    kubernetes.io/ingress-bandwidth: 1M
    kubernetes.io/egress-bandwidth: 1M
...
```

## {{% heading "whatsnext" %}}

- دربارهٔ [شبکهٔ کلاستر](/docs/concepts/cluster-administration/networking/) بیشتر بیاموزید
- دربارهٔ [سیاست‌های شبکه](/docs/concepts/services-networking/network-policies/) بیشتر بیاموزید
- دربارهٔ [عیب‌یابی خطاهای مرتبط با افزونهٔ CNI](/docs/tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors/) بیاموزید

