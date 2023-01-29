import requests
import json 


# SETTINGS 
endpoint_url = "https://api.spotify.com/v1/recommendations?"
token = "BQBsxZR8pLj-Opw0nQ5Qh8JLzBNrtvpwS6l3zWuHUWIqk_LZAvK7UsBwznmvUse6XmD0DqqscPmlZcAHTw93xU3J66yN4k__RmxxNzkFmDIcufdGpnK4IDvFL3w8Ae1ufwQxAaUe2-C99Z-f6Fs0eX8VkTCdTM5Y2L8vzELr-HPdw6nJ22hUs3SEivCC-pCs8KHFG5DINosDjzy90kv7XwnSjnOWKoImcbI_y2cvWO_MjHfM"
user_id = "camilabraz03"

# OUR FILTERS
limit=30
market="US&UK"
seed_genres="slow"
target_danceability=1.0
uris = [] 
seed_artists = '4dpARuHxo51G3z768sgnrY'
seed_tracks='3bNv3VuUOKgrf5hu3YcuRo'

# PERFORM THE QUERY
query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'
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

endpoint_url = f"https://api.spotify.com/v1/playlists/2fVN4SQ7iyXWsa90zSABAD/tracks"

request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

print(response.status_code)

print(f'Your playlist is ready at {url}')
