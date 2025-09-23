# Rollercoaster

### On-Demand Developer Environments

---

## Overview

Rollercoaster is an internal self-service platform designed to streamline the developer workflow by providing on-demand, isolated, and collaborative development and testing environments. It eliminates the pain points of manual environment setup, inconsistent configurations, and resource over-provisioning.

The platform allows developers to:

* **Provision environments instantly**: Spin up a full, dedicated dev/test environment (including databases, services, and mock external dependencies) with a single command.
* **Collaborate in real time**: Multiple developers can share a single environment to debug issues, view logs, and share state together.
* **Automate lifecycle management**: Environments are automatically torn down when no longer needed, preventing resource leaks and unnecessary costs.
* **Ensure consistency**: Environments are provisioned from version-controlled templates, ensuring consistency across feature branches and QA.
* **Track resources**: A built-in dashboard provides visibility into environment usage and costs.

---

## Features

* **Ephemeral Environments**: Spin up and tear down isolated, full-stack environments.
* **Real-time Collaboration**: Shared terminal, logs, and dashboards for live debugging.
* **Cost & Resource Tracking**: Automatically monitor and report on resource usage to prevent cost overruns.
* **Versioned Templates**: Pin service versions and dependencies to reproduce a specific environment state.
* **Integrated Monitoring**: Built-in monitoring and logging for each environment.

---

## Tech Stack

* **Containerization**: Docker, Kubernetes (K8s)
* **Infrastructure as Code (IaC)**: Terraform, Helm
* **Backend**: Python (FastAPI)
* **Frontend**: React
* **Real-time Collaboration**: WebSockets
* **Database**: PostgreSQL, Redis
* **Infrastructure**: AWS/GCP/Azure

---

## Getting Started

*(This section will be filled in once the project is more mature.)*

To get started, clone this repository:

```bash
git clone https://github.com/dpereowei/rollercoaster