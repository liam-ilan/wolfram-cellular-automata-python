import time
import os
import sys

# returns string with length of width of terminal, with a 1 at the middle
def init():
  pad = int((float(os.popen('stty size', 'r').read().split()[1]) / 2) - 1)
  return ('0' * pad) + '1' + ('0' * pad)

def validate_user_input(string):
  return True if (-1 < int(string) < 256) else False

# prints to screen
def render(string):
  print(string.replace('1', chr(0x2588)).replace('0', ' '))

def evolve(pop, rule):

  # set ruleset to bin string
  ruleset = rule
  ruleset = str(bin(ruleset))[2:].zfill(8)

  # make res population in witch all 1 are 0
  res = pop.replace('1', '0')

  # run on every charechter in population
  for y in range(0,len(pop)):

    #run on every pattern
    for x in range(0,len(ruleset)):

      # get pattern
      pattern = str(bin(x))[2:].zfill(3).replace('0', '2').replace('1', '0').replace('2', '1')
      
      #update res to correct rules based on pattern
      if pop[y-1:y+2] == pattern:
        res = list(res)
        res[y] = ruleset[x]
        res = "".join(res)

  return res

# main

if validate_user_input(sys.argv[1]):
  
  string = init()

  while True:
    render(string)
    string = evolve(string, int(sys.argv[1]))
    time.sleep(0.1)

else:
  print('Please enter a rule number between 0 and 255.')



