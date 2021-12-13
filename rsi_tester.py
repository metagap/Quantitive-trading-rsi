# %%
import csv,numpy,talib
from data_process import data_processing
import matplotlib.pyplot as plt
import math

rsis=[]
closes = []
date = []
RSI_PERIOD = 14

filename = 'kline_ETHUSDT_1m_1 Dec, 2020_to_31 Dec, 2020.csv'

closes,rsis,date = data_processing(filename,RSI_PERIOD)

Account_Balance = 10000
Account_eth = 0
trade_quantity = 0
in_the_position = False
over_buy = 70
over_sell = 30
tx_fee_rate = 0.0005
tx_fee = 0
Account = []


for i in range(len(rsis)):
    if rsis[i] > 70:
        if in_the_position:
            trade = Account_eth*closes[i]
            tx_fee = tx_fee_rate * trade
            trade_quantity = Account_eth
            Account_Balance = Account_Balance + trade - tx_fee
            Account_eth -= trade_quantity
            in_the_position = False
            print("you have sold {} eth at {}".format(trade_quantity,closes[i]))         
    
    if rsis[i] < 30:
        if not in_the_position:
            trade_quantity = Account_Balance/closes[i]
            trade = trade_quantity*closes[i]
            Account_Balance -= trade
            Account_eth += trade_quantity*(1-tx_fee_rate)
            in_the_position = True
            print("you have bought {} eth at {}".format(trade_quantity,closes[i]))

    Checking = Account_Balance+Account_eth*closes[i]
    Account.append(Checking)

checking = 0

if in_the_position:
    checking = Account_Balance + Account_eth*closes[-1]
else:
    checking = Account_Balance

print('The current cash balance is {}'.format(Account_Balance))
print('The current eth balance is {}'.format(Account_eth))
print('The starting price is {}'.format(closes[0]))
print('The ending price is {}'.format(closes[-1]))
APY_coin = closes[-1]/closes[0]
APY_strategeis = checking/10000

if APY_coin <= APY_strategeis:
    print('The chosen period of holding coins yield is {}'.format(APY_coin))
    print('The chosen period of strategies yield is {}'.format(APY_strategeis))
    print('The strategy is great.')
else:
    print('The chosen period of holding coins yield is {}'.format(APY_coin))
    print('The chosen period of strategies yield is {}'.format(APY_strategeis))
    print('The strategy is not good enough.')

new_closes = numpy.array(closes)/closes[0]
new_checking = numpy.array(Account)/Account[0]
# %%
plt.plot(date,new_closes,'b-',label = 'eth.yield')
plt.plot(date,new_checking,'r-',label = 'strategy.yield')
plt.legend()
new_date = [date[0],date[math.floor(len(date)/4)],date[math.floor(len(date)/2)],date[math.floor(len(date)/4*3)],date[len(date)-1]]
plt.xticks(new_date)

# %%
