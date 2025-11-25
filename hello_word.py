from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

# 1. นิยาม DAG
with DAG(
    dag_id='hello_world_k3s',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None, # รันเมื่อสั่งเท่านั้น (Manual)
    catchup=False,
    tags=['example'],
) as dag:

    # 2. สร้าง Task 1: พิมพ์ Hello ด้วย Bash
    t1 = BashOperator(
        task_id='say_hello',
        bash_command='echo "Hello from k3s Airflow!"',
    )

    # 3. สร้าง Task 2: ใช้ Python
    def my_python_func():
        print("This is Python running inside Kubernetes!")

    t2 = PythonOperator(
        task_id='run_python',
        python_callable=my_python_func,
    )

    # 4. กำหนดลำดับการทำงาน (t1 ทำก่อน t2)
    t1 >> t2