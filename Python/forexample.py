my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    if num%2 == 0:
        print(f' Even : {num}')
    else:
        print(f' Odd : {num}')

list_sum = 0

for num in my_list:
    list_sum = list_sum + num

print(f'Sum : {list_sum}')


for letter in 'alsdjlas':
    print(letter)

for _ in 'alsdjlas':
    print(letter)

my_list = [(1, 2), (3, 4), (5, 6)]

print(len(my_list))

# tuple unpacking

for (a, b) in my_list:
    print(f'A = {a}')
    print(f"B = {b}")

# dict unpacking

my_dict = {'k1': 1, 'k2': 2, 'k3': 3}

for item in my_dict.items():
    print(item)

for (key, value) in my_dict.items():
    print(f'key = {key}, value = {value}')
