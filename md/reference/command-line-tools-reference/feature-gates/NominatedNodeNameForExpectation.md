---
title: NominatedNodeNameForExpectation
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.34"
    toVersion: "1.34"
  - stage: beta
    defaultValue: true
    fromVersion: "1.35"

---
هنگامی که این قابلیت فعال باشد، kube-scheduler از `.status.nominatedNodeName` برای بیان این موضوع استفاده می‌کند که یک
Pod قرار است به کدام نود متصل (bind) شود. فیلد `.status.nominatedNodeName` زمانی مقداردهی می‌شود که kube-scheduler
پیش‌دستی (preemption) Podها را آغاز کند، یا پیش‌بینی کند که فاز WaitOnPermit یا PreBinding
نسبتاً طولانی خواهد بود.
سایر مؤلفه‌ها می‌توانند `.status.nominatedNodeName` را بخوانند و از آن استفاده کنند، اما نباید آن را مقداردهی کنند.

هنگامی که این قابلیت غیرفعال باشد، kube-scheduler فقط پیش از آغاز پیش‌دستی (preemption)، مقدار `.status.nominatedNodeName` را تنظیم می‌کند.
