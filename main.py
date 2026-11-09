# DEV 1
from tambah import tambah
from kurang import kurang
from kali import kali
from bagi import bagi

# DEV 2
print("=== KALKULATOR SEDERHANA ===")
print("1. Tambah (+)")
print("2. Kurang (-)")
print("3. Kali (*)")
print("4. Bagi (/)")

# DEV 3
pilihan = input("Pilih (1-4): ")
a = float(input("Angka pertama: "))
b = float(input("Angka kedua: "))

# DEV 4
if pilihan == '1':
    print("Hasil:", tambah(a, b))
elif pilihan == '2':
    print("Hasil:", kurang(a, b))
elif pilihan == '3':
    print("Hasil:", kali(a, b))
elif pilihan == '4':
    print("Hasil:", bagi(a, b))
else:
    print("Pilihan tidak valid")