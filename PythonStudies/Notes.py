# ____________________Урок1________________07.09.2020_____

# a,b,d= map(int,input('Введіть три числа розділених комою без пробілу:\n').split(','))
# c=a
# a=b
# b=d
# d=c
# print(a,b,d)


# m1,m2=map(float,input("Введіть довжину та ширину своєї кімнати. (два числа розділених одним пробілом):\n").split(' '))
# priceCategory=int(input("\n Введіть в яку ціну ви шукаєте килим. (одне число котре є ціною за квадратний метр):\n"))
# rug=(m1*m2)*priceCategory
# print("\n Килим на всю вашу кімнату буде коштувати ",rug," гривень.\n",sep="")

#_________________________Урок2__________________13.09.2022______

# print("Hello {0}, your balance is {0}".format("Andrii",230))
# print("{:05d}".format(12))
# print("{:8.3f}".format(12.2346))
# = -переносить мінус вліво
#^ -по центру 
#< - по лівому берегу
#> - по правому
# print("{:^05}".format("cat"))
# print(end="")


#__________________________Урок3_______________14.09.2022______


#continue - exit iteration of cycle
#break - exit cycle itself
#else - can be part of cycle itself


#logical (and,or)


#________________Урок4______________20.09.2022

#abs(x) --- модуль
#round (x) --- заокруглення до десятих
#round (x,y)--- заокруглення до певних чисел
#pow(x,y)--- піднесення до степені
#divmod(x,y)--- повертає ціле частку від ділення

# import math
# math.sqrt(x) --- 

# import math as a
# a.sqrt(x)

#from math import e,sqrt
#from math import *(no recomendation)

#pip freeze
#pip install (PACKET)
#pip install -U pip (PACKET)
#pip uninstall (PACKET)

    
#__________________________Урок5_______________21.09.2022______


#import random as r

#r.random() ---значення від 0 до 1
#r.uniform(x,y) --- повертає рнадомний флоат з проміжку x до y 
#r.randint(x,y) --- -\- тільки про цілі
#r.choice(x.[])--- повертає випадковий елемент послідовності
#r.radrange(x,y,i) --- як ранд-інт але ще має можливість кроку (швидше завсе дає більшу нагрузку на код)
#r.shuffle(<список>) --- перемішує список(з гівном)(не працює для незмінюваних массивів)

# eval(expresion[,globals[,locals]]) --- 
# expresion --- приймає як байт код пайтона(не приймає присвоєння)
# globals(optional) - словник функцій
# locals (optional) 

 
#__________________________Урок6_______________22.09.2022______

#конкатенація
# string --- type
# len(string)
#in(<послідовність>) -- чи є елемент в масиві -- bool
#min\max(<послідoвність>) ---

# ord(<символ>) -- показує код символа
# chr(<код>)

# str[x:y]
#x- індекс початку зрізу
#y- індекс кінця зрізу(сам елемент не входить в зріз)

# n=int(input("Input number of numbers you want to input\n")) 

# frag1=0  #on negative 
# number1=0
# frag2=0  #on interval
# number2=0
# i=0

# while i<n:
#     i+=1
#     a=float(input("Input a your ",i," number \n")) 
#     if(a<0 and frag1==0):
#         frag1 = i
#         number1 = a
#     if(a>=-10 and a<=10 and frag1==0):
#         frag1 = i
#         number1 = a

# if (frag1==0):
#     print("You have array without negative numbs")
# else:
#     print("Your first negative number (which is {}) the {} number that you wrote".format(number1,frag1))


# if (frag2==0):
#     print("You have array without numbs that are in the interval from -10 to 10")
# else:
#     print("Your first number in the interval from -10 to 10 (which is {}) the {} number that you wrote".format(number2,frag2))

#1618151.Mr

#<відокрмлювач>.join(<послідовність>)
#s="da"
#s1="p"
#s2="iz"
#print("".join((s1,s2,s)))

#str.upper()
#str.lower()
#str.capitalize()
#str.title()
# str = input ("Input your password\n")
# print(str[0]+str[-1]+str[2]+str[-3]) 

# from random import randint
# i=0
# win=True
# while True: 
#     if(win == True):
#         numb=randint (-1024,1024)
#         win = False

#     ch=input("Guess a number or press Q to quit\n:")
#     i+=1
#     if(ch.upper=="Q"):
#         break
#     elif(int(ch)>=numb+750 or int(ch)<=numb-750):
#         print("Atempt:",i)
#         print("you`re forzingly far")
#         continue
#     elif((int(ch)<=numb+750 and int(ch)>numb+250) or (int(ch)<=numb-750 and int(ch)>numb-250)):
#         print("Atempt:",i)
#         print("you`re chillingly far")
#         continue
#     elif((int(ch)<=numb+250 and int(ch)>numb+50) or (int(ch)<=numb-250 and int(ch)>numb-50)):
#         print("Atempt:",i)
#         print("you`re far from true number")
#         continue
#     elif((int(ch)<=numb+50 and int(ch)>numb+10) or (int(ch)<=numb-50 and int(ch)>numb-10)):
#         print("Atempt:",i)
#         print("it`s hot,you`re close")
#         continue
#     elif((int(ch)<=numb+10 and int(ch)>numb+1) or (int(ch)<=numb-10 and int(ch)>numb-1)):
#         print("Atempt:",i)
#         print("You`re hellishly close!")
#         continue
#     elif(int(ch)==numb):
#         print("Yoooooooo, You won at last it only took you",i,"atempts!\n")
#         choice=input("Do you want to repeat?(Y/N)\n")
#         if(choice.lower()=="y"):
#             i=0
#             win=True
#             continue
#         elif(choice.lower()=="n"):
#             break
#     else:
#         print("please repeat")
#         i-=1
#         continue
#__________________________Урок7_______________28.09.2022______
# 
# find(char,[from],[to])
#   
# s= "hello world"
# s.find('e') - (1)
# s.find('z') - (-1)

# index() -- on false = Value Error

#count(char,[from],[to])
#s.count(o) - 2
#s.count(o,6) - 1

# .replace(old_str,new_str,[how many])

#.isalpha() -- (only char) (space is not char)
#.isdigit() -- (only digit) (space is not digit)
#.isalnum() -- (only chars and digits) (fuck spaces I guess)

#.rjust(how many,[char]) -- додає n(=how many-len) знаків справа (пустих або вказаний(вказати можна ЛИШЕ один))
#.ljust(how many,[char]) -- додає n(=how many-len) знаків зліва  (пустих або вказаний(вказати можна ЛИШЕ один))

# str1="%s i %s" 
# print (str1 % ("Pupa", "Lupa"))
#%s - for string
#%d - for digital
#% 
#%
#%
#% 
#%



# import string as r
# name = "Jon"
# age = 10
#s = r.Template("Name`s $na. $years years old.")


#f(uuck(?))-strings
# x= 10
# y =5
# print(f"{x} X {y} = {x*y/2}")


#bin()
#oct()
#hex()

#__________________________Урок8_______________04.10.2022______

#list - впорядкований список з різних елементів, познчаються - [,]

# list.copy()
#z='python, 3.14'
# rez=z.split(,) 
# list(z) - перетворюють не список обидва але тут по елементно
# ''.join(z)


# random.sample(range(6,50,2),n) --- набирає з на значаної послідовності n рандомних значеннь

# z = input ("input some number\n")
# z1=list(map(int,z))
# sum =0
# c=0
# while(len(z1)>c):
#     if(len(z1)-1==c):
#         print(z1[c],end=' ')
#     else:
#         print(z1[c],"+",end=' ')
#     sum+=z1[c]
#     c+=1
# print ("=",sum)




#__________________________Урок9_______________05.10.2022______


# .append(x) -- додає в кінець списку елемент X

# .extend(T) -- додає інші види массивів в кінець списку (! append додає їх одним вкладеним списком) 

# .insert(i,x) -- вставля є елемент x на індекс i

# .pop(i) -- дістає і видаляє елемент з індексом і 

# .remove(x) -- видаляє всі елементи зі значенням х

# .count(x)

# .find(x)

# .index(x) -- <.find 

# .reverse() -- реверс списку

# .clear() -- очищає зі списку всі елементи

# .sort([reverse=False]) - сортує по зростанню [або по спаданню]

# sorted(l,[reverse=False])

#______________ FOR ______________

# for <x> in <object>:
    #<smth>
#[else:
    #<smth>
#]

#x -- х = елементи зі списку (WARNING)

# flag=True
# pip= input("")
# dat= input("")
# misNarodzh= input("")
# adresa= input("")
# dodatky= input("")
# choice= False

# while flag:
#     print(f"{pip}{dat}{misNarodzh}{adresa}")
#     if dodatky!='' and dodatky!=' ' :
#         print(f"Other bio:\n{dodatky}")
#     ch=input("Do you want to correct something?(Yes/No)")
#     if ch.lower()=='yes':
#         choice = True
#         isFirst = True
#         while choice:
#             if isFirst ==True:
#                 choose=input("What?\n1.\n2.\n3.\n4.\n5.\n0.If you`re done")
#             else:
#                 choose=input("Smth else?\n1.\n2.\n3.\n4.\n5.\n0.If you`re done")
#             if(choose==1):
#                 pip= input("")
#                 isFirst = False
#             elif(choose==2):
#                 dat= input("")
#                 isFirst = False
#             elif(choose==3):
#                 misNarodzh= input("")
#                 isFirst = False
#             elif(choose==4):
#                 adresa= input("")
#                 isFirst = False
#             elif(choose==5):
#                 dodatky= input("")
#                 isFirst = False
#             elif(choose==0):
#                 isFirst = True
#                 choice = False
#             else:
#                 print("Sorry. Again")
#     elif ch.lower()=='no':
#         flag=False
#     else:
#         print("Oops")


#__________________________Урок12_______________18.10.2022______
# def smth (some x`s)
#return s

#__________________________Урок13_______________19.10.2022______

# try
# except
# finaly
# else

#____Файли____
# open()

# write()

# close()
# open with()as
# w
# a
# r
# 

# read()
# readline()
# readkines()
# 