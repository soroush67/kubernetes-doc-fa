---
content_type: concept
title: مشارکت در مستندات کوبرنتیز
weight: 09
card:
  name: contribute
  weight: 11
  title: مشارکت در مستندات
---


این وب‌سایت توسط [Kubernetes SIG Docs](/docs/contribute/#get-involved-with-sig-docs) نگهداری می‌شود.
پروژه کوبرنتیز از کمک همه مشارکت‌کنندگان، چه تازه‌کار و چه باتجربه، استقبال می‌کند!

مشارکت‌کنندگان مستندات کوبرنتیز:

- محتوای موجود را بهبود می‌دهند
- محتوای جدید تولید می‌کنند
- مستندات را ترجمه می‌کنند
- بخش‌های مربوط به مستندات را در چرخه انتشار کوبرنتیز مدیریت و منتشر می‌کنند

تیم وبلاگ، که بخشی از SIG Docs است، در مدیریت وبلاگ‌های رسمی کمک می‌کند. برای کسب اطلاعات بیشتر،
[مشارکت در وبلاگ‌های کوبرنتیز](/docs/contribute/blog/) را بخوانید.

---

{{< note >}}
برای کسب اطلاعات بیشتر درباره مشارکت در کوبرنتیز به‌طور کلی، به وب‌سایت
[مستندات عمومی مشارکت‌کنندگان](https://www.kubernetes.dev/docs/) مراجعه کنید.
{{< /note >}}


<!-- body -->

## شروع کار

هر کسی می‌تواند درباره مستندات یک issue باز کند یا با ارسال یک
pull request (PR) به
[مخزن GitHub با نام `kubernetes/website`](https://github.com/kubernetes/website)
تغییری را ارائه دهد.
برای فعالیت مؤثر در جامعه کوبرنتیز باید با
[git](https://git-scm.com/) و
[GitHub](https://skills.github.com/)
آشنایی کافی داشته باشید.

برای مشارکت در مستندات:

1. [موافقت‌نامه مجوز مشارکت‌کننده](https://github.com/kubernetes/community/blob/main/CLA.md) (Contributor License Agreement) بنیاد CNCF را امضا کنید.
2. با [مخزن مستندات](https://github.com/kubernetes/website)
   و [مولد سایت ایستا](https://gohugo.io) وب‌سایت آشنا شوید.
3. مطمئن شوید که فرایندهای پایه‌ای
   [باز کردن یک pull request](/docs/contribute/new-content/open-a-pr/) و
   [بازبینی تغییرات](/docs/contribute/review/reviewing-prs/) را درک کرده‌اید.

<!-- See https://github.com/kubernetes/website/issues/28808 for live-editor URL to this figure -->
<!-- You can also cut/paste the mermaid code into the live editor at https://mermaid-js.github.io/mermaid-live-editor to play around with it -->

{{< mermaid >}}
flowchart TB
subgraph third[Open PR]
direction TB
U[ ] -.-
Q[Improve content] --- N[Create content]
N --- O[Translate docs]
O --- P[Manage/publish docs parts<br>of K8s release cycle]

end

subgraph second[Review]
direction TB
   T[ ] -.-
   D[Look over the<br>kubernetes/website<br>repository] --- E[Check out the<br>Hugo static site<br>generator]
   E --- F[Understand basic<br>GitHub commands]
   F --- G[Review open PR<br>and change review <br>processes]
end

subgraph first[Sign up]
    direction TB
    S[ ] -.-
    B[Sign the CNCF<br>Contributor<br>License Agreement] --- C[Join sig-docs<br>Slack channel] 
    C --- V[Join kubernetes-sig-docs<br>mailing list]
    V --- M[Attend weekly<br>sig-docs calls<br>or slack meetings]
end

A([fa:fa-user New<br>Contributor]) --> first
A --> second
A --> third
A --> H[Ask Questions!!!]


classDef grey fill:#dddddd,stroke:#ffffff,stroke-width:px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:px,color:#000,font-weight:bold
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
class A,B,C,D,E,F,G,H,M,Q,N,O,P,V grey
class S,T,U spacewhite
class first,second,third white
{{</ mermaid >}}
شکل ۱. شروع کار برای یک مشارکت‌کننده جدید.

شکل ۱ نقشه راهی برای مشارکت‌کنندگان جدید را نشان می‌دهد. می‌توانید برخی یا همه مراحل `Sign up` و `Review` را دنبال کنید. اکنون آماده‌اید PRهایی باز کنید که اهداف مشارکت شما را محقق می‌کنند؛ برخی از این اهداف در بخش `Open PR` فهرست شده‌اند. باز هم تأکید می‌کنیم که پرسش‌های شما همیشه خوش‌آمد است!

برخی وظایف به اعتماد و دسترسی بیشتری در سازمان کوبرنتیز نیاز دارند.
برای جزئیات بیشتر درباره نقش‌ها و مجوزها، [مشارکت در SIG Docs](/docs/contribute/participate/) را ببینید.

## نخستین مشارکت شما

می‌توانید با مرور چند مرحله از پیش، برای نخستین مشارکت خود آماده شوید.
شکل ۲ مراحل را نشان می‌دهد و جزئیات در ادامه آمده است.

<!-- See https://github.com/kubernetes/website/issues/28808 for live-editor URL to this figure -->
<!-- You can also cut/paste the mermaid code into the live editor at https://mermaid-js.github.io/mermaid-live-editor to play around with it -->

{{< mermaid >}}
flowchart LR
    subgraph second[First Contribution]
    direction TB
    S[ ] -.-
    G[Review PRs from other<br>K8s members] -->
    A[Check kubernetes/website<br>issues list for<br>good first PRs] --> B[Open a PR!!]
    end
    subgraph first[Suggested Prep]
    direction TB
       T[ ] -.-
       D[Read contribution overview] -->E[Read K8s content<br>and style guides]
       E --> F[Learn about Hugo page<br>content types<br>and shortcodes]
    end
    

    first ----> second
     

classDef grey fill:#dddddd,stroke:#ffffff,stroke-width:px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:px,color:#000,font-weight:bold
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
class A,B,D,E,F,G grey
class S,T spacewhite
class first,second white
{{</ mermaid >}}
شکل ۲. آماده‌سازی برای نخستین مشارکت شما.

- [مرور کلی مشارکت](/docs/contribute/new-content/) را بخوانید تا
  با روش‌های مختلف مشارکت آشنا شوید.
- [فهرست issueهای `kubernetes/website`](https://github.com/kubernetes/website/issues/)
  را بررسی کنید تا issueهایی را که نقطه شروع مناسبی هستند بیابید.
- [با استفاده از GitHub یک pull request باز کنید](/docs/contribute/new-content/open-a-pr/#changes-using-github)
  برای مستندات موجود و درباره ثبت issue در GitHub بیشتر بیاموزید.
- pull requestهای سایر اعضای جامعه کوبرنتیز را از نظر صحت و زبان
  [بازبینی کنید](/docs/contribute/review/reviewing-prs/).
- [راهنمای محتوا](/docs/contribute/style/content-guide/) و
  [راهنمای سبک نگارش](/docs/contribute/style/style-guide/) کوبرنتیز را بخوانید تا بتوانید نظرات آگاهانه ارائه دهید.
- درباره [انواع محتوای صفحه](/docs/contribute/style/page-content-types/)
  و [shortcodeهای Hugo](/docs/contribute/style/hugo-shortcodes/) بیاموزید.

## دریافت کمک هنگام مشارکت

انجام نخستین مشارکت می‌تواند دشوار به نظر برسد.
[سفیران مشارکت‌کنندگان جدید](https://github.com/kubernetes/website#new-contributor-ambassadors)
در کنار شما هستند تا شما را در انجام چند مشارکت نخست راهنمایی کنند. می‌توانید در
[Slack کوبرنتیز](https://slack.k8s.io/)، ترجیحاً در کانال `#sig-docs`، با آن‌ها در ارتباط باشید. همچنین
[جلسه معارفه و آشنایی مشارکت‌کنندگان جدید](https://www.kubernetes.dev/resources/calendar/)
در اولین سه‌شنبه هر ماه برگزار می‌شود. در این جلسه می‌توانید با سفیران مشارکت‌کنندگان جدید تعامل کنید
و پرسش‌های خود را حل کنید.

## مشارکت در SIG Docs

[SIG Docs](/docs/contribute/participate/) گروهی از مشارکت‌کنندگان است که
مستندات کوبرنتیز و وب‌سایت را منتشر و نگهداری می‌کنند. مشارکت در
SIG Docs راهی عالی برای مشارکت‌کنندگان کوبرنتیز (چه در توسعه قابلیت‌ها و چه در سایر حوزه‌ها) است تا
تأثیر بزرگی بر پروژه کوبرنتیز بگذارند.

SIG Docs از روش‌های مختلفی برای ارتباط استفاده می‌کند:

- [به کانال `#sig-docs` در Slack کوبرنتیز بپیوندید](https://slack.k8s.io/). حتماً
  خودتان را معرفی کنید!
- [به فهرست پستی `kubernetes-sig-docs` بپیوندید](https://groups.google.com/forum/#!forum/kubernetes-sig-docs)،
  که بحث‌های گسترده‌تر در آن انجام می‌شود و تصمیم‌های رسمی در آن ثبت می‌گردد.
- در [جلسه ویدیویی SIG Docs](https://github.com/kubernetes/community/tree/main/sig-docs)
  که هر دو هفته یک بار برگزار می‌شود شرکت کنید. این جلسات همیشه در `#sig-docs` اطلاع‌رسانی می‌شوند و به
  [تقویم جلسات جامعه کوبرنتیز](https://calendar.google.com/calendar/embed?src=cgnt364vd8s86hr2phapfjc6uk%40group.calendar.google.com&ctz=America/Los_Angeles)
  افزوده می‌شوند.
  باید [کلاینت Zoom](https://zoom.us/download) را دانلود کنید یا از طریق تلفن تماس بگیرید.
- در هفته‌هایی که جلسه ویدیویی Zoom به‌صورت زنده برگزار نمی‌شود، در جلسه استندآپ ناهمگام SIG Docs در Slack شرکت کنید. این جلسات همیشه در `#sig-docs` اطلاع‌رسانی می‌شوند.
  تا ۲۴ ساعت پس از اعلام جلسه می‌توانید در هر یک از رشته‌گفتگوها (thread) مشارکت کنید.

## سایر روش‌های مشارکت

- از [وب‌سایت جامعه کوبرنتیز](/community/) دیدن کنید. در Twitter یا Stack Overflow شرکت کنید،
  درباره میت‌آپ‌ها و رویدادهای محلی کوبرنتیز بیاموزید و موارد دیگر.
- [برگه تقلب مشارکت‌کنندگان](https://www.kubernetes.dev/docs/contributor-cheatsheet/)
  را بخوانید تا در توسعه قابلیت‌های کوبرنتیز مشارکت کنید.
- از وب‌سایت مشارکت‌کنندگان دیدن کنید تا درباره [مشارکت‌کنندگان کوبرنتیز](https://www.kubernetes.dev/)
  و [منابع بیشتر برای مشارکت‌کنندگان](https://www.kubernetes.dev/resources/) بیشتر بیاموزید.
- بیاموزید چگونه [در وبلاگ‌های رسمی مشارکت کنید](/docs/contribute/blog/)
- یک [مطالعه موردی](/docs/contribute/new-content/case-studies/) ارسال کنید

## گام‌های بعدی

- بیاموزید چگونه [از یک کپی محلی (clone)](/docs/contribute/new-content/open-a-pr/#fork-the-repo)
  از مخزن کار کنید.
- [قابلیت‌های یک نسخه](/docs/contribute/new-content/new-features/) را مستندسازی کنید.
- در [SIG Docs](/docs/contribute/participate/) مشارکت کنید و
  [عضو یا بازبین](/docs/contribute/participate/roles-and-responsibilities/) شوید.

- در [بومی‌سازی](/docs/contribute/localization/) مستندات شروع به کار کنید یا به آن کمک کنید.
