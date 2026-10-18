
from datetime import datetime
import time

# Menampilkan tanggal dan waktu sekarang
sekarang = datetime.now()

print("=== PROGRAM DATE AND TIME ===")
print("Tanggal:", sekarang.strftime("%d-%m-%Y"))
print("Waktu:", sekarang.strftime("%H:%M:%S"))

# Mengubah teks menjadi datetime
teks = "17-10-2026 10:30:00"
hasil = datetime.strptime(
    teks, "%d-%m-%Y %H:%M:%S"
)

print("\nTanggal hasil konversi:", hasil)

# Mengubah datetime menjadi timestamp
timestamp = hasil.timestamp()
print("Timestamp:", timestamp)

# Mengubah timestamp kembali ke datetime lokal
hasil_konversi = datetime.fromtimestamp(timestamp)
print("Hasil timestamp:", hasil_konversi)

# Hitung mundur
print("\n=== HITUNG MUNDUR ===")

for angka in range(5, 0, -1):
    print(angka)
    time.sleep(1)

print("Program selesai!")
