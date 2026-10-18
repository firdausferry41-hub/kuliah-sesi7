from datetime import datetime

teks_tanggal = "17-10-2026 10:30:00"

# Mengubah teks menjadi objek datetime
hasil = datetime.strptime(
    teks_tanggal, "%d-%m-%Y %H:%M:%S"
)

print("Teks awal:", teks_tanggal)
print("Hasil konversi:", hasil)
print("Tipe data:", type(hasil))

# Mengambil bagian tanggal
print("Tanggal:", hasil.day)
print("Bulan:", hasil.month)
print("Tahun:", hasil.year)