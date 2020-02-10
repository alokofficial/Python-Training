import random
jackpot=random.randint(1,100)
#print(jackpot)
guess=int(input("chal guess kar"))
counter=1

while guess!=jackpot:
    counter+=1
    if guess>jackpot:
        print("guess lower")
        guess=int(input("chal dubaara guess kar"))
    else:
        print("guess higher")
        guess=int(input("chal dubaara guess kar"))
print("shi guess")
print(counter)
