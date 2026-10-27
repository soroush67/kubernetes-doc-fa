---
title: DeploymentReplicaSetTerminatingReplicas
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.34"
  - stage: beta
    defaultValue: true
    fromVersion: "1.35"
---
یک فیلد وضعیت جدید با نام `.status.terminatingReplicas` را در Deploymentها و ReplicaSetها فعال می‌کند تا امکان ردیابی Podهای در حال خاتمه (terminating) فراهم شود.
