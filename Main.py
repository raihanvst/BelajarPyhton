def salam():
    print("hello aku sekarang sekolah di smk")
salam()

def abcd():
    print("aku masuk jueusan rpl karna ada animasi nya")
abcd()

def apa():
    print("ternyata animasi nya cuma sedikit")
apa()

def mey():
    print("tapi gpp tetep semangat hal baru")
mey()

def bt():
    print("tapi rada hese gening hehe")
bt()

def heppi():
    print("bisa deng dikit")
heppi()

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
#pemanggilan fungsi
print("luas persegi : %d" % luas_persegi(100))

#membuat variabel global
nama = "python"
versi = "1.0.0"

def help():
    #ini variabel lokal
    nama = "c#"
    versi = "1.0.2"
    #mengakses variabel lokal
    print ("nama: %s" % nama)
    print ("versi: %s" % versi)


#mengakses variabel global
print ("nama: %s" % nama)
print ("versi: %s" % versi)

# memanggil fungsi help()
help()

def halo_dunia():
    print('haloo python! hallo dunia')
#memanggil fungsi
halo_dunia()


def selamat_datang (nama) :
    print(f'hallo {nama}, selamat datang!')

selamat_datang('andiya')
selamat_datang('devina')
selamat_datang('nivya')
selamat_datang('angel')

def selamat_tinggal (nama) :
    print(f'selamat tinggal {nama}, sampai jumpa lagi')

selamat_tinggal('andiya')
selamat_tinggal('devina')
selamat_tinggal('nivya')
selamat_tinggal('angel')


def fluar ():
   def fdalam():
    print('fdalam() dipanggil')
    #perintah fungsi untuk fluar()
    print ('fluar() dipanggil')
    #memanggil fungsi fdalam()
   fdalam()
fluar()
fluar()

def outer_fuction(siapa):
    def inner_function():
        print(f"hello,{siapa}")
    inner_function()
outer_fuction("mey")

# otside function
def outer():
    message = 'local'

    # nested function
    def inner():

        # declaremnonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()

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

def faktorial(n):
    if n == 0: return 1
    return n * faktorial(n-1)

def main():
    n = int(input("masukan bilangan bulat : "))
    print('%d! = %d' % (n,faktorial(n)))
if __name__ == '__main__':
    main()
