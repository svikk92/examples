def primes_count(num):
    if num < 2:
        return 0
    else:
        primes = [2]
        x = 3
        while x <= num:
            for y in range(3, x, 2):
                if x%y == 0:
                    x = x + 2
                    break
            else:
                primes.append(x)
                x = x + 2
        print(primes)
        return len(primes)


print(primes_count(3))


def spy_game(num_list):
    comp_list = [0, 0, 7, 'x']
    for num in num_list:
        if comp_list[0] == num:
            comp_list.pop(0)
        if len(comp_list) == 1:
            return True
    return False


print(spy_game([1, 0, 2, 7, 0, 1, 1]))


