from random import *

def beolvas():
    file = open('nevsor.txt', 'r', encoding='utf-8')
    for line in file:
        list.append(line)
    file.close()
def valaszt():
    num = randint(0, len(list) -1)
    print(list[num])
    return num
list = []

##not gonna use these anymore but could be  usefull

#print(list)
#kilep = False

#num = randint(0, len(list))
#print(list[num])

beolvas()
ujnev = 'i'
while ujnev == 'i' and 0 < len(list):
    if ujnev == "i":
        a = valaszt()
        list.remove(list[a])
    ujnev = input("Kérsz egy új nevet? (i/n)")