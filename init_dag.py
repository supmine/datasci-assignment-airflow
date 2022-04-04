import json

from airflow.utils.dates import days_ago
from airflow import DAG

from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator


def print_complete():
    print("Test Complete")


with DAG('assignment_restapi', start_date=days_ago(1)) as dag:
    start = DummyOperator(task_id='start_task')
    post_op1 = SimpleHttpOperator(
        task_id='post_compute1',
        method='POST',
        endpoint='compute',
        http_conn_id='localhttp',
        data=json.dumps({"m": 2, "x": 14, "c": 3}),
        headers={"Content-Type": "application/json"},
        response_check=lambda response: response.json()['y'] == 31
    )
    post_op2 = SimpleHttpOperator(
        task_id='post_compute2',
        method='POST',
        endpoint='compute',
        http_conn_id='localhttp',
        data=json.dumps({"m": -0.5, "x": 3, "c": 0}),
        headers={"Content-Type": "application/json"},
        response_check=lambda response: response.json()['y'] == -1.5
    )
    finish = PythonOperator(task_id='finish_task',
                            python_callable=print_complete)

    start >> post_op1 >> post_op2 >> finish
