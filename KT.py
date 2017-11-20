################################################# ÜL 1
print("Palun sisestage kaks numbrit")

a = int(input("Esimene: "))
b = int(input("Teine: "))

for x in range(a, b):
    if x % 2 == 0:
        print(x)

#################################### ÜL 2
############################### 1.

f = open("kttekst.txt","r")
data = f.read()
sõnad = len(data.split())
print("Tekstis sõnu kokku on:",sõnad)

################################# 2.

########################################### ÜL 3
###################################### 1.
d = [11, 15, 6, 13, 13, 25, 32, 11, 20, 5, 31, 16, 32, 29, 11, 13, 3, 29, 28, 24]
e = [5, 19, 16, 4, 12, 7, 2, 28, 34, 29, 29, 36, 6, 8, 24, 18, 31, 7, 1, 7]
c = list((set(d).intersection(set(e))))
print(c)
#################################### 2.

max = 0
for i in d:
    if i > max:
        max = i
print(max)

max = 0
for i in e:
    if i > max:
        max = i
print(max)
################################## 3.

min= 32
for i in d:
    if i < min:
        min=i
print(min)

min= 36
for i in e:
    if i < min:
        min=i
print(min)

################################ 4.
listSum = sum(e)
listlen = len(e)
listavg = listSum/listlen
print(listavg)

listSum = sum(d)
listlen = len(d)
listavg = listSum/listlen
print(listavg)

################################ 5.







