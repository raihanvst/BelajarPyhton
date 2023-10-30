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