import os
import boto3
import json
import decimal
import datetime
import ccxt

region = os.environ.get('AWS_DEFAULT_REGION', 'ap-northeast-1')
dynamodb = boto3.resource('dynamodb', region_name=region)

class CryptoApi(object):

    def __init__(self, table_prefix, exchange, pair):
        self.table_prefix = table_prefix
        self.exchange = exchange
        self.pair = pair

    def ingest_new(self):
        # injest new item
        today = datetime.date.today()
        table_name = "{}_{}".format(self.table_prefix, self._format_date(today))

        exchange = getattr(ccxt, self.exchange)()
        if self.pair in exchange.load_markets().keys():
            ticker = exchange.fetch_ticker(symbol=self.pair)
            if ticker is None:
                return 'fetch_ticker is empty'
            dt = datetime.datetime.utcfromtimestamp(int(str(ticker['timestamp'])[:10]))
            timestamp = dt.strftime("%Y/%m/%d %H:%M:%S")
            item = {'name': ticker['symbol'], 'datetime': timestamp, 'high': ticker['high'], 'low': ticker['low'], 'open': ticker['open'], 'close': ticker['closel'], 'volume': ticker['baseVolume']}
            try:
                current_table = dynamodb.Table(table_name)
                response = current_table.put_item(Item = item)
                return 'put_item succeeded'
            except Exception as e:
                return 'put_item failed {}'.format(e.args)
        else:
            return 'pair is invalid in exchange'

    @staticmethod
    def __format_date(d):
        return d.strftime("%Y-%m-%d")

