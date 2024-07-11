def is_prime(fun):
    def wrapper(*arg, **args):
        result = fun(*arg, **args)
        count = 0
        for i in range(1, result+1):
            if result%i == 0:
                count += 1
        if count == 2:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper


def sum_three(*arg):
    summ = sum(arg)
    return summ

new_sum = is_prime(sum_three)

a = sum_three(1, 2, 3)
print(a)
print()
print(new_sum(1, 2, 3))
print()
print(new_sum(2, 3, 6))
print()
print(new_sum(0, 0, 0))
print()
print(new_sum(0, 0, 1))
print()
print(new_sum(3, 3, 3))
print()
print(new_sum(5, 5, 7))