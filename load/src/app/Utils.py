#!/usr/bin/env python3
from google.cloud import bigquery

#Obtener el Cliente de Bigquery
def get_client_bq():
    return bigquery.Client()

#Ejecuta job de carga a Bigquery
def job_load_bq(uri, table_id, source_format):
    job_config = bigquery.LoadJobConfig(source_format=source_format,)
    load_job = get_client_bq().load_table_from_uri(uri, table_id, job_config=job_config)