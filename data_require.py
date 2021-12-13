import config,csv,talib,numpy
from binance.client import Client


api_secret = config.API_SECRET
api = config.API_KEY


client = Client(api,api_secret)


SYMBOL = 'ETHUSDT'
TIME_START = '1 Jan, 2020' #date Month year
TIME_END = '31 Dec, 2020'

def main(SYMBOL,TIME_START,TIME_END):
    try:
        klines = client.get_historical_klines(SYMBOL, Client.KLINE_INTERVAL_1MINUTE, TIME_START, TIME_END)
        csvfile = open('kline_{}_1m_{}_to_{}.csv'.format(SYMBOL,TIME_START,TIME_END),'w',newline = '')
        csvwriter = csv.writer(csvfile, delimiter = ',')

        for kline in klines:
            csvwriter.writerow(kline)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return True

if __name__ == "__main__":
    main(SYMBOL,TIME_START,TIME_END)



