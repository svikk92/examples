def hello_function(name = 'NAME!'):
    """
    prints hello
    :param name: name
    :return: None
    """
    print('Hello ' + name)

def add_fun(par1, par2):
    return par1+par2

hello_function()

hello_function('Vikas')

print(add_fun(10, 15))

def myfunc(a, b):
    return 0.05 * sum((a, b))

print(myfunc(100, 200))


# multiple args
def percentages(*args):
    # passes as tuple
    return sum(args) * 0.05

print(percentages(10, 20, 20))

# keyword arguments

def fruitchoice(**kwargs):
    # passes as dict
    if 'fruit' in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    else:
        print('blahblah')

fruitchoice(fruit = 'apple')

# args and kwargs are just indicative names, can be anything
# both can be used for same function, *args followed by **kwargs
rs = ''
for i, v in enumerate('hello'):
    if (i+1) % 2 == 0:
        rs = rs + v.upper()
    else:
        rs = rs + v.lower()

print(rs)


def myfunct(arg):
    retstr = ''
    for i, v in enumerate(arg):
        if (i+1) % 2 == 0:
            retstr = retstr + v.upper()
        else:
            retstr = retstr + v.lower()
    return retstr

myfunct('vikas')