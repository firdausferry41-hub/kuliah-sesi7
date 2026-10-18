import time

# Timestamp saat ini
timestamp = time.time()
print("Timestamp:", timestamp)

# Waktu lokal dalam bentuk struct_time
waktu_lokal = time.localtime()

print("Tahun:", waktu_lokal.tm_year)
print("Bulan:", waktu_lokal.tm_mon)
print("Tanggal:", waktu_lokal.tm_mday)

# Menampilkan waktu dengan format tertentu
format_waktu = time.strftime(
    "%d-%m-%Y %H:%M:%S",
    waktu_lokal
)

print("Waktu lokal:", format_waktu)

# Mengukur durasi proses
awal = time.perf_counter()

total = sum(range(100000))

akhir = time.perf_counter()

print("Total:", total)
print("Durasi:", akhir - awal, "detik")