# 📺 Section 03 - The Importante Views of the Airflow UI

## 🇧🇷 PORTUGUÊS (Brasil)

### Visão Geral

Esta seção explica as principais views (visões) da interface web do Apache Airflow. Os exemplos de código desta pasta incluem `my_dag.py` e `user.py`, que servem como referência para entender como DAGs e tasks aparecem e se comportam na UI.

---

### Objetivo

Fornecer uma referência prática sobre as views mais utilizadas na UI do Airflow, como navegar, interpretar estados de execução, acessar logs e gerenciar conexões/variáveis.

---

### Arquivos importantes

- `my_dag.py` — Exemplo de DAG usado para demonstrar execução, retries e dependências.
- `user.py` — Exemplo auxiliar (por exemplo, operadores customizados, utilitários ou scripts utilizados nas tasks).

---

### Visões importantes da UI do Airflow

- **DAGs**: Lista todos os DAGs disponíveis. Permite ativar/desativar DAGs, visualizar tags e informações básicas.
- **Graph (Grafo)**: Visualização do grafo de dependências entre tasks — útil para entender fluxo e dependências.
- **Tree (Árvore)**: Mostra execuções históricas por run date com status das tasks por execução. Excelente para inspeção rápida de falhas.
- **DAG Runs**: Lista das execuções do DAG com status, start/end e duration.
- **Task Instance / Log**: Acessar logs individuais da task; primeiro local para investigar falhas.
- **Logs**: Logs consolidados; importante buscar stack traces e mensagens de erro específicas.
- **Code**: Visualiza o código fonte do DAG diretamente pela UI (útil para checagens rápidas sem abrir o repositório)
- **Admin**:
  - **Connections**: Gerenciar conexões (ex.: conexões a bancos, AWS, GCP).
  - **Variables**: Variáveis globais do Airflow usadas em templates/params.
  - **Pools**: Recursos concorrentes limitados por pool.
  - **Users/Roles**: Gerenciamento de usuários e permissões (quando RBAC habilitado).
- **Scheduler/Workers / Queues**: Ver status do scheduler, workers (em deployments com Celery/Kubernetes) e filas.

---

### Boas práticas ao usar a UI

1. Sempre checar os **logs** de uma Task Instance antes de alterar o código.
2. Use a view **Graph** para validar dependências adicionadas recentemente.
3. Utilize **Connections** e **Variables** para evitar hardcode de credenciais no DAG.
4. Em produção, monitore o **Scheduler** e as métricas de execução para identificar gargalos.

---

### Executando o exemplo localmente (resumo)

1. Tenha o ambiente do Section 02 (Docker Compose) configurado e rodando.
2. Copie `my_dag.py` para a pasta de DAGs configurada pelo Airflow (ex.: `dags/`).
3. Acesse a UI (por padrão: http://localhost:8080) e verifique o DAG na lista.

Comandos rápidos (exemplo com Docker Compose):

```bash
# iniciar serviços (no diretório do docker-compose):
docker-compose up -d

# ver logs do scheduler:
docker-compose logs -f scheduler
```

---

### Próximos passos

- Revisar `my_dag.py` para entender retries e triggers.
- Avançar para tutoriais sobre criação de operadores customizados e integração com serviços externos.

---

### Recursos

- https://airflow.apache.org/docs/
- https://airflow.apache.org/docs/apache-airflow/stable/ui.html

---

**Última atualização**: 01 de Junho de 2026
**Status**: ✅ Completado

## 🇬🇧 ENGLISH

### Overview

This section explains the main views of the Apache Airflow web UI. The code examples in this folder (`my_dag.py`, `user.py`) are provided to demonstrate how DAGs and tasks are represented and behave in the UI.

---

### Purpose

Provide a practical reference about the most used UI views in Airflow: how to navigate them, interpret run states, access logs, and manage connections/variables.

---

### Important files

- `my_dag.py` — Example DAG used to demonstrate execution, retries and dependencies.
- `user.py` — Helper/example script (e.g., custom operators or utilities used by tasks).

---

### Key Airflow UI views

- **DAGs**: Lists all available DAGs. Allows enabling/disabling DAGs, viewing tags and basic info.
- **Graph**: Shows task dependency graph — useful to understand flow and relationships.
- **Tree**: Displays historical runs by execution date with task instance states; great for quick failure inspection.
- **DAG Runs**: Lists DAG runs with status, start/end and duration.
- **Task Instance / Log**: Access individual task logs — the first place to inspect failures.
- **Logs**: Aggregated logs; search for stack traces and error messages.
- **Code**: View DAG source code directly in the UI (handy for quick checks without opening the repo).
- **Admin**:
  - **Connections**: Manage connections (e.g., DB, AWS, GCP).
  - **Variables**: Global variables used in templates/params.
  - **Pools**: Limit concurrent resources by pool.
  - **Users/Roles**: Manage users and permissions when RBAC is enabled.
- **Scheduler/Workers / Queues**: Monitor scheduler health and worker status (in Celery/Kubernetes deployments).

---

### Best practices

1. Always check a Task Instance's **logs** before changing code.
2. Use the **Graph** view to validate newly added dependencies.
3. Use **Connections** and **Variables** to avoid hardcoding credentials in DAGs.
4. In production, monitor the **Scheduler** and execution metrics to spot bottlenecks.

---

### Quick run (summary)

1. Have the Section 02 environment (Docker Compose) configured and running.
2. Place `my_dag.py` into the Airflow `dags/` folder.
3. Open the UI (default: http://localhost:8080) and locate the DAG in the list.

Quick commands (example with Docker Compose):

```bash
# start services (from docker-compose directory):
docker-compose up -d

# follow scheduler logs:
docker-compose logs -f scheduler
```

---

### Next steps

- Inspect `my_dag.py` to learn about retries and triggers.
- Continue to tutorials on creating custom operators and integrating external services.

---

### Resources

- https://airflow.apache.org/docs/
- https://airflow.apache.org/docs/apache-airflow/stable/ui.html

---

**Last updated**: June 01, 2026
**Status**: ✅ Completed
