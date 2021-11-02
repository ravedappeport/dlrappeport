import yaml
??yaml.load
creds = yaml.load('/Users/daverappeport/.spotify/creds.yml', Loader=yaml.FullLoader)
cres
creds
creds = yaml.load(open('/Users/daverappeport/.spotify/creds.yml','r'), Loader=yaml.FullLoader)
creds
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"
??SpotifyOAuth
help(SpotifyOAuth)
??SpotifyOAuth
redirect_url="http://localhost:9001/callback"
creds.get('client_id')
auth_manager=SpotifyOAuth(client_id=creds.get('client_id'), client_secret=creds.get('client_secret'), redirect_uri=redirect_url)
sp = spotipy.Spotify(auth_manager=auth_manager(scope=scope))
auth_manager=SpotifyOAuth(client_id=creds.get('client_id'), client_secret=creds.get('client_secret'), redirect_uri=redirect_url, scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
%history -f /Users/daverappeport/git-personal/dlrappeport/scripts/spotif-auth.py
