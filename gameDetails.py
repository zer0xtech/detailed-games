import requests
import os 
import json

def userChoice():
    os.system('cls')
    
    while True:
        print('1 - View Hidden Games of a Roblox user\n2 - Get experienceID from placeID\n3 - Get details on a game using experienceID')
        user_choice = input('What do you want to do : ')

        if user_choice == '1':
            userGames()
        elif user_choice == '2':
            universeIDfromPlaceID()
        elif user_choice == '3':
            viewGameDetails()
        else:
            print('Error please retry')

def userGames():
    os.system('cls')
    usernameInput = input('Enter the roblox username of the person you want the ID of : ')

    url = "https://users.roblox.com/v1/usernames/users"
    requestJSON = {"usernames": [usernameInput]}

    getUserID = requests.post(url, json=requestJSON)

    if getUserID.status_code == 200:
        response = getUserID.json()
        for user in response["data"]:
            print(f'{user["requestedUsername"]} - {user["id"]}')
    else:
        print("Error fetching user ID.")

def universeIDfromPlaceID():
    gameID = input('Enter the place ID of the game you want the UniverseID : ')
    universeIDRequest = requests.get(f'https://apis.roblox.com/universes/v1/places/{gameID}/universe')

    if universeIDRequest.status_code == 200:
        responseUniverseID = universeIDRequest.json()["universeId"]
        print(f'The universeID of the game you wanted is : {responseUniverseID}')
        input('Enter anything to continue...')
    else:
        print("Error fetching the request.")

def viewGameDetails():
    universeID = input('Enter the universe ID of the game you want the details of : ')
    checkGameDetails = requests.get(f'https://games.roblox.com/v1/games?universeIds={universeID}')

    if checkGameDetails.status_code == 200:
        data = checkGameDetails.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))
        input('Enter anything to continue...')
    else:
        print("Error fetching the request.")
userChoice()