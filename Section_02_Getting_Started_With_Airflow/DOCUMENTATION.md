# Section 02 - Getting Started with Airflow

---

## PORTUGUÊS

### Visão Geral

Esta seção apresenta um ambiente local do Apache Airflow 3 com Docker Compose.
O arquivo `docker-compose.yaml` sobe os serviços principais para estudar orquestração de workflows.

---

### Conteúdo da Seção

#### 1. Arquivo principal

- `docker-compose.yaml`: configuração base para rodar Airflow localmente.
- Imagem padrão: `apache/airflow:3.0.0`.
- Banco de dados: `postgres:13`.
- Executor configurado: `LocalExecutor`.

#### 2. Serviços ativos

- `postgres`
- `airflow-init`
- `airflow-apiserver` (porta `8080`)
- `airflow-scheduler`
- `airflow-dag-processor`
- `airflow-triggerer`
- `airflow-cli` (perfil `debug`)

#### 3. Volumes e pastas locais

O compose monta as pastas abaixo para desenvolvimento local:

- `./dags` -> `/opt/airflow/dags`
- `./logs` -> `/opt/airflow/logs`
- `./config` -> `/opt/airflow/config`
- `./plugins` -> `/opt/airflow/plugins`

---

### Objetivos da Seção

1. Entender a estrutura mínima de um ambiente Airflow com Docker.
2. Subir o Airflow localmente para explorar a interface web e os serviços.
3. Preparar o projeto para criação de DAGs nas próximas seções.

---

### Requisitos

- Docker Desktop instalado e em execução.
- Docker Compose disponível.
- Mínimo recomendado pelo próprio compose:
  - 4 GB de RAM
  - 2 CPUs
  - 10 GB de disco livre

---

### Como executar (resumo)

No diretório `Section_02_Getting_Started_With_Airflow`, execute:

```bash
docker compose up airflow-init
docker compose up -d
```

Depois acesse:

- Airflow API/UI: `http://localhost:8080`
- Usuário padrão: `airflow`
- Senha padrão: `airflow`

Para parar o ambiente:

```bash
docker compose down
```

---

### Observações importantes

- Esta configuração é para estudo/local development, não para produção.
- O arquivo inclui variáveis de ambiente para personalização via `.env`.
- Serviços de Celery/Redis e Flower estão comentados no compose.

---

## ENGLISH

### Overview

This section introduces a local Apache Airflow 3 environment using Docker Compose.
The `docker-compose.yaml` file starts the core services required to study workflow orchestration.

---

### Section Content

#### 1. Main file

- `docker-compose.yaml`: base configuration to run Airflow locally.
- Default image: `apache/airflow:3.0.0`.
- Database: `postgres:13`.
- Configured executor: `LocalExecutor`.

#### 2. Active services

- `postgres`
- `airflow-init`
- `airflow-apiserver` (port `8080`)
- `airflow-scheduler`
- `airflow-dag-processor`
- `airflow-triggerer`
- `airflow-cli` (`debug` profile)

#### 3. Volumes and local folders

The compose file mounts the folders below for local development:

- `./dags` -> `/opt/airflow/dags`
- `./logs` -> `/opt/airflow/logs`
- `./config` -> `/opt/airflow/config`
- `./plugins` -> `/opt/airflow/plugins`

---

### Section Objectives

1. Understand the minimum structure of a Docker-based Airflow setup.
2. Run Airflow locally to explore the web interface and services.
3. Prepare the project for DAG creation in upcoming sections.

---

### Requirements

- Docker Desktop installed and running.
- Docker Compose available.
- Minimum resources recommended by the compose setup:
  - 4 GB RAM
  - 2 CPUs
  - 10 GB free disk space

---

### How to run (quick steps)

From `Section_02_Getting_Started_With_Airflow`, run:

```bash
docker compose up airflow-init
docker compose up -d
```

Then access:

- Airflow API/UI: `http://localhost:8080`
- Default username: `airflow`
- Default password: `airflow`

To stop the environment:

```bash
docker compose down
```

---

### Important notes

- This setup is for study/local development, not production.
- The file includes environment variable support for customization via `.env`.
- Celery/Redis and Flower services are present but commented out.

---

Last update: 2026-05-29
Status: Completed
