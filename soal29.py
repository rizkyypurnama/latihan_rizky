angka = int(input("Masukkan sebuah angka: "))
angka_format = "{:05}".format(angka)

output = "Angka dengan 5 digit: {}".format(angka_format)

print(output)