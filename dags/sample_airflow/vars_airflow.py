import json

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os


def print_var(var_name):
    raw_var = os.getenv(var_name)
    if raw_var:
        var_json = json.loads(raw_var)
        print(var_json['sample_api_key'])


default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'depends_on_past': False
}

with DAG(
        'retrieve_variables',
        default_args=default_args,
        description='Sample dag to retrieve env variables',
        schedule_interval='@once',  # Run every minute
        start_date=datetime(2025, 2, 12),
        catchup=False,
        tags=['hello_airflow']
) as dag:
    get_var = PythonOperator(
        task_id='hello_task',
        python_callable=print_var,
        op_kwargs={"var_name": "AIRFLOW_VAR_SAMPLE_JSON_VAR"}
    )

    get_var
