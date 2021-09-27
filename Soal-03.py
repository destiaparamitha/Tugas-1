#Destia Paramitha

praktek = int(input("Masukkan nilai ujian praktek : "))
teori = int(input("Masukkan nilai ujian teori: "))

if praktek < 70:
    hasil = "Anda harus mengulang ujian praktek."
elif teori < 70:
    hasil = "Anda harus mengulang ujian teori."
elif praktek and teori >= 70:
    hasil = "Selamat, Anda lulus!"
elif praktek and teori <= 70:
    hasil = "Anda harus mengulang ujian teori dan praktek."

print(str(hasil))


