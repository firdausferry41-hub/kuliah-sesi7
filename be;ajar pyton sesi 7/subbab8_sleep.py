import time

print("Program dimulai")

# Menunggu selama 3 detik
time.sleep(3)

print("Program dilanjutkan setelah 3 detik")

# Contoh hitung mundur
for angka in range(5, 0, -1):
    print(angka)
    time.sleep(1)

print("Selesai!")