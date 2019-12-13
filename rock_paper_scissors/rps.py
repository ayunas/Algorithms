#!/usr/bin/python

# import sys
##U[P]ER - Planning
# -n comes in, specifying the number of players.
# define a set for the possible values : {'rock','paper','scissors'}
# -length of the set (3 in this case).  **n power.
# -generate s**n lists of s elements in it.  
# or 3^2 = 9 lists for 2 players playing RPS
# -loop through the set, and for each element push itself with each other member, including itself.

  
# def tool_helper(n):
#   rps = ['rock','paper','scissors']
#   possibilities = []

#   if n < 1:
#     return possibilities

#   for tool in rps:
#     outcome = []
#     outcome.append(tool)
#     possibilities.append(outcome)
#   return possibilities

# def rock_paper_scissors(n):
#   print('n value', n)
  
#   possibilities = tool_helper(n)
  
#   print('possibilities length', len(possibilities))
#   return possibilities

# print(rock_paper_scissors(4))


def rock_paper_scissors(n):
  # n = 3 
  rps = ['rock','paper','scissors']
  possibilities = []

  # outcome_length = len(rps)**n
  # print(outcome_length)

  if n == 1:
    return [['rock'],['paper'],['scissors']]
  if n == 0:
    return [[]]

  # for tool1 in rps:
  #   for tool2 in rps:
  for tool in rock_paper_scissors(n-1):
        # outcome = []
        # outcome.append(tool1)
        # outcome.append(tool2)
        # outcome.append(tool3)
    possibilities.append(tool + [rps[0]])
    possibilities.append(tool + [rps[1]])
    possibilities.append(tool + [rps[2]])

  # print(possibilities)
  return possibilities

print(rock_paper_scissors(3))


# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')