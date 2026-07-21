from airflow.sdk import dag, task, Context

@dag
def branch():

    @task
    def a():
        return 1

    @task.branch
    def b(val: int):
        if val ==1:
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

branch()
