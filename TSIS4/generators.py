def squares_generator(N):
    for i in range(N):
        yield i ** 2



def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i




def divisible_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i



def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2



def numbers_down_to_zero(n):
    while n >= 0:
        yield n
        n -= 1


