import numpy, talib, csv
from datetime import datetime

closes = []
rsis = []
dates = []

def data_processing(filename,RSI_PERIOD):
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            close = row[4]
            date = row[0]
            date = datetime.fromtimestamp(int(date)/1000)
            closes.append(float(close))
            dates.append(date)
            np_closes = numpy.array(closes)
            RSI = talib.RSI(np_closes,RSI_PERIOD)
            rsis.append(RSI[-1])
    
    return closes,rsis,dates