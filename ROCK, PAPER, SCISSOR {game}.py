import random
max_attempt=6
ls=['rock','paper','scissor']
c_c=random.choice(ls)
user = input("ENTER YOUR CHOICE :")
if (c_c=='scissor' and user=='paper') or (c_c=='rock' and user=='scissor') or(c_c=='paper' and user=='rock'):
    print("c_c is winner you loose")
else:
    print("you won the game")
    

