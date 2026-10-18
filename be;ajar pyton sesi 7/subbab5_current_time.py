from datetime import datetime

# Mengambil waktu sekarang
sekarang = datetime.now()

# Mengambil jam, menit, dan detik
waktu = sekarang.strftime("%H:%M:%S")

print("Waktu sekarang:", waktu)

# Format 12 jam dengan AM/PM
waktu_12_jam = sekarang.strftime("%I:%M:%S %p")

print("Format 12 jam:", waktu_12_jam)