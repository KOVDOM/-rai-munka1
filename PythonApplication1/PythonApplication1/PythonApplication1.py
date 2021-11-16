print("Működik a Git?")
print("Mindjárt kiderül")

szamok=[3,4,2,7,8,1,9,7,3]

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
print(db)
