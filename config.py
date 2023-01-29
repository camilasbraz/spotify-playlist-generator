import os 
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
user_id = os.getenv("USER_ID")

# Endpoints
# Recommendations:
rec_endpoint = "https://api.spotify.com/v1/recommendations?"
# Create new playlist:
create_endpoint = ""
#Populate playlist
pop_play_endpoint = ""