from datetime import datetime
import time

# Mengambil timestamp sekarang
timestamp_sekarang = time.time()

print("Timestamp:", timestamp_sekarang)

# Mengubah timestamp menjadi datetime lokal
tanggal_waktu = datetime.fromtimestamp(
    timestamp_sekarang
)

print("Tanggal dan waktu:", tanggal_waktu)

# Mengubah datetime menjadi timestamp
timestamp_kembali = tanggal_waktu.timestamp()

print("Timestamp kembali:", timestamp_kembali)