import random
print("Rolling Dice Simulator")
print("======================")


again = True

while again :
    pilih = input("Do you wanna roll? (y/n) :")

    x = random.randint(1,6)

    if pilih == "y":
        print(f"Selamat Angka Dadu Anda {x}")
        print ("Terima Kasih")

    else :
        print("Yasudah Terimakasih")
        break
