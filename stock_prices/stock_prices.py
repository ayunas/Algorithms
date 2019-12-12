#!/usr/bin/python

import argparse

## TODO U[P]ER : Planning
'''
  pseudocode:
  [1050, 270, 1540, 3800, 2] => 3530
  create a sorted copy of the array.
  compare the 1st and last elements in the array.  (l and h).
  if the low precedes the high.  calculate h - l and save that value in a profit variable.
  also save the index of the low and high values.  save the indexes of the main array as being the "time periods" to buy and sell respectively.
  if the low is after the high, then find the next lowest, and check if that precedes the high and repeat.
  continue until l index is one less than the h index or the midpoint of the array.
  if the lowest is the last element in the list, ignore that case
'''
import math
import random

def find_max_profit(prices):

  #determine the largest dif by subtracting every successive element from the previous element.
  print('original prices', prices)
  profits = []
  for b,buy in enumerate(prices):
    sells = prices[b+1:]
    # print('sells', sells)
    for s,sell in enumerate(sells):
      profit = -buy + sell
      s_index = prices.index(sell)
      profits.append({'buy':buy,'sell':sell,'profit':profit,'periods':[b,s_index]})
  # print('profits',profits)
  # print('profits',profits)
  #calc the largest profit from profits

  max_profit_val = max([p['profit'] for p in profits])
  # valid_profits = [p for p in profits if p['profit'][0] < p['profit'][1]]
  # print('valid profits', valid_profits)
  max_profit = [p for p in profits if p['profit'] == max_profit_val ][0]
  #and p['periods'][0] < p['periods'][1]
  print('max_profit', max_profit)

  # print(max_profit.values())
  b,s,p,periods = max_profit.values()
  t1,t2 = periods

  print(f'Buy in period {t1} at ${b},  and sell in period :{t2} at ${s} for a gain of: ${p}')


  return max_profit_val


# test = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]
# test2 = [1990, 2501, 1683, 328, 992]
# test_prices = [math.floor(random.random()*5000) for i in range(5) ]
# print(find_max_profit(test_prices))





  # print([v for d in profits for v in d.values()])

# def find_max_profit(prices):
#   print('original prices', prices)
#   high = max(prices)
#   highpoint = prices.index(high)
#   if highpoint == len(prices) - 1:  #if highest price end of the array
#     return prices
#   elif highpoint == 0:
#     #find the one with minimal difference
#     #for each element in arr, subtract from each eleemnt to the right.  keep the lowest positive number as the loss.
#     diffs = []
#     for i,price in enumerate(prices):
#       sells = prices[i+1:]
#       for sell in sells:
#         dif = price - sell
#         if dif >= 1:
#           diffs.append({'high': price, 'low': sell, 'dif': dif})
    
#     difvalues = [d['dif'] for d in diffs]
#     minimum = min(difvalues)
#     min_loss = [d for d in diffs if d['dif'] == minimum]
#     high = min_loss[0]['high']
#     low = min_loss[0]['low']
#     loss = min_loss[0]['dif']
#     l = prices.index(low)
#     h = prices.index(high)
    
#     print(f'Buy in period {h} at ${high},  and sell in period :{l} at ${low} for a loss of: ${loss}')
#     return -loss
    
#     # sells = prices[1:]
#     # high_sell = max(sells)
#     # profit = high - high_sell
#     # print(f'Buy in period {lowpoint} at ${low}, and sell in period : {highpoint} at ${high} for a profit of: ${profit}')
#   else:
#     buys = prices[:highpoint]
#     low = min(buys)
#     lowpoint = prices.index(low)
#     profit = high - low
#     print(f'Buy in period {lowpoint} at ${low}, and sell in period : {highpoint} at ${high} for a profit of: ${profit}')
#     return profit



# prices = [1050, 270, 1540, 3800, 2]

# test = [100, 90, 80, 50, 20, 10]








# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))