from dotenv import load_dotenv
import os
import requests

def main():
    # eventually read these in as command line args
    artist1 = 'Potsu'
    artist2 = 'Pig Destroyer'

    load_dotenv()

    auth_response = requests.post('https://accounts.spotify.com/api/token', {
        'grant_type': 'client_credentials',
        'client_id': os.environ["CLIENT_ID"],
        'client_secret': os.environ["CLIENT_SECRET"],
    }).json()
    access_token = auth_response['access_token']

    start = get_artist_id(artist1, access_token)
    end = get_artist_id(artist2, access_token)
    


def get_artist_id(artist_name, access_token):
    search_response = requests.get('https://api.spotify.com/v1/search', {
        'q': artist_name,
        'type': 'artist',
        'limit': 1
    }, headers={'Authorization': f'Bearer {access_token}'}).json()
    return search_response['artists']['items'][0]['id']

if __name__ == '__main__':
    main()