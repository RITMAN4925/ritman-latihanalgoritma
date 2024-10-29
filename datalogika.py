logika ="saya suka logika, saya suka belajar python"
print ("logika")
# Meminta input umur dan status ujian
umur = int(input("Masukkan umur Anda: "))
ujian_lulus = input("Apakah Anda sudah lulus ujian (ya/tidak)? ")

# Logika untuk menentukan kelayakan mendapatkan SIM
if umur >= 17 and ujian_lulus.lower() == 'ya':
    print("Anda memenuhi syarat untuk mendapatkan SIM.")
else:
    print("Anda tidak memenuhi syarat untuk mendapatkan SIM.")
