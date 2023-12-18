#!/usr/bin/env python3
import sys
from Utils import job_load_bq
import json
from google.cloud import bigquery

def get_conf(file_conf):
     with open(file_conf) as file:
         conf = json.load(file)
     return conf

def main(path_conf):
    json_conf = get_conf(path_conf)
    table_id = json_conf["table_id"]
    uri = json_conf["bucket_source"]
    
    if json_conf["format"] == "PARQUET":
        source_format = bigquery.SourceFormat.PARQUET
    
    job_load_bq(uri, table_id, source_format)

if __name__ == "__main__":
    main(sys.argv[1])