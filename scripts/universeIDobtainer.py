def universeIDfromPlaceID():
    gameID = input('Enter the place ID of the game you want the UniverseID : ')
    universeIDRequest = requests.get(f'https://apis.roblox.com/universes/v1/places/{gameID}/universe')

    # if the request works, return the universeID
    if universeIDRequest.status_code == 200:
        responseUniverseID = universeIDRequest.json()["universeId"]
        print(f'The universeID of the game you wanted is : {responseUniverseID}')
        input('Enter anything to continue...')
    else:
        print("Error fetching the request.")

universeIDfromPlaceID()