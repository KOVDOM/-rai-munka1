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