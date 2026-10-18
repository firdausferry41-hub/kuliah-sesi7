from datetime import datetime

sekarang = datetime.now()

# Mengubah format tanggal
tanggal = sekarang.strftime("%d-%m-%Y")

# Mengubah format waktu
waktu = sekarang.strftime("%H:%M:%S")

# Mengubah format lengkap
lengkap = sekarang.strftime("%A, %d %B %Y")

print("Tanggal:", tanggal)
print("Waktu:", waktu)
print("Tanggal lengkap:", lengkap)