def f(n):
    import time
    if n == 0:
        print("Go!")
        return
    print(n, end='')
    time.sleep(1)
    f(n-1)

f(3)
f(10)
