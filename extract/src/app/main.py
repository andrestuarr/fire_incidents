#!/usr/bin/env python3
import sys
from Utils import read_data,write_gcs
from datetime import date
import json


def get_conf(file_conf):
    with open(file_conf) as file:
        conf = json.load(file)
    return conf


def main(path_conf):

    json_conf = get_conf(path_conf)
    identifier = json_conf['identifier']
    limit = json_conf['limit']
    bucket_name = json_conf['bucket_name']
    file_name = json_conf['file_name']

    df = read_data(identifier,limit)
    today = date.today()
    blob_name = file_name + today.strftime("%Y-%m-%d") + '.parquet'
    write_gcs(df,bucket_name, blob_name)

if __name__ == "__main__":
    main(sys.argv[1])