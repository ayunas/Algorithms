#!/usr/bin/python

import math

'''
1. compare values of each key
2. subtract ing key from recipe key for all keys
3. if any keys are negative - return 0
4. after a single subtract operation, increment a serving counter.
5. go back to step 2 and repeat.
'''

def recipe_batches(recipe, ingredients):
  print('recipe', recipe)
  print('ingredients', ingredients)

  #create a placeholder serving dictionary to keep track of calculations
  serving = {}
  for ing in recipe:
    if ing not in ingredients:
      print(f'cannot make recipe, do not have any {ing}')
      return 0
    serving[ing] = ingredients[ing]

  # print('serving', serving)
  #----------------------------------------------------------------------
  
  serving_count = 0

  # while any(ing < 0 for ing in serving.values())
  print(any(ing > 0 for ing in serving.values()))
  # while serving['milk'] > 0 or serving['butter'] > 0 or serving['flour'] > 0:  #while the every ing key in serving > 0
  while any(ing > 0 for ing in serving.values()):
    # print('serving_count', serving_count)
    # print(any(ing > 0 for ing in serving.values()))
    for ing in recipe:
      serving[ing] = serving[ing] - recipe[ing]
    
    # print('serving after', serving)  
    
    for ing in serving:
      if serving[ing] < 0:
        print(f'able to make {serving_count} servings of the recipe')
        return serving_count
    
    serving_count = serving_count + 1

  
  return serving_count
 


# recipe = { 'milk': 10, 'butter': 10, 'flour': 5 }
# ingredients = { 'milk': 50, 'butter': 60, 'flour': 75 }

# recipe_batches(recipe,ingredients)


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))