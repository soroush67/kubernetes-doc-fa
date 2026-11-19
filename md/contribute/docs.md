---
content_type: concept
title: مشارکت در مستندات کوبرنتیز
weight: 09
card:
  name: contribute
  weight: 11
  title: مشارکت در مستندات
---


نگهداری این وب‌سایت بر عهدهٔ [SIG Docs کوبرنتیز](/docs/contribute/#get-involved-with-sig-docs) است.
پروژهٔ کوبرنتیز از کمک همهٔ مشارکت‌کنندگان، چه تازه‌کار و چه باتجربه، استقبال می‌کند!

مشارکت‌کنندگان مستندات کوبرنتیز این کارها را انجام می‌دهند:

- بهبود محتوای موجود
- ایجاد محتوای جدید
- ترجمهٔ مستندات
- مدیریت و انتشار بخش‌های مربوط به مستندات در چرخهٔ انتشار کوبرنتیز

تیم وبلاگ که بخشی از SIG Docs است، در مدیریت وبلاگ‌های رسمی کمک می‌کند. برای آگاهی بیشتر،
[مشارکت در وبلاگ‌های کوبرنتیز](/docs/contribute/blog/) را بخوانید.

---

{{< note >}}
برای آگاهی بیشتر دربارهٔ مشارکت در کوبرنتیز به‌طور کلی، به وب‌سایت عمومی
[مستندات مشارکت‌کنندگان](https://www.kubernetes.dev/docs/) مراجعه کنید.
{{< /note >}}


<!-- body -->

## شروع کار

هر کسی می‌تواند دربارهٔ مستندات یک issue باز کند یا با ارسال یک درخواست ادغام (pull request یا PR) به
[مخزن GitHub `kubernetes/website`](https://github.com/kubernetes/website) تغییری را پیشنهاد دهد.
برای اینکه بتوانید در جامعهٔ کوبرنتیز به‌طور مؤثر کار کنید، باید با
[git](https://git-scm.com/) و
[GitHub](https://skills.github.com/)
آشنایی کافی داشته باشید.

برای مشارکت در مستندات:

1. [توافق‌نامهٔ مجوز مشارکت‌کننده](https://github.com/kubernetes/community/blob/main/CLA.md) (CLA) بنیاد CNCF را امضا کنید.
2. با [مخزن مستندات](https://github.com/kubernetes/website)
   و [تولیدکنندهٔ سایت ایستای](https://gohugo.io) وب‌سایت آشنا شوید.
3. مطمئن شوید که فرایندهای پایه‌ای
   [باز کردن یک درخواست ادغام](/docs/contribute/new-content/open-a-pr/) و
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
شکل ۱. شروع کار برای یک مشارکت‌کنندهٔ تازه‌وارد.

شکل ۱ نقشهٔ راهی را برای مشارکت‌کنندگان تازه‌وارد ترسیم می‌کند. می‌توانید برخی یا همهٔ
گام‌های بخش‌های `Sign up` (ثبت‌نام) و `Review` (بازبینی) را دنبال کنید. پس از آن آماده‌اید
درخواست‌های ادغامی باز کنید که به اهداف مشارکت شما دست یابند؛ برخی از این اهداف در بخش
`Open PR` (باز کردن PR) فهرست شده‌اند. باز هم تأکید می‌کنیم که پرسیدن همیشه پذیرفته است!

برخی کارها به اعتماد و سطح دسترسی بیشتری در سازمان کوبرنتیز نیاز دارند.
برای جزئیات بیشتر دربارهٔ نقش‌ها و مجوزها، به [مشارکت در SIG Docs](/docs/contribute/participate/) مراجعه کنید.

## نخستین مشارکت شما

می‌توانید با مرور چند گام از پیش، برای نخستین مشارکت خود آماده شوید.
شکل ۲ این گام‌ها را نشان می‌دهد و جزئیات آن‌ها در ادامه آمده است.

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
شکل ۲. آمادگی برای نخستین مشارکت شما.

- [نمای کلی مشارکت](/docs/contribute/new-content/) را بخوانید تا با
  روش‌های گوناگون مشارکت آشنا شوید.
- [فهرست issueهای `kubernetes/website`](https://github.com/kubernetes/website/issues/)
  را برای یافتن issueهایی که نقطهٔ شروع مناسبی هستند بررسی کنید.
- برای مستندات موجود
  [با استفاده از GitHub یک درخواست ادغام باز کنید](/docs/contribute/new-content/open-a-pr/#changes-using-github)
  و دربارهٔ ثبت issue در GitHub بیشتر بیاموزید.
- [درخواست‌های ادغام](/docs/contribute/review/reviewing-prs/) سایر اعضای جامعهٔ
  کوبرنتیز را از نظر درستی و نگارش بازبینی کنید.
- [راهنمای محتوا](/docs/contribute/style/content-guide/) و
  [راهنمای سبک نگارش](/docs/contribute/style/style-guide/) کوبرنتیز را بخوانید تا بتوانید نظرهای آگاهانه بدهید.
- با [انواع محتوای صفحه](/docs/contribute/style/page-content-types/)
  و [شورت‌کدهای Hugo](/docs/contribute/style/hugo-shortcodes/) آشنا شوید.

## دریافت کمک هنگام مشارکت

انجام نخستین مشارکت ممکن است دشوار و طاقت‌فرسا به نظر برسد.
[سفیران مشارکت‌کنندگان تازه‌وارد](https://github.com/kubernetes/website#new-contributor-ambassadors)
آماده‌اند تا شما را در انجام چند مشارکت نخست همراهی کنند. می‌توانید در
[Slack کوبرنتیز](https://slack.k8s.io/)، ترجیحاً در کانال `#sig-docs`، با آن‌ها در تماس باشید.
افزون بر این، [جلسهٔ آشنایی با مشارکت‌کنندگان تازه‌وارد](https://www.kubernetes.dev/resources/calendar/)
در نخستین سه‌شنبهٔ هر ماه برگزار می‌شود. در این جلسه می‌توانید با سفیران مشارکت‌کنندگان
تازه‌وارد گفتگو کنید و پاسخ پرسش‌های خود را بگیرید.

## مشارکت در SIG Docs

[SIG Docs](/docs/contribute/participate/) گروهی از مشارکت‌کنندگان است که
مستندات و وب‌سایت کوبرنتیز را منتشر و نگهداری می‌کنند. مشارکت در SIG Docs
راهی عالی برای مشارکت‌کنندگان کوبرنتیز (چه در توسعهٔ قابلیت‌ها و چه در زمینه‌های دیگر)
است تا تأثیر چشمگیری بر پروژهٔ کوبرنتیز بگذارند.

اعضای SIG Docs از روش‌های گوناگونی با یکدیگر ارتباط برقرار می‌کنند:

- [به کانال `#sig-docs` در Slack کوبرنتیز بپیوندید](https://slack.k8s.io/). حتماً
  خودتان را معرفی کنید!
- [به فهرست پستی `kubernetes-sig-docs` بپیوندید](https://groups.google.com/forum/#!forum/kubernetes-sig-docs)؛
  گفتگوهای گسترده‌تر در این فهرست انجام می‌شود و تصمیم‌های رسمی در آن ثبت می‌شوند.
- در [جلسهٔ ویدئویی SIG Docs](https://github.com/kubernetes/community/tree/main/sig-docs)
  که هر دو هفته یک بار برگزار می‌شود شرکت کنید. این جلسه‌ها همیشه در `#sig-docs` اطلاع‌رسانی
  و به [تقویم جلسه‌های جامعهٔ کوبرنتیز](https://calendar.google.com/calendar/embed?src=cgnt364vd8s86hr2phapfjc6uk%40group.calendar.google.com&ctz=America/Los_Angeles)
  افزوده می‌شوند. برای شرکت در جلسه باید [نرم‌افزار Zoom](https://zoom.us/download) را بارگیری کنید یا با تلفن به جلسه وصل شوید.
- در هفته‌هایی که جلسهٔ ویدئویی حضوری در Zoom برگزار نمی‌شود، در جلسهٔ کوتاه ناهمگام
  (async standup) SIG Docs در Slack شرکت کنید. این جلسه‌ها نیز همیشه در `#sig-docs` اطلاع‌رسانی می‌شوند.
  تا ۲۴ ساعت پس از اعلام جلسه می‌توانید در هر یک از رشته‌گفتگوها مشارکت کنید.

## راه‌های دیگر مشارکت

- از [وب‌سایت جامعهٔ کوبرنتیز](/community/) دیدن کنید. در Twitter یا Stack Overflow فعالیت کنید،
  با گردهمایی‌ها و رویدادهای محلی کوبرنتیز آشنا شوید و کارهای بسیار دیگری انجام دهید.
- برای مشارکت در توسعهٔ قابلیت‌های کوبرنتیز،
  [برگهٔ راهنمای سریع مشارکت‌کنندگان](https://www.kubernetes.dev/docs/contributor-cheatsheet/) را بخوانید.
- برای آگاهی بیشتر دربارهٔ [مشارکت‌کنندگان کوبرنتیز](https://www.kubernetes.dev/)
  و [منابع بیشتر برای مشارکت‌کنندگان](https://www.kubernetes.dev/resources/)، از وب‌سایت مشارکت‌کنندگان دیدن کنید.
- با چگونگی [مشارکت در وبلاگ‌های رسمی](/docs/contribute/blog/) آشنا شوید.
- یک [مطالعهٔ موردی](/docs/contribute/new-content/case-studies/) ارسال کنید.

## گام‌های بعدی

- بیاموزید چگونه [با یک نسخهٔ محلی (clone)](/docs/contribute/new-content/open-a-pr/#fork-the-repo)
  از مخزن کار کنید.
- [قابلیت‌های یک نسخهٔ انتشار](/docs/contribute/new-content/new-features/) را مستند کنید.
- در [SIG Docs](/docs/contribute/participate/) مشارکت کنید و
  [عضو یا بازبین](/docs/contribute/participate/roles-and-responsibilities/) شوید.
                       
- یک [بومی‌سازی](/docs/contribute/localization/) را آغاز کنید یا در آن کمک کنید.
