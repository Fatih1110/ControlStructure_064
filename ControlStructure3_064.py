n = int(input("Masukkan jumlah suku Fibonacci: "))

a = 0
b = 1

print("Deret Fibonacci:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c