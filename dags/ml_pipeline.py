from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


##Define our Task1

def preprocess_data():
    print("Processing_data...")


##Define our Task2
def train_model():
    print("Training Model...")

##Define Task3

def evaluate_model():
    print("Evaluate Models...")


##Define the Dag
with DAG(
    'ml_pipeline',
    start_date = datetime(2024,1,1),
    schedule='@weekly'
) as dag:
    ##Define the task
    preprocess=PythonOperator(task_id="preprocess_data",python_callable=preprocess_data)
    train=PythonOperator(task_id="train_task",python_callable=train_model)
    evaluate=PythonOperator(task_id="evaluate_task",python_callable=evaluate_model)


    ##Set Dependencies
    preprocess >>train >>evaluate