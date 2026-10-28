---
title: kube-scheduler
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


زمان‌بند کوبرنتیز یک فرایند control plane است که Podها را به نودها اختصاص می‌دهد. زمان‌بند بر اساس محدودیت‌ها و منابع در دسترس مشخص می‌کند که کدام نودها برای قرار گرفتن هر Pod موجود در صف زمان‌بندی معتبر هستند. سپس زمان‌بند هر نود معتبر را رتبه‌بندی می‌کند و Pod را به نود مناسب متصل (bind) می‌کند. در یک کلاستر می‌توان از چند زمان‌بند مختلف استفاده کرد؛ kube-scheduler پیاده‌سازی مرجع است.
برای اطلاعات بیشتر درباره زمان‌بندی و مؤلفه kube-scheduler به [زمان‌بندی](https://kubernetes.io/docs/concepts/scheduling-eviction/) مراجعه کنید.

```
kube-scheduler [flags]
```

## {{% heading "options" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--allow-metric-labels stringToString&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: []</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نگاشتی از برچسب متریک (metric label) به فهرست مقادیر مجاز آن برچسب. قالب کلید به صورت &lt;MetricName&gt;,&lt;LabelName&gt; است. قالب مقدار به صورت &lt;allowed_value&gt;,&lt;allowed_value&gt;... است؛ برای مثال: metric1,label1='v1,v2,v3', metric1,label2='v1,v2,v3' metric2,label1='v1,v2,v3'.</p></td>
</tr>

<tr>
<td colspan="2">--allow-metric-labels-manifest string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل مانیفستی که نگاشت فهرست مجاز را در بر دارد. قالب این فایل مشابه قالب پرچم --allow-metric-labels است، یعنی:<br/>allowListMapping:<br/>&quot;metric1,label1&quot;: &quot;value11,value12&quot;<br/>&quot;metric2,label2&quot;: &quot;&quot;<br/>توجه کنید که پرچم --allow-metric-labels بر فایل مانیفست اولویت دارد و آن را بازنویسی می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--authentication-kubeconfig string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig که به سرور «core» کوبرنتیز اشاره می‌کند و دسترسی کافی برای ایجاد tokenreviews.authentication.k8s.io را دارد. این گزینه اختیاری است. اگر خالی باشد، همه درخواست‌های توکن ناشناس در نظر گرفته می‌شوند و هیچ CA کلاینتی در کلاستر جست‌وجو نمی‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--authentication-skip-lookup</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر false باشد، از authentication-kubeconfig برای جست‌وجوی پیکربندی احراز هویت مفقود در کلاستر استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--authentication-token-webhook-cache-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان نگهداری پاسخ‌های احراز‌کننده هویت توکن مبتنی بر webhook در حافظه نهان.</p></td>
</tr>

<tr>
<td colspan="2">--authentication-tolerate-lookup-failure&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، شکست در جست‌وجوی پیکربندی احراز هویت مفقود از کلاستر، خطای مهلک تلقی نمی‌شود. توجه کنید که این امر می‌تواند به احراز هویتی منجر شود که همه درخواست‌ها را ناشناس در نظر می‌گیرد.</p></td>
</tr>

<tr>
<td colspan="2">--authorization-always-allow-paths strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "/healthz,/readyz,/livez"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از مسیرهای HTTP که در هنگام اعطای مجوز نادیده گرفته می‌شوند؛ یعنی این مسیرها بدون تماس با سرور «core» کوبرنتیز مجاز شمرده می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--authorization-kubeconfig string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig که به سرور «core» کوبرنتیز اشاره می‌کند و دسترسی کافی برای ایجاد subjectaccessreviews.authorization.k8s.io را دارد. این گزینه اختیاری است. اگر خالی باشد، همه درخواست‌هایی که از اعطای مجوز مستثنا نشده‌اند ممنوع می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--authorization-webhook-cache-authorized-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان نگهداری پاسخ‌های «مجاز» از مجوزدهنده webhook در حافظه نهان.</p></td>
</tr>

<tr>
<td colspan="2">--authorization-webhook-cache-unauthorized-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان نگهداری پاسخ‌های «غیرمجاز» از مجوزدهنده webhook در حافظه نهان.</p></td>
</tr>

<tr>
<td colspan="2">--bind-address string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 0.0.0.0</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی IP که برای پورت --secure-port روی آن گوش داده می‌شود. رابط‌های مرتبط باید برای سایر بخش‌های کلاستر و همچنین برای کلاینت‌های CLI/وب در دسترس باشند. اگر خالی یا یک نشانی نامشخص (0.0.0.0 یا ::) باشد، همه رابط‌ها و خانواده‌های نشانی IP استفاده می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--cert-dir string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری‌ای که گواهی‌های TLS در آن قرار دارند. اگر --tls-cert-file و --tls-private-key-file مشخص شده باشند، این پرچم نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--client-ca-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر تنظیم شود، هر درخواستی که گواهی کلاینتی ارائه کند که توسط یکی از مراجع موجود در client-ca-file امضا شده باشد، با هویتی متناظر با CommonName گواهی کلاینت احراز هویت می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل پیکربندی.</p></td>
</tr>

<tr>
<td colspan="2">--contention-profiling&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>منسوخ‌شده: در صورت فعال بودن پروفایل‌گیری، block profiling را فعال می‌کند. اگر فایل پیکربندی در --config مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--disable-http2-serving</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، سرویس‌دهی HTTP2 غیرفعال می‌شود [پیش‌فرض=false]</p></td>
</tr>

<tr>
<td colspan="2">--disabled-metrics strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>این پرچم راهی اضطراری برای متریک‌های پرمشکل فراهم می‌کند. برای غیرفعال کردن یک متریک باید نام کاملاً مشخص (fully qualified) آن را وارد کنید. توجه: اولویت غیرفعال کردن متریک‌ها از نمایش متریک‌های پنهان بالاتر است.</p></td>
</tr>

<tr>
<td colspan="2">--emulated-version strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخه‌هایی که اجزای مختلف قابلیت‌های خود (APIها، ویژگی‌ها و ...) را بر اساس آن شبیه‌سازی می‌کنند.<br/>در صورت تنظیم، جزء مورد نظر به‌جای نسخه باینری زیرین، رفتار این نسخه را شبیه‌سازی می‌کند.<br/>قالب نسخه فقط می‌تواند major.minor باشد، برای مثال: '--emulated-version=wardle=1.2,kube=1.31'.<br/>گزینه‌ها: kube=1.34..1.37(پیش‌فرض:1.37)<br/>اگر جزء مشخص نشود، به‌طور پیش‌فرض &quot;kube&quot; در نظر گرفته می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--feature-gates colonSeparatedMultimapStringString</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی جداشده با ویرگول از جفت‌های component:key=value که feature gateهای ویژگی‌های آلفا/آزمایشی اجزای مختلف را توصیف می‌کنند.<br/>اگر جزء مشخص نشود، به‌طور پیش‌فرض &quot;kube&quot; در نظر گرفته می‌شود. این پرچم را می‌توان چندین بار به کار برد. برای مثال: --feature-gates 'wardle:featureA=true,wardle:featureB=false' --feature-gates 'kube:featureC=true'. گزینه‌ها:<br/>kube:APIResponseCompression=true|false (BETA - default=true)<br/>kube:APIServerIdentity=true|false (BETA - default=true)<br/>kube:APIServerWebhookAuthenticationToken=true|false (ALPHA - default=false)<br/>kube:APIServingWithRoutine=true|false (ALPHA - default=false)<br/>kube:AllAlpha=true|false (ALPHA - default=false)<br/>kube:AllBeta=true|false (BETA - default=false)<br/>kube:AllowParsingUserUIDFromCertAuth=true|false (BETA - default=true)<br/>kube:AllowUnsafeMalformedObjectDeletion=true|false (BETA - default=true)<br/>kube:AtomicFIFO=true|false (BETA - default=true)<br/>kube:AtomicWriteVolumeUserFields=true|false (ALPHA - default=false)<br/>kube:AuthorizePodWebsocketUpgradeCreatePermission=true|false (BETA - default=true)<br/>kube:CBORServingAndStorage=true|false (ALPHA - default=false)<br/>kube:CPUManagerPolicyAlphaOptions=true|false (ALPHA - default=false)<br/>kube:CPUManagerPolicyBetaOptions=true|false (BETA - default=true)<br/>kube:CRDObservedGenerationTracking=true|false (BETA - default=true)<br/>kube:CRIListStreaming=true|false (ALPHA - default=false)<br/>kube:CSIVolumeHealth=true|false (ALPHA - default=false)<br/>kube:ClearingNominatedNodeNameAfterBinding=true|false (BETA - default=true)<br/>kube:ClientsAllowCARotation=true|false (BETA - default=true)<br/>kube:ClientsAllowCBOR=true|false (ALPHA - default=false)<br/>kube:ClientsAllowTLSCacheGC=true|false (BETA - default=true)<br/>kube:ClientsPreferCBOR=true|false (ALPHA - default=false)<br/>kube:CloudControllerManagerWatchBasedRoutesReconciliation=true|false (ALPHA - default=false)<br/>kube:CloudControllerManagerWebhook=true|false (ALPHA - default=false)<br/>kube:ComponentFlagz=true|false (BETA - default=true)<br/>kube:ComponentStatusz=true|false (BETA - default=true)<br/>kube:CompositePodGroup=true|false (ALPHA - default=false)<br/>kube:ConcurrentWatchObjectDecode=true|false (BETA - default=true)<br/>kube:ConsistentListFromCacheSkipTimeoutFallback=true|false (ALPHA - default=false)<br/>kube:ConstrainedImpersonation=true|false (BETA - default=true)<br/>kube:ContainerCheckpoint=true|false (BETA - default=true)<br/>kube:ContainerRestartRules=true|false (BETA - default=true)<br/>kube:ContainerStopSignals=true|false (ALPHA - default=false)<br/>kube:ContextualLogging=true|false (BETA - default=true)<br/>kube:ControllerManagerReleaseLeaderElectionLockOnExit=true|false (ALPHA - default=false)<br/>kube:CoordinatedLeaderElection=true|false (BETA - default=false)<br/>kube:CrossNamespaceVolumeDataSource=true|false (ALPHA - default=false)<br/>kube:DRAConsumableCapacity=true|false (BETA - default=true)<br/>kube:DRADerivedAttributes=true|false (ALPHA - default=false)<br/>kube:DRADeviceBindingConditions=true|false (BETA - default=true)<br/>kube:DRADeviceCompatibilityGroups=true|false (ALPHA - default=false)<br/>kube:DRAFractionalCapacityRange=true|false (BETA - default=false), or DRAFractionalCapacityRange=true|false (BETA - default=true) if --min-compatibility-version&gt;=1.37<br/>kube:DRAListTypeAttributes=true|false (ALPHA - default=false)<br/>kube:DRANodeAllocatableResources=true|false (ALPHA - default=false)<br/>kube:DRAOptionalNodeOperations=true|false (ALPHA - default=false)<br/>kube:DRAPartitionableDevices=true|false (BETA - default=true)<br/>kube:DRAPartitionableDevicesType=true|false (ALPHA - default=false)<br/>kube:DRAResourceClaimGranularStatusAuthorization=true|false (BETA - default=true)<br/>kube:DRAResourcePoolStatus=true|false (ALPHA - default=false)<br/>kube:DRASchedulerFilterTimeout=true|false (BETA - default=true)<br/>kube:DRAWorkloadResourceClaims=true|false (BETA - default=false)<br/>kube:DeclarativeValidationBeta=true|false (BETA - default=true)<br/>kube:DefaultPodSysctls=true|false (ALPHA - default=false)<br/>kube:DeploymentReplicaSetTerminatingReplicas=true|false (BETA - default=true)<br/>kube:DetectCacheInconsistency=true|false (BETA - default=true)<br/>kube:EmptyDirVolumeMode=true|false (ALPHA - default=false)<br/>kube:EnvFiles=true|false (BETA - default=true)<br/>kube:EtcdRangeStream=true|false (BETA - default=true)<br/>kube:EventedPLEG=true|false (ALPHA - default=false)<br/>kube:EvictionRequestAPI=true|false (ALPHA - default=false)<br/>kube:ExcludeAdmissionWebhookVirtualResources=true|false (BETA - default=true)<br/>kube:ExtendWebSocketsToKubelet=true|false (BETA - default=true)<br/>kube:GRPCContainerProbeTLS=true|false (ALPHA - default=false)<br/>kube:GenericWorkload=true|false (BETA - default=false)<br/>kube:GracefulNodeShutdown=true|false (BETA - default=true)<br/>kube:GracefulNodeShutdownBasedOnPodPriority=true|false (BETA - default=true)<br/>kube:H2CContainerProbe=true|false (ALPHA - default=false)<br/>kube:HPAGeneration=true|false (BETA - default=true)<br/>kube:HPAOptimizedSelectorStore=true|false (BETA - default=true)<br/>kube:HPAScaleToZero=true|false (BETA - default=true)<br/>kube:HugepageAwareEviction=true|false (BETA - default=true)<br/>kube:ImageVolumeWithDigest=true|false (ALPHA - default=false)<br/>kube:InOrderInformersBatchProcess=true|false (BETA - default=true)<br/>kube:InPlacePodLevelResourcesVerticalScaling=true|false (BETA - default=true)<br/>kube:InPlacePodVerticalScalingExclusiveCPUs=true|false (ALPHA - default=false)<br/>kube:InPlacePodVerticalScalingExclusiveMemory=true|false (ALPHA - default=false)<br/>kube:InPlacePodVerticalScalingMemoryBackedVolumes=true|false (ALPHA - default=false)<br/>kube:InPlacePodVerticalScalingSchedulerPreemption=true|false (ALPHA - default=false)<br/>kube:InterPodAffinityHostnameFastPath=true|false (ALPHA - default=false)<br/>kube:KubeProxyNFTablesLocalhostNodePorts=true|false (ALPHA - default=false)<br/>kube:KubeletAllocatedPodsEndpoint=true|false (ALPHA - default=false)<br/>kube:KubeletCrashLoopBackOffMax=true|false (BETA - default=true)<br/>kube:KubeletEnsureSecretPulledImages=true|false (BETA - default=true)<br/>kube:KubeletInUserNamespace=true|false (BETA - default=true)<br/>kube:KubeletSeparateDiskGC=true|false (BETA - default=true)<br/>kube:KubeletServiceAccountTokenForCredentialProviders=true|false (BETA - default=true)<br/>kube:ListFromCacheSnapshot=true|false (BETA - default=true)<br/>kube:LocalStorageCapacityIsolationFSQuotaMonitoring=true|false (BETA - default=false)<br/>kube:LoggingAlphaOptions=true|false (ALPHA - default=false)<br/>kube:LoggingBetaOptions=true|false (BETA - default=true)<br/>kube:ManifestBasedAdmissionControlConfig=true|false (BETA - default=true)<br/>kube:MatchLabelKeysInPodTopologySpread=true|false (BETA - default=true)<br/>kube:MatchLabelKeysInPodTopologySpreadSelectorMerge=true|false (BETA - default=true)<br/>kube:MaxUnavailableStatefulSet=true|false (BETA - default=true)<br/>kube:MemoryQoS=true|false (BETA - default=true)<br/>kube:MutablePVNodeAffinity=true|false (ALPHA - default=false)<br/>kube:MutablePodResourcesForSuspendedJobs=true|false (BETA - default=true)<br/>kube:MutableSchedulingDirectivesForSuspendedJobs=true|false (BETA - default=true)<br/>kube:NFTablesNetlink=true|false (BETA - default=true)<br/>kube:NativeHistograms=true|false (BETA - default=true)<br/>kube:NodeControllerLeaseCircuitBreaker=true|false (BETA - default=true)<br/>kube:NodeLifecycleConditions=true|false (ALPHA - default=false)<br/>kube:NominatedNodeNameForExpectation=true|false (BETA - default=true)<br/>kube:OpenAPIEnums=true|false (BETA - default=true)<br/>kube:OpportunisticBatching=true|false (BETA - default=true)<br/>kube:PersistentVolumeClaimUnusedSinceTime=true|false (BETA - default=true)<br/>kube:PodAndContainerStatsFromCRI=true|false (BETA - default=false)<br/>kube:PodDeletionCost=true|false (BETA - default=true)<br/>kube:PodGroupPreemptionPolicy=true|false (ALPHA - default=false)<br/>kube:PodLevelResourceManagers=true|false (BETA - default=false)<br/>kube:PodLevelResources=true|false (BETA - default=true)<br/>kube:PodLevelResourcesFixDefaulting=true|false (BETA - default=true)<br/>kube:PodLevelResourcesFixKubeletQOSClass=true|false (BETA - default=true)<br/>kube:PodLogsQuerySplitStreams=true|false (ALPHA - default=false)<br/>kube:PodTopologyLabelsAdmission=true|false (BETA - default=true)<br/>kube:PodsAPI=true|false (BETA - default=true)<br/>kube:PortForwardWebsockets=true|false (BETA - default=true)<br/>kube:QOSReserved=true|false (ALPHA - default=false)<br/>kube:ReduceDefaultCrashLoopBackOffDecay=true|false (ALPHA - default=false)<br/>kube:ReloadKubeletClientCAFile=true|false (BETA - default=true)<br/>kube:ReloadKubeletServerCertificateFile=true|false (BETA - default=true)<br/>kube:RemoteRequestHeaderUID=true|false (BETA - default=true)<br/>kube:ResourceHealthStatus=true|false (BETA - default=true)<br/>kube:ResourceHealthStatusMessage=true|false (BETA - default=true)<br/>kube:RestartAllContainersOnContainerExits=true|false (BETA - default=true)<br/>kube:RotateKubeletServerCertificate=true|false (BETA - default=true)<br/>kube:RuntimeClassInImageCriApi=true|false (ALPHA - default=false)<br/>kube:SchedulerAsyncAPICalls=true|false (BETA - default=false)<br/>kube:SchedulerAsyncPreemption=true|false (BETA - default=true)<br/>kube:SchedulerPopFromBackoffQ=true|false (BETA - default=true)<br/>kube:SchedulerPreQueueingHints=true|false (ALPHA - default=false)<br/>kube:ServiceAccountNodeAudienceRestriction=true|false (BETA - default=true)<br/>kube:ShardedListAndWatch=true|false (ALPHA - default=false)<br/>kube:SizeBasedListCostEstimate=true|false (BETA - default=true)<br/>kube:StaleControllerConsistencyDaemonSet=true|false (BETA - default=true)<br/>kube:StaleControllerConsistencyHPA=true|false (BETA - default=true)<br/>kube:StaleControllerConsistencyJob=true|false (BETA - default=true)<br/>kube:StaleControllerConsistencyReplicaSet=true|false (BETA - default=true)<br/>kube:StaleControllerConsistencyStatefulSet=true|false (BETA - default=true)<br/>kube:StatefulSetRecreateStrategy=true|false (ALPHA - default=false)<br/>kube:StatefulSetSemanticRevisionComparison=true|false (BETA - default=true)<br/>kube:StorageCapacityScoring=true|false (BETA - default=true)<br/>kube:StorageVersionAPI=true|false (ALPHA - default=false)<br/>kube:StorageVersionHash=true|false (BETA - default=true)<br/>kube:StrictIPCIDRValidation=true|false (BETA - default=true)<br/>kube:StructuredAuthenticationConfigurationEgressSelector=true|false (BETA - default=true)<br/>kube:StructuredAuthenticationConfigurationJWKSMetrics=true|false (BETA - default=true)<br/>kube:TaintTolerationComparisonOperators=true|false (ALPHA - default=false)<br/>kube:TokenRequestServiceAccountUIDValidation=true|false (BETA - default=true)<br/>kube:TopologyAwareWorkloadScheduling=true|false (ALPHA - default=false)<br/>kube:TopologyManagerPolicyAlphaOptions=true|false (ALPHA - default=false)<br/>kube:TopologyManagerPolicyBetaOptions=true|false (BETA - default=true)<br/>kube:TranslateStreamCloseWebsocketRequests=true|false (BETA - default=true)<br/>kube:UnauthenticatedHTTP2DOSMitigation=true|false (BETA - default=true)<br/>kube:UnknownVersionInteroperabilityProxy=true|false (BETA - default=true)<br/>kube:UnlockWhileProcessingFIFO=true|false (BETA - default=true)<br/>kube:UserNamespacesHostNetworkSupport=true|false (ALPHA - default=false)<br/>kube:VolumeBindMountOptions=true|false (ALPHA - default=false)<br/>kube:VolumeLimitScaling=true|false (BETA - default=true)<br/>kube:WatchList=true|false (BETA - default=true)<br/>kube:WatchListClient=true|false (BETA - default=true)<br/>kube:WatchListCompression=true|false (BETA - default=true)<br/>kube:WebhookRoundTripLoadBalancing=true|false (BETA - default=true)<br/>kube:WindowsCPUAndMemoryAffinity=true|false (ALPHA - default=false)<br/>kube:WindowsGracefulNodeShutdown=true|false (BETA - default=true)<br/>kube:WorkloadWithJob=true|false (ALPHA - default=false)</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای kube-scheduler</p></td>
</tr>

<tr>
<td colspan="2">--http2-max-streams-per-connection int</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر تعداد stream‌هایی که سرور در یک اتصال HTTP/2 به کلاینت‌ها اجازه می‌دهد. مقدار صفر به معنای استفاده از مقدار پیش‌فرض golang است.</p></td>
</tr>

<tr>
<td colspan="2">--kube-api-burst int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 100</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>منسوخ‌شده: مقدار burst برای ارتباط با kube-apiserver کوبرنتیز. اگر فایل پیکربندی در --config مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--kube-api-content-type string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "application/vnd.kubernetes.protobuf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>منسوخ‌شده: نوع محتوای (content type) درخواست‌های ارسالی به apiserver. اگر فایل پیکربندی در --config مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--kube-api-qps float&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 50</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>منسوخ‌شده: نرخ QPS مورد استفاده هنگام ارتباط با kube-apiserver کوبرنتیز. اگر در --config یک فایل پیکربندی مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>منسوخ‌شده: مسیر فایل kubeconfig که اطلاعات احراز هویت و مکان master را در بر دارد. اگر در --config یک فایل پیکربندی مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--leader-elect&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک کلاینت انتخاب رهبر (leader election) را راه‌اندازی می‌کند و پیش از اجرای حلقه اصلی، رهبری را به دست می‌گیرد. هنگام اجرای مؤلفه‌های replicated برای دستیابی به دسترس‌پذیری بالا، این گزینه را فعال کنید.</p></td>
</tr>

<tr>
<td colspan="2">--leader-elect-lease-duration duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 15s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که نامزدهای غیررهبر پس از مشاهده تمدید رهبری صبر می‌کنند تا برای به دست گرفتن رهبری یک جایگاه رهبری که اشغال شده اما تمدید نشده است اقدام کنند. این مقدار در عمل بیشترین مدتی است که یک رهبر می‌تواند متوقف باشد تا نامزد دیگری جایگزین آن شود. این گزینه فقط در صورت فعال بودن انتخاب رهبر کاربرد دارد.</p></td>
</tr>

<tr>
<td colspan="2">--leader-elect-renew-deadline duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فاصله زمانی میان تلاش‌های رهبر فعلی برای تمدید جایگاه رهبری پیش از آنکه از رهبری دست بکشد. این مقدار باید کمتر از مدت lease باشد. این گزینه فقط در صورت فعال بودن انتخاب رهبر کاربرد دارد.</p></td>
</tr>

<tr>
<td colspan="2">--leader-elect-resource-lock string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "leases"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوع آبجکت منبعی که هنگام انتخاب رهبر برای قفل کردن استفاده می‌شود. گزینه‌های پشتیبانی‌شده: 'leases'.</p></td>
</tr>

<tr>
<td colspan="2">--leader-elect-resource-name string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "kube-scheduler"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام آبجکت منبعی که هنگام انتخاب رهبر برای قفل کردن استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--leader-elect-resource-namespace string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "kube-system"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فضای نام (namespace) آبجکت منبعی که هنگام انتخاب رهبر برای قفل کردن استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--leader-elect-retry-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 2s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که کلاینت‌ها باید میان تلاش‌های خود برای به دست آوردن و تمدید رهبری صبر کنند. این گزینه فقط در صورت فعال بودن انتخاب رهبر کاربرد دارد.</p></td>
</tr>

<tr>
<td colspan="2">--log-flush-frequency duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشترین تعداد ثانیه میان دو بار flush شدن لاگ‌ها</p></td>
</tr>

<tr>
<td colspan="2">--log-text-info-buffer-size quantity</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>[آلفا] در قالب متنی با جریان‌های خروجی جداشده، پیام‌های اطلاعاتی را می‌توان برای مدتی بافر کرد تا کارایی افزایش یابد. مقدار پیش‌فرض صفر بایت، بافر کردن را غیرفعال می‌کند. اندازه را می‌توان به‌صورت تعداد بایت (512)، مضرب‌های 1000 (1K)، مضرب‌های 1024 (2Ki) یا توان‌های آن‌ها (3M، 4G، 5Mi، 6Gi) مشخص کرد. برای استفاده از این گزینه، feature gate با نام LoggingAlphaOptions را فعال کنید.</p></td>
</tr>

<tr>
<td colspan="2">--log-text-split-stream</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>[آلفا] در قالب متنی، پیام‌های خطا را در stderr و پیام‌های اطلاعاتی را در stdout می‌نویسد. رفتار پیش‌فرض، نوشتن یک جریان واحد در stdout است. برای استفاده از این گزینه، feature gate با نام LoggingAlphaOptions را فعال کنید.</p></td>
</tr>

<tr>
<td colspan="2">--logging-format string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "text"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>قالب لاگ را تعیین می‌کند. قالب‌های مجاز: &quot;text&quot;.</p></td>
</tr>

<tr>
<td colspan="2">--master string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی API server کوبرنتیز (هر مقداری را که در kubeconfig وجود دارد بازنویسی می‌کند)</p></td>
</tr>

<tr>
<td colspan="2">--min-compatibility-version strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>کمترین نسخه مؤلفه‌های control plane که سرور باید با آن سازگار باشد.<br/>باید کمتر از emulated-version یا برابر با آن باشد. قالب نسخه فقط می‌تواند major.minor باشد، برای مثال: '--min-compatibility-version=wardle=1.2,kube=1.31'.<br/>گزینه‌ها: kube=1.34..1.37(پیش‌فرض:1.36)<br/>اگر مؤلفه مشخص نشود، مقدار پیش‌فرض &quot;kube&quot; است</p></td>
</tr>

<tr>
<td colspan="2">--permit-address-sharing</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هنگام bind کردن پورت از SO_REUSEADDR استفاده می‌شود. این کار امکان bind همزمان به IPهای wildcard مانند 0.0.0.0 و IPهای مشخص را فراهم می‌کند و از انتظار برای آزاد شدن سوکت‌های در وضعیت TIME_WAIT توسط هسته جلوگیری می‌کند. [پیش‌فرض=false]</p></td>
</tr>

<tr>
<td colspan="2">--permit-port-sharing</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هنگام bind کردن پورت از SO_REUSEPORT استفاده می‌شود که به بیش از یک نمونه اجازه می‌دهد روی همان نشانی و پورت bind شوند. [پیش‌فرض=false]</p></td>
</tr>

<tr>
<td colspan="2">--pod-max-in-unschedulable-pods-duration duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>منسوخ‌شده: بیشترین مدتی که یک Pod می‌تواند در unschedulablePods بماند. اگر یک Pod بیش از این مقدار در unschedulablePods بماند، از unschedulablePods به backoffQ یا activeQ منتقل می‌شود. این پرچم منسوخ شده است و در نسخه‌ای در آینده حذف خواهد شد.</p></td>
</tr>

<tr>
<td colspan="2">--profiling&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>منسوخ‌شده: فعال‌سازی profiling از طریق رابط وب در host:port/debug/pprof/. اگر در --config یک فایل پیکربندی مشخص شده باشد، این پارامتر نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-allowed-names strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست common nameهای گواهی کلاینت که اجازه دارند نام‌های کاربری را در هدرهای مشخص‌شده با --requestheader-username-headers ارائه کنند. اگر خالی باشد، هر گواهی کلاینتی که توسط مراجع موجود در --requestheader-client-ca-file اعتبارسنجی شود مجاز است.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-client-ca-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بسته گواهی ریشه که پیش از اعتماد به نام‌های کاربری موجود در هدرهای مشخص‌شده با --requestheader-username-headers، برای تأیید گواهی‌های کلاینت در درخواست‌های ورودی استفاده می‌شود. هشدار: به‌طور کلی به این موضوع که احراز مجوز (authorization) برای درخواست‌های ورودی از قبل انجام شده است، تکیه نکنید.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-extra-headers-prefix strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "x-remote-extra-"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست پیشوندهای هدر درخواست که باید بررسی شوند. مقدار X-Remote-Extra- پیشنهاد می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-group-headers strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "x-remote-group"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست هدرهای درخواست که برای گروه‌ها بررسی می‌شوند. مقدار X-Remote-Group پیشنهاد می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-uid-headers strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست هدرهای درخواست که برای UIDها بررسی می‌شوند. مقدار X-Remote-Uid پیشنهاد می‌شود. نیازمند فعال بودن قابلیت RemoteRequestHeaderUID است.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-username-headers strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "x-remote-user"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست هدرهای درخواست که برای نام‌های کاربری بررسی می‌شوند. مقدار X-Remote-User رایج است.</p></td>
</tr>

<tr>
<td colspan="2">--secure-port int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10259</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پورتی که HTTPS همراه با احراز هویت و احراز مجوز روی آن سرویس‌دهی می‌شود. اگر 0 باشد، HTTPS اصلاً سرویس‌دهی نمی‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--show-hidden-metrics-for-version string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخه قبلی که می‌خواهید معیارهای (metrics) پنهان آن نمایش داده شود. فقط نسخه minor قبلی معنادار است و مقادیر دیگر مجاز نخواهند بود. قالب آن &lt;major&gt;.&lt;minor&gt; است، برای مثال: '1.16'. هدف از این قالب آن است که اگر نسخه بعدی معیارهای بیشتری را پنهان کرد، فرصت داشته باشید متوجه شوید و هنگام حذف دائمی آن‌ها در نسخه پس از آن غافلگیر نشوید.</p></td>
</tr>

<tr>
<td colspan="2">--tls-cert-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایلی که گواهی x509 پیش‌فرض برای HTTPS را در بر دارد. (گواهی CA، در صورت وجود، پس از گواهی سرور به آن الحاق می‌شود). اگر سرویس‌دهی HTTPS فعال باشد و --tls-cert-file و --tls-private-key-file ارائه نشده باشند، یک گواهی و کلید خودامضا برای نشانی عمومی تولید می‌شود و در دایرکتوری مشخص‌شده با --cert-dir ذخیره می‌گردد.</p></td>
</tr>

<tr>
<td colspan="2">--tls-cipher-suites strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست مجموعه‌های رمز (cipher suite) سرور، جداشده با ویرگول. اگر مشخص نشود، از cipher suiteهای پیش‌فرض Go استفاده می‌شود.<br/>مقادیر ترجیحی: TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305, TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305, TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256.<br/>مقادیر ناامن: TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_ECDSA_WITH_RC4_128_SHA, TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_RSA_WITH_RC4_128_SHA, TLS_RSA_WITH_3DES_EDE_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_256_GCM_SHA384, TLS_RSA_WITH_RC4_128_SHA.</p></td>
</tr>

<tr>
<td colspan="2">--tls-curve-preferences int32Slice&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: []</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست مقادیر عددی CurveID در crypto/tls زبان Go، جداشده با ویرگول، به‌عنوان سازوکارهای مجاز تبادل کلید برای سرور. مقادیر پشتیبانی‌شده به نسخه Go مورد استفاده بستگی دارد. برای مقادیر پشتیبانی‌شده در هر نسخه Go به https://pkg.go.dev/crypto/tls#CurveID مراجعه کنید. ترتیب فهرست نادیده گرفته می‌شود و سازوکارهای تبادل کلید توسط Go از این فهرست و با استفاده از یک ترتیب ترجیحی داخلی انتخاب می‌شوند. اگر مشخص نشود، از curveهای پیش‌فرض Go استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--tls-min-version string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>کمترین نسخه TLS پشتیبانی‌شده. مقادیر ممکن: VersionTLS10, VersionTLS11, VersionTLS12, VersionTLS13</p></td>
</tr>

<tr>
<td colspan="2">--tls-private-key-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایلی که کلید خصوصی x509 پیش‌فرض متناظر با --tls-cert-file را در بر دارد.</p></td>
</tr>

<tr>
<td colspan="2">--tls-sni-cert-key string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک جفت مسیر فایل گواهی x509 و کلید خصوصی که در صورت تمایل می‌تواند با فهرستی از الگوهای دامنه (domain patterns) ادامه یابد؛ این الگوها نام‌های دامنه کاملاً معتبر (fully qualified) هستند و ممکن است بخش‌های wildcard پیشوندی داشته باشند. الگوهای دامنه نشانی‌های IP را نیز مجاز می‌دانند، اما IPها فقط زمانی باید استفاده شوند که apiserver به نشانی IP درخواستی کلاینت دسترسی داشته باشد. اگر هیچ الگوی دامنه‌ای ارائه نشود، نام‌های موجود در گواهی استخراج می‌شوند. تطابق‌های بدون wildcard بر تطابق‌های wildcard برتری دارند و الگوهای دامنه صریح بر نام‌های استخراج‌شده برتری دارند. برای چند جفت کلید/گواهی، --tls-sni-cert-key را چند بار استفاده کنید. نمونه‌ها: &quot;example.crt,example.key&quot; یا &quot;foo.crt,foo.key:*.foo.com,foo.com&quot;.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>--version و --version=raw اطلاعات نسخه را چاپ می‌کنند و خارج می‌شوند؛ --version=vX.Y.Z... نسخه گزارش‌شده را تنظیم می‌کند</p></td>
</tr>

<tr>
<td colspan="2">--vmodule pattern=N,...</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست تنظیمات pattern=N جداشده با ویرگول برای لاگ‌گیری با فیلتر بر اساس فایل (فقط برای قالب لاگ متنی کار می‌کند)</p></td>
</tr>

<tr>
<td colspan="2">--write-config-to string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر تنظیم شود، مقادیر پیکربندی را در این فایل می‌نویسد و خارج می‌شود.</p></td>
</tr>

</tbody>
</table>
