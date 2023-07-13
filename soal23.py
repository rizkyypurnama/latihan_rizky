angka = int(input("masukan angka"))
if angka % 2 ==0:
    jenis_bilangan = "genap"
else:
    jenis_bilangan = "ganjil"
output = "angka {} adalah {}".format(angka,jenis_bilangan)
print(output)