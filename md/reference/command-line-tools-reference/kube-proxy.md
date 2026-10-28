---
title: kube-proxy
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  
---


<!--
The file is auto-generated from the Go source code of the component using a generic
[generator](https://github.com/kubernetes-sigs/reference-docs/). To learn how
to generate the reference documentation, please read
[Contributing to the reference documentation](/docs/contribute/generate-ref-docs/).
To update the reference content, please follow the
[Contributing upstream](/docs/contribute/generate-ref-docs/contribute-upstream/)
guide. You can file document formatting bugs against the
[reference-docs](https://github.com/kubernetes-sigs/reference-docs/) project.
-->


## {{% heading "synopsis" %}}


پراکسی شبکه کوبرنتیز روی هر نود اجرا می‌شود. این پراکسی Serviceهای تعریف‌شده در API کوبرنتیز را روی هر نود بازتاب می‌دهد و می‌تواند ارسال ساده جریان‌های TCP، UDP و SCTP را انجام دهد یا ارسال TCP، UDP و SCTP را به‌صورت round robin میان مجموعه‌ای از بک‌اندها انجام دهد.
IPهای کلاستر و پورت‌های Service در حال حاضر از طریق متغیرهای محیطی سازگار با Docker-links پیدا می‌شوند که پورت‌های بازشده توسط پراکسی Service را مشخص می‌کنند. یک افزونه (addon) اختیاری نیز وجود دارد که DNS کلاستر را برای این IPهای کلاستر فراهم می‌کند. کاربر باید با استفاده از API سرور API (apiserver) یک Service ایجاد کند تا پراکسی را پیکربندی کند.

```
kube-proxy [flags]
```

## {{% heading "options" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--add_dir_header</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت true بودن، مسیر دایرکتوری فایل به سرایند (header) پیام‌های لاگ اضافه می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--alsologtostderr</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>لاگ‌ها علاوه بر فایل‌ها، در خروجی خطای استاندارد نیز نوشته می‌شوند (در صورت true بودن -logtostderr بی‌تأثیر است).</p></td>
</tr>

<tr>
<td colspan="2">--alsologtostderrthreshold int</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورتی که -alsologtostderr برابر true باشد، لاگ‌هایی که سطح آن‌ها برابر با این آستانه یا بالاتر از آن باشد به stderr ارسال می‌شوند (در صورت true بودن -logtostderr بی‌تأثیر است).</p></td>
</tr>

<tr>
<td colspan="2">--bind-address string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 0.0.0.0</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>برداشت kube-proxy از IP اصلی نود خود را بازنویسی می‌کند. توجه کنید که این نام یک یادگار تاریخی است و kube-proxy در واقع هیچ سوکتی را به این IP متصل (bind) نمی‌کند. در صورتی که فایل پیکربندی با --config مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--bind-address-hard-fail</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت true بودن، kube-proxy شکست در اتصال به یک پورت را خطای مهلک تلقی می‌کند و خارج می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--cleanup</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت true بودن، قوانین iptables و ipvs پاک‌سازی می‌شوند و برنامه خارج می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--cluster-cidr string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>محدوده CIDR پادهای کلاستر. (برای کلاسترهای dual-stack می‌تواند یک جفت محدوده CIDR dual-stack جداشده با کاما باشد.) وقتی --detect-local-mode روی ClusterCIDR تنظیم شده باشد، kube-proxy ترافیکی را محلی در نظر می‌گیرد که IP مبدأ آن در این محدوده باشد. (در غیر این صورت استفاده نمی‌شود.) در صورتی که فایل پیکربندی با --config مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل پیکربندی.</p></td>
</tr>

<tr>
<td colspan="2">--config-sync-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 15m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تناوب به‌روزرسانی پیکربندی دریافتی از apiserver. باید بزرگ‌تر از 0 باشد.</p></td>
</tr>

<tr>
<td colspan="2">--conntrack-max-per-core int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 32768</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشترین تعداد اتصال‌های NAT که به‌ازای هر هسته CPU ردیابی می‌شود (مقدار 0 محدودیت را بدون تغییر باقی می‌گذارد و conntrack-min را نادیده می‌گیرد).</p></td>
</tr>

<tr>
<td colspan="2">--conntrack-min int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 131072</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>کمترین تعداد ورودی‌های conntrack که صرف‌نظر از conntrack-max-per-core تخصیص داده می‌شود (برای بدون تغییر ماندن محدودیت، conntrack-max-per-core=0 را تنظیم کنید).</p></td>
</tr>

<tr>
<td colspan="2">--conntrack-tcp-be-liberal</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>با تنظیم nf_conntrack_tcp_be_liberal روی 1، حالت آسان‌گیرانه (liberal) برای ردیابی بسته‌های TCP فعال می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--conntrack-tcp-timeout-close-wait duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1h0m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مهلت NAT برای اتصال‌های TCP در وضعیت CLOSE_WAIT</p></td>
</tr>

<tr>
<td colspan="2">--conntrack-tcp-timeout-established duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 24h0m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مهلت بیکاری برای اتصال‌های TCP برقرارشده (مقدار 0 بدون تغییر باقی می‌گذارد)</p></td>
</tr>

<tr>
<td colspan="2">--conntrack-udp-timeout duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مهلت بیکاری برای اتصال‌های UDP از نوع UNREPLIED (مقدار 0 بدون تغییر باقی می‌گذارد)</p></td>
</tr>

<tr>
<td colspan="2">--conntrack-udp-timeout-stream duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مهلت بیکاری برای اتصال‌های UDP از نوع ASSURED (مقدار 0 بدون تغییر باقی می‌گذارد)</p></td>
</tr>

<tr>
<td colspan="2">--detect-local-mode LocalMode</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حالتی که برای تشخیص ترافیک محلی استفاده می‌شود. در صورتی که فایل پیکربندی با --config مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--feature-gates &lt;comma-separated 'key=True|False' pairs&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مجموعه‌ای از جفت‌های key=value که feature gateهای قابلیت‌های آلفا/آزمایشی را توصیف می‌کنند. گزینه‌ها عبارت‌اند از:<br/>APIResponseCompression=true|false (BETA - default=true)<br/>APIServerIdentity=true|false (BETA - default=true)<br/>APIServerWebhookAuthenticationToken=true|false (ALPHA - default=false)<br/>APIServingWithRoutine=true|false (ALPHA - default=false)<br/>AllAlpha=true|false (ALPHA - default=false)<br/>AllBeta=true|false (BETA - default=false)<br/>AllowParsingUserUIDFromCertAuth=true|false (BETA - default=true)<br/>AllowUnsafeMalformedObjectDeletion=true|false (BETA - default=true)<br/>AtomicFIFO=true|false (BETA - default=true)<br/>AtomicWriteVolumeUserFields=true|false (ALPHA - default=false)<br/>AuthorizePodWebsocketUpgradeCreatePermission=true|false (BETA - default=true)<br/>CBORServingAndStorage=true|false (ALPHA - default=false)<br/>CPUManagerPolicyAlphaOptions=true|false (ALPHA - default=false)<br/>CPUManagerPolicyBetaOptions=true|false (BETA - default=true)<br/>CRDObservedGenerationTracking=true|false (BETA - default=true)<br/>CRIListStreaming=true|false (ALPHA - default=false)<br/>CSIVolumeHealth=true|false (ALPHA - default=false)<br/>ClearingNominatedNodeNameAfterBinding=true|false (BETA - default=true)<br/>ClientsAllowCARotation=true|false (BETA - default=true)<br/>ClientsAllowCBOR=true|false (ALPHA - default=false)<br/>ClientsAllowTLSCacheGC=true|false (BETA - default=true)<br/>ClientsPreferCBOR=true|false (ALPHA - default=false)<br/>CloudControllerManagerWatchBasedRoutesReconciliation=true|false (ALPHA - default=false)<br/>CloudControllerManagerWebhook=true|false (ALPHA - default=false)<br/>ComponentFlagz=true|false (BETA - default=true)<br/>ComponentStatusz=true|false (BETA - default=true)<br/>CompositePodGroup=true|false (ALPHA - default=false)<br/>ConcurrentWatchObjectDecode=true|false (BETA - default=true)<br/>ConsistentListFromCacheSkipTimeoutFallback=true|false (ALPHA - default=false)<br/>ConstrainedImpersonation=true|false (BETA - default=true)<br/>ContainerCheckpoint=true|false (BETA - default=true)<br/>ContainerRestartRules=true|false (BETA - default=true)<br/>ContainerStopSignals=true|false (ALPHA - default=false)<br/>ContextualLogging=true|false (BETA - default=true)<br/>ControllerManagerReleaseLeaderElectionLockOnExit=true|false (ALPHA - default=false)<br/>CoordinatedLeaderElection=true|false (BETA - default=false)<br/>CrossNamespaceVolumeDataSource=true|false (ALPHA - default=false)<br/>DRAConsumableCapacity=true|false (BETA - default=true)<br/>DRADerivedAttributes=true|false (ALPHA - default=false)<br/>DRADeviceBindingConditions=true|false (BETA - default=true)<br/>DRADeviceCompatibilityGroups=true|false (ALPHA - default=false)<br/>DRAFractionalCapacityRange=true|false (BETA - default=false), or DRAFractionalCapacityRange=true|false (BETA - default=true) if --min-compatibility-version&gt;=1.37<br/>DRAListTypeAttributes=true|false (ALPHA - default=false)<br/>DRANodeAllocatableResources=true|false (ALPHA - default=false)<br/>DRAOptionalNodeOperations=true|false (ALPHA - default=false)<br/>DRAPartitionableDevices=true|false (BETA - default=true)<br/>DRAPartitionableDevicesType=true|false (ALPHA - default=false)<br/>DRAResourceClaimGranularStatusAuthorization=true|false (BETA - default=true)<br/>DRAResourcePoolStatus=true|false (ALPHA - default=false)<br/>DRASchedulerFilterTimeout=true|false (BETA - default=true)<br/>DRAWorkloadResourceClaims=true|false (BETA - default=false)<br/>DeclarativeValidationBeta=true|false (BETA - default=true)<br/>DefaultPodSysctls=true|false (ALPHA - default=false)<br/>DeploymentReplicaSetTerminatingReplicas=true|false (BETA - default=true)<br/>DetectCacheInconsistency=true|false (BETA - default=true)<br/>EmptyDirVolumeMode=true|false (ALPHA - default=false)<br/>EnvFiles=true|false (BETA - default=true)<br/>EtcdRangeStream=true|false (BETA - default=true)<br/>EventedPLEG=true|false (ALPHA - default=false)<br/>EvictionRequestAPI=true|false (ALPHA - default=false)<br/>ExcludeAdmissionWebhookVirtualResources=true|false (BETA - default=true)<br/>ExtendWebSocketsToKubelet=true|false (BETA - default=true)<br/>GRPCContainerProbeTLS=true|false (ALPHA - default=false)<br/>GenericWorkload=true|false (BETA - default=false)<br/>GracefulNodeShutdown=true|false (BETA - default=true)<br/>GracefulNodeShutdownBasedOnPodPriority=true|false (BETA - default=true)<br/>H2CContainerProbe=true|false (ALPHA - default=false)<br/>HPAGeneration=true|false (BETA - default=true)<br/>HPAOptimizedSelectorStore=true|false (BETA - default=true)<br/>HPAScaleToZero=true|false (BETA - default=true)<br/>HugepageAwareEviction=true|false (BETA - default=true)<br/>ImageVolumeWithDigest=true|false (ALPHA - default=false)<br/>InOrderInformersBatchProcess=true|false (BETA - default=true)<br/>InPlacePodLevelResourcesVerticalScaling=true|false (BETA - default=true)<br/>InPlacePodVerticalScalingExclusiveCPUs=true|false (ALPHA - default=false)<br/>InPlacePodVerticalScalingExclusiveMemory=true|false (ALPHA - default=false)<br/>InPlacePodVerticalScalingMemoryBackedVolumes=true|false (ALPHA - default=false)<br/>InPlacePodVerticalScalingSchedulerPreemption=true|false (ALPHA - default=false)<br/>InterPodAffinityHostnameFastPath=true|false (ALPHA - default=false)<br/>KubeProxyNFTablesLocalhostNodePorts=true|false (ALPHA - default=false)<br/>KubeletAllocatedPodsEndpoint=true|false (ALPHA - default=false)<br/>KubeletCrashLoopBackOffMax=true|false (BETA - default=true)<br/>KubeletEnsureSecretPulledImages=true|false (BETA - default=true)<br/>KubeletInUserNamespace=true|false (BETA - default=true)<br/>KubeletSeparateDiskGC=true|false (BETA - default=true)<br/>KubeletServiceAccountTokenForCredentialProviders=true|false (BETA - default=true)<br/>ListFromCacheSnapshot=true|false (BETA - default=true)<br/>LocalStorageCapacityIsolationFSQuotaMonitoring=true|false (BETA - default=false)<br/>LoggingAlphaOptions=true|false (ALPHA - default=false)<br/>LoggingBetaOptions=true|false (BETA - default=true)<br/>ManifestBasedAdmissionControlConfig=true|false (BETA - default=true)<br/>MatchLabelKeysInPodTopologySpread=true|false (BETA - default=true)<br/>MatchLabelKeysInPodTopologySpreadSelectorMerge=true|false (BETA - default=true)<br/>MaxUnavailableStatefulSet=true|false (BETA - default=true)<br/>MemoryQoS=true|false (BETA - default=true)<br/>MutablePVNodeAffinity=true|false (ALPHA - default=false)<br/>MutablePodResourcesForSuspendedJobs=true|false (BETA - default=true)<br/>MutableSchedulingDirectivesForSuspendedJobs=true|false (BETA - default=true)<br/>NFTablesNetlink=true|false (BETA - default=true)<br/>NativeHistograms=true|false (BETA - default=true)<br/>NodeControllerLeaseCircuitBreaker=true|false (BETA - default=true)<br/>NodeLifecycleConditions=true|false (ALPHA - default=false)<br/>NominatedNodeNameForExpectation=true|false (BETA - default=true)<br/>OpenAPIEnums=true|false (BETA - default=true)<br/>OpportunisticBatching=true|false (BETA - default=true)<br/>PersistentVolumeClaimUnusedSinceTime=true|false (BETA - default=true)<br/>PodAndContainerStatsFromCRI=true|false (BETA - default=false)<br/>PodDeletionCost=true|false (BETA - default=true)<br/>PodGroupPreemptionPolicy=true|false (ALPHA - default=false)<br/>PodLevelResourceManagers=true|false (BETA - default=false)<br/>PodLevelResources=true|false (BETA - default=true)<br/>PodLevelResourcesFixDefaulting=true|false (BETA - default=true)<br/>PodLevelResourcesFixKubeletQOSClass=true|false (BETA - default=true)<br/>PodLogsQuerySplitStreams=true|false (ALPHA - default=false)<br/>PodTopologyLabelsAdmission=true|false (BETA - default=true)<br/>PodsAPI=true|false (BETA - default=true)<br/>PortForwardWebsockets=true|false (BETA - default=true)<br/>QOSReserved=true|false (ALPHA - default=false)<br/>ReduceDefaultCrashLoopBackOffDecay=true|false (ALPHA - default=false)<br/>ReloadKubeletClientCAFile=true|false (BETA - default=true)<br/>ReloadKubeletServerCertificateFile=true|false (BETA - default=true)<br/>RemoteRequestHeaderUID=true|false (BETA - default=true)<br/>ResourceHealthStatus=true|false (BETA - default=true)<br/>ResourceHealthStatusMessage=true|false (BETA - default=true)<br/>RestartAllContainersOnContainerExits=true|false (BETA - default=true)<br/>RotateKubeletServerCertificate=true|false (BETA - default=true)<br/>RuntimeClassInImageCriApi=true|false (ALPHA - default=false)<br/>SchedulerAsyncAPICalls=true|false (BETA - default=false)<br/>SchedulerAsyncPreemption=true|false (BETA - default=true)<br/>SchedulerPopFromBackoffQ=true|false (BETA - default=true)<br/>SchedulerPreQueueingHints=true|false (ALPHA - default=false)<br/>ServiceAccountNodeAudienceRestriction=true|false (BETA - default=true)<br/>ShardedListAndWatch=true|false (ALPHA - default=false)<br/>SizeBasedListCostEstimate=true|false (BETA - default=true)<br/>StaleControllerConsistencyDaemonSet=true|false (BETA - default=true)<br/>StaleControllerConsistencyHPA=true|false (BETA - default=true)<br/>StaleControllerConsistencyJob=true|false (BETA - default=true)<br/>StaleControllerConsistencyReplicaSet=true|false (BETA - default=true)<br/>StaleControllerConsistencyStatefulSet=true|false (BETA - default=true)<br/>StatefulSetRecreateStrategy=true|false (ALPHA - default=false)<br/>StatefulSetSemanticRevisionComparison=true|false (BETA - default=true)<br/>StorageCapacityScoring=true|false (BETA - default=true)<br/>StorageVersionAPI=true|false (ALPHA - default=false)<br/>StorageVersionHash=true|false (BETA - default=true)<br/>StrictIPCIDRValidation=true|false (BETA - default=true)<br/>StructuredAuthenticationConfigurationEgressSelector=true|false (BETA - default=true)<br/>StructuredAuthenticationConfigurationJWKSMetrics=true|false (BETA - default=true)<br/>TaintTolerationComparisonOperators=true|false (ALPHA - default=false)<br/>TokenRequestServiceAccountUIDValidation=true|false (BETA - default=true)<br/>TopologyAwareWorkloadScheduling=true|false (ALPHA - default=false)<br/>TopologyManagerPolicyAlphaOptions=true|false (ALPHA - default=false)<br/>TopologyManagerPolicyBetaOptions=true|false (BETA - default=true)<br/>TranslateStreamCloseWebsocketRequests=true|false (BETA - default=true)<br/>UnauthenticatedHTTP2DOSMitigation=true|false (BETA - default=true)<br/>UnknownVersionInteroperabilityProxy=true|false (BETA - default=true)<br/>UnlockWhileProcessingFIFO=true|false (BETA - default=true)<br/>UserNamespacesHostNetworkSupport=true|false (ALPHA - default=false)<br/>VolumeBindMountOptions=true|false (ALPHA - default=false)<br/>VolumeLimitScaling=true|false (BETA - default=true)<br/>WatchList=true|false (BETA - default=true)<br/>WatchListClient=true|false (BETA - default=true)<br/>WatchListCompression=true|false (BETA - default=true)<br/>WebhookRoundTripLoadBalancing=true|false (BETA - default=true)<br/>WindowsCPUAndMemoryAffinity=true|false (ALPHA - default=false)<br/>WindowsGracefulNodeShutdown=true|false (BETA - default=true)<br/>WorkloadWithJob=true|false (ALPHA - default=false)<br/>در صورتی که فایل پیکربندی با --config مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--healthz-bind-address ipport&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 0.0.0.0:10256</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>آدرس IP و پورتی که سرور بررسی سلامت (health check) روی آن سرویس می‌دهد؛ مقدار پیش‌فرض &quot;0.0.0.0:10256&quot; است. در صورتی که فایل پیکربندی با --config مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای kube-proxy</p></td>
</tr>

<tr>
<td colspan="2">--hostname-override string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت غیرخالی بودن، به‌عنوان نام Node‌ای که kube-proxy روی آن اجرا می‌شود استفاده می‌گردد. در صورت تنظیم نشدن، فرض می‌شود نام نود با نام میزبان (hostname) آن یکسان است.</p></td>
</tr>

<tr>
<td colspan="2">--init-only</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت true بودن، هر گام راه‌اندازی اولیه‌ای که باید با دسترسی کامل root انجام شود اجرا می‌شود و سپس برنامه خارج می‌شود. پس از این کار، می‌توانید kube-proxy را دوباره و تنها با قابلیت (capability) CAP_NET_ADMIN اجرا کنید.</p></td>
</tr>

<tr>
<td colspan="2">--iptables-localhost-nodeports&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت false بودن، kube-proxy رفتار قدیمی (legacy) مجاز بودن دسترسی به سرویس‌های NodePort از طریق localhost را غیرفعال می‌کند. (فقط در حالت iptables و برای IPv4 اعمال می‌شود؛ NodePortهای localhost در سایر حالت‌های پروکسی یا با IPv6 هرگز مجاز نیستند.)</p></td>
</tr>

<tr>
<td colspan="2">--iptables-masquerade-bit int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 14</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت استفاده از حالت پروکسی iptables یا ipvs، بیتی از فضای fwmark که بسته‌های نیازمند SNAT با آن علامت‌گذاری می‌شوند. باید در بازه [0, 31] باشد.</p></td>
</tr>

<tr>
<td colspan="2">--iptables-min-sync-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>کمترین فاصله زمانی میان همگام‌سازی‌های مجدد قوانین iptables (برای مثال '5s'، '1m'، '2h22m'). مقدار 0 به این معناست که هر تغییر در Service یا EndpointSlice بلافاصله به یک همگام‌سازی مجدد iptables منجر می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--iptables-sync-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 30s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فاصله زمانی (برای مثال '5s'، '1m'، '2h22m') که نشان می‌دهد عملیات مختلف همگام‌سازی مجدد و پاک‌سازی هر چند وقت یک بار انجام می‌شوند. باید بزرگ‌تر از 0 باشد.</p></td>
</tr>

<tr>
<td colspan="2">--ipvs-exclude-cidrs strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از CIDRها، جداشده با کاما، که ipvs proxier هنگام پاک‌سازی قوانین IPVS نباید به آن‌ها دست بزند.</p></td>
</tr>

<tr>
<td colspan="2">--ipvs-min-sync-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>کمترین فاصله زمانی میان همگام‌سازی‌های مجدد قوانین IPVS (برای مثال '5s'، '1m'، '2h22m'). مقدار 0 به این معناست که هر تغییر در Service یا EndpointSlice بلافاصله به یک همگام‌سازی مجدد IPVS منجر می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--ipvs-scheduler string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوع زمان‌بند ipvs در زمانی که حالت پروکسی ipvs است</p></td>
</tr>

<tr>
<td colspan="2">--ipvs-strict-arp</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>با تنظیم arp_ignore روی 1 و arp_announce روی 2، ARP سخت‌گیرانه (strict ARP) فعال می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--ipvs-sync-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 30s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بازه‌ای زمانی (مثلاً '5s'، '1m'، '2h22m') که مشخص می‌کند عملیات مختلف همگام‌سازی مجدد و پاک‌سازی هر چند وقت یک‌بار انجام شوند. مقدار آن باید بزرگ‌تر از 0 باشد.</p></td>
</tr>

<tr>
<td colspan="2">--ipvs-tcp-timeout duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مهلت زمانی برای اتصال‌های TCP بیکار در IPVS؛ مقدار 0 مقدار فعلی را بدون تغییر نگه می‌دارد. (مثلاً '5s'، '1m'، '2h22m').</p></td>
</tr>

<tr>
<td colspan="2">--ipvs-tcpfin-timeout duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مهلت زمانی برای اتصال‌های TCP در IPVS پس از دریافت بسته FIN؛ مقدار 0 مقدار فعلی را بدون تغییر نگه می‌دارد. (مثلاً '5s'، '1m'، '2h22m').</p></td>
</tr>

<tr>
<td colspan="2">--ipvs-udp-timeout duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مهلت زمانی برای بسته‌های UDP در IPVS؛ مقدار 0 مقدار فعلی را بدون تغییر نگه می‌دارد. (مثلاً '5s'، '1m'، '2h22m').</p></td>
</tr>

<tr>
<td colspan="2">--kube-api-burst int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار burst که هنگام ارتباط با apiserver کوبرنتیز استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--kube-api-content-type string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "application/vnd.kubernetes.protobuf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوع محتوای درخواست‌هایی که به apiserver ارسال می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--kube-api-qps float&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار QPS که هنگام ارتباط با apiserver کوبرنتیز استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kubeconfig حاوی اطلاعات احراز هویت و مجوزدهی (نشانی master را می‌توان با پرچم master بازنویسی کرد).</p></td>
</tr>

<tr>
<td colspan="2">--legacy_stderr_threshold_behavior&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، در حالتی که logtostderr=true است، stderrthreshold نادیده گرفته می‌شود (رفتار قدیمی). اگر false باشد، stderrthreshold حتی زمانی که logtostderr=true است نیز اعمال می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--log-flush-frequency duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر تعداد ثانیه‌های بین دو بار تخلیه (flush) لاگ‌ها</p></td>
</tr>

<tr>
<td colspan="2">--log-text-info-buffer-size quantity</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>[آلفا] در قالب متنی با جریان‌های خروجی جداشده، پیام‌های اطلاعاتی را می‌توان برای مدتی بافر کرد تا کارایی افزایش یابد. مقدار پیش‌فرض صفر بایت است که بافر کردن را غیرفعال می‌کند. اندازه را می‌توان به‌صورت تعداد بایت (512)، مضرب‌هایی از 1000 (1K)، مضرب‌هایی از 1024 (2Ki) یا توان‌های آن‌ها (3M، 4G، 5Mi، 6Gi) مشخص کرد. برای استفاده از این گزینه، feature gate با نام LoggingAlphaOptions را فعال کنید.</p></td>
</tr>

<tr>
<td colspan="2">--log-text-split-stream</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>[آلفا] در قالب متنی، پیام‌های خطا را در stderr و پیام‌های اطلاعاتی را در stdout می‌نویسد. به‌طور پیش‌فرض یک جریان واحد در stdout نوشته می‌شود. برای استفاده از این گزینه، feature gate با نام LoggingAlphaOptions را فعال کنید.</p></td>
</tr>

<tr>
<td colspan="2">--log_backtrace_at &lt;a string in the form 'file:N'&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: :0</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هنگامی که لاگ‌گذاری به خط file:N برسد، یک stack trace تولید می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--log_dir string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر خالی نباشد، فایل‌های لاگ در این دایرکتوری نوشته می‌شوند (در صورت logtostderr=true بی‌اثر است)</p></td>
</tr>

<tr>
<td colspan="2">--log_file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر خالی نباشد، از این فایل لاگ استفاده می‌شود (در صورت logtostderr=true بی‌اثر است)</p></td>
</tr>

<tr>
<td colspan="2">--log_file_max_size uint&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1800</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر اندازه‌ای را که یک فایل لاگ می‌تواند به آن برسد تعیین می‌کند (در صورت logtostderr=true بی‌اثر است). واحد آن مگابایت است. اگر مقدار 0 باشد، حداکثر اندازه فایل نامحدود است.</p></td>
</tr>

<tr>
<td colspan="2">--logging-format string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "text"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>قالب لاگ را تعیین می‌کند. قالب‌های مجاز: &quot;text&quot;.</p></td>
</tr>

<tr>
<td colspan="2">--logtostderr&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>لاگ‌ها به‌جای فایل‌ها در خروجی خطای استاندارد نوشته می‌شوند</p></td>
</tr>

<tr>
<td colspan="2">--masquerade-all</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>برای تمام ترافیکی که از طریق IPهای کلاستر Service ارسال می‌شود، SNAT انجام می‌دهد. ممکن است در برخی افزونه‌های CNI لازم باشد. فقط در لینوکس پشتیبانی می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--master string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی سرور API کوبرنتیز (هر مقدار موجود در kubeconfig را بازنویسی می‌کند)</p></td>
</tr>

<tr>
<td colspan="2">--metrics-bind-address ipport&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 127.0.0.1:10249</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی IP و پورتی که سرور متریک‌ها روی آن سرویس‌دهی می‌کند؛ مقدار پیش‌فرض &quot;127.0.0.1:10249&quot; است. (برای اتصال به همه اینترفیس‌ها، آن را روی &quot;0.0.0.0:10249&quot; / &quot;[::]:10249&quot; تنظیم کنید.) اگر فایل پیکربندی با --config مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--nodeport-addresses strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از محدوده‌های CIDR و/یا کلیدواژه‌هایی که به محدوده‌های CIDR گسترش می‌یابند. سرویس‌های NodePort فقط روی IPهای نودی که در این فهرست قرار می‌گیرند در دسترس هستند. کلیدواژه‌های پشتیبانی‌شده: 'primary' (نشانی‌های IPv4 و/یا IPv6 اصلی آبجکت Node)، 'localhost' (127.0.0.0/8 و ::1/128) و 'all' (0.0.0.0/0 و ::/0). هر ترکیبی از کلیدواژه‌ها و CIDRهای معتبر را می‌توان در فهرست قرار داد. سرویس‌دهی NodePortها روی IPهای loopback فقط در حالت iptables پشتیبانی می‌شود (فقط IPv4، به --iptables-localhost-nodeports مراجعه کنید)، و فقط برای TCP در حالت nftables، زمانی که feature gate با نام KubeProxyNFTablesLocalhostNodePorts فعال باشد و فهرست به‌صراحت loopback را شامل شود (مثلاً 'localhost'). اگر تنظیم نشود، مقدار پیش‌فرض در حالت‌های iptables و ipvs برابر 'all' و در حالت nftables برابر 'primary' است. اگر فایل پیکربندی با --config مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--one_output</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، لاگ‌ها فقط در سطح شدت اصلی خود نوشته می‌شوند (به‌جای نوشته شدن در هر سطح شدت پایین‌تر نیز؛ در صورت logtostderr=true بی‌اثر است)</p></td>
</tr>

<tr>
<td colspan="2">--oom-score-adj int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: -999</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار oom-score-adj برای فرایند kube-proxy. مقادیر باید در بازه [-1000, 1000] باشند. اگر فایل پیکربندی با --config مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--pod-bridge-interface string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام یک اینترفیس bridge. زمانی که --detect-local-mode روی BridgeInterface تنظیم شده باشد، kube-proxy ترافیکی را که از این bridge سرچشمه بگیرد محلی در نظر می‌گیرد.</p></td>
</tr>

<tr>
<td colspan="2">--pod-interface-name-prefix string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پیشوند نام اینترفیس. زمانی که --detect-local-mode روی InterfaceNamePrefix تنظیم شده باشد، kube-proxy ترافیکی را که از هر اینترفیسی با نامی که با این پیشوند آغاز می‌شود سرچشمه بگیرد محلی در نظر می‌گیرد.</p></td>
</tr>

<tr>
<td colspan="2">--profiling</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، پروفایل‌گیری از طریق رابط وب روی handler با مسیر /debug/pprof فعال می‌شود. اگر فایل پیکربندی با --config مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--proxy-mode ProxyMode</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حالت پراکسی مورد استفاده: در لینوکس می‌تواند 'iptables' (پیش‌فرض)، 'ipvs' یا 'nftables' باشد. در ویندوز تنها مقدار پشتیبانی‌شده 'kernelspace' است. اگر فایل پیکربندی با --config مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--show-hidden-metrics-for-version string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخه قبلی که می‌خواهید متریک‌های پنهان‌شده آن نمایش داده شوند. فقط نسخه فرعی (minor) قبلی معنا دارد و مقادیر دیگر پذیرفته نمی‌شوند. قالب آن &lt;major&gt;.&lt;minor&gt; است، مثلاً: '1.16'. هدف از این قالب آن است که اگر انتشار بعدی متریک‌های بیشتری را پنهان کرد، فرصت داشته باشید متوجه شوید و هنگام حذف دائمی آن‌ها در انتشار پس از آن غافلگیر نشوید. اگر فایل پیکربندی با --config مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--skip_headers</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، از افزودن پیشوند سرصفحه (header) به پیام‌های لاگ خودداری می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--skip_log_headers</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هنگام باز کردن فایل‌های لاگ از نوشتن سرصفحه‌ها خودداری می‌شود (در صورت logtostderr=true بی‌اثر است)</p></td>
</tr>

<tr>
<td colspan="2">--stderrthreshold int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 2</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>لاگ‌هایی که در این آستانه یا بالاتر از آن باشند، هنگام نوشتن همزمان در فایل‌ها و stderr به stderr ارسال می‌شوند (در صورت logtostderr=true یا alsologtostderr=true بی‌اثر است، مگر آنکه legacy_stderr_threshold_behavior=false باشد)</p></td>
</tr>

<tr>
<td colspan="2">-v, --v int</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>عددی برای سطح جزئیات (verbosity) لاگ</p></td>
</tr>

<tr>
<td colspan="2">--version version[=true]</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>--version و --version=raw اطلاعات نسخه را چاپ کرده و خارج می‌شوند؛ --version=vX.Y.Z... نسخه گزارش‌شده را تنظیم می‌کند</p></td>
</tr>

<tr>
<td colspan="2">--vmodule pattern=N,...</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی جداشده با کاما از تنظیمات pattern=N برای لاگ‌گذاری فیلترشده بر اساس فایل (فقط برای قالب لاگ متنی کار می‌کند)</p></td>
</tr>

<tr>
<td colspan="2">--write-config-to string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر تنظیم شود، مقادیر پیش‌فرض پیکربندی را در این فایل می‌نویسد و خارج می‌شود.</p></td>
</tr>

</tbody>
</table>
