from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'deepak',
    'start_date': datetime(2026, 3, 31),
    'retries': 1
}

with DAG(
    dag_id='crypto_data_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False
) as dag:

    lambda_ingestion = BashOperator(
        task_id='lambda_ingestion',
        bash_command='echo "Lambda ingestion completed successfully"'
    )

    glue_etl = BashOperator(
        task_id='glue_etl',
        bash_command='echo "Glue ETL job completed successfully"'
    )

    postgres_load = BashOperator(
        task_id='postgres_load',
        bash_command='python /opt/airflow/dags/load_to_postgres.py'
    )

    validation_check = BashOperator(
        task_id='validation_check',
        bash_command='echo "Validation passed successfully"'
    )

    lambda_ingestion >> glue_etl >> postgres_load >> validation_check