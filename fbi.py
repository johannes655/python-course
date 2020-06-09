ole = {"age" : 20, "full name" : "OLE THE TIGER","Crime" : "Killing Tigers"}
ian = {"age" : 26, "full name" : "DIANANA","Crime" : "KITTEN PREDATOR"}
edu = {"age" : 21, "full name" : "EDUDOROS BANKS","Crime" : "DOG HUNTER"}
kim = {"age" : 10, "full name" : "KINININ","Crime" : "HEAD OF MAFIA"}

mostwanted = [ole,ian,edu,kim]

print ('====================')
print ('FBI MOST WANTED LIST')
print ('====================')

import time

counter = 0
for loop in range (3):
  for x in range (0,4):
    b = "loading" + "." * x
    print(b)
    time.sleep (0.2)
  #counter += 1

print (f" \n Here's The List \n ")

for x in mostwanted :
    for key,val in x.items():
            print(f"{key} : {val}")
