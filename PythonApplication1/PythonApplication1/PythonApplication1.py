print("Működik a Git?")
print("Mindjárt kiderül")

szamok=[3,4,2,7,8,1,9,7,3,2,3,5,1,5,2,6,7,8,9,4,6,2,5,4,6]

#összegzés tétele
osszeg =0
for x in szamok:
    osszeg=osszeg+x
print(osszeg)

#eldöntés tétele
vane =False
for x in szamok:
    if (x==1):
        vane=True
print(vane)
   
#megszámlálás tétele hány darab 3as van a listában
db=0
for x in szamok:
    if x==3 :
        db=db+1;
print("A hármasok darabszáma")
print(db)

#feltételes összeg csak a páros számokat összegzem
print("Feltétel összegezése:")
osszeg=0
for x in szamok:
    if x%2==0 :
        print(x)
        osszeg=osszeg+x
print("A páros számok összege:")
print(osszeg)

#minimum kiválasztás tétele
print("minimum kiválasztás tétele")
min1=1000
for x in szamok:
    if x<min1:
        min1=x
print(min1)
print(min(szamok))

#maximum kiválasztás tétele
print("maximum kiválasztás tétele")
max1=1000
for x in szamok:
    if x>max1:
        max1=x
print(max1)
print(max(szamok))

#órai feladat1
list=[24,53,65,50,75,49,32,94,34,63]
valt=0
atlag=0
for x in list:
    atlag=sum(list)/len(list)
print(atlag)

min2=0
for x in list:
    if x<min2:
        min2=x
print(min(list))

max2=100
for x in list:
    if x>max2:
        max2=x
print(max(list))

vane =False
for x in list:
    if (x%2==0):
        vane=True
print(vane)

otven =0
for x in list:
    if x>50:
     otven=otven+x
print(otven)

kilenc =False
for x in list:
    if (x==9):
        kilenc=True
print(kilenc)

kilenc1=0
for x in list:
    if (x==9):
        kilenc1=kilenc1+0
print(kilenc1)
