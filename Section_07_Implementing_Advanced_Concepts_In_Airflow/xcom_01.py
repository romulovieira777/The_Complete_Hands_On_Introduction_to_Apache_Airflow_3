from airflow.sdk import dag, task

@dag
def xcom_dag():

    @task
    def t1() -> Dict[str, Any]:
        mv_val = 42
        my_sentence = "Hello World!"

        return {
            "my_key": mv_val,
            "my_sentence": my_sentence
        }

    @task
    def t2(data: Dict[str, Any]):
        print(data["my_key"])
        print(data["my_sentence"])

    val = t1()
    t2(val)

xcom_dag()
