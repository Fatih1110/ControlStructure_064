a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

if a >= b and a >= c:
    largest = a
    print("Angka Terbesar adalah:", largest)
elif b >= a and b >= c:
    largest = b
    print("Angka Terbesar adalah:", largest)
elif c >= a and c >= b:
    largest = c
    print("Angka Terbesar adalah:", largest)
else:
    print("Tidak Ada Angka Terbesar")