# This is a password generator between 8 to 12.
import random
s1=["1","2","3","4","5","6","7","8","9","0"]
s2=["!","@","$","%","^","&","%","&","*","#"]
s3=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
s4=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","W","x","y","z"]
num=[]
print("Enter the length of the passward you want is 8 to 12:-")
k=int(input())
if(7<k<13):
    print("Starting with Capital letter ? Y/N")
    l = input()
    if(l=="y" or l=="Y"):
        pcchoice = random.choice(s3)
        num.append(pcchoice)
        k=k-1
    elif(l=="n"or l=="N"):
        pcchoice = random.choice( s4 + s1+s2)
        num.append(pcchoice)
        k = k - 1
    print("\n You want special cherector two= y/Y")
    l2 = input()
    if(l2=="y" or l2=="Y"):
        pcchoice = random.choice(s2)
        num.append(pcchoice)
        k = k - 1
        pcchoice = random.choice(s2)
        num.append(pcchoice)
        k=k-1
    elif(l2=="n"or l2=="N"):
        pcchoice = random.choice(s3+s4+s1)
        num.append(pcchoice)
        k=k-1
        pcchoice = random.choice(s3+s4+s1)
        num.append(pcchoice)
        k=k-1
    while (k>0):
        pcchoice = random.choice(s1+s2+s3+s4)
        num.append(pcchoice)
        k = k -1
    print("\n")
    print("".join(num)) # Here "".join() function use for the add string and number.
else:
    print("You can choose only one number between 8 and 12")






