# global variable
name = 'GLOBAL'


def greet():
    # enclosing function variable
    name = 'ENCLOSING'

    def hello():

        # local variable
        name = 'LOCAL'
        print(name)

    hello()


greet()


# global keyword


def change_global():
    global name
    print(f'old value {name}')
    name = 'CHANGED LOCALLY'


change_global()

print(f'new name is {name}')

