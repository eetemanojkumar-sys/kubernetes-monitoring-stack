# Kubernetes Monitoring Stack with Prometheus, Grafana & Alertmanager

## Overview

A Kubernetes observability project built around Prometheus, Grafana, Alertmanager, and the Prometheus Operator through the `kube-prometheus-stack` Helm chart.

A custom Flask application is deployed to Kubernetes and used to generate measurable workload. Prometheus collects metrics, Grafana visualizes them, and custom alert rules detect high CPU usage.

The stack was tested on a Minikube cluster running on an AWS EC2 Ubuntu instance.

## Architecture

```text
Monitoring Demo Application
          |
          v
   Kubernetes Cluster
          |
          v
      Prometheus
      /        \
 PromQL      Alert Rules
    |            |
    v            v
 Grafana     Alertmanager

Additional exporters:
- kube-state-metrics
- Node Exporter
```

## Tech Stack

- Kubernetes / Minikube
- Helm
- Prometheus
- Grafana
- Alertmanager
- Prometheus Operator
- kube-state-metrics
- Node Exporter
- Docker
- Python / Flask
- Linux
- AWS EC2

## What This Project Demonstrates

- Kubernetes monitoring and observability
- Prometheus metric scraping
- PromQL queries
- Grafana dashboards
- Custom Prometheus alert rules
- Alert lifecycle validation
- CPU load generation for testing
- Helm-based monitoring stack deployment

## Monitoring Flow

```text
Application
    ↓
Kubernetes metrics
    ↓
Prometheus scraping
    ├── Grafana dashboards
    └── Alert rules → Alertmanager
```

## Demo Application

The Flask application exposes:

```text
/        Application status
/health  Health check
/work    Generates CPU workload for monitoring tests
```

## Example Alert

A custom alert detects elevated CPU usage for the demo workload.

```yaml
alert: MonitoringDemoHighCPU
for: 1m
labels:
  severity: warning
annotations:
  summary: Monitoring demo CPU usage is high
```

## Useful PromQL

Check target availability:

```promql
up
```

Calculate CPU utilization:

```promql
100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

## Install Monitoring Stack

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

kubectl create namespace monitoring

helm install monitoring prometheus-community/kube-prometheus-stack \
  --namespace monitoring
```

Verify:

```bash
kubectl get pods -n monitoring
```

## Deploy the Demo Application

```bash
git clone https://github.com/eetemanojkumar-sys/kubernetes-monitoring-stack.git
cd kubernetes-monitoring-stack

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f monitoring-demo-alerts.yaml
```

## Validation Performed

The project was validated by:

1. Deploying the custom application.
2. Installing the Prometheus monitoring stack.
3. Confirming metric collection.
4. Viewing metrics through Grafana.
5. Generating CPU load.
6. Triggering a custom Prometheus alert.
7. Observing the alert lifecycle through Alertmanager.

## Key Skills Demonstrated

- Kubernetes
- Helm
- Prometheus
- Grafana
- Alertmanager
- Prometheus Operator
- PromQL
- Docker
- Python Flask
- Kubernetes troubleshooting
- Monitoring and observability

## Security Notes

- No Kubernetes Secrets are committed.
- No SMTP passwords or kubeconfig files are stored in the repository.
- Public infrastructure addresses are not hard-coded.

## Outcome

This project demonstrates the full observability path from application workload to metrics collection, visualization, alert generation, and alert handling.

---

**Author:** Manoj Kumar  
**Focus:** Cloud & DevOps Engineering
