## ÜL 1
print("Palun sisestage kaks numbrit")

a = int(input("Esimene: "))
b = int(input("Teine: "))

for x in range(a, b):
    if x % 2 == 0:
        print(x)

## ÜL 2
## 1.

f = open("kttekst.txt","r")
data = f.read()
tähed = len(data)
print("Tekstis tähti kokku on:",tähed)

## 2.




