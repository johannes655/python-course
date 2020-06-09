import time

print('===============')
print('TIMER')
print('===============')

detik = int(input('berapa detik yang mau dihitung :'))
menit = int(input('berapa menit yang mau dihitung :'))
jam = int(input('berapa jam yang mau dihitung :'))
waktu = detik + menit  * 60 + jam *3600

for x in range (waktu, 0 , -1) :
    time.sleep(1)
    print(x)
