harga_per_jam = 3500

durasi_parkir = int(input("Masukkan durasi parkir (jam): "))

if durasi_parkir == 1:
    harga_total = harga_per_jam
elif durasi_parkir == 2:
    harga_total = 5500
elif durasi_parkir == 3:
    harga_total = 7500
else:
    harga_total = 7500 + (durasi_parkir - 3) * 2000

print(f"Harga parkir untuk {durasi_parkir} jam adalah Rp {harga_total}")
