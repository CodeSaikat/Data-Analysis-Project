"""
snake is winner choose water.
Gun is winer when choose snake.
water is winner when choose Gun.
"""

import random
dic={1:"Snake",2:"Water",3:"Gun"}
i=0
ctus=0
ctpc=0
print("                                         Welcome Sanake, Water & Gun Game                 \n")
while(i<10):
    pcchoice= random.randint(1,3)
    print("Enter your choice \n 1-Snake \n 2-Water \n 3-Gun ")
    usr=int(input("\n"))
    if(0<usr<4):
        if(pcchoice != usr):
            if(usr==1 and pcchoice==2):
                ctus=ctus+1
                print(f"User is winner, The point get User={ctus} \n")
            elif(usr==2 and pcchoice==1):
                ctpc =ctpc+1
                print(f"PC is winner, The point get PC={ctpc} \n")
            elif(usr==2 and pcchoice==3):
                ctus=ctus+1
                print(f"User is winner, The point get User={ctus} \n")
            elif(usr==3 and pcchoice==2):
                ctpc = ctpc + 1
                print(f"PC is winner, The point get PC={ctpc} \n")
            elif(usr==3 and pcchoice==1):
                ctus=ctus+1
                print(f"User is winner, The point get User={ctus} \n")
            elif(usr==1 and pcchoice==3):
                ctpc = ctpc + 1
                print(f"PC is winner, The point get PC={ctpc} \n")
        else:
            print("Draw means no point")
        i+=1
        print(f"Left the chances {10 - i}\n")
    else:
        print("Wrong input")
if(ctus>ctpc):
    print(f"Win the game by USER={ctus}times.")
elif(ctus==ctpc):
    print("Tie")
else:
    print(f"Win the game by PC={ctpc}times.")