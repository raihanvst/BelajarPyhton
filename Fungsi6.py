def faktorial(n):
    if n == 0: return 1
    return n * faktorial(n-1)

def main():
    n = int(input("masukan bilangan bulat : "))
    print('%d! = %d' % (n,faktorial(n)))
if __name__ == '__main__':
    main()