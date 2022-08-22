def f(n):
    return sum(list(map(int, str(n))))

def check(n):
    return n % f(n)**2 == 0

def get(n):
    s = i = 0

    while s < n:
        i += 1
        if check(i):
            s += 1

    return i


n = int(input())
print(get(n))
