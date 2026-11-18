---
reviewers:
- tallclair
title: استانداردهای امنیتی Pod
description: >
  نگاهی دقیق به سطوح مختلف سیاستی که در استانداردهای امنیتی Pod تعریف شده‌اند.
content_type: concept
weight: 15
---

<!-- overview -->

استانداردهای امنیتی Pod سه _سیاست_ متفاوت را تعریف می‌کنند تا طیف امنیت را به‌طور گسترده پوشش دهند.
این سیاست‌ها _تجمعی_ هستند و از بسیار سهل‌گیرانه تا بسیار سخت‌گیرانه را در بر می‌گیرند.
این راهنما الزامات هر سیاست را شرح می‌دهد.

| پروفایل | توضیحات |
| ------ | ----------- |
| <strong style="white-space: nowrap">Privileged</strong> | سیاستی بدون محدودیت که گسترده‌ترین سطح ممکن از مجوزها را فراهم می‌کند. این سیاست ارتقای امتیاز (privilege escalation) شناخته‌شده را مجاز می‌داند. |
| <strong style="white-space: nowrap">Baseline</strong> | سیاستی با کمترین میزان محدودیت که از ارتقای امتیاز شناخته‌شده جلوگیری می‌کند. این سیاست پیکربندی پیش‌فرض (با حداقل مشخصات) Pod را مجاز می‌داند. |
| <strong style="white-space: nowrap">Restricted</strong> | سیاستی به‌شدت محدودکننده که از بهترین شیوه‌های فعلی برای مقاوم‌سازی Pod پیروی می‌کند. |

<!-- body -->

## جزئیات پروفایل‌ها

### Privileged

**سیاست _Privileged_ عامدانه باز و کاملاً بدون محدودیت است.** این نوع سیاست معمولاً برای
بارهای کاری سطح سیستم و زیرساخت در نظر گرفته شده است که کاربران دارای امتیاز و مورد اعتماد آن‌ها را مدیریت می‌کنند.

ویژگی تعریف‌کنندهٔ سیاست Privileged نبود هرگونه محدودیت است. اگر Pod‌ای تعریف کنید که سیاست امنیتی Privileged
بر آن اعمال می‌شود، آن Pod می‌تواند سازوکارهای معمول جداسازی کانتینر را دور بزند.
برای مثال، می‌توانید Pod‌ای تعریف کنید که به شبکهٔ میزبانِ نود دسترسی داشته باشد.

### Baseline

**هدف سیاست _Baseline_ آسان‌کردن به‌کارگیری برای بارهای کاری کانتینری رایج و در عین حال
جلوگیری از ارتقای امتیاز شناخته‌شده است.** مخاطبان این سیاست، اپراتورهای برنامه‌ها و
توسعه‌دهندگان برنامه‌های غیرحیاتی هستند. کنترل‌های فهرست‌شدهٔ زیر باید
اعمال یا ممنوع شوند:

{{< note >}}
در این جدول، نویسه‌های عام (`*`) نشان‌دهندهٔ همهٔ عناصر یک فهرست هستند. برای مثال،
`spec.containers[*].securityContext` به آبجکت Security Context برای _همهٔ کانتینرهای
تعریف‌شده_ اشاره دارد. اگر هر یک از کانتینرهای فهرست‌شده الزامات را برآورده نکند، کل Pod
در اعتبارسنجی رد می‌شود.
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
				<p>Pod‌های ویندوزی امکان اجرای <a href="/docs/tasks/configure-pod-container/create-hostprocess-pod">کانتینرهای HostProcess</a> را فراهم می‌کنند که دسترسی دارای امتیاز به ماشین میزبان ویندوز را ممکن می‌سازد. در سیاست Baseline، دسترسی دارای امتیاز به میزبان ممنوع است. {{< feature-state for_k8s_version="v1.26" state="stable" >}}</p>
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
			<td style="white-space: nowrap">فضاهای نام میزبان</td>
			<td>
				<p>اشتراک‌گذاری فضاهای نام (namespace) میزبان باید ممنوع شود.</p>
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
			<td style="white-space: nowrap">کانتینرهای دارای امتیاز</td>
			<td>
				<p>Pod‌های دارای امتیاز بیشتر سازوکارهای امنیتی را غیرفعال می‌کنند و باید ممنوع شوند.</p>
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
			<td style="white-space: nowrap">قابلیت‌ها (Capabilities)</td>
			<td>
				<p>افزودن قابلیت‌هایی فراتر از موارد فهرست‌شدهٔ زیر باید ممنوع شود.</p>
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
			<td style="white-space: nowrap">حجم‌های HostPath</td>
			<td>
				<p>حجم‌های (volume) HostPath باید ممنوع شوند.</p>
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
			<td style="white-space: nowrap">پورت‌های میزبان</td>
			<td>
				<p>پورت‌های میزبان (HostPort) باید به‌طور کامل ممنوع شوند (توصیه‌شده) یا به فهرستی شناخته‌شده محدود شوند.</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.containers[*].ports[*].hostPort</code></li>
					<li><code>spec.initContainers[*].ports[*].hostPort</code></li>
					<li><code>spec.ephemeralContainers[*].ports[*].hostPort</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>تعریف‌نشده/nil</li>
					<li>فهرست شناخته‌شده (در <a href="/docs/concepts/security/pod-security-admission/">کنترل‌کنندهٔ داخلی Pod Security Admission</a> پشتیبانی نمی‌شود)</li>
					<li><code>0</code></li>
				</ul>
			</td>
		</tr>
		<tr>
			<td>پروب‌ها / هوک‌های چرخهٔ حیات میزبان (v1.34+)</td>
			<td>
				<p>فیلد Host در پروب‌ها و هوک‌های چرخهٔ حیات باید ممنوع شود.</p>
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
				<p>در میزبان‌هایی که از AppArmor پشتیبانی می‌کنند، پروفایل AppArmor با نام <code>RuntimeDefault</code> به‌طور پیش‌فرض اعمال می‌شود. سیاست Baseline باید از بازنویسی یا غیرفعال‌کردن پروفایل پیش‌فرض AppArmor جلوگیری کند، یا بازنویسی‌ها را به مجموعه‌ای مجاز از پروفایل‌ها محدود کند.</p>
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
				<p>تنظیم نوع SELinux محدود است و تنظیم گزینهٔ سفارشی کاربر یا نقش SELinux ممنوع است.</p>
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
			<td style="white-space: nowrap">نوع اتصال <code>/proc</code></td>
			<td>
				<p>ماسک‌های پیش‌فرض <code>/proc</code> برای کاهش سطح حمله تنظیم شده‌اند و باید الزامی باشند.</p>
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
  				<p>پروفایل Seccomp نباید به‌صراحت روی <code>Unconfined</code> تنظیم شود.</p>
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
				<p>تنظیمات sysctl می‌توانند سازوکارهای امنیتی را غیرفعال کنند یا بر همهٔ کانتینرهای یک میزبان اثر بگذارند؛ بنابراین باید به‌جز زیرمجموعه‌ای مجاز و «امن» ممنوع شوند. یک sysctl زمانی امن تلقی می‌شود که در فضای نامِ کانتینر یا Pod قرار گرفته باشد و از سایر Podها یا فرایندهای روی همان نود جدا باشد.</p>
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

### محدود (Restricted)

**هدف سیاست _Restricted_ اعمال بهترین شیوه‌های فعلی برای مقاوم‌سازی Pod است، هرچند به بهای کاهش بخشی از سازگاری.** مخاطب این سیاست گردانندگان و توسعه‌دهندگان برنامه‌های حساس از نظر امنیتی و همچنین کاربرانی با سطح اعتماد پایین‌تر است. کنترل‌های فهرست‌شده در ادامه باید اعمال یا ممنوع شوند:

{{< note >}}
در این جدول، نویسه‌های عام (`*`) به همه‌ی عناصر یک فهرست اشاره دارند. برای مثال، `spec.containers[*].securityContext` به آبجکت Security Context برای _همه‌ی کانتینرهای تعریف‌شده_ اشاره می‌کند. اگر هر یک از کانتینرهای فهرست‌شده الزامات را برآورده نکند، کل پاد در اعتبارسنجی رد می‌شود.
{{< /note >}}

<table>
	<caption style="display:none">مشخصات سیاست Restricted</caption>
	<tbody>
		<tr>
			<td><strong>کنترل</strong></td>
			<td><strong>سیاست</strong></td>
		</tr>
		<tr>
			<td colspan="2"><em>همه‌ی موارد سیاست Baseline</em></td>
		</tr>
		<tr>
			<td style="white-space: nowrap">انواع حجم</td>
			<td>
				<p>سیاست Restricted فقط انواع حجم زیر را مجاز می‌داند.</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.volumes[*]</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				هر مورد در فهرست <code>spec.volumes[*]</code> باید یکی از فیلدهای زیر را با مقداری غیرتهی تنظیم کند:
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
			<td style="white-space: nowrap">ارتقای سطح دسترسی (نسخه‌ی 1.8 به بعد)</td>
			<td>
				<p>ارتقای سطح دسترسی (برای مثال از طریق حالت فایل set-user-ID یا set-group-ID) نباید مجاز باشد. <em>از نسخه‌ی 1.25 به بعد، <a href="#os-specific-policy-controls">این سیاست فقط مخصوص لینوکس است</a> <code>(spec.os.name != windows)</code></em></p>
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
			<td style="white-space: nowrap">اجرا با کاربر غیر root</td>
			<td>
				<p>کانتینرها باید ملزم به اجرا با کاربران غیر root باشند.</p>
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
					اگر فیلد سطح پاد یعنی
					<code>spec.securityContext.runAsNonRoot</code> روی <code>true</code> تنظیم شده باشد، فیلدهای کانتینر می‌توانند تعریف‌نشده یا <code>nil</code> باشند.
				</small>
			</td>
		</tr>
		<tr>
			<td style="white-space: nowrap">اجرا با شناسه‌ی کاربری غیر root (نسخه‌ی 1.23 به بعد)</td>
			<td>
				<p>کانتینرها نباید <tt>runAsUser</tt> را روی 0 تنظیم کنند.</p>
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
  			<td style="white-space: nowrap">Seccomp (نسخه‌ی 1.19 به بعد)</td>
  			<td>
  				<p>پروفایل Seccomp باید به‌صراحت روی یکی از مقادیر مجاز تنظیم شود. هم پروفایل <code>Unconfined</code> و هم <em>نبودِ</em> پروفایل ممنوع است. <em>از نسخه‌ی 1.25 به بعد، <a href="#os-specific-policy-controls">این سیاست فقط مخصوص لینوکس است</a> <code>(spec.os.name != windows)</code></em></p>
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
					اگر فیلد سطح پاد یعنی
					<code>spec.securityContext.seccompProfile.type</code> به‌درستی تنظیم شده باشد، فیلدهای کانتینر می‌توانند تعریف‌نشده یا <code>nil</code> باشند.
					برعکس، اگر _همه‌ی_ فیلدهای سطح کانتینر تنظیم شده باشند، فیلد سطح پاد می‌تواند تعریف‌نشده یا <code>nil</code> باشد.
				</small>
  			</td>
  		</tr>
		  <tr>
			<td style="white-space: nowrap">قابلیت‌ها (نسخه‌ی 1.22 به بعد)</td>
			<td>
				<p>
					کانتینرها باید <code>ALL</code> قابلیت‌ها را کنار بگذارند و فقط مجازند
 					قابلیت <code>NET_BIND_SERVICE</code> را دوباره اضافه کنند. <em>از نسخه‌ی 1.25 به بعد، <a href="#os-specific-policy-controls">این سیاست فقط مخصوص لینوکس است</a> <code>(.spec.os.name != "windows")</code></em>
				</p>
				<p><strong>فیلدهای محدودشده</strong></p>
				<ul>
					<li><code>spec.containers[*].securityContext.capabilities.drop</code></li>
					<li><code>spec.initContainers[*].securityContext.capabilities.drop</code></li>
					<li><code>spec.ephemeralContainers[*].securityContext.capabilities.drop</code></li>
				</ul>
				<p><strong>مقادیر مجاز</strong></p>
				<ul>
					<li>هر فهرستی از قابلیت‌ها که شامل <code>ALL</code> باشد</li>
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
					<li>تعریف‌نشده/nil</li>
					<li><code>NET_BIND_SERVICE</code></li>
				</ul>
			</td>
		</tr>
	</tbody>
</table>

## پیاده‌سازی سیاست‌ها

جدا کردن تعریف سیاست از پیاده‌سازی آن باعث می‌شود درک مشترک و زبانی یکسان از سیاست‌ها در همه‌ی کلاسترها شکل بگیرد، فارغ از اینکه سازوکار اعمال آن‌ها در لایه‌ی زیرین چه باشد.

با بلوغ سازوکارها، آن‌ها در ادامه به تفکیک هر سیاست تعریف خواهند شد. روش‌های اعمال هر یک از سیاست‌ها در اینجا تعریف نشده‌اند.

[**کنترل‌کننده‌ی پذیرش امنیت پاد (Pod Security Admission Controller)**](/docs/concepts/security/pod-security-admission/)

- {{< example file="security/podsecurity-privileged.yaml" >}}فضای نام Privileged{{< /example >}}
- {{< example file="security/podsecurity-baseline.yaml" >}}فضای نام Baseline{{< /example >}}
- {{< example file="security/podsecurity-restricted.yaml" >}}فضای نام Restricted{{< /example >}}

### جایگزین‌ها

{{% thirdparty-content %}}

جایگزین‌های دیگری برای اعمال سیاست‌ها در اکوسیستم کوبرنتیز در حال توسعه هستند، از جمله:

- [Kubewarden](https://github.com/kubewarden)
- [Kyverno](https://kyverno.io/policies)
- [OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper)

## فیلد سیستم‌عامل پاد

کوبرنتیز به شما امکان می‌دهد از نودهایی استفاده کنید که لینوکس یا ویندوز اجرا می‌کنند. می‌توانید هر دو نوع نود را در یک کلاستر ترکیب کنید.
ویندوز در کوبرنتیز در مقایسه با بارهای کاری مبتنی بر لینوکس محدودیت‌ها و تفاوت‌هایی دارد. به‌طور مشخص، بسیاری از فیلدهای `securityContext` پاد
[در ویندوز هیچ اثری ندارند](/docs/concepts/windows/intro/#compatibility-v1-pod-spec-containers-securitycontext).

{{< note >}}
نسخه‌های kubelet پیش از 1.24 فیلد سیستم‌عامل پاد را اعمال نمی‌کنند. بنابراین اگر کلاستری نودهایی با نسخه‌های پیش از 1.24 داشته باشد، سیاست‌های Restricted باید روی نسخه‌ای پیش از 1.25 ثابت شوند.
{{< /note >}}

### تغییرات استاندارد امنیت پاد Restricted
تغییر مهم دیگری که در کوبرنتیز نسخه‌ی 1.25 انجام شد این است که سیاست _Restricted_ به‌روزرسانی شده تا از فیلد `pod.spec.os.name` استفاده کند. بر اساس نام سیستم‌عامل، برخی سیاست‌ها که مختص یک سیستم‌عامل خاص هستند می‌توانند برای سیستم‌عامل دیگر سهل‌گیرانه‌تر اعمال شوند.

#### کنترل‌های سیاست مختص سیستم‌عامل
محدودیت‌های مربوط به کنترل‌های زیر فقط زمانی الزامی است که مقدار `.spec.os.name` برابر `windows` نباشد:
- ارتقای سطح دسترسی
- Seccomp
- قابلیت‌های لینوکس

## فضاهای نام کاربری

فضاهای نام کاربری (User Namespaces) قابلیتی مختص لینوکس برای اجرای بارهای کاری با جداسازی بیشتر هستند. نحوه‌ی تعامل آن‌ها با استانداردهای امنیت پاد در [مستندات](/docs/concepts/workloads/pods/user-namespaces#integration-with-pod-security-admission-checks) مربوط به پادهایی که از فضاهای نام کاربری استفاده می‌کنند شرح داده شده است.

## پرسش‌های متداول

### چرا پروفایلی بین Privileged و Baseline وجود ندارد؟

سه پروفایلی که در اینجا تعریف شده‌اند روندی خطی و روشن از امن‌ترین (Restricted) تا کم‌امن‌ترین (Privileged) دارند و طیف گسترده‌ای از بارهای کاری را پوشش می‌دهند. دسترسی‌هایی که فراتر از سیاست Baseline لازم می‌شوند معمولاً کاملاً به برنامه وابسته‌اند، به همین دلیل در این حوزه پروفایل استانداردی ارائه نمی‌کنیم. این به آن معنا نیست که در چنین حالتی همیشه باید از پروفایل Privileged استفاده کرد، بلکه سیاست‌های این حوزه باید به‌صورت موردی تعریف شوند.

اگر در آینده نیاز روشنی به پروفایل‌های دیگر پدید آید، SIG Auth ممکن است در این موضع تجدیدنظر کند.

### تفاوت پروفایل امنیتی با زمینه‌ی امنیتی چیست؟

[زمینه‌های امنیتی (Security Contexts)](/docs/tasks/configure-pod-container/security-context/) پادها و کانتینرها را در زمان اجرا پیکربندی می‌کنند. زمینه‌های امنیتی به‌عنوان بخشی از مشخصات پاد و کانتینر در مانیفست پاد تعریف می‌شوند و پارامترهایی را برای محیط اجرای کانتینر نشان می‌دهند.

پروفایل‌های امنیتی سازوکارهایی در control plane هستند که تنظیمات مشخصی را در Security Context و همچنین پارامترهای مرتبط دیگری خارج از آن اعمال می‌کنند. از ژوئیه‌ی ۲۰۲۱،
[سیاست‌های امنیت پاد (Pod Security Policies)](/docs/concepts/security/pod-security-policy/) به نفع
[کنترل‌کننده‌ی پذیرش امنیت پاد](/docs/concepts/security/pod-security-admission/) داخلی منسوخ شده‌اند.


### پادهای سندباکس‌شده چه وضعیتی دارند؟

در حال حاضر هیچ استاندارد API وجود ندارد که تعیین کند یک پاد سندباکس‌شده به شمار می‌آید یا نه. پادهای سندباکس‌شده را می‌توان از روی استفاده از یک محیط اجرای سندباکس‌شده (مانند gVisor یا Kata Containers) شناسایی کرد، اما تعریف استانداردی برای محیط اجرای سندباکس‌شده وجود ندارد.

حفاظت‌های لازم برای بارهای کاری سندباکس‌شده ممکن است با سایر بارهای کاری متفاوت باشد. برای مثال، وقتی بار کاری از هسته‌ی زیرین جدا شده باشد، نیاز به محدود کردن دسترسی‌های ممتاز کمتر می‌شود. به این ترتیب، بارهای کاری‌ای که به دسترسی‌های بالاتری نیاز دارند همچنان می‌توانند جداسازی‌شده باقی بمانند.

افزون بر این، حفاظت از بارهای کاری سندباکس‌شده به‌شدت به روش سندباکس‌سازی وابسته است. از این رو، هیچ پروفایل واحدی برای همه‌ی بارهای کاری سندباکس‌شده توصیه نمی‌شود.
