#Gussing game with in number of gusses.
# We have 9 numbers of gusses, Game is over.
# print how many guess left and no of gusse.
n=56
i=0
k=0
while(1):
    print("Guess a number=\n")
    i=int(input())
    k = k+1
    print("left gusses =",(9-k))
    if 0<k<9:
        if i>n :
                print("\n You want to less number\n")
        elif i == n:
                print("\n You guess currectly.\n")
                print("You take chance number=",k )
                break
        else:
            print("\n You want to increase number \n")
        continue
    else:
        print("Game is over")
        break