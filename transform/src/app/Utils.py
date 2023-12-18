#!/usr/bin/env python3
from google.cloud import bigquery

#Obtener el Cliente de Bigquery
def get_client_bq():
    return bigquery.Client()

#Obtiene query de un script
def get_query(path_query):
     f = open (path_query,'r')
     query = f.read()
     return query

#Crea la configuracion del job con parametros
def create_job_config(source_table, final_table):
    job_config = bigquery.QueryJobConfig(
        query_parameters=[bigquery.ScalarQueryParameter("source_table", "STRING", "source_table"),
        bigquery.ScalarQueryParameter("final_table", "STRING", "final_table"),])

#Ejecuta job de carga a Bigquery
def job_bq(source_table, final_table, query):
    job_config = create_job_config(source_table, final_table)
    query_job = get_client_bq().query(query,job_config) 
