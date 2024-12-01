import numpy as np


with open("day_1/input.txt", "r") as file:
    data = file.read()



list_rows = data.split("\n")[:-1]
left_list = []
right_list = []
for row in list_rows:
    left_item, right_item = row.split("   ")
    left_list.append(int(left_item))
    right_list.append(int(right_item))


## Part 1

left_array = np.array(sorted(left_list))
right_array = np.array(sorted(right_list))

distance = np.sum(np.abs(left_array - right_array))
print(distance)

## Part 2

similarity = 0
for i in range(len(left_array)):
    occurences = np.sum(right_array == left_array[i])
    similarity += left_array[i] * occurences

print(similarity)
