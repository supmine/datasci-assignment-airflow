import json

from airflow.utils.dates import days_ago
from airflow import DAG

from airflow.providers.http.operators.http import SimpleHttpOperator

with DAG('rest_test', start_date=days_ago(1)) as dag:
    post_op = SimpleHttpOperator(
        task_id='post_op',
        endpoint='items',
        http_conn_id='localhttp',
        data=json.dumps({"m": 2, "x": 14, "c": 3}),
        headers={"Content-Type": "application/json"},
        response_check=lambda response: response.json()['y'] == 31
    )
