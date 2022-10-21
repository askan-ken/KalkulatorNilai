num1 = input("Masukkan nilai quiz: ")
num2 = input("Masukkan nilai UTS: ")
num3 = input("masukkan nilai UAS: ")
num4 = 3
nilai1 = "A"
nilai2 = "B"
nilai3 = "C"
hasil = int(num1)+int(num2)+int(num3)
hakhir = hasil/int(num4)

if (hakhir >= 81):
	print("Kerja bagus perthankan, nilai kamu = ",hakhir ,"(",nilai1,")")
if (hakhir <= 80):
	print("sudah bagus nilai kamu = ",hakhir ,"(",nilai2,")")
if (hakhir <= 60):
	print("Perbaiki lagi nilai kamu = ",hakhir ,"(",nilai3,")")
