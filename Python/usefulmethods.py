for num in range(5):
    print(num)

for num in range(2, 5):
    print(num)

for num in range(2, 10, 2):
    print(num)


my_list = list(range(5, 15, 3))

print(my_list)

# use of enumerate
name = 'abcdef'

for item in enumerate(name):
    print(item)

for index, letter in enumerate(name):
    print(f"index = {index} , letter = {letter}")

# zip the lists

list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']
list_c = ['x', 'y', 'z']
for item in zip(list_a, list_b, list_c):
    print(item)

# ignores extra elements
list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c']
list_c = ['x', 'y', 'z']
for item in zip(list_a, list_b, list_c):
    print(item)

# in keyword works with iterable objects

print(2 in [1, 2])

print('k1' in {'k1': 1, 'k2': 2})

# min and max

print(min(list_a))

print(max(list_a))

# shuffle the list(operates in-place)

from random import shuffle

my_list = list(range(0, 10))

print(my_list)

shuffle(my_list)

print(my_list)

# return a random integer

from random import randint

my_num = randint(1, 100)

print(my_num)

result = input('Enter a number : ')

print(result)

print(type(result))

result = int(input('Enter another number : '))

print(result)

print(type(result))