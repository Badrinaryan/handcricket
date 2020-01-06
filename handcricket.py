import random
print("Lets go for the toss")
print("what you want odd or even")
uin=input('enter: ')
cout=random.randint(1,6)
uout=int(input("enter: "))
print(cout)
total=cout+uout
if total%2==0 and uin=="even":
    print('you won the toss')
    choice=input('enter what you want: ')
    if choice == 'bat':
        print('you are bating now')
        userchoice=0
        computerchoice=1
        mainusertotal=0
        while userchoice!=computerchoice:
            userchoice=int(input('enter: '))
            computerchoice=random.randint(1,6)
            print(computerchoice)
            mainusertotal=mainusertotal+userchoice
        print(f"your total {mainusertotal}")
        if userchoice==computerchoice:
            print('You are balling now')
            comchoice=0
            usechoice=1
            maincomputertotal=0
            while comchoice!=usechoice and mainusertotal>=maincomputertotal:
                usechoice=int(input('enter: '))
                comchoice=random.randint(1,6)
                print(comchoice)
                maincomputertotal=maincomputertotal+comchoice
            print(f"computer total {maincomputertotal}")
            if maincomputertotal>mainusertotal:
                print(f"computer won the game")
            if maincomputertotal<mainusertotal:
                print(f"you won the game by {mainusertotal-maincomputertotal} runs")

    if choice == 'ball':
        print("you are balling")
        userchoice=1
        computerchoice=0
        maincomputertotal=0
        while userchoice!=computerchoice:
            userchoice=int(input('enter: '))
            computerchoice=random.randint(1,6)
            print(computerchoice)
            maincomputertotal=maincomputertotal+computerchoice
        print(f"computer total {maincomputertotal}")
        if userchoice==computerchoice:
            print('You are bating now')
            comchoice=1
            usechoice=0
            mainusertotal=0
            while comchoice!=usechoice and maincomputertotal>=mainusertotal:
                usechoice=int(input('enter: '))
                comchoice=random.randint(1,6)
                print(comchoice)
                mainusertotal=mainusertotal+usechoice
            print(f"your total {mainusertotal}")
            if maincomputertotal>mainusertotal:
                print(f"computer won the game by {maincomputertotal-mainusertotal} runs")
            if maincomputertotal<mainusertotal:
                print(f"you won the game")
        
if total%2!=0 and uin=='even':
    print("you lose the toss")
    lst=('ball','bat')
    choice=random.choice(lst)
    if choice=='bat':
        print("you are balling")
        userchoice=1
        computerchoice=0
        maincomputertotal=0
        while userchoice!=computerchoice:
            userchoice=int(input('enter: '))
            computerchoice=random.randint(1,6)
            print(computerchoice)
            maincomputertotal=maincomputertotal+computerchoice
        print(f"computer total {maincomputertotal}")
        if userchoice==computerchoice:
            print('You are bating now')
            comchoice=1
            usechoice=0
            mainusertotal=0
            while comchoice!=usechoice and maincomputertotal>=mainusertotal:
                usechoice=int(input('enter: '))
                comchoice=random.randint(1,6)
                print(comchoice)
                mainusertotal=mainusertotal+usechoice
            print(f"your total {mainusertotal}")
            if maincomputertotal>mainusertotal:
                print(f"computer won the game by {maincomputertotal-mainusertotal} runs")
            if maincomputertotal<mainusertotal:
                print(f"you won the game")
    
    if choice=='ball':
        print('you are bating now')
        userchoice=0
        computerchoice=1
        mainusertotal=0
        while userchoice!=computerchoice:
            userchoice=int(input('enter: '))
            computerchoice=random.randint(1,6)
            print(computerchoice)
            mainusertotal=mainusertotal+userchoice
        print(f"your total {mainusertotal}")
        if userchoice==computerchoice:
            print('You are balling now')
            comchoice=0
            usechoice=1
            maincomputertotal=0
            while comchoice!=usechoice and mainusertotal>=maincomputertotal:
                usechoice=int(input('enter: '))
                comchoice=random.randint(1,6)
                print(comchoice)
                maincomputertotal=maincomputertotal+comchoice
            print(f"computer total {maincomputertotal}")
            if maincomputertotal>mainusertotal:
                print(f"computer won the game")
            if maincomputertotal<mainusertotal:
                print(f"you won the game by {mainusertotal-maincomputertotal} runs")

if total%2!=0 and uin=='odd':
    print("you won the toss")
    choice=input('enter what you want bat or ball: ')
    if choice == 'bat':
        print('you are bating now')
        userchoice=0
        computerchoice=1
        mainusertotal=0
        while userchoice!=computerchoice:
            userchoice=int(input('enter: '))
            computerchoice=random.randint(1,6)
            print(computerchoice)
            mainusertotal=mainusertotal+userchoice
        print(f"your total {mainusertotal}")
        if userchoice==computerchoice:
            print('You are balling now')
            comchoice=0
            usechoice=1
            maincomputertotal=0
            while comchoice!=usechoice and mainusertotal>=maincomputertotal:
                usechoice=int(input('enter: '))
                comchoice=random.randint(1,6)
                print(comchoice)
                maincomputertotal=maincomputertotal+comchoice
            print(f"computer total {maincomputertotal}")
            if maincomputertotal>mainusertotal:
                print(f"computer won the game")
            if maincomputertotal<mainusertotal:
                print(f"you won the game by {mainusertotal-maincomputertotal} runs")

    if choice == 'ball':
        print("you are balling")
        userchoice=1
        computerchoice=0
        maincomputertotal=0
        while userchoice!=computerchoice:
            userchoice=int(input('enter: '))
            computerchoice=random.randint(1,6)
            print(computerchoice)
            maincomputertotal=maincomputertotal+computerchoice
        print(f"computer total {maincomputertotal}")
        if userchoice==computerchoice:
            print('You are bating now')
            comchoice=1
            usechoice=0
            mainusertotal=0
            while comchoice!=usechoice and maincomputertotal>=mainusertotal:
                usechoice=int(input('enter: '))
                comchoice=random.randint(1,6)
                print(comchoice)
                mainusertotal=mainusertotal+usechoice
            print(f"your total {mainusertotal}")
            if maincomputertotal>mainusertotal:
                print(f"computer won the game by {maincomputertotal-mainusertotal} runs")
            if maincomputertotal<mainusertotal:
                print(f"you won the game")
        
if total%2==0 and uin=='odd':
    print('you lose the toss')
    lst=('bat','ball')
    choice=random.choice(lst)
    if choice=='bat':

        print("you are balling")
        userchoice=1
        computerchoice=0
        maincomputertotal=0
        while userchoice!=computerchoice:
            userchoice=int(input('enter: '))
            computerchoice=random.randint(1,6)
            print(computerchoice)
            maincomputertotal=maincomputertotal+computerchoice
        print(f"computer total {maincomputertotal}")
        if userchoice==computerchoice:
            print('You are bating now')
            comchoice=1
            usechoice=0
            mainusertotal=0
            while comchoice!=usechoice and maincomputertotal>=mainusertotal:
                usechoice=int(input('enter: '))
                comchoice=random.randint(1,6)
                print(comchoice)
                mainusertotal=mainusertotal+usechoice
            print(f"your total {mainusertotal}")
            if maincomputertotal>mainusertotal:
                print(f"computer won the game by {maincomputertotal-mainusertotal} runs")
            if maincomputertotal<mainusertotal:
                print(f"you won the game")
    
    if choice=='ball':
        print('you are bating now')
        userchoice=0
        computerchoice=1
        mainusertotal=0
        while userchoice!=computerchoice:
            userchoice=int(input('enter: '))
            computerchoice=random.randint(1,6)
            print(computerchoice)
            mainusertotal=mainusertotal+userchoice
        print(f"your total {mainusertotal}")
        if userchoice==computerchoice:
            print('You are balling now')
            comchoice=0
            usechoice=1
            maincomputertotal=0
            while comchoice!=usechoice and mainusertotal>=maincomputertotal:
                usechoice=int(input('enter: '))
                comchoice=random.randint(1,6)
                print(comchoice)
                maincomputertotal=maincomputertotal+comchoice
            print(f"computer total {maincomputertotal}")
            if maincomputertotal>mainusertotal:
                print(f"computer won the game")
            if maincomputertotal<mainusertotal:
                print(f"you won the game by {mainusertotal-maincomputertotal} runs")
input('')
