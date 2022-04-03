# Given a number count the total number of digits in a number
# For example, the number is 75869, so the output should be 5.
print("Enter a number =")
num=int(input())
i=1
while(True):
    if((num/10)>=1):
        i= i+1
        num=(num/10)
    else:
        print("number of digit",i)
        break
