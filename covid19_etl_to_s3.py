from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
import requests
import pandas as pd
from datetime import datetime

# S3 bucket name and path
BUCKET_NAME = 'Bucket_Name'
FILE_NAME = 'covid_data_pakistan.csv'
S3_KEY = FILE_NAME

# Define the function to extract data
def extract_data(ti, **kwargs):
    url = "https://disease.sh/v3/covid-19/countries/pakistan"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    # Push the data to XCom for the next task
    ti.xcom_push(key='covid_data', value=data)

# Define the function to transform data
def transform_data(ti, **kwargs):
    # Pull data from XCom
    data = ti.xcom_pull(key='covid_data', task_ids='extract_data')
    df = pd.DataFrame([data])  # Convert data to a single-row DataFrame
    df = df[['country', 'cases', 'todayCases', 'deaths', 'todayDeaths', 'recovered', 'active', 'critical', 'updated']]
    # Save DataFrame to CSV
    df.to_csv(FILE_NAME, index=False)
    print(f"CSV file '{FILE_NAME}' created successfully.")

# Define the function to load data into S3
def load_data():
    # Create an S3 hook
    s3 = S3Hook()
    # Upload the CSV file to the specified S3 bucket
    s3.load_file(filename=FILE_NAME, bucket_name=BUCKET_NAME, key=S3_KEY, replace=True)
    print(f"File '{FILE_NAME}' uploaded to S3 bucket '{BUCKET_NAME}' as '{S3_KEY}'.")

# Default args for DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 8),
    'retries': 1,
}

# Define the DAG
with DAG(
    'covid19_etl_to_s3',
    default_args=default_args,
    description='Extract COVID-19 data and load to S3',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # Task to extract data
    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
        provide_context=True,  # Ensures context is passed to the function
    )

    # Task to transform data
    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        provide_context=True,  # Ensures context is passed to the function
    )

    # Task to load data to S3
    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
    )

    # Set task dependencies
    extract_task >> transform_task >> load_task
