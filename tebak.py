import random

x=random.randint(0,10)

while True:
    umur = int(input('Berapa umur burungku? :'))
    if umur < x :
        print('Kekecilan Burungnya')
    elif umur > x:
        print('Kegedean Burungnya')
    else:
        print('Pas Sekali')
        break
