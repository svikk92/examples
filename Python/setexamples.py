my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(2)
print(my_set)

my_set.remove(1)

print(my_set)

my_list = [1, 3, 3, 4, 4, 5, 5, 5, 6]

my_set = set(my_list)

print(my_set)

my_list = list(my_set)

print(my_list)