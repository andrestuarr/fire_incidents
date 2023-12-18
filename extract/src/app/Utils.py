#!/usr/bin/env python3
import pandas as pd
from sodapy import Socrata
#import multiprocessing

#Obtine el cliente
def get_client():
    return Socrata("data.sfgov.org", None)

#Obtiene data con un limite de filas
def get_data(client,dataset_identifier, limit):
    results = client.get(dataset_identifier, limit = limit)
    return results

#Obtiene la data completa
def get_all_data(client,dataset_identifier):
    results = client.get_all(dataset_identifier)
    return results

#Genera una lista de con cada registro del dataset de Socrata
def json_append(jsonList,json):
    return jsonList.append(json)

#Convierte la lista de Json en un Dataframe
def list_toDF(results):
    return pd.DataFrame.from_dict(results)

#Almacena en un dataframe la data obtenida
def read_data(dataset_identifier,limit):
    list_json = []
    cliente = get_client()
    if limit == '0' :
        try:
            results = get_all_data(cliente,dataset_identifier)
        except:
            print("Something went wrong when calling the API")
    else:   
        try: 
            results = get_data(cliente,dataset_identifier,limit)
        except:
            print("Something went wrong when calling the API")

    for item in results:
        list_json.append(item)

    return list_toDF(results)

#Escribe dataframe en formato parquet en Gcs
def write_gcs(df,bucket_name, blob_name):
    destination_uri= 'gs://{}/{}'.format(bucket_name,blob_name)
    try:
        df.to_parquet(destination_uri)
    except:
        print("Something went wrong writing to the file")

#n_jobs  = multiprocessing.cpu_count()
#pool    = multiprocessing.Pool(processes=multiprocessing.cpu_count())
#list_json = pool.starmap(json_append, [ (list_json, item) for item in results])






