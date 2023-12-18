#!/usr/bin/env python3
import sys
from Utils import job_bq,get_query
import json
from google.cloud import bigquery

def get_conf(file_conf):
     with open(file_conf) as file:
         conf = json.load(file)
     return conf

def main(path_conf, path_query):
    json_conf = get_conf(path_conf)
    source_table = json_conf["source_table"]
    final_table = json_conf["final_table"]
    query = get_query(path_query)
    job_bq(source_table, final_table, query)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])