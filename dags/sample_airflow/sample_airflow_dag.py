from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def print_text(text):
    print(text)


default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'depends_on_past': False
}


with DAG(
        'sample_airflow_dag',
        default_args=default_args,
        description='A simple hello world DAG',
        schedule_interval='@once',  # Run every minute
        start_date=datetime(2025, 2, 12),
        catchup=False,
        tags=['hello_airflow']
) as dag:

    task_hello = PythonOperator(
        task_id='hello_task',
        python_callable=print_text,
        op_kwargs={'text': 'Hello, Airflow!'}
    )

    task_goodbye = PythonOperator(
        task_id='goodbye_task',
        python_callable=print_text,
        op_kwargs={'text': 'Goodbye, Airflow!'}
    )

    task_hello >> task_goodbye
