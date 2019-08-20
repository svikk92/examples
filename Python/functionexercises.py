def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 ==0:
        return min(num1, num2)
    else:
        return max(num1, num2)


print(lesser_of_two_evens(10, 23))


def word_cracker(arg):
    mylist = arg.lower().split()
    return mylist[0][0] == mylist[1][0]


print(word_cracker('Hello World'))


def other_side_of_seven(num):
    return (7-num)*2 + 7


print(other_side_of_seven(4))

print(other_side_of_seven(12))


def capitalize_first_and_fourth(arg):
    first_part = arg[:3].capitalize()
    second_part = arg[3:].capitalize()
    return first_part + second_part


print(capitalize_first_and_fourth('hello'))


def master_yoda(word):
    my_list = word.split()
    my_list = my_list[::-1]
    return ' '.join(my_list)


print(master_yoda("hello dear world"))


def almost_there(num):
    return abs(100-num) <= 10 or abs(200-num) <= 10


print(almost_there(189))

