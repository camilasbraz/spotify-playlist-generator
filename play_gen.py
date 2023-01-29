import requests
import json 

from config import *
from get_user_inputs import *

# get inputs from user

# Perform query based on desired inputs
query = f'{rec_endpoint}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'
query += f'&seed_artists={seed_artists}'
query += f'&seed_tracks={seed_tracks}'

response = requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})
json_response = response.json()

print('Recommended Songs:')
for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")

    

# CREATE A NEW PLAYLIST

endpoint_url = f"https://api.spotify.com/v1/users/camilabraz03/playlists"

#Playlist name and desc
request_body = json.dumps({
          "name": "Spotify Music Generator bot using Python",
          "description": "My first programmatic playlist!",
          "public": True
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

url = response.json()['external_urls']['spotify']



# FILL THE NEW PLAYLIST WITH THE RECOMMENDATIONS

playlist_id = response.json()['id']
print(playlist_id)

endpoint_url = f"https://api.spotify.com/v1/playlists/45NkBrcF929N8ADHVv0dFc/tracks"

request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

print(response.status_code)

print(f'Your playlist is ready at {url}')
