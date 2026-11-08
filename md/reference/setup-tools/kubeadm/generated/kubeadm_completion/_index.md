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


### خلاصه



این دستور کد تکمیل خودکار شل را برای شل مشخص‌شده (bash یا zsh) تولید می‌کند. برای فعال شدن تکمیل تعاملی دستورهای kubeadm، باید این کد در شل ارزیابی شود. برای این کار می‌توانید آن را از طریق فایل .bash_profile با دستور source بارگذاری کنید.

توجه: این قابلیت به چارچوب bash-completion نیاز دارد.

برای نصب آن روی Mac از homebrew استفاده کنید:
    $ brew install bash-completion
پس از نصب، باید bash_completion ارزیابی شود. برای این کار می‌توانید خط زیر را به فایل .bash_profile اضافه کنید:
    $ source $(brew --prefix)/etc/bash_completion

اگر bash-completion روی Linux نصب نیست، بستهٔ 'bash-completion' را با مدیر بستهٔ توزیع خود نصب کنید.

نکته برای کاربران zsh: [1] تکمیل خودکار zsh فقط در نسخه‌های &gt;= 5.2 از zsh پشتیبانی می‌شود.

```
kubeadm completion SHELL [flags]
```

### نمونه‌ها

```

# Install bash completion on a Mac using homebrew
brew install bash-completion
printf "\n# Bash completion support\nsource $(brew --prefix)/etc/bash_completion\n" >> $HOME/.bash_profile
source $HOME/.bash_profile

# Load the kubeadm completion code for bash into the current shell
source <(kubeadm completion bash)

# Write bash completion code to a file and source it from .bash_profile
kubeadm completion bash > ~/.kube/kubeadm_completion.bash.inc
printf "\n# Kubeadm shell completion\nsource '$HOME/.kube/kubeadm_completion.bash.inc'\n" >> $HOME/.bash_profile
source $HOME/.bash_profile

# Load the kubeadm completion code for zsh[1] into the current shell
source <(kubeadm completion zsh)
```

### گزینه‌ها

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور completion را نمایش می‌دهد.</p></td>
</tr>

</tbody>
</table>



### گزینه‌های به‌ارث‌رسیده از دستورهای والد

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--rootfs string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سیستم‌فایل ریشهٔ «واقعی» میزبان را مشخص می‌کند. با تعیین این مسیر، kubeadm با chroot به آن وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
