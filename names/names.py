import time
from bst_dataStructure.bst_dataStructure import BSTNode

# per readme last line of item 2

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
""" 19 second method(less characters, easier to read"""

faster_names = BSTNode("Not Target")

for i in names_2:
    faster_names.insert(i)

for i in names_1:
    if faster_names.contains(i):
        duplicates.append(i)

"""21 second method(excessive code, not as readable): 

faster_names = BSTNode(names_1[0])  # use pre created data structure

for i in names_1:
    faster_names.insert(i)
    
for i in range(len(names_2)):
    if faster_names.contains(names_2[i]):
        duplicates.append(names_2[i])"""

""" Original Code to change to recursive to run faster"""
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
