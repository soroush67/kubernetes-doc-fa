### الزامات:

- به دستگاهی نیاز دارید که لینوکس یا macOS اجرا کند. در ویندوز از
  [زیرسیستم ویندوز برای لینوکس (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
  استفاده کنید، زیرا ابزارهای ساخت به `make` و اسکریپت‌های Bash وابسته هستند.

- باید این ابزارها نصب شده باشند:

  - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  - [Go](https://go.dev/dl/)، هر نسخهٔ اخیر (Go به‌طور خودکار toolchain دقیق موردنیاز هر مولد را دانلود می‌کند)
  - [make](https://www.gnu.org/software/make/)
  - [کامپایلر/لینکر gcc](https://gcc.gnu.org/)
  - [Docker](https://docs.docker.com/engine/installation/) (فقط برای پیش‌نمایش محلی وب‌سایت با `make container-serve` لازم است)

- باید بدانید چگونه یک pull request به یک مخزن GitHub ایجاد کنید.
  این کار شامل ایجاد fork شخصی خودتان از مخزن است. برای اطلاعات بیشتر، به
  [کار با یک کلون محلی](/docs/contribute/new-content/open-a-pr/#fork-the-repo) مراجعه کنید.
