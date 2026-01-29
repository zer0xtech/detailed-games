import json

def viewGameDetails():
    placeid = input('Enter the universe ID of the game you want the details of : ')
    checkGameDetails = requests.get(f'https://economy.roblox.com/v2/assets/{placeid}/details')

    # if the request works, returns all details
    if checkGameDetails.status_code == 200:
        data = checkGameDetails.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))
        input('Enter anything to continue...')
    else:
        print("Error fetching the request.")
viewGameDetails()