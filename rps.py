import random 
def rps (userInput):
    numb = random.random()    
    if(numb>=0 and numb< 0.33):
        computerInput = "rock"
    elif(numb >= 0.34 and numb < 0.66):
        computerInput = "paper"
    else:
        computerInput = "scissors"
    print(computerInput)

    isUserWin=False;
    if(userInput == 'rock'):
        if (computerInput == 'rock'):
            isUserWin =False;
        elif(computerInput == 'paper'):
            isUserWin = False;
        else:
            isUserWin = True;
    elif(userInput == 'paper'):
        if (computerInput == 'rock'):
            isUserWin =True;
        elif(computerInput == 'paper'):
            isUserWin = False;
        else:
            isUserWin = False;
    elif(userInput == 'scissors') :
        if (computerInput == 'rock'):
            isUserWin =False;
        elif(computerInput == 'paper'):
            isUserWin = True;
        else:
            isUserWin = False;
    else:
        print("please type correctly");
    return isUserWin;

def gambling():
    global computerMoney
    global userMoney;
    userBet = int(input("How much money are you going to bet?: "))
    if(userBet > userMoney ):
        print("You cannot bet more than the money you have")
        return
    if(userBet> computerMoney):
        print("You cannot bet more than the moeny computer have");
        return

    userInput = input("Choose between rock, paper, and scissors: ")
    isUserWin = rps(userInput)



    # isUserWin = True;
    if (isUserWin == True):
        userMoney = userMoney + userBet;
        computerMoney = computerMoney - userBet;
    else:
        userMoney = userMoney - userBet;
        computerMoney = computerMoney + userBet;
    print("userMoney: ", userMoney);
    print("computerMoney: ", computerMoney);

computerMoney = 1000
userMoney = 1000

while (computerMoney > 0 and userMoney>0):
    gambling();

print("final money for user is : ", userMoney);
print("final money for computer is : ", computerMoney);


# import random 
# def rps (userInput):
#     numb = random.random()    
#     if(numb>=0 and numb< 0.33):
#         computerInput = "rock"
#     elif(numb >= 0.33 and numb < 0.66):
#         computerInput = "paper"
#     else:
#         computerInput = "scissors"
#     print(computerInput)

#     isUserWin=False;
#     if(userInput == 'rock'):
#         if (computerInput == 'rock'):
#             isUserWin =False;
#         elif(computerInput == 'paper'):
#             isUserWin = False;
#         else:
#             isUserWin = True;
#     elif(userInput == 'paper'):
#         if (computerInput == 'rock'):
#             isUserWin =True;
#         elif(computerInput == 'paper'):
#             isUserWin = False;
#         else:
#             isUserWin = False;
#     elif(userInput == 'scissors') :
#         if (computerInput == 'rock'):
#             isUserWin =False;
#         elif(computerInput == 'paper'):
#             isUserWin = True;
#         else:
#             isUserWin = False;
#     else:
#         print("please type correctly");
#     return isUserWin;

# def gambling():
#     global computerMoney
#     global userMoney;
#     userBet = int(input("How much money are you going to bet?: "))
#     if(userBet > userMoney ):
#         print("You cannot bet more than the money you have")
#         return
#     if(userBet> computerMoney):
#         print("You cannot bet more than the moeny computer have");
#         return

#     userInput = input("Choose between rock, paper, and scissors: ")
#     isUserWin = rps(userInput)



#     # isUserWin = True;
#     if (isUserWin == True):
#         userMoney = userMoney + userBet;
#         computerMoney = computerMoney - userBet;
#     else:
#         userMoney = userMoney - userBet;
#         computerMoney = computerMoney + userBet;
#     print("userMoney: ", userMoney);
#     print("computerMoney: ", computerMoney);

# computerMoney = 1000
# userMoney = 1000

# while (computerMoney > 0 and userMoney>0):
#     gambling();

# print("final money for user is : ", userMoney);
# print("final money for computer is : ", computerMoney);