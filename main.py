import json
from stateMaker import re # State Creater
from Matcher import match # Match Algorithum
from endStartSymbol import check
Expression = input()
Input = input()
states = re(Expression)#  convert a expression to States
print(json.dumps(states, indent = 4))
output = check(Expression,match(Input,states),Input) # print the output
print( output) # output as list 
#[] * +  {}