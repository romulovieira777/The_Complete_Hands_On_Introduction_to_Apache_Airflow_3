# 📦 Section 07 - Implementing Advanced Concepts in Airflow

## 🇧🇷 PORTUGUÊS (Brasil)

### Visão Geral

Esta seção aborda conceitos avançados do Apache Airflow, incluindo:
- Comunicação entre tasks usando XCom (XCross-Communication)
- Agrupamento de tarefas com `@task_group`
- Fluxos condicionais com `@task.branch`

Esses recursos permitem criar pipelines mais complexos, modulares e dinâmicos.

---

### Arquivos da seção

- `xcom_01.py` — Demonstra o uso básico de XCom com retorno direto entre tasks.
- `xcom.py` — Demonstra XCom avançado com `context`, `xcom_push()` e `xcom_pull()`.
- `group.py` — Demonstra `@task_group` para agrupar tarefas e grupos aninhados.
- `branch.py` — Demonstra `@task.branch` para criar fluxos de execução condicionais.

---

### O que cada arquivo demonstra

#### `xcom_01.py` - XCom Simples

Mostra a forma mais simplificada de compartilhar dados entre tasks:

```python
@task
def t1() -> Dict[str, Any]:
    return {"my_key": 42, "my_sentence": "Hello World!"}

@task
def t2(data: Dict[str, Any]):
    print(data["my_key"])
    print(data["my_sentence"])

val = t1()
t2(val)
```

- `t1()` retorna um dicionário que é automaticamente armazenado em XCom.
- `t2()` recebe o retorno de `t1()` como parâmetro (push/pull automático).
- Ideal para payloads pequenos e estrutura simples.

#### `xcom.py` - XCom Avançado

Demonstra XCom com contexto e controle manual:

```python
@task
def t1(context: Context):
    val = 42
    context['ti'].xcom_push(key='my_key', value=val)

@task
def t2(context: Context):
    val = context['ti'].xcom_pull(task_ids='t1', key='my_key')
    print(val)

t1() >> t2()
```

- `context['ti'].xcom_push()` — armazena um valor com uma chave específica.
- `context['ti'].xcom_pull()` — recupera um valor armazenado por outra task.
- Oferece controle fino sobre nomes de chaves e manipulação de dados.

#### `group.py` - Task Groups

Demonstra o uso de grupos de tarefas:

```python
@task_group(default_args={"retries": 2})
def my_group(val: int):
    def b(my_val: int):
        print(my_val + 42)

    @task_group(default_args={"retries": 3})
    def my_nested_group():
        def c():
            print("c")
        c()

    b(val) >> my_nested_group()
```

- `@task_group` agrupa múltiplas tasks em uma unidade lógica.
- Task groups podem ser aninhadas para criar hierarquias complexas.
- Cada grupo pode ter seus próprios `default_args` (retries, etc.).
- Útil para organizar pipelines grandes e melhorar legibilidade.

#### `branch.py` - Fluxos Condicionais

Demonstra o uso de branching:

```python
@task.branch
def b(val: int):
    if val == 1:
        return "equal_1"
    return "difference_than_1"

@task
def equal_1(val: int):
    print(f"equal to {val}")

@task
def difference_than_1(val: int):
    print(f"difference than 1: {val}")

val = a()
b(val) >> [equal_1(val), difference_than_1(val)]
```

- `@task.branch` retorna o ID de uma task (ou lista de IDs) para executar.
- Permite criar fluxos dinâmicos onde o caminho é decidido em tempo de execução.
- Útil para processamento condicional, tratamento de erros e workflows paramétricos.

---

### Requisitos

1. Airflow instalado (versão com SDK moderno que suporta `@dag` e `@task`).
2. Biblioteca `requests` (opcional, para exemplos estendidos).
3. Compreensão básica de DAGs e tasks (veja Section 04).

---

### Como usar

1. Copie esta pasta para o diretório de DAGs do Airflow (`AIRFLOW_HOME/dags`).
2. Ative as DAGs no Airflow Web UI.
3. Execute cada DAG manualmente para ver os resultados:
   - `xcom_dag` (de `xcom_01.py` ou `xcom.py`)
   - `group` (de `group.py`)
   - `branch` (de `branch.py`)

Exemplo de teste local:

```bash
# Listar DAGs disponíveis
airflow dags list

# Testar uma DAG (syntax check)
airflow dags test xcom_dag 2026-07-21

# Executar uma DAG manualmente
airflow dags trigger xcom_dag
```

---

### Boas práticas

- Use XCom simples para retornos diretos; use XCom avançado quando precisar de controle fino.
- Organize tasks relacionadas em `@task_group` para melhorar legibilidade.
- Evite armazenar payloads grandes em XCom; use armazenamento externo (S3, banco de dados).
- Use `@task.branch` com cuidado; garanta que todos os branches possíveis tenham tasks associadas.
- Documente o fluxo de dados entre tasks (XCom keys, tipos).

---

### Próximos passos

- Combinar XCom com hooks para passar dados de/para bancos de dados.
- Criar task groups dinâmicas usando loops e geradores.
- Integrar branching com sensores para workflows complexos.
- Adicionar testes unitários para tasks que usam contexto.

---

### Recursos

- Documentação Airflow: https://airflow.apache.org/docs/
- XCom: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html
- Task Groups: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html#task-groups
- Branching: https://airflow.apache.org/docs/apache-airflow/stable/concepts.html#branching

---

## 🇬🇧 ENGLISH

### Overview

This section covers advanced Apache Airflow concepts, including:
- Inter-task communication using XCom (Cross-Communication)
- Task grouping with `@task_group`
- Conditional workflows with `@task.branch`

These features enable building complex, modular, and dynamic pipelines.

---

### Section files

- `xcom_01.py` — Demonstrates basic XCom usage with direct returns between tasks.
- `xcom.py` — Demonstrates advanced XCom with `context`, `xcom_push()`, and `xcom_pull()`.
- `group.py` — Demonstrates `@task_group` for grouping tasks and nesting groups.
- `branch.py` — Demonstrates `@task.branch` for conditional task execution.

---

### What each file demonstrates

#### `xcom_01.py` - Simple XCom

Shows the simplest way to share data between tasks:

```python
@task
def t1() -> Dict[str, Any]:
    return {"my_key": 42, "my_sentence": "Hello World!"}

@task
def t2(data: Dict[str, Any]):
    print(data["my_key"])
    print(data["my_sentence"])

val = t1()
t2(val)
```

- `t1()` returns a dict that is automatically stored in XCom.
- `t2()` receives the return value of `t1()` as a parameter (automatic push/pull).
- Ideal for small payloads and simple structures.

#### `xcom.py` - Advanced XCom

Demonstrates XCom with context and manual control:

```python
@task
def t1(context: Context):
    val = 42
    context['ti'].xcom_push(key='my_key', value=val)

@task
def t2(context: Context):
    val = context['ti'].xcom_pull(task_ids='t1', key='my_key')
    print(val)

t1() >> t2()
```

- `context['ti'].xcom_push()` — stores a value with a specific key.
- `context['ti'].xcom_pull()` — retrieves a value stored by another task.
- Provides fine-grained control over key names and data manipulation.

#### `group.py` - Task Groups

Demonstrates task grouping:

```python
@task_group(default_args={"retries": 2})
def my_group(val: int):
    def b(my_val: int):
        print(my_val + 42)

    @task_group(default_args={"retries": 3})
    def my_nested_group():
        def c():
            print("c")
        c()

    b(val) >> my_nested_group()
```

- `@task_group` groups multiple tasks into a logical unit.
- Task groups can be nested to create complex hierarchies.
- Each group can have its own `default_args` (retries, etc.).
- Useful for organizing large pipelines and improving readability.

#### `branch.py` - Conditional Workflows

Demonstrates branching:

```python
@task.branch
def b(val: int):
    if val == 1:
        return "equal_1"
    return "difference_than_1"

@task
def equal_1(val: int):
    print(f"equal to {val}")

@task
def difference_than_1(val: int):
    print(f"difference than 1: {val}")

val = a()
b(val) >> [equal_1(val), difference_than_1(val)]
```

- `@task.branch` returns the ID of a task (or list of IDs) to execute.
- Enables dynamic workflows where the execution path is decided at runtime.
- Useful for conditional processing, error handling, and parameterized workflows.

---

### Requirements

1. Airflow installed (version with modern SDK supporting `@dag` and `@task`).
2. `requests` library (optional, for extended examples).
3. Basic understanding of DAGs and tasks (see Section 04).

---

### How to use

1. Copy this folder into the Airflow DAGs directory (`AIRFLOW_HOME/dags`).
2. Enable the DAGs in Airflow Web UI.
3. Run each DAG manually to see the results:
   - `xcom_dag` (from `xcom_01.py` or `xcom.py`)
   - `group` (from `group.py`)
   - `branch` (from `branch.py`)

Example local test commands:

```bash
# List available DAGs
airflow dags list

# Test a DAG (syntax check)
airflow dags test xcom_dag 2026-07-21

# Trigger a DAG manually
airflow dags trigger xcom_dag
```

---

### Best practices

- Use simple XCom for direct returns; use advanced XCom when you need fine-grained control.
- Organize related tasks in `@task_group` to improve readability.
- Avoid storing large payloads in XCom; use external storage (S3, databases).
- Use `@task.branch` carefully; ensure all possible branches have associated tasks.
- Document data flow between tasks (XCom keys, types).

---

### Next steps

- Combine XCom with hooks to pass data to/from databases.
- Create dynamic task groups using loops and generators.
- Integrate branching with sensors for complex workflows.
- Add unit tests for tasks that use context.

---

### Resources

- Airflow documentation: https://airflow.apache.org/docs/
- XCom: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html
- Task Groups: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html#task-groups
- Branching: https://airflow.apache.org/docs/apache-airflow/stable/concepts.html#branching

---

**Last updated**: July 21, 2026
**Status**: ✅ Completed
