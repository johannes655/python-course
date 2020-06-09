username1 = "jo655"
password1 = "65304585"

username2 = "edu 555"
password2 = "081586108377"

for tries in range (3,0,-1):
    print(f"Anda Memiliki {tries} Kali Coba Untuk Login")
    username = input("masukan username anda : ")
    password = input("masukan password anda : ")

    if username == "jo655" and password == password1:
        print ("Selamat Anda Berhasil Login !!!")
        break
    elif username == "edu555" and password == password2:
        print ("Selamat Anda Berhasil Login !!!")
        break
    else:
        print ("Username Atau Password Anda Salah")

    if tries == 0:
        print('Terlalu Banyak Mencoba, Silahkan Coba Kembali Setelah 5 menit')
        break
    else:
        continue
