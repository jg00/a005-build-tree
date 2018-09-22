# Assignment 1 - Return Unique List (Revised - Shorter Version)
names = ["Alex","John","Mary","Steve","John", "Steve"]
unique = []

for name in names:
    if (name not in unique):
        unique.append(name)

print("Unique list: " + str(unique))


# Assignment 1 - Return Unique List (Long)
# names = ["Alex","John","Mary","Steve","John", "Steve"]
# unique = []
# for name in names:

#     count = 0
#     for chkname in names:
#         if (name == chkname):
#             count += 1
    
#     # print(name + " " + str(count))

#     if (count == 1):
#         unique.append(name)
#     else:
#         if (name not in unique):
#             unique.append(name)

# print(unique)


# Assignment 2 - Max
items2 = [8,15,4,3,-2,-18,5,2,9,-3,9]

current_value = items2[0]
for index in range(len(items2)-1):
    if (current_value < items2[index + 1]):
        current_value = items2[index + 1]
print("Max: {}".format(current_value))

# Assignment 2b - Max (Another Version)
# print(max(items2))


# Assignment 3 - Min
current_value = items2[0]
for index in range(len(items2)-1):
    if (current_value > items2[index + 1]):
        current_value = items2[index + 1]
print("Min: {}".format(current_value))

print("\n")


# Assignment 4 - Create Tree with *
print("Build tree based on odd number of *: ")
odd_number = 19

count_of_odd_numbers = 0
for i in range(1, odd_number+1, 2):
    count_of_odd_numbers += 1
# print(count_of_odd_numbers)

# Create list in reverse order based on count_of_odd_numbers 
lvl_list = []
for i in range(count_of_odd_numbers-1, -1, -1):
    lvl_list.append(i)
# print(lvl_list)

# Concatenate list of blanks (based on lvl_list in reverse order (highest number first)) to * per level
idx = max(lvl_list)
for j in range(1, odd_number+1, 2):
    print( (" " * idx) + ("*" * j) )
    idx = idx - 1


