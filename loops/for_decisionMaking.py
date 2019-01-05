
"""
for variable_expression operator variable_name suit
    statements 

for i in technologies:
    print(i)

    if i == "AI":
        print("Welcome to AI World")

for i in range(1,10):  #start element and end element-1 : 10-1 = 9
    print(i)

# Loop Controls : break and continue

for i in technologies:
    print(i)

    if i == "Bigdata":
        continue
        #break
        
for i in range(6):  # start index 0 1 2 3 4 5  range(6) end-1 = 5
    print(i)
else:
    print("Completed")
        
"""
# Neasted For Loop:

"""
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop"
"""

technologies = ['Cloud','Bigdata','AI','DevOps']
cloud_vendors = ['AWS','Azure','GCP']


for i in technologies:   # Outer loop

    for var in cloud_vendors:  # Inner Loop
        print(i,var)
