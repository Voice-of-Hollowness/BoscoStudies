from random import choice, randint

spec=False
num=False
lChar=False
bChar=False

n=int(input("\n"))

while(spec==False or num==False or lChar==False or bChar==False):
    if(n<4):
        break
    spec=False
    num=False
    lChar=False
    bChar=False

    parol=[]

    for i in range(n):
        ch=""
        rd = randint(1,4)
        if(rd==1):
            ch = choice(['1','2','3','4','5','6','7','8','9','0'])
            parol.append(ch)
            num=True

        elif(rd==2):
            ch = choice(['a','s','h','j','k','l','z','x','v','n','m','b','c','d','e','f','g','t','r','w','y','u','i','o','p'])
            parol.append(ch)
            lChar=True

        elif(rd==3):
            ch = choice(['A','S','H','J','K','L','Z','X','V','N','M','B','C','D','E','F','G','T','R','W','Y','U','I','O','P'])
            parol.append(ch)
            bChar=True

        elif(rd==4):
            ch = choice(['@','!',"#",'$','%','*','?','=','-','+','_','№'])
            parol.append(ch)
            spec=True

if(spec==True and num==True and lChar==True and bChar==True):
    print(''.join(parol))