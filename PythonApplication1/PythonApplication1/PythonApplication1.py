print("Működik a Git?")
print("Mindjárt kiderül")
#Írjon programot, mely kiírja a képernyőre a páros számokat 1-től 100-ig.
for i in range(0, 101, 2): 
    print(i)
    if (i%2==1):
        print(i)

#Olvass be két számot, írd ki a négyzetüket!
szam1=int(input("Kérek egy szabadon választott számot! "))
szam2=int(input("Mivel egy szám kevés ezért kérek még egy szabadon választott számot! "))
eredmeny=szam1**szam2
print(eredmeny)

#Írjon programot, mely kiírja a képernyőre a páros számokat 50-től 10-ig.
for i in range(50, 9, -2): 
    print(i)