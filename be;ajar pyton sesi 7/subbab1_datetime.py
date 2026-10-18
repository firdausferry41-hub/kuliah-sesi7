import datetime

# Mengambil tanggal dan waktu sekarang
sekarang = datetime.datetime.now()

# Mengambil tanggal hari ini
hari_ini = datetime.date.today()

print("Tanggal dan waktu:", sekarang)
print("Tanggal hari ini:", hari_ini)

# Membuat tanggal sendiri
tanggal = datetime.date(2026, 10, 17)
print("Tanggal yang dibuat:", tanggal)