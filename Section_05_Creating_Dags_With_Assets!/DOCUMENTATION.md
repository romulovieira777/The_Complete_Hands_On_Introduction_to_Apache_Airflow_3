# 📦 Section 05 - Creating DAGs with Assets!

## 🇧🇷 PORTUGUÊS (Brasil)

### Visão Geral

Esta seção aborda a criação de DAGs usando Assets no Apache Airflow. Mostra conceitos práticos sobre como organizar código, expor ativos (assets) e como os assets se integram ao catálogo/observabilidade do Airflow.

---

### Conteúdo da Seção

- Introdução aos Assets no Airflow
- Estrutura de projeto recomendada
- Exemplo prático (arquivo `user.py` presente nesta pasta)
- Execução e observabilidade dos assets

---

### Arquivos importantes

- `user.py` — Exemplo prático que demonstra a criação de assets/DAGs

---

### Requisitos

1. Ter o Airflow instalado (ou ambiente Docker conforme Section 02)
2. Python 3.8+ (ou versão compatível com o Airflow usado no curso)
3. Docker Desktop (opcional, recomendado para ambientes isolados)

---

### Como usar / Execução rápida

1. Copie/cole `user.py` no diretório de DAGs configurado no seu Airflow (`AIRFLOW_HOME/dags`) ou monte a pasta via Docker Compose.
2. Reinicie o scheduler/webserver se necessário.
3. Acesse a UI do Airflow e verifique os assets/DAGs na aba DAGs e, quando aplicável, na visualização de Assets/Lineage.

Exemplo de comando (quando usar Docker Compose da seção 02):

```bash
docker-compose -f path/to/docker-compose.yaml up -d
```

---

### Boas práticas

- Organize assets por domínio (ex.: users/, orders/)
- Use nomes de task legíveis e idempotência nas tasks
- Versione seu código e mantenha small, testable units

---

### Próximos passos

- Revisar `Section 04` para entender DAGs básicos
- Explorar integrações com sensores, XCom e hooks

---

## 🔗 Recursos

- https://airflow.apache.org/docs/
- Artigos e exemplos sobre Assets no Airflow

---

**Última atualização**: 11 de Junho de 2026
**Status**: ✅ Completado

---

## 🇬🇧 ENGLISH

### Overview

This section covers creating DAGs using Assets in Apache Airflow. It provides practical guidance on organizing code, exposing assets, and how assets integrate with Airflow's catalog and observability features.

---

### Section Content

- Introduction to Assets in Airflow
- Recommended project structure
- Practical example (the `user.py` file in this folder)
- Running and observing assets

---

### Important files

- `user.py` — Practical example demonstrating asset/DAG creation

---

### Requirements

1. Airflow installed (or Docker environment as in Section 02)
2. Python 3.8+ (or compatible with the Airflow version used in the course)
3. Docker Desktop (optional, recommended for isolated environments)

---

### How to use / Quick run

1. Place `user.py` into your Airflow DAGs folder (`AIRFLOW_HOME/dags`) or mount this folder via Docker Compose.
2. Restart the scheduler/webserver if required.
3. Open the Airflow UI and check the DAG/Assets views; inspect lineage and metadata when available.

Example command (if using the Docker Compose from Section 02):

```bash
docker-compose -f path/to/docker-compose.yaml up -d
```

---

### Best practices

- Organize assets by domain (e.g. users/, orders/)
- Use readable task names and ensure task idempotency
- Keep small, testable units and version control your code

---

### Next steps

- Review `Section 04` to learn about basic DAGs
- Explore integrations with sensors, XCom and hooks

---

### Resources

- https://airflow.apache.org/docs/

---

**Last updated**: June 11, 2026
**Status**: ✅ Completed
