
import subprocess
import sys

print("================================")
print("   PROGRAM BELAJAR DATE TIME")
print("================================")
print("1. Datetime Module")
print("2. Strftime")
print("3. Strptime")
print("4. Current Date and Time")
print("5. Current Time")
print("6. Timestamp to Datetime")
print("7. Time Module")
print("8. Time Sleep")
print("9. Latihan Gabungan")

pilihan = input("\nPilih materi (1-9): ")

file_materi = {
    "1": "subbab1_datetime.py",
    "2": "subbab2_strftime.py",
    "3": "subbab3_strptime.py",
    "4": "subbab4_current_datetime.py",
    "5": "subbab5_current_time.py",
    "6": "subbab6_timestamp.py",
    "7": "subbab7_time_module.py",
    "8": "subbab8_sleep.py",
    "9": "latihan_gabungan.py"
}

if pilihan in file_materi:
    print("\nMenjalankan materi...\n")
    subprocess.run(
        [sys.executable, file_materi[pilihan]]
    )
else:
    print("Pilihan tidak tersedia!")
