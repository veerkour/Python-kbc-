que=[
    "1: who was the first female president in india",
    "2: when bhagat singh wrote his first letter in jail and how old he was that time",
    "3: what is the current calculation of population in the world",
    "4: where female population was very less  in the world in 2015",
    "5: what is the main festival of the world"
    ]
option=[
    ["1:indira gandhi","2:pratibha devisingh patil","3:swati mukharji","4:sarswati devi"],
    ["1:nov 1 1926(19 year)","2:jan 2 1921(20 year)","3:feb 30 1890(22 year)","4:mar 3 1987(25 year)"],
    ["1:7.96 (Billin people)","2:8.92(Billin people)","3:3.93 (Billian people)","4:2.93 (Billian people)"],
    ["1:United Arab Emirates only 26.7%","2:iran only 23.1%","3:UK only 20.3%","4:netherland only 21.5%"],
    ["1:Carnival in Rio de Janeiro","2:dewali","3:Deventer Book Fair","4:Berlin Love Parade","Edinburgh Fringe Festival",]]

solution_list=[2,1,1,1,1]

lifeline=[["2:pratibha devisingh patil","3:swati mukharji"],
["1:nov 1 1992(19 year)","4:mar 3 1987(25 year)"],
["1:7.96% Billion people","3:3.93 Billion people"],
["1:United Arab Emirates only 26.7%","2:iran only 23.1%"],
[ "1:Carnival in Rio de janerio","3:Berlin Love parade"]]

print(         "Welcome to KBC"     )
print(      "your game starts now"    )

i=0
money=0
c=1000
life=2
while i<(len(que)):
    print(que[i])
    j=0
    while j<len(option):
        if i==j:
            k=0
            while k<len(option[j]):
                print(option[j][k])
                k=k+1
        j=j+1
    if life > 0:
        use=input("do you want lifeline yes [y] or no [n]:-")
        if use=="y":
            k=0
            while k<len(lifeline[i]):
                print(lifeline[i][k])
                k=k+1
            life=life-1
            ans=int(input("enter the your answer:-"))
            if ans==solution_list[i]:
                print("your answer is right")
                money=money+c
            else:
                print("your answer is wrong:-")
        else:
            ans=int(input("enter the answer:-"))
            if ans==solution_list[i]:
                print("your answer is right")
                money=money+c
    else:
        print("you cant take lifeline:-")
        ans=int(input("enter the your answer:-"))
        if ans==solution_list[i]:
            print("your answer in right")
            money=money+c 
  
    i=i+1
print(money)


	
