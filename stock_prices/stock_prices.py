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
  print('original prices', prices)
  high = max(prices)
  highpoint = prices.index(high)
  print(high)
  buys = prices[:highpoint]
  low = min(buys)
  lowpoint = prices.index(low)
  profit = high - low
  print(f'Buy in period {lowpoint} at ${low}, and sell in period : {highpoint} at ${high} for a profit of: ${profit}')



prices = [1050, 270, 1540, 3800, 2]

test_prices = [math.floor(random.random()*5000) for i in range(5) ]
print('test_prices', test_prices)
find_max_profit(test_prices)






# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))