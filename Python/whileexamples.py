n = 0
while n < 5:
    print(f'value is {n}')
    n+= 1
else:
    print('Loop ended')

# else runs only if while executes atleast once

n = 0
while n < 5:
    if n == 3:
        break
    print(f'value is {n}')
    n+= 1

n = 0
while n < 5:
    if n == 3:
        pass
    print(f'value is {n}')
    n+= 1

n = 0

while n < 5:
    if n == 2:
        continue
    print(f'value is {n}')
    n = n+1