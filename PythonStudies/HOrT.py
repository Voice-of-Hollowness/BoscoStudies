import random as r

a=1 
times=r.randrange(1,7,2)
print("We play",times,"rounds")
wincount=0

while a<=times:
    while True:
        hotChoice=int(input("Heads or tails?( write 1 or 2 respectively)\n")) 
        if (hotChoice!=1 and hotChoice!=2):
            print("are you an idiot?\n Choose again")
            continue
        break
    HOT=r.randint(1,2)
    if (HOT == hotChoice):
        wincount= wincount+1
        print("You won this round")
    else:
        print("You lost this round")
    a =a+1


if (wincount>times/2):
    print("You win congrats")
else:
    print("You are pathetic loser")
   