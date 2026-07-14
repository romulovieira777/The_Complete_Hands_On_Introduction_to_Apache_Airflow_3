# 📦 Section 06 - Databases and Executors

## 🇧🇷 PORTUGUÊS (Brasil)

### Visão Geral

Esta seção mostra como combinar bancos de dados e executores no Apache Airflow. O foco é:
- Criar e carregar dados em uma tabela Postgres
- Usar sensor para aguardar uma API externa
- Processar dados temporários em CSV
- Distribuir tarefas em uma fila específica com executor baseado em workers

---

### Arquivos da seção

- `user_processing.py` — DAG que cria a tabela `users`, consulta uma API pública, processa o usuário e insere os dados no Postgres.
- `celery.py` — DAG simples que demonstra o uso de `queue='high_cpu'` em tarefas para envio a uma fila específica.

---

### O que cada arquivo demonstra

#### `user_processing.py`

- `create_table`: executa SQL para criar a tabela `users` caso ela não exista.
- `is_api_available`: sensor que consulta o JSON público e espera a API ficar disponível.
- `extract_user`: transforma o JSON recebido em um dicionário com `id`, `firstname`, `lastname` e `email`.
- `process_user`: adiciona `created_at` e grava os dados em `/tmp/user_info.csv`.
- `store_user`: usa `PostgresHook.copy_expert` para fazer o `COPY users FROM STDIN WITH CSV HEADER`.

Fluxo principal:
`create_table >> is_api_available >> extract_user >> process_user >> store_user`

#### `celery.py`

- `a`: tarefa inicial.
- `b`, `c` e `d`: tarefas enviadas para a fila `high_cpu`.
- Encadeamento: `a() >> [b(), c()] >> d()`

Esse exemplo é útil para entender como direcionar tarefas para filas diferentes quando o Airflow usa workers distribuídos.

---

### Requisitos

1. Airflow com os providers necessários instalados.
2. Conexão Postgres configurada no Airflow com `conn_id='postgres'`.
3. Biblioteca `requests` disponível no ambiente.
4. Para o exemplo com fila, um executor compatível com workers e a fila `high_cpu` configurada nos workers.

---

### Como usar

1. Copie esta pasta para o diretório de DAGs do Airflow.
2. Configure a conexão `postgres` no Airflow UI.
3. Garanta que o ambiente tenha acesso ao endpoint da API usada no sensor.
4. Ative as DAGs no Airflow e execute os fluxos.

---

### Boas práticas

- Evite caminhos fixos em produção; use volumes ou storage externo.
- Não coloque credenciais no código.
- Configure retries e tratamento de falhas nas tasks.
- Para cargas maiores, prefira armazenamento externo em vez de CSV local.

---

## 🇬🇧 ENGLISH

### Overview

This section shows how to combine databases and executors in Apache Airflow. The main goals are:
- Create and load data into a Postgres table
- Use a sensor to wait for an external API
- Process temporary data into a CSV file
- Route tasks to a specific queue with a worker-based executor

---

### Section files

- `user_processing.py` — DAG that creates the `users` table, checks a public API, processes the user, and inserts data into Postgres.
- `celery.py` — Simple DAG that demonstrates using `queue='high_cpu'` to send tasks to a dedicated queue.

---

### What each file demonstrates

#### `user_processing.py`

- `create_table`: runs SQL to create the `users` table if it does not exist.
- `is_api_available`: sensor that queries the public JSON and waits until the API is available.
- `extract_user`: transforms the JSON payload into a dict with `id`, `firstname`, `lastname`, and `email`.
- `process_user`: adds `created_at` and writes the data to `/tmp/user_info.csv`.
- `store_user`: uses `PostgresHook.copy_expert` to run `COPY users FROM STDIN WITH CSV HEADER`.

Main flow:
`create_table >> is_api_available >> extract_user >> process_user >> store_user`

#### `celery.py`

- `a`: initial task.
- `b`, `c`, and `d`: tasks sent to the `high_cpu` queue.
- Chain: `a() >> [b(), c()] >> d()`

This example helps explain how to route tasks to different queues when Airflow uses distributed workers.

---

### Requirements

1. Airflow with the required providers installed.
2. A Postgres connection configured in Airflow with `conn_id='postgres'`.
3. The `requests` package available in the environment.
4. For the queue example, a worker-compatible executor and the `high_cpu` queue configured on the workers.

---

### How to use

1. Copy this folder into the Airflow DAGs directory.
2. Configure the `postgres` connection in the Airflow UI.
3. Make sure the environment can reach the API endpoint used by the sensor.
4. Enable the DAGs in Airflow and trigger the workflows.

---

### Best practices

- Avoid fixed paths in production; use volumes or external storage.
- Do not store credentials in code.
- Configure retries and failure handling on tasks.
- For larger loads, prefer external storage instead of a local CSV.

---

**Last updated**: July 14, 2026
**Status**: Completed
