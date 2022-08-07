import sys
import os
sys.path.append(os.getcwd()+ '/dependencies')
import requests

def handler(event, context):
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    return r.json()
    # df = wr.s3.read_parquet(path=['s3://redshift-s3-project/userdata1.parquet'])
    # return "No of rows in userdata1.parquet is "+ len(df)

# Test
