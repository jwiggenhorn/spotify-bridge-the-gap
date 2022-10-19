from dotenv import load_dotenv
import os
import requests
import networkx as nx

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

    G = nx.Graph()

    source = get_artist_id(artist1, access_token)
    goal = get_artist_id(artist2, access_token)

    G.add_node(source, name=artist1)
    G.add_node(goal, name=artist2)

    add_related_artists(G, source, access_token)
    add_related_artists(G, goal, access_token)

    for neighbor in list(G[source]):
        add_related_artists(G, neighbor, access_token)

    for neighbor in list(G[goal]):
        add_related_artists(G, neighbor, access_token)

    while (not nx.has_path(G, source, goal)):
        for node in list(filter(lambda n: G.degree[n] < 15, G.nodes)):
            add_related_artists(G, node, access_token)

    nx.write_gexf(G, "artists.gexf")

def get_artist_id(artist_name, access_token):
    response = requests.get('https://api.spotify.com/v1/search', {
        'q': artist_name,
        'type': 'artist',
        'limit': 1
    }, headers={'Authorization': f'Bearer {access_token}'}).json()
    return response['artists']['items'][0]['id']

def add_related_artists(G, artist_id, access_token):
    response = requests.get(f'https://api.spotify.com/v1/artists/{artist_id}/related-artists',
        headers={'Authorization': f'Bearer {access_token}'}).json()
    artists = response['artists']
    for artist in artists:
        G.add_node(artist['id'], name=artist['name'])
        G.add_edge(artist_id, artist['id'])

if __name__ == '__main__':
    main()