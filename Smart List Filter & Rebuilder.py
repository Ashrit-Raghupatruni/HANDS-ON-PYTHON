data = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = input("Enter element: ")
    is_num = True
    if val == "":
        is_num = False
    else:
        for ch in val:
            if ch < '0' or ch > '9':
                is_num = False
                break
    if is_num:
        data = data + [int(val)]
    else:
        data = data + [val]

num_count = 0
str_count = 0

for item in data:
    if type(item) == int:
        num_count = num_count + 1
    elif type(item) == str:
        if item != "":
            str_count = str_count + 1

num_list = [0] * num_count
str_list = [""] * str_count

num_index = 0
str_index = 0

for item in data:
    if type(item) == int:
        num_list[num_index] = item
        num_index = num_index + 1
    elif type(item) == str:
        if item != "":
            str_list[str_index] = item
            str_index = str_index + 1

reg_number = 11746

last_digit = reg_number % 10
if (last_digit & 1) == 0:
    reversed_nums = [0] * num_count
    index = 0
    for i in range(num_count - 1, -1, -1):
        reversed_nums[index] = num_list[i]
        index = index + 1
    num_list = reversed_nums
else:
    reversed_str = [""] * str_count
    index = 0
    for i in range(str_count - 1, -1, -1):
        reversed_str[index] = str_list[i]
        index = index + 1
    str_list = reversed_str

print("Numbers List:", num_list)
print("Strings List:", str_list)

print("\nTotal Numbers:", num_count)
print("Total Strings:", str_count)