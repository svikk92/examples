# LEs are way to create one time use anonymous functions
from builtins import map


def square(num):
    return num**2


# use of map
my_list = [1, 2, 3, 4, 5]
for item in map(square, my_list):
    print(item)

result_list = list(map(square, my_list))
print(result_list)

# use of filter, works with functions returning true or false


def check_even(num):
    return num % 2 == 0


my_num = [1, 2, 3, 4, 5]
result_list = list(filter(check_even, my_num))

print(result_list)

# lambda expressions for def square(num): return num**2

myfunc = lambda num: num**2

print(myfunc(10))

# we can do above but lambda is more useful for anonymous functions

result_list = list(map(lambda num: num**2, my_list))

print(result_list)

# same thing we can do with filter also

result_list = list(filter(lambda num: num%2 == 0, my_list))

print(result_list)

# getting first letter of strings in list

names = ['Vikas', 'Kumar', 'Sharma']

result_list = list(map(lambda x: x[0], names))

print(result_list)







