# -*- coding: utf-8 -*-
import airflow
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators import kubernetes_pod_operator

# Dag
DAG_ID = 'dag-ingest-dwh-fire' 
CREATED_BY = 'Andres'
CREATION_DATE = datetime(2023, 12, 17)
SCHEDULE = '30 08 * * *'
catchup = False

args = {
    'owner': CREATED_BY,
    'depends_on_past': False,
    'start_date': CREATION_DATE,
    'email_on_failure': False,
    'retries': 0,
    'retry_delay': timedelta(hours=0)
}

with DAG(
    dag_id = DAG_ID,
    default_args = args,
    schedule_interval = SCHEDULE,
    catchup = catchup,
    concurrency = 1,
    max_active_runs = 1
) as dag:

    begin = DummyOperator(
        task_id = 'Begin'
    )

    extract = kubernetes_pod_operator.KubernetesPodOperator(
    task_id='extract',
    name='extract', 
    namespace='default',
    image='us-central1-docker.pkg.dev/copper-verbena-408405/andres-tume/extract:last',
    affinity={
        'nodeAffinity': {
            'requiredDuringSchedulingIgnoredDuringExecution': {
                'nodeSelectorTerms': [{
                    'matchExpressions': [{
                        'key': 'cloud.google.com/gke-nodepool',
                        'operator': 'In',
                        'values': [
                            'andres-tume-pipeline-pool'
                        ]
                    }]
                }]
            }
        }
    }
    )

    load_dwh = kubernetes_pod_operator.KubernetesPodOperator(
    task_id='load_dwh',
    name='load_dwh', 
    namespace='default',
    image='us-central1-docker.pkg.dev/copper-verbena-408405/andres-tume/load:last',
    affinity={
        'nodeAffinity': {
            'requiredDuringSchedulingIgnoredDuringExecution': {
                'nodeSelectorTerms': [{
                    'matchExpressions': [{
                        'key': 'cloud.google.com/gke-nodepool',
                        'operator': 'In',
                        'values': [
                            'andres-tume-pipeline-pool'
                        ]
                    }]
                }]
            }
        }
    }
    )

    add_codmes = kubernetes_pod_operator.KubernetesPodOperator(
    task_id='add_codmes',
    name='add_codmes', 
    namespace='default',
    image='us-central1-docker.pkg.dev/copper-verbena-408405/andres-tume/transform:last',
    affinity={
        'nodeAffinity': {
            'requiredDuringSchedulingIgnoredDuringExecution': {
                'nodeSelectorTerms': [{
                    'matchExpressions': [{
                        'key': 'cloud.google.com/gke-nodepool',
                        'operator': 'In',
                        'values': [
                            'andres-tume-pipeline-pool'
                        ]
                    }]
                }]
            }
        }
    }
    )

    save_history = kubernetes_pod_operator.KubernetesPodOperator(
    task_id='save_history',
    name='save_history', 
    namespace='default',
    image='us-central1-docker.pkg.dev/copper-verbena-408405/andres-tume/transform:last',
    affinity={
        'nodeAffinity': {
            'requiredDuringSchedulingIgnoredDuringExecution': {
                'nodeSelectorTerms': [{
                    'matchExpressions': [{
                        'key': 'cloud.google.com/gke-nodepool',
                        'operator': 'In',
                        'values': [
                            'andres-tume-pipeline-pool'
                        ]
                    }]
                }]
            }
        }
    }
    )

    finish = DummyOperator(
        task_id = 'finish'
    )


    begin >> extract >> load_dwh >> add_codmes >> save_history >> finish   
