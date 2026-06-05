# 📦 Section 04 - Coding Your First Data Pipeline with Airflow

## 🇧🇷 PORTUGUÊS (Brasil)

### Visão Geral

Esta seção mostra como construir um pipeline simples de ETL usando Apache Airflow. O exemplo inclui:
- Criação de tabela no Postgres
- Sensor para verificar disponibilidade de uma API pública
- Extração e processamento de um usuário falso
- Inserção dos dados no Postgres a partir de um CSV temporário

Os arquivos presentes nesta pasta são:
- `user_processing.py` — DAG escrita com o novo estilo `@dag` e `@task` do Airflow SDK; usa sensor, tarefas Python e `PostgresHook` para armazenar dados.
- `user_processing_.py` — variação que demonstra o uso de `PythonOperator` tradicional e uma função auxiliar `_extract_user`.

---

### Estrutura principal (explicação dos componentes)

- `create_table` (SQLExecuteQueryOperator): cria a tabela `users` se não existir.
- `is_api_available` (decorated sensor task): faz um GET para o JSON de exemplo e retorna um `PokeReturnValue` com `xcom_value` contendo o usuário quando disponível.
- `extract_user` (task / PythonOperator): converte o JSON em um dicionário simples com os campos `id`, `firstname`, `lastname`, `email`.
- `process_user` (task): escreve um arquivo CSV temporário em `/tmp/user_info.csv` com os dados do usuário e adiciona `created_at`.
- `store_user` (task): usa `PostgresHook.copy_expert` para executar `COPY users FROM STDIN WITH CSV HEADER` e carregar o CSV para o banco.

Observações importantes:
- Em `user_processing.py` a cadeia de dependências é montada com `process_user(extract_user(create_table >> is_api_available())) >> store_user()` — ou seja, `create_table` e `is_api_available` são encadeadas antes da extração/ processamento, e por fim o armazenamento.
- Em `user_processing_.py` há uma versão que demonstra o uso do `PythonOperator` clássico para a extração.

---

### Requisitos e Pré-requisitos

1. Airflow (compatível com as APIs usadas). Recomenda-se usar uma imagem/container com os providers necessários instalados:
   - `apache-airflow-providers-postgres`
   - `requests` (biblioteca Python para requisições HTTP)

2. Conexão Postgres configurada no Airflow com `conn_id='postgres'` apontando para um banco acessível.

3. Sistema de arquivos temporário acessível em `/tmp` (em Windows com Docker, use um volume compartilhado ou ajuste o caminho).

4. Permissões para executar `COPY FROM STDIN` no banco Postgres para o usuário configurado.

---

### Como executar localmente (rápido)

1. Coloque este diretório na pasta de DAGs do seu Airflow (ou ajuste `dags_folder`).
2. Verifique as dependências (`requests`, providers do Postgres) no ambiente do Airflow.
3. Configure a conexão `postgres` no Airflow UI (Admin → Connections).
4. Inicie o scheduler e o webserver do Airflow.
5. No Web UI, ative a DAG `user_processing` e execute manualmente ou aguarde o horário programado.

Exemplo de comandos (dependendo da sua instalação; se usar docker-compose, adapte aos serviços):

```bash
# instalar requests no ambiente do Airflow (exemplo pip)
pip install requests

# se estiver usando o pacote de providers
pip install apache-airflow-providers-postgres
```

---

### Boas práticas e recomendações

- Evite usar caminhos fixos como `/tmp` em produção; prefira volumes configuráveis ou armazenamento mais robusto (S3, GCS, etc.).
- Não escreva credenciais no código. Use conexões do Airflow e variáveis de ambiente.
- Trate falhas e retries adequadamente (ex.: argumentos `retries`, `retry_delay` nas tasks/operadores).
- Considere usar XComs apenas para objetos pequenos; para payloads maiores use armazenamento externo.

---

### Próximos passos

- Adicionar testes unitários para as funções de processamento (ex.: extrair e transformar).
- Substituir o CSV temporário por upload direto via `hook.insert_rows` ou streaming para o banco.
- Introduzir DAG params e templates para tornar o pipeline mais flexível.

---

### Recursos

- Documentação Airflow: https://airflow.apache.org/docs/
- Providers Postgres: https://airflow.apache.org/docs/apache-airflow-providers-postgres/stable/
- Requests: https://docs.python-requests.org/

---

**Última atualização**: 05 de Junho de 2026
**Status**: ✅ Completado

## 🇬🇧 ENGLISH

### Overview

This section demonstrates how to build a simple ETL pipeline using Apache Airflow. The example covers:
- Creating a table in Postgres
- A sensor checking a public API availability
- Extracting and processing a fake user
- Loading data into Postgres from a temporary CSV

Files in this folder:
- `user_processing.py` — DAG written with the Airflow SDK `@dag` and `@task` style; uses a sensor, Python tasks and `PostgresHook` to persist data.
- `user_processing_.py` — variation showing the classic `PythonOperator` and helper function `_extract_user`.

---

### Main components (explanation)

- `create_table` (SQLExecuteQueryOperator): creates the `users` table if it does not exist.
- `is_api_available` (decorated sensor task): performs a GET to the example JSON and returns a `PokeReturnValue` with `xcom_value` containing the user when available.
- `extract_user` (task / PythonOperator): converts the JSON into a simple dict with `id`, `firstname`, `lastname`, `email`.
- `process_user` (task): writes a temporary CSV at `/tmp/user_info.csv` with the user data and adds `created_at`.
- `store_user` (task): uses `PostgresHook.copy_expert` to run `COPY users FROM STDIN WITH CSV HEADER` and load the CSV into the database.

Notes:
- In `user_processing.py` task dependencies are chained as `process_user(extract_user(create_table >> is_api_available())) >> store_user()` — meaning `create_table` and `is_api_available` are chained before extraction/processing, and finally the storage step runs.
- `user_processing_.py` demonstrates the use of the classical `PythonOperator` for extraction.

---

### Requirements and prerequisites

1. Airflow (compatible with used APIs). Recommended providers installed:
   - `apache-airflow-providers-postgres`
   - `requests` Python package

2. A Postgres connection configured in Airflow with `conn_id='postgres'` pointing to an accessible database.

3. Writable temporary filesystem at `/tmp` (on Windows with Docker use a shared volume or adapt the path).

4. Permissions to run `COPY FROM STDIN` in Postgres for the configured user.

---

### How to run locally (quick)

1. Place this folder in your Airflow `dags_folder` (or set `dags_folder` to include it).
2. Ensure dependencies are available (`requests`, Postgres provider) in the Airflow environment.
3. Configure the `postgres` connection in Airflow UI (Admin → Connections).
4. Start the scheduler and webserver.
5. In the Web UI, enable DAG `user_processing` and trigger a run.

Example commands (adjust to your environment):

```bash
# install requests in the Airflow environment
pip install requests

# install postgres provider
pip install apache-airflow-providers-postgres
```

---

### Best practices and recommendations

- Avoid fixed paths like `/tmp` in production; use configurable volumes or object storage (S3, GCS).
- Do not store credentials in code. Use Airflow Connections and environment variables.
- Configure retries and failure handling for operators/tasks.
- Use XComs for small payloads only; for larger payloads use external storage.

---

### Next steps

- Add unit tests for processing functions (extract/transform).
- Replace the temporary CSV with direct insertion or streaming to the database.
- Add DAG parameters and templates to make the pipeline flexible.

---

### Resources

- Airflow docs: https://airflow.apache.org/docs/
- Postgres provider: https://airflow.apache.org/docs/apache-airflow-providers-postgres/stable/
- Requests: https://docs.python-requests.org/

---

**Last updated**: June 05, 2026
**Status**: ✅ Completed
