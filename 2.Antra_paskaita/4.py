import random

list1 = []
for x in range(3):
    list1.append(random.randint(1, 6))
print(list1)
if 5 in list1:
    print("Pralaimėjai...")
else:
    print("Laimėjai!")