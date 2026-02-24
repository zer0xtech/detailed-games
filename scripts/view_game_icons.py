import requests 
import os 
import json

def main():
    gameID = int(input("Enter the universeid you want to see the icons : "))
    view_icons = requests.get(f'https://games.roblox.com/v2/games/{gameID}/media?fetchAllExperienceRelatedMedia=false')

    if view_icons.status_code == 200:
        data = view_icons.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))
        download_choice = input("Do you want to download any icon ? (y / n) : ")

        if download_choice == 'y':
            iconID = int(input('Enter the icon ID you want to download : '))
            download_icon = requests.get(f'https://assetdelivery.roblox.com/v1/asset/?id={iconID}')

            if download_icon.status_code == 200:
                print('Icon was succefully downloaded on your PC (/Downloads)')
            else:
                print('Error fetching request..')
        else:
            print('Exiting..')
    else:
        print("Error when fetching the request.")

if __name__ == "__main__":
    main()
