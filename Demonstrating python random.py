import random
rangenumber = int(input("Range of the numbers"))
numbers = int(input("numbers"))
numbersor = numbers
numb=[]
numbr=0
while numbers >0:
    numbr=random.randint(1,rangenumber)
    print(numbr)
    numb.append(numbr)
    numbers -= 1
sm = 0
for nubr in numb:
    sm+=nubr
print("average =", sm/(numbersor))
i=input("Press Return to continue")
