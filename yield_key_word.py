def countdown(n):
    while n > 0:
        yield n
        n -= 1
gen = countdown(5)
print(next(gen))
print(next(gen))
print(next(gen))