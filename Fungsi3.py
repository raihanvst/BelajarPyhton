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