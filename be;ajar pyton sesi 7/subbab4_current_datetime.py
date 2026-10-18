from datetime import datetime

# Mengambil tanggal dan waktu sekarang
sekarang = datetime.now()

print("Tanggal dan waktu sekarang:", sekarang)

# Menampilkan dalam format Indonesia
format_indonesia = sekarang.strftime(
    "%d-%m-%Y %H:%M:%S"
)

print("Format Indonesia:", format_indonesia)