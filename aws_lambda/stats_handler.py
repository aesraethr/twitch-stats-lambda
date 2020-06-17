import os
import requests
import redis

def stats_handler(event, context):
    REDIS_URL = os.environ.get('REDIS_URL')
    r = redis.StrictRedis(host=REDIS_URL, decode_responses=True)

    ## oauth2 ##
    token = r.hgetall("token")
    if token == {} or r.ttl("token") < 60:
        token = requests.post(url=f"https://id.twitch.tv/oauth2/token?client_id={os.environ['TWITCH_CLIENT_ID']}&client_secret={os.environ['TWITCH_CLIENT_SECRET']}&grant_type=client_credentials").json()
        r.hmset("token",token)
        r.expire("token",token["expires_in"])
    
    headers = {
        'Client-ID':os.environ['TWITCH_CLIENT_ID'],
        'Authorization':f'Bearer {token["access_token"]}'
    }

    followers = requests.get(url="https://api.twitch.tv/helix/users/follows?to_id=456444689",headers=headers).json()
    stream = requests.get(url="https://api.twitch.tv/helix/streams?user_login=rtsesport_tv",headers=headers).json()
    print(stream)
    return

if __name__ == '__main__':
    stats_handler("dummy","dummy")