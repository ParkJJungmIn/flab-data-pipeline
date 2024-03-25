import airflow
from datetime import timedelta
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago
from airflow.providers.apache.druid.operators.druid import DruidOperator

default_args = {
    'owner': 'airflow',
    'retry_delay': timedelta(minutes=5),
    'start_date': days_ago(1),
}

dag = DAG(
    dag_id="data_pipeline_dag",
    default_args=default_args,
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=120),
    description='Spark and Druid data pipeline',
    tags=['spark', 'druid', 'data pipeline'],
)

spark_sliver_task = SparkSubmitOperator(
    task_id='spark_silver_task',
    application='/opt/airflow/dags/spark/spark_sliver.py',
    conn_id='spark',
    total_executor_cores='2',
    executor_cores='1',
    num_executors='1',
    name='spark_silver_job',
    execution_timeout=timedelta(minutes=20),
    packages='org.apache.hadoop:hadoop-aws:3.3.4',
    verbose=True,
    conf={
        'spark.hadoop.fs.s3a.access.key': '{{ var.value.AWS_ACCESS_KEY }}',
        'spark.hadoop.fs.s3a.secret.key': '{{ var.value.AWS_SECRET_KEY }}',
    },
    dag=dag,
)

spark_gold_task = SparkSubmitOperator(
    task_id='spark_gold_task',
    application='/opt/airflow/dags/spark/spark_gold.py',
    conn_id='spark',
    total_executor_cores='2',
    executor_cores='1',
    num_executors='1',
    name='spark_gold_job',
    execution_timeout=timedelta(minutes=20),
    packages='org.apache.hadoop:hadoop-aws:3.3.4',
    verbose=True,
    conf={
        'spark.hadoop.fs.s3a.access.key': '{{ var.value.AWS_ACCESS_KEY }}',
        'spark.hadoop.fs.s3a.secret.key': '{{ var.value.AWS_SECRET_KEY }}',
    },
    dag=dag,
)

druid_ingestion_task = DruidOperator(
    task_id='druid_ingestion_task',
    json_index_file="druid/eventsim_ingestion.json",
    druid_ingest_conn_id="druid_connection",
    dag=dag,
)

spark_sliver_task >> spark_gold_task >> druid_ingestion_task
