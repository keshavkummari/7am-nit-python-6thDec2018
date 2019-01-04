"""
A for loop is used for iterating over a sequence i.e. a List, A Tuple, A Dict, a Set or A String
for = Keyword

: = Suit

in: operator
"""
technologies = ['Cloud','Bigdata','AI','DevOps']

"""
for variable_expression operator variable_name suit
    statements 
"""

for i in technologies:
    print(i)

for i in [1,2,3,4,5,6]:
    print(i)

for a in (1,2,3,4,5,6):
    print(a)

for a in "AWS Azure DevOps Python":
    print(a)

for a in {"Name":"DevOps","Tech":"Python"}:
    print(a)