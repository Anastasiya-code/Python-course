from random import randint

arr = []
for x in range(1, 10):
    arr.append(randint(1, 100))
print(arr)
count = 0
unique_arr = []
for x in arr:
    if x not in unique_arr:
        count += 1
        unique_arr.append(x)
print(len(unique_arr))