# Health Management System
# 3 clients - Harry, Rohan and Hammad
# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

def getdate(): # This is a time function use here.
    import datetime
    return datetime.datetime.now()

cl={1: "Harry" ,2: "Rohan" ,3: "Hammad"}
me={1: "Food",2: "Excise"}
print("Enter the name of clint choose option \n 1 - Harry \n 2 - Rohan \n 3 - Hammad \n")
nam=int(input())
print("Choose any option \n 1- Food \n 2- Excise \n")
num=int(input())
print("You choose 1 - Enter data or 2- Retrive data")
l=int(input())
if(0<nam<4 and 0<num<3 and 0<l<3):
    k = cl[nam] + me[num]
    if(l==1):
        print("You choose",k,"Enter data","\n")
        #f=open(cl[nam] + me[num]+".txt","x")
        txtfile=open(cl[nam] + me[num]+".txt","a")
        while(1):
                mytext = input() # mytext variable taken for the input from the users and store in it.
                txtfile.write("[ " + str(getdate()) + " ] : " + mytext + "\n") # This form show how to enter data in the ".txt" file.
                print("Want you continue?-y,n ")
                y= input()
                if(y=="n" or y=="N"):
                    txtfile.close()
                    break
    else:
        txtfile=open(cl[nam] + me[num]+".txt")
        print("You choose",k,"Report","\n")
        contents = txtfile.readlines()   #Take readlines() for the read all the lines at a time.
        for line in contents:
            print(line, end="")
        txtfile.close()
else:
    print("You choose wrong option , choose only 1 ,2 & 3")



