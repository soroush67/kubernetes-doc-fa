---
reviewers:
- tallclair
- liggitt
title: نگاشت PodSecurityPolicyها به Pod Security Standards
content_type: concept
weight: 95
---

<!-- overview -->
جدول‌های زیر پارامترهای پیکربندی آبجکت‌های `PodSecurityPolicy` را فهرست می‌کنند، و نشان می‌دهند که
هر فیلد پادها را تغییر می‌دهد (mutate) و/یا اعتبارسنجی می‌کند، و مقادیر پیکربندی چگونه به
[Pod Security Standards](/docs/concepts/security/pod-security-standards/) نگاشت می‌شوند.

برای هر پارامتر مرتبط، مقادیر مجاز برای پروفایل‌های
[Baseline](/docs/concepts/security/pod-security-standards/#baseline) و
[Restricted](/docs/concepts/security/pod-security-standards/#restricted) فهرست شده است.
هر مقداری خارج از مقادیر مجاز آن پروفایل‌ها در دسته‌ی پروفایل
[Privileged](/docs/concepts/security/pod-security-standards/#privileged) قرار می‌گیرد. عبارت «No opinion»
به این معناست که همه‌ی مقادیر در تمامی Pod Security Standards مجاز هستند.

برای مشاهده‌ی راهنمای گام‌به‌گام مهاجرت، به
[مهاجرت از PodSecurityPolicy به کنترل‌کننده‌ی پذیرش داخلی PodSecurity](/docs/tasks/configure-pod-container/migrate-from-psp/)
مراجعه کنید.

<!-- body -->

## مشخصات PodSecurityPolicy (PodSecurityPolicy Spec) {#podsecuritypolicy-spec}

فیلدهای فهرست‌شده در این جدول بخشی از `PodSecurityPolicySpec` هستند که
در مسیر فیلد `.spec` مشخص می‌شود.

<table class="no-word-break">
  <caption style="display:none">نگاشت فیلدهای PodSecurityPolicySpec به Pod Security Standards</caption>
  <tbody>
    <tr>
      <th><code>PodSecurityPolicySpec</code></th>
      <th>نوع</th>
      <th>معادل در Pod Security Standards</th>
    </tr>
    <tr>
      <td><code>privileged</code></td>
      <td>اعتبارسنجی (Validating)</td>
      <td><b>Baseline و Restricted</b>: <code>false</code> / تعریف‌نشده / nil</td>
    </tr>
    <tr>
      <td><code>defaultAddCapabilities</code></td>
      <td>تغییر‌دهنده و اعتبارسنج (Mutating & Validating)</td>
      <td>الزامات با <code>allowedCapabilities</code> در ادامه یکسان است.</td>
    </tr>
    <tr>
      <td><code>allowedCapabilities</code></td>
      <td>اعتبارسنجی (Validating)</td>
      <td>
        <p><b>Baseline</b>: زیرمجموعه‌ای از</p>
        <ul>
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
        <p><b>Restricted</b>: خالی / تعریف‌نشده / nil یا فهرستی که <i>فقط</i> شامل <code>NET_BIND_SERVICE</code> باشد
      </td>
    </tr>
    <tr>
      <td><code>requiredDropCapabilities</code></td>
      <td>تغییر‌دهنده و اعتبارسنج (Mutating & Validating)</td>
      <td>
        <p><b>Baseline</b>: بدون نظر (no opinion)</p>
        <p><b>Restricted</b>: باید شامل <code>ALL</code> باشد</p>
      </td>
    </tr>
    <tr>
      <td><code>volumes</code></td>
      <td>اعتبارسنجی (Validating)</td>
      <td>
        <p><b>Baseline</b>: هر مقداری به‌جز</p>
        <ul>
          <li><code>hostPath</code></li>
          <li><code>*</code></li>
        </ul>
        <p><b>Restricted</b>: زیرمجموعه‌ای از</p>
        <ul>
          <li><code>configMap</code></li>
          <li><code>csi</code></li>
          <li><code>downwardAPI</code></li>
          <li><code>emptyDir</code></li>
          <li><code>ephemeral</code></li>
          <li><code>persistentVolumeClaim</code></li>
          <li><code>projected</code></li>
          <li><code>secret</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><code>hostNetwork</code></td>
      <td>اعتبارسنجی (Validating)</td>
      <td><b>Baseline و Restricted</b>: <code>false</code> / تعریف‌نشده / nil</td>
    </tr>
    <tr>
      <td><code>hostPorts</code></td>
      <td>اعتبارسنجی (Validating)</td>
      <td><b>Baseline و Restricted</b>: تعریف‌نشده / nil / خالی</td>
    </tr>
    <tr>
      <td><code>hostPID</code></td>
      <td>اعتبارسنجی (Validating)</td>
      <td><b>Baseline و Restricted</b>: <code>false</code> / تعریف‌نشده / nil</td>
    </tr>
    <tr>
      <td><code>hostIPC</code></td>
      <td>اعتبارسنجی (Validating)</td>
      <td><b>Baseline و Restricted</b>: <code>false</code> / تعریف‌نشده / nil</td>
    </tr>
    <tr>
      <td><code>seLinux</code></td>
      <td>تغییر‌دهنده و اعتبارسنج (Mutating & Validating)</td>
      <td>
        <p><b>Baseline و Restricted</b>:
        مقدار <code>seLinux.rule</code> برابر <code>MustRunAs</code> است، با <code>options</code> زیر</p>
        <ul>
          <li><code>user</code> تنظیم نشده است (<code>""</code> / تعریف‌نشده / nil)</li>
          <li><code>role</code> تنظیم نشده است (<code>""</code> / تعریف‌نشده / nil)</li>
          <li><code>type</code> تنظیم نشده است یا یکی از این مقادیر است: <code>container_t, container_init_t, container_kvm_t, container_engine_t</code></li>
          <li><code>level</code> هر مقداری می‌تواند باشد</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><code>runAsUser</code></td>
      <td>تغییر‌دهنده و اعتبارسنج (Mutating & Validating)</td>
      <td>
        <p><b>Baseline</b>: هر مقداری</p>
        <p><b>Restricted</b>: مقدار <code>rule</code> برابر <code>MustRunAsNonRoot</code> است</p>
      </td>
    </tr>
    <tr>
      <td><code>runAsGroup</code></td>
      <td>تغییر‌دهنده (MustRunAs) و اعتبارسنج (Mutating (MustRunAs) & Validating)</td>
      <td>
        <i>بدون نظر (No opinion)</i>
      </td>
    </tr>
    <tr>
      <td><code>supplementalGroups</code></td>
      <td>تغییر‌دهنده و اعتبارسنج (Mutating & Validating)</td>
      <td>
        <i>بدون نظر (No opinion)</i>
      </td>
    </tr>
    <tr>
      <td><code>fsGroup</code></td>
      <td>تغییر‌دهنده و اعتبارسنج (Mutating & Validating)</td>
      <td>
        <i>بدون نظر (No opinion)</i>
      </td>
    </tr>
    <tr>
      <td><code>readOnlyRootFilesystem</code></td>
      <td>تغییر‌دهنده و اعتبارسنج (Mutating & Validating)</td>
      <td>
        <i>بدون نظر (No opinion)</i>
      </td>
    </tr>
    <tr>
      <td><code>defaultAllowPrivilegeEscalation</code></td>
      <td>تغییر‌دهنده (Mutating)</td>
      <td>
        <i>بدون نظر (No opinion) (بدون اعتبارسنجی)</i>
      </td>
    </tr>
    <tr>
      <td><code>allowPrivilegeEscalation</code></td>
      <td>تغییر‌دهنده و اعتبارسنج (Mutating & Validating)</td>
      <td>
        <p><i>فقط در صورتی تغییر‌دهنده است که روی <code>false</code> تنظیم شده باشد</i></p>
        <p><b>Baseline</b>: بدون نظر (No opinion)</p>
        <p><b>Restricted</b>: <code>false</code></p>
      </td>
    </tr>
    <tr>
      <td><code>allowedHostPaths</code></td>
      <td>اعتبارسنجی (Validating)</td>
      <td><i>بدون نظر (No opinion) (فیلد volumes اولویت دارد)</i></td>
    </tr>
    <tr>
      <td><code>allowedFlexVolumes</code></td>
      <td>اعتبارسنجی (Validating)</td>
      <td><i>بدون نظر (No opinion) (فیلد volumes اولویت دارد)</i></td>
    </tr>
    <tr>
      <td><code>allowedCSIDrivers</code></td>
      <td>اعتبارسنجی (Validating)</td>
      <td><i>بدون نظر (No opinion) (فیلد volumes اولویت دارد)</i></td>
    </tr>
    <tr>
      <td><code>allowedUnsafeSysctls</code></td>
      <td>اعتبارسنجی (Validating)</td>
      <td><b>Baseline و Restricted</b>: تعریف‌نشده / nil / خالی</td>
    </tr>
    <tr>
      <td><code>forbiddenSysctls</code></td>
      <td>اعتبارسنجی (Validating)</td>
      <td><i>بدون نظر (No opinion)</i></td>
    </tr>
    <tr>
      <td><code>allowedProcMountTypes</code><br><i>(قابلیت آلفا)</i></td>
      <td>اعتبارسنجی (Validating)</td>
      <td><b>Baseline و Restricted</b>: <code>["Default"]</code> یا تعریف‌نشده / nil / خالی</td>
    </tr>
    <tr>
      <td><code>runtimeClass</code><br><code>&nbsp;.defaultRuntimeClassName</code></td>
      <td>تغییر‌دهنده (Mutating)</td>
      <td><i>بدون نظر (No opinion)</i></td>
    </tr>
    <tr>
      <td><code>runtimeClass</code><br><code>&nbsp;.allowedRuntimeClassNames</code></td>
      <td>اعتبارسنجی (Validating)</td>
      <td><i>بدون نظر (No opinion)</i></td>
    </tr>
  </tbody>
</table>

## حاشیه‌نویسی‌های PodSecurityPolicy (PodSecurityPolicy annotations) {#podsecuritypolicy-annotations}

[حاشیه‌نویسی‌های (annotations)](/docs/concepts/overview/working-with-objects/annotations/) فهرست‌شده در این
جدول را می‌توان در `.metadata.annotations` آبجکت PodSecurityPolicy مشخص کرد.

<table class="no-word-break">
  <caption style="display:none">نگاشت حاشیه‌نویسی‌های PodSecurityPolicy به Pod Security Standards</caption>
  <tbody>
    <tr>
      <th><code>PSP Annotation</code></th>
      <th>نوع</th>
      <th>معادل در Pod Security Standards</th>
    </tr>
    <tr>
      <td><code>seccomp.security.alpha.kubernetes.io</code><br><code>/defaultProfileName</code></td>
      <td>تغییر‌دهنده (Mutating)</td>
      <td><i>بدون نظر (No opinion)</i></td>
    </tr>
    <tr>
      <td><code>seccomp.security.alpha.kubernetes.io</code><br><code>/allowedProfileNames</code></td>
      <td>اعتبارسنجی (Validating)</td>
      <td>
        <p><b>Baseline</b>: <code>"runtime/default,"</code> <i>(کاما در انتها برای مجاز بودن حالت تنظیم‌نشده)</i></p>
        <p><b>Restricted</b>: <code>"runtime/default"</code> <i>(بدون کاما در انتها)</i></p>
        <p><i>مقادیر <code>localhost/*</code> نیز برای هر دو پروفایل Baseline و Restricted مجاز هستند.</i></p>
      </td>
    </tr>
    <tr>
      <td><code>apparmor.security.beta.kubernetes.io</code><br><code>/defaultProfileName</code></td>
      <td>تغییر‌دهنده (Mutating)</td>
      <td><i>بدون نظر (No opinion)</i></td>
    </tr>
    <tr>
      <td><code>apparmor.security.beta.kubernetes.io</code><br><code>/allowedProfileNames</code></td>
      <td>اعتبارسنجی (Validating)</td>
      <td>
        <p><b>Baseline</b>: <code>"runtime/default,"</code> <i>(کاما در انتها برای مجاز بودن حالت تنظیم‌نشده)</i></p>
        <p><b>Restricted</b>: <code>"runtime/default"</code> <i>(بدون کاما در انتها)</i></p>
        <p><i>مقادیر <code>localhost/*</code> نیز برای هر دو پروفایل Baseline و Restricted مجاز هستند.</i></p>
      </td>
    </tr>
  </tbody>
</table>
