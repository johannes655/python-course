while True :
    loop = input('APAKAH KAMU MAU MENGGUNAKAN KALKULATOR (y/n):')

    if loop == ('y'):

        angka1 = int(input('Masukan angka pertama : '))
        angka2 = int(input('Masukan angka kedua :'))

        print ('1 = tambah')
        print ('2 = kurang')
        print ('3 = kali')
        print ('4 = bagi')
        print ('5 = pangkat')
        operasi = int(input('masukan angka operasi diatas : '))

        if operasi == 1 :
            print (angka1 + angka2)
        if operasi == 2 :
            print (angka1 - angka2)
        if operasi == 3 :
            print (angka1 * angka2)
        if operasi == 4 :
            print (angka1 / angka2)
        if operasi == 5 :
            print (angka1 ** angka2)

    else:
        break
print ('bye bitch terimakasih')
