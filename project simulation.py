import random

oneroll = 0
tworoll = 0
threeroll = 0
fourroll = 0
fiveroll = 0
sixroll = 0

trialnum = 0
dice_choice = int(input("How many times do you want to roll the dice?"))

while(trialnum < dice_choice):
    rolled_dice = random.randint(1,6)


    if rolled_dice == 6:
        sixroll = sixroll + 1
    if rolled_dice == 5:
        fiveroll = fiveroll + 1
    if rolled_dice == 4:
        fourroll = fourroll + 1
    if rolled_dice == 3:
        threeroll = threeroll + 1
    if rolled_dice == 2:
        tworoll = tworoll + 1
    if rolled_dice == 1:
        oneroll = oneroll + 1

    trialnum += 1


print("Total times rolled:-", trialnum)
print("1 rolls:-", oneroll)
print("2 rolls:-", tworoll)
print("3 rolls:-", threeroll)
print("4 rolls:-", fourroll)
print("5 rolls:-", fiveroll)
print("6 rolls:-", sixroll)

choice = 0

while choice != "stop":
    choice = input("Which number of dice would you like to know the probability of rolling?")
    if choice == "1":
        print(oneroll/dice_choice,"%")
    elif choice == "2":
        print(tworoll/dice_choice,"%")
    elif choice == "3":
        print(threeroll/dice_choice,"%")
    elif choice == "4":
        print(fourroll/dice_choice,"%")
    elif choice == "5":
        print(fiveroll/dice_choice,"%")
    elif choice == "6":
        print(sixroll/dice_choice,"%")
    else:
        print("Thats not a numbered dice!!")

print("Thanks for playing :)")