# unique way of quickly creating a list

myname = 'vikas'
my_title = 'sharma'

my_list = []
for letter in myname:
    my_list.append(letter)

print(my_list)

my_list = [letter for letter in my_title]

print(my_list)

my_list = [x for x in 'word']

print(my_list)

# it works for all iterables and supports various operations

my_list = [num**2 for num in range(1, 6)]

print(my_list)

my_list = [num**2 for num in range(0, 10) if num % 2 == 0]

print(my_list)

celcius = [10, 20, 30, 40.5, 50]

fahrenheit = [((9/5)*temp + 32) for temp in celcius]

print(fahrenheit)

# order changes if we use if-else here
my_list = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]

print(my_list)

my_list = []

for x in [2, 3, 4]:
    for y in [1, 10, 100]:
        my_list.append(x*y)

print(my_list)

my_list = []

my_list = [x*y for x in [2, 3, 4] for y in [1, 10, 100]]

print(my_list)