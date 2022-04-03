# Make a calculator with faulty 45*5=555,56+6=72,77/11=9

from operator import add, sub, mul, truediv # taking an operator and import from.
op={"+":add,"-":sub,"*":mul,"/":truediv} # where op is directory
print("Enter a value=")
a=int(input())
ops=input("Enter operation(+,-,*,/):") # takes ops a variable.
print("Enter other number=")
b= int(input())
c=op[ops](a,b) # This is c a variable with the helps of user data ops.
if ops==add or ops==mul or ops==truediv:
    print(" you are Right")
elif a==45 and b==5 and c==225:
    print("your answer=555")
elif a==56 and b==6 and c==62:
     print("your answer=72")
elif a==77 and b==11 and c==7.0:
    print("your answer=9")
elif b==45 and a==5 and c==225:
    print("your answer=555") # It is reverse.
elif b==56 and a==6 and c==62:
    print("your answer=72") # it is reverse.
else:
    print(" Your answer = ",c)
