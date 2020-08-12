import os
from crypto import CryptoApi

def lambda_handler(event, context):
    operation = event['operation']
    obj = CryptoApi(table_prefix=os.environ['TABLE_NAME'], exchange=os.environ['EXCHANGE_NAME'], pair=os.environ['PAIR_NAME'])
    if operation == 'ingest_new':
        obj.ingest_new()
    else:
        raise ValueError('Invalid Operation')

