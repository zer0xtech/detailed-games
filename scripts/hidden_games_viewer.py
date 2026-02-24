import os
from time import sleep

def main():
    os.system('cls')

    print('Patched by Roblox :(')
    sleep(2)
    os.system('cls')
    
    # usernameInput = input('Enter the Roblox username of the person you want to see the games : ')
    # gameAmount = input('Enter the amount of games you want to see : ')

    # url = "https://users.roblox.com/v1/usernames/users"
    # requestJSON = {"usernames": [usernameInput]}

    # getUserID = requests.post(url, json=requestJSON)
    # if getUserID.status_code == 200:
    #     response = getUserID.json()
    #     for user in response["data"]:
    #         print(f'Viewing games of : {user["requestedUsername"]} - {user["id"]}')
    #         sleep(1)
    #         viewHiddenGames = requests.get(f'https://inventory.roblox.com/v1/users/{user["id"]}/places/inventory?itemsPerPage={gameAmount}&placesTab=Created')
    #         if viewHiddenGames.status_code == 200:
    #             data2 = viewHiddenGames.json()
    #             print(json.dumps(data2, indent=2, ensure_ascii=False))
    #             input('Enter anything to continue...')
    #             userChoice()
    #         else:
    #             print('Error fetching the request.')
    # else:
    #     print("Error fetching user ID.")

if __name__ == "__main__":
    main()