---
reviewers:
- tallclair
title: استانداردهای امنیتی Pod
description: >
  نگاهی دقیق به سطوح مختلف سیاست تعریف‌شده در استانداردهای امنیتی Pod.
content_type: concept
weight: 15
---

<!-- overview -->

استانداردهای امنیتی Pod سه _سیاست_ مختلف را تعریف می‌کنند تا طیف امنیتی را به‌طور گسترده پوشش دهند.
این سیاست‌ها _تجمعی_ هستند و از بسیار آزادمنشانه تا بسیار محدودکننده را شامل می‌شوند.
این راهنما الزامات هر سیاست را تشریح می‌کند.

| پروفایل | توضیحات |
| ------ | ----------- |
| <strong style="white-space: nowrap">Privileged</strong> | سیاست بدون محدودیت که گسترده‌ترین سطح ممکن از مجوزها را فراهم می‌کند. این سیاست امکان ارتقای سطح دسترسی (privilege escalation) شناخته‌شده را می‌دهد. |
| <strong style="white-space: nowrap">Baseline</strong> | سیاستی با حداقل محدودیت که از ارتقای سطح دسترسی شناخته‌شده جلوگیری می‌کند. پیکربندی پیش‌فرض Pod (با حداقل مشخصات) را مجاز می‌داند. |
| <strong style="white-space: nowrap">Restricted</strong> | سیاستی به‌شدت محدودکننده که از بهترین شیوه‌های کنونی برای مقاوم‌سازی (hardening) Pod پیروی می‌کند. |

<!-- body -->

## جزئیات پروفایل‌ها {#profile-details}

### Privileged

**سیاست _Privileged_ عمداً باز و کاملاً بدون محدودیت است.** این نوع سیاست
معمولاً برای بارهای کاری سطح سیستم و زیرساخت که توسط کاربران مورد اعتماد و دارای دسترسی ویژه مدیریت می‌شوند، در نظر گرفته شده است.

سیاست Privileged با نبود محدودیت‌ها تعریف می‌شود. اگر Podی را تعریف کنید که سیاست امنیتی Privileged
بر آن اعمال می‌شود، این Pod می‌تواند سازوکارهای معمول جداسازی کانتینر را دور بزند.
برای مثال، می‌توانید Podی تعریف کنید که به شبکه میزبان نود دسترسی دارد.

### Baseline

**سیاست _Baseline_ با هدف سهولت پذیرش برای بارهای کاری کانتینری رایج تعریف شده است و در عین حال
از ارتقای سطح دسترسی شناخته‌شده جلوگیری می‌کند.** این سیاست برای اپراتورهای برنامه و
توسعه‌دهندگان برنامه‌های غیرحیاتی در نظر گرفته شده است. کنترل‌های فهرست‌شده زیر باید
اعمال یا ممنوع شوند:

{{< note >}}
در این جدول، علامت wildcard یعنی `*` نشان‌دهنده همه عناصر یک فهرست است. برای مثال،
`spec.containers[*].securityContext` به آبجکت Security Context برای _همه کانتینرهای تعریف‌شده_
اشاره دارد. اگر هر یک از کانتینرهای فهرست‌شده الزامات را برآورده نکند، کل Pod
در اعتبارسنجی رد خواهد شد.
{{< /note >}}

<table>
	<caption style="display:none">مشخصات سیاست Baseline</caption>
	<tbody>
		<tr>
			<th>کنترل</th>
			<th>سیاست</th>
		</tr>
		<tr>
			<td style="white-space: nowrap">HostProcess</td>
			<td>
				<p>Podهای ویندوز امکان اجرای <a href="/docs/tasks/configure-pod-container/create-hostprocess-pod">کانتینرهای HostProcess</a> را فراهم می‌کنند که دسترسی ویژه (privileged) به ماشین میزبان ویندوز را ممکن می‌سازد. دسترسی ویژه به میزبان در سیاست Baseline ممنوع است. {{< feature-state for_k8s_version="v1.26" state="stable" >}}</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.securityContext.windowsOptions.hostProcess</code></li>
					<li><code>spec.containers[*].securityContext.windowsOptions.hostProcess</code></li>
					<li><code>spec.initContainers[*].securityContext.windowsOptions.hostProcess</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.windowsOptions.hostProcess</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>تعریف‌نشده/nil</li>
					<li><code>false</code></li>
				</ul>
			</td>
		</tr>
		<tr>
			<td style="white-space: nowrap">Host Namespaces</td>
			<td>
				<p>اشتراک‌گذاری فضاهای نام (namespace) میزبان باید ممنوع باشد.</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.hostNetwork</code></li>
					<li><code>spec.hostPID</code></li>
					<li><code>spec.hostIPC</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>تعریف‌نشده/nil</li>
					<li><code>false</code></li>
				</ul>
			</td>
		</tr>
		<tr>
			<td style="white-space: nowrap">Privileged Containers</td>
			<td>
				<p>Podهای Privileged بیشتر سازوکارهای امنیتی را غیرفعال می‌کنند و باید ممنوع باشند.</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.containers[*].securityContext.privileged</code></li>
					<li><code>spec.initContainers[*].securityContext.privileged</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.privileged</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>تعریف‌نشده/nil</li>
					<li><code>false</code></li>
				</ul>
			</td>
		</tr>
		<tr>
			<td style="white-space: nowrap">Capabilities</td>
			<td>
				<p>افزودن capabilityهای اضافی فراتر از موارد فهرست‌شده در زیر باید ممنوع باشد.</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.containers[*].securityContext.capabilities.add</code></li>
					<li><code>spec.initContainers[*].securityContext.capabilities.add</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.capabilities.add</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>تعریف‌نشده/nil</li>
					<li><code>AUDIT_WRITE</code></li>
					<li><code>CHOWN</code></li>
					<li><code>DAC_OVERRIDE</code></li>
					<li><code>FOWNER</code></li>
					<li><code>FSETID</code></li>
					<li><code>KILL</code></li>
					<li><code>MKNOD</code></li>
					<li><code>NET_BIND_SERVICE</code></li>
					<li><code>SETFCAP</code></li>
					<li><code>SETGID</code></li>
					<li><code>SETPCAP</code></li>
					<li><code>SETUID</code></li>
					<li><code>SYS_CHROOT</code></li>
				</ul>
			</td>
		</tr>
		<tr>
			<td style="white-space: nowrap">HostPath Volumes</td>
			<td>
				<p>حجم‌های (volume) HostPath باید ممنوع باشند.</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.volumes[*].hostPath</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>تعریف‌نشده/nil</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td style="white-space: nowrap">Host Ports</td>
			<td>
				<p>HostPortها باید به‌طور کامل ممنوع شوند (توصیه می‌شود) یا به یک فهرست شناخته‌شده محدود شوند.</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.containers[*].ports[*].hostPort</code></li>
					<li><code>spec.initContainers[*].ports[*].hostPort</code></li>
					<li><code>spec.ephemeralContainers[*].ports[*].hostPort</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>تعریف‌نشده/nil</li>
					<li>فهرست شناخته‌شده (توسط <a href="/docs/concepts/security/pod-security-admission/">کنترل‌کننده Pod Security Admission</a> داخلی پشتیبانی نمی‌شود)</li>
					<li><code>0</code></li>
				</ul>
			</td>
		</tr>
		<tr>
			<td>Host Probes / Lifecycle Hooks (v1.34+)</td>
			<td>
				<p>فیلد Host در probeها و lifecycle hookها باید ممنوع باشد.</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.containers[*].livenessProbe.httpGet.host</code></li>
					<li><code>spec.containers[*].readinessProbe.httpGet.host</code></li>
					<li><code>spec.containers[*].startupProbe.httpGet.host</code></li>
					<li><code>spec.containers[*].livenessProbe.tcpSocket.host</code></li>
					<li><code>spec.containers[*].readinessProbe.tcpSocket.host</code></li>
					<li><code>spec.containers[*].startupProbe.tcpSocket.host</code></li>
					<li><code>spec.containers[*].lifecycle.postStart.tcpSocket.host</code>
					<li><code>spec.containers[*].lifecycle.preStop.tcpSocket.host</code>
					<li><code>spec.containers[*].lifecycle.postStart.httpGet.host</code></li>
					<li><code>spec.containers[*].lifecycle.preStop.httpGet.host</code></li>
					<li><code>spec.initContainers[*].livenessProbe.httpGet.host</code></li>
					<li><code>spec.initContainers[*].readinessProbe.httpGet.host</code></li>
					<li><code>spec.initContainers[*].startupProbe.httpGet.host</code></li>
					<li><code>spec.initContainers[*].livenessProbe.tcpSocket.host</code></li>
					<li><code>spec.initContainers[*].readinessProbe.tcpSocket.host</code></li>
					<li><code>spec.initContainers[*].startupProbe.tcpSocket.host</code></li>
					<li><code>spec.initContainers[*].lifecycle.postStart.tcpSocket.host</code>
					<li><code>spec.initContainers[*].lifecycle.preStop.tcpSocket.host</code>
					<li><code>spec.initContainers[*].lifecycle.postStart.httpGet.host</code></li>
					<li><code>spec.initContainers[*].lifecycle.preStop.httpGet.host</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>تعریف‌نشده/nil</li>
					<li>""</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td style="white-space: nowrap">AppArmor</td>
			<td>
				<p>در میزبان‌های پشتیبانی‌شده، پروفایل AppArmor با نام <code>RuntimeDefault</code> به‌طور پیش‌فرض اعمال می‌شود. سیاست Baseline باید از بازنویسی یا غیرفعال‌سازی پروفایل پیش‌فرض AppArmor جلوگیری کند یا بازنویسی‌ها را به مجموعه‌ای از پروفایل‌های مجاز محدود سازد.</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.securityContext.appArmorProfile.type</code></li>
					<li><code>spec.containers[*].securityContext.appArmorProfile.type</code></li>
					<li><code>spec.initContainers[*].securityContext.appArmorProfile.type</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.appArmorProfile.type</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>تعریف‌نشده/nil</li>
					<li><code>RuntimeDefault</code></li>
					<li><code>Localhost</code></li>
				</ul>
				<hr />
				<ul>
					<li><code>metadata.annotations["container.apparmor.security.beta.kubernetes.io/*"]</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>تعریف‌نشده/nil</li>
					<li><code>runtime/default</code></li>
					<li><code>localhost/*</code></li>
				</ul>
			</td>
		</tr>
		<tr>
			<td style="white-space: nowrap">SELinux</td>
			<td>
				<p>تنظیم نوع SELinux محدود شده است و تنظیم گزینه کاربر یا نقش سفارشی SELinux ممنوع است.</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.securityContext.seLinuxOptions.type</code></li>
					<li><code>spec.containers[*].securityContext.seLinuxOptions.type</code></li>
					<li><code>spec.initContainers[*].securityContext.seLinuxOptions.type</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.seLinuxOptions.type</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>تعریف‌نشده/""</li>
					<li><code>container_t</code></li>
					<li><code>container_init_t</code></li>
					<li><code>container_kvm_t</code></li>
					<li><code>container_engine_t</code> (از کوبرنتیز 1.31)</li>
				</ul>
				<hr />
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.securityContext.seLinuxOptions.user</code></li>
					<li><code>spec.containers[*].securityContext.seLinuxOptions.user</code></li>
					<li><code>spec.initContainers[*].securityContext.seLinuxOptions.user</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.seLinuxOptions.user</code></li>
					<li><code>spec.securityContext.seLinuxOptions.role</code></li>
					<li><code>spec.containers[*].securityContext.seLinuxOptions.role</code></li>
					<li><code>spec.initContainers[*].securityContext.seLinuxOptions.role</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.seLinuxOptions.role</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>تعریف‌نشده/""</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td style="white-space: nowrap">نوع mount مسیر <code>/proc</code></td>
			<td>
				<p>maskهای پیش‌فرض <code>/proc</code> برای کاهش سطح حمله تنظیم شده‌اند و باید الزامی باشند.</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.containers[*].securityContext.procMount</code></li>
					<li><code>spec.initContainers[*].securityContext.procMount</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.procMount</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>تعریف‌نشده/nil</li>
					<li><code>Default</code></li>
				</ul>
			</td>
		</tr>
		<tr>
  			<td>Seccomp</td>
  			<td>
  				<p>پروفایل Seccomp نباید صراحتاً روی <code>Unconfined</code> تنظیم شود.</p>
  				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.securityContext.seccompProfile.type</code></li>
					<li><code>spec.containers[*].securityContext.seccompProfile.type</code></li>
					<li><code>spec.initContainers[*].securityContext.seccompProfile.type</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.seccompProfile.type</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>تعریف‌نشده/nil</li>
					<li><code>RuntimeDefault</code></li>
					<li><code>Localhost</code></li>
				</ul>
  			</td>
  		</tr>
		<tr>
			<td style="white-space: nowrap">Sysctls</td>
			<td>
				<p>Sysctlها می‌توانند سازوکارهای امنیتی را غیرفعال کنند یا بر همه کانتینرهای یک میزبان اثر بگذارند و باید به‌جز زیرمجموعه‌ای «ایمن» که مجاز شمرده می‌شود، ممنوع باشند. یک sysctl زمانی ایمن تلقی می‌شود که در سطح کانتینر یا Pod دارای فضای نام (namespace) باشد و از سایر Podها یا فرایندهای روی همان نود جدا باشد.</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.securityContext.sysctls[*].name</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>تعریف‌نشده/nil</li>
					<li><code>kernel.shm_rmid_forced</code></li>
					<li><code>net.ipv4.ip_local_port_range</code></li>
					<li><code>net.ipv4.ip_unprivileged_port_start</code></li>
					<li><code>net.ipv4.tcp_syncookies</code></li>
					<li><code>net.ipv4.ping_group_range</code></li>
					<li><code>net.ipv4.ip_local_reserved_ports</code> (از کوبرنتیز 1.27)</li>
					<li><code>net.ipv4.tcp_keepalive_time</code> (از کوبرنتیز 1.29)</li>
					<li><code>net.ipv4.tcp_fin_timeout</code> (از کوبرنتیز 1.29)</li>
					<li><code>net.ipv4.tcp_keepalive_intvl</code> (از کوبرنتیز 1.29)</li>
					<li><code>net.ipv4.tcp_keepalive_probes</code> (از کوبرنتیز 1.29)</li>
					<li><code>net.ipv4.tcp_rmem</code> (از کوبرنتیز 1.32)</li>
					<li><code>net.ipv4.tcp_wmem</code> (از کوبرنتیز 1.32)</li>
					<li><code>net.ipv4.tcp_slow_start_after_idle</code> (از کوبرنتیز 1.37)</li>
					<li><code>net.ipv4.tcp_notsent_lowat</code> (از کوبرنتیز 1.37)</li>
				</ul>
			</td>
		</tr>
	</tbody>
</table>

### Restricted

**سیاست _Restricted_ با هدف اعمال بهترین شیوه‌های فعلی برای مقاوم‌سازی Podها طراحی شده است، هرچند این کار به قیمت کاهش مقداری از سازگاری انجام می‌شود.** این سیاست برای اپراتورها و توسعه‌دهندگان برنامه‌های حیاتی از نظر امنیتی و همچنین کاربران با سطح اعتماد پایین‌تر در نظر گرفته شده است. کنترل‌های فهرست‌شده‌ی زیر باید اعمال یا ممنوع شوند:

{{< note >}}
در این جدول، نویسه‌های عام (`*`) نشان‌دهنده‌ی همه‌ی عناصر یک فهرست هستند. برای مثال،
`spec.containers[*].securityContext` به آبجکت Security Context مربوط به _همه‌ی کانتینرهای تعریف‌شده_ اشاره دارد. اگر هر یک از کانتینرهای فهرست‌شده الزامات را برآورده نکند، اعتبارسنجی کل Pod با شکست مواجه می‌شود.
{{< /note >}}

<table>
	<caption style="display:none">Restricted policy specification</caption>
	<tbody>
		<tr>
			<td><strong>کنترل</strong></td>
			<td><strong>سیاست</strong></td>
		</tr>
		<tr>
			<td colspan="2"><em>همه‌ی موارد سیاست Baseline</em></td>
		</tr>
		<tr>
			<td style="white-space: nowrap">انواع حجم (Volume Types)</td>
			<td>
				<p>سیاست Restricted تنها انواع حجم زیر را مجاز می‌داند.</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.volumes[*]</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				در هر آیتم از فهرست <code>spec.volumes[*]</code> باید یکی از فیلدهای زیر روی یک مقدار غیر null تنظیم شود:
				<ul>
					<li><code>spec.volumes[*].configMap</code></li>
					<li><code>spec.volumes[*].csi</code></li>
					<li><code>spec.volumes[*].downwardAPI</code></li>
					<li><code>spec.volumes[*].emptyDir</code></li>
					<li><code>spec.volumes[*].ephemeral</code></li>
					<li><code>spec.volumes[*].persistentVolumeClaim</code></li>
					<li><code>spec.volumes[*].projected</code></li>
					<li><code>spec.volumes[*].secret</code></li>
				</ul>
			</td>
		</tr>
		<tr>
			<td style="white-space: nowrap">ارتقای سطح دسترسی (Privilege Escalation) (v1.8+)</td>
			<td>
				<p>ارتقای سطح دسترسی (مانند استفاده از حالت فایل set-user-ID یا set-group-ID) نباید مجاز باشد. <em><a href="#os-specific-policy-controls">این سیاست تنها برای لینوکس است</a> در نسخه‌ی v1.25 و بالاتر <code>(spec.os.name != windows)</code></em></p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.containers[*].securityContext.allowPrivilegeEscalation</code></li>
					<li><code>spec.initContainers[*].securityContext.allowPrivilegeEscalation</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.allowPrivilegeEscalation</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li><code>false</code></li>
				</ul>
			</td>
		</tr>
		<tr>
			<td style="white-space: nowrap">اجرا به‌عنوان کاربر غیر root</td>
			<td>
				<p>اجرای کانتینرها باید به‌عنوان کاربران غیر root الزامی شود.</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.securityContext.runAsNonRoot</code></li>
					<li><code>spec.containers[*].securityContext.runAsNonRoot</code></li>
					<li><code>spec.initContainers[*].securityContext.runAsNonRoot</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.runAsNonRoot</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li><code>true</code></li>
				</ul>
				<small>
					اگر فیلد سطح Pod یعنی
					<code>spec.securityContext.runAsNonRoot</code> روی <code>true</code> تنظیم شده باشد، فیلدهای کانتینر می‌توانند تعریف‌نشده/<code>nil</code> باشند.
				</small>
			</td>
		</tr>
		<tr>
			<td style="white-space: nowrap">اجرا به‌عنوان کاربر غیر root (v1.23+)</td>
			<td>
				<p>کانتینرها نباید <tt>runAsUser</tt> را روی 0 تنظیم کنند</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.securityContext.runAsUser</code></li>
				    <li><code>spec.containers[*].securityContext.runAsUser</code></li>
					<li><code>spec.initContainers[*].securityContext.runAsUser</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.runAsUser</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>هر مقدار غیر صفر</li>
					<li><code>undefined/null</code></li>
				</ul>
			</td>
		</tr>
		<tr>
  			<td style="white-space: nowrap">Seccomp (v1.19+)</td>
  			<td>
  				<p>پروفایل Seccomp باید به‌صراحت روی یکی از مقادیر مجاز تنظیم شود. هم پروفایل <code>Unconfined</code> و هم <em>نبودِ</em> پروفایل ممنوع است. <em><a href="#os-specific-policy-controls">این سیاست تنها برای لینوکس است</a> در نسخه‌ی v1.25 و بالاتر <code>(spec.os.name != windows)</code></em></p>
  				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.securityContext.seccompProfile.type</code></li>
					<li><code>spec.containers[*].securityContext.seccompProfile.type</code></li>
					<li><code>spec.initContainers[*].securityContext.seccompProfile.type</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.seccompProfile.type</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li><code>RuntimeDefault</code></li>
					<li><code>Localhost</code></li>
				</ul>
				<small>
					اگر فیلد سطح Pod یعنی
					<code>spec.securityContext.seccompProfile.type</code> به‌درستی تنظیم شده باشد، فیلدهای کانتینر می‌توانند تعریف‌نشده/<code>nil</code> باشند.
					در مقابل، اگر فیلدهای سطح کانتینرِ _همه‌ی_ کانتینرها تنظیم شده باشند، فیلد سطح Pod می‌تواند تعریف‌نشده/<code>nil</code> باشد.
				</small>
  			</td>
  		</tr>
		  <tr>
			<td style="white-space: nowrap">Capabilities (v1.22+)</td>
			<td>
				<p>
					کانتینرها باید همه‌ی capabilityها (<code>ALL</code>) را حذف (drop) کنند و فقط مجازند capability با نام <code>NET_BIND_SERVICE</code> را دوباره اضافه کنند. <em><a href="#os-specific-policy-controls">این سیاست تنها برای لینوکس است</a> در نسخه‌ی v1.25 و بالاتر <code>(.spec.os.name != "windows")</code></em>
				</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.containers[*].securityContext.capabilities.drop</code></li>
					<li><code>spec.initContainers[*].securityContext.capabilities.drop</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.capabilities.drop</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>هر فهرستی از capabilityها که شامل <code>ALL</code> باشد</li>
				</ul>
				<hr />
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.containers[*].securityContext.capabilities.add</code></li>
					<li><code>spec.initContainers[*].securityContext.capabilities.add</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.capabilities.add</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>Undefined/nil</li>
					<li><code>NET_BIND_SERVICE</code></li>
				</ul>
			</td>
		</tr>
	</tbody>
</table>

## نمونه‌سازی سیاست (Policy Instantiation)

جداسازی تعریف سیاست از نمونه‌سازی آن، امکان درک مشترک و زبانی یکسان برای سیاست‌ها را در کلاسترهای مختلف و مستقل از سازوکار اجرایی زیربنایی فراهم می‌کند.

با بلوغ سازوکارها، این موارد در ادامه و به‌ازای هر سیاست تعریف خواهند شد. روش‌های اعمال سیاست‌های منفرد در اینجا تعریف نشده است.

[**Pod Security Admission Controller**](/docs/concepts/security/pod-security-admission/)

- {{< example file="security/podsecurity-privileged.yaml" >}}فضای نام Privileged{{< /example >}}
- {{< example file="security/podsecurity-baseline.yaml" >}}فضای نام Baseline{{< /example >}}
- {{< example file="security/podsecurity-restricted.yaml" >}}فضای نام Restricted{{< /example >}}

### جایگزین‌ها

{{% thirdparty-content %}}

جایگزین‌های دیگری برای اعمال سیاست‌ها در اکوسیستم کوبرنتیز در حال توسعه هستند، از جمله:

- [Kubewarden](https://github.com/kubewarden)
- [Kyverno](https://kyverno.io/policies)
- [OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper)

## فیلد OS در Pod

کوبرنتیز به شما امکان می‌دهد از نودهایی استفاده کنید که لینوکس یا ویندوز اجرا می‌کنند. می‌توانید هر دو نوع نود را در یک کلاستر ترکیب کنید.
ویندوز در کوبرنتیز محدودیت‌ها و تفاوت‌هایی با بارهای کاری مبتنی بر لینوکس دارد. به‌طور مشخص، بسیاری از فیلدهای `securityContext` در Pod
[بر ویندوز تأثیری ندارند](/docs/concepts/windows/intro/#compatibility-v1-pod-spec-containers-securitycontext).

{{< note >}}
kubeletهای قبل از نسخه‌ی v1.24 فیلد OS در Pod را اعمال نمی‌کنند و اگر کلاستر دارای نودهایی با نسخه‌های قدیمی‌تر از v1.24 باشد، سیاست‌های Restricted باید روی نسخه‌ای قبل از v1.25 قفل (pin) شوند.
{{< /note >}}

### تغییرات استاندارد امنیتی Restricted در Pod
تغییر مهم دیگری که در کوبرنتیز v1.25 انجام شد این است که سیاست _Restricted_
به‌گونه‌ای به‌روزرسانی شده که از فیلد `pod.spec.os.name` استفاده کند. بر اساس نام سیستم‌عامل، برخی سیاست‌هایی که مختص یک سیستم‌عامل مشخص هستند می‌توانند برای سیستم‌عامل دیگر تعدیل شوند.

#### کنترل‌های سیاستیِ مختص سیستم‌عامل
محدودیت‌های مربوط به کنترل‌های زیر فقط در صورتی لازم است که `.spec.os.name` برابر `windows` نباشد:
- ارتقای سطح دسترسی (Privilege Escalation)
- Seccomp
- Linux Capabilities

## فضاهای نام کاربر (User namespaces)

فضاهای نام کاربر (User Namespaces) قابلیتی مختص لینوکس برای اجرای بارهای کاری با ایزولاسیون بیشتر هستند. نحوه‌ی همکاری آن‌ها با استانداردهای امنیتی Pod در [مستندات](/docs/concepts/workloads/pods/user-namespaces#integration-with-pod-security-admission-checks) مربوط به Podهایی که از فضاهای نام کاربر استفاده می‌کنند توضیح داده شده است.

## پرسش‌های متداول

### چرا پروفایلی بین Privileged و Baseline وجود ندارد؟

سه پروفایل تعریف‌شده در اینجا یک روند خطی روشن از امن‌ترین (Restricted) تا کم‌امن‌ترین (Privileged) دارند و طیف گسترده‌ای از بارهای کاری را پوشش می‌دهند. سطوح دسترسی موردنیاز فراتر از سیاست Baseline معمولاً بسیار وابسته به برنامه هستند؛ به همین دلیل پروفایل استانداردی برای این حوزه ارائه نمی‌کنیم. این بدان معنا نیست که در این حالت باید همیشه از پروفایل privileged استفاده کرد، بلکه به این معناست که سیاست‌ها در این حوزه باید به‌صورت موردی تعریف شوند.

SIG Auth ممکن است در آینده و در صورت بروز نیاز آشکار به پروفایل‌های دیگر، در این موضع بازنگری کند.

### تفاوت میان پروفایل امنیتی و security context چیست؟

[Security Contextها](/docs/tasks/configure-pod-container/security-context/) Podها و کانتینرها را در زمان اجرا پیکربندی می‌کنند. Security Contextها به‌عنوان بخشی از مشخصات Pod و کانتینر در مانیفست Pod تعریف می‌شوند و پارامترهایی برای container runtime به شمار می‌آیند.

پروفایل‌های امنیتی سازوکارهایی در control plane هستند که برای اعمال تنظیمات مشخصی در Security Context و نیز سایر پارامترهای مرتبط خارج از Security Context به کار می‌روند. از ژوئیه‌ی ۲۰۲۱،
[Pod Security Policyها](/docs/concepts/security/pod-security-policy/) به نفع
[Pod Security Admission Controller](/docs/concepts/security/pod-security-admission/) داخلی منسوخ شده‌اند.


### درباره‌ی Podهای sandboxed چه باید گفت؟

در حال حاضر هیچ استاندارد API وجود ندارد که تعیین کند یک Pod sandboxed محسوب می‌شود یا خیر. Podهای sandbox را می‌توان از طریق استفاده از یک runtime مبتنی بر sandbox (مانند gVisor یا Kata Containers) شناسایی کرد، اما تعریف استانداردی برای اینکه runtime مبتنی بر sandbox چیست وجود ندارد.

حفاظت‌های لازم برای بارهای کاری sandboxed می‌تواند با سایر بارهای کاری متفاوت باشد. برای مثال، وقتی بار کاری از کرنل زیربنایی ایزوله شده باشد، نیاز به محدودسازی مجوزهای ممتاز کمتر می‌شود. این موضوع به بارهای کاری‌ای که به مجوزهای بالاتر نیاز دارند اجازه می‌دهد همچنان ایزوله باقی بمانند.

علاوه بر این، حفاظت از بارهای کاری sandboxed به‌شدت به روش پیاده‌سازی sandbox وابسته است. بنابراین، هیچ پروفایل واحدی برای همه‌ی بارهای کاری sandboxed توصیه نمی‌شود.
