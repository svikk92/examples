from builtins import sorted

my_list = [1, 'two', 3.3]

print(my_list[2])

print(my_list[:])

print(my_list[1:])

print(my_list[:1])

print(my_list[::-1])

my_list.append(99)

print(my_list)

popped_item = my_list.pop()

print(my_list)

print(popped_item)

num_list = [5, 6, 2, 2, 45, 5, 6]

num_list.sort()

num_list.reverse()

print(num_list)

num_list = [5, 6, 2, 2, 45, 5, 6]

print(sorted(num_list))


