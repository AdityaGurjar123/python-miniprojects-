import random
max_attempt=5
rd=random.randint(1,10)
while max_attempt:
    num=int(input("plzz guess the number"))
    if num<rd:
        print ("too small try again")
    elif num>rd:
        print("too large try again")
    elif num==rd:
        print("winner congratulations")
    max_attempt-=1
else:
    print("looser try again")
        
            