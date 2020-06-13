import os
import requests

def stats_handler(event, context):
    ## oauth2 ##
    token = requests.post(url=f"https://id.twitch.tv/oauth2/token?client_id={os.environ['TWITCH_CLIENT_ID']}&client_secret={os.environ['TWITCH_CLIENT_SECRET']}&grant_type=client_credentials").json()
        #TODO:Check si on en a deja un, sinon le stocker
    
    headers = {
        'Client-ID':'gddbva13mup10zamsdju7o8qtnxs7t',
        'Authorization':f'Bearer {token["access_token"]}'
    }

    followers = requests.get(url="https://api.twitch.tv/helix/users/follows?to_id=456444689",headers=headers).json()
    stream = requests.get(url="https://api.twitch.tv/helix/streams?user_login=rtsesport_tv",headers=headers).json()
    print(stream)
    return

if __name__ == '__main__':
    stats_handler("dummy","dummy")