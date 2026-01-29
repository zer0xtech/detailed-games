from scripts import viewHiddenGames, universeIDfromPlaceID, viewGameDetails

def userChoice():
    os.system('cls')
    while True:
        print('1 - View Hidden Games of a Roblox user\n2 - Get experienceID from placeID\n3 - Get details on a game using experienceID')
        user_choice = input('What do you want to do : ')
        try:
            if user_choice == '1':
                hiddenGames()
            elif user_choice == '2':
                universeIDfromPlaceID()
            elif user_choice == '3':
                viewGameDetails()
            else:
                print('Error, please choose a number')
                sleep(1)
                os.system('cls')
        except:
            print('Error, please retry.')