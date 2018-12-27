"""
24. rfind() method :
25. rindex() method :
26. split() method :
27. splitlines() methods :
"""
pyworld = """
aws
azure
python
devops
"""
pyworld = "aws\n \
        devops\n \
          azur\n \
          python"

print(pyworld, type(pyworld), id(pyworld), len(pyworld))

"""
print("find", pyworld.find('azure'))  # It searching a substring from left to right
print("rfind",pyworld.rfind('azure')) # It searching a substring from right to left

print("index: ",pyworld.index('azure'))
print("rindex: ",pyworld.rindex('azure'))
print("split : ",pyworld.split('$'))
"""
print("split : ",pyworld.split(' ',3)) # 0 1 2 3 = 4

print("splitlines() Method : ",pyworld.splitlines())