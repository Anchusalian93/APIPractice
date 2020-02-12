import requests
import json
base_url = "https://deckofcardsapi.com/"
token_url = base_url + 'api/deck/new/shuffle/?deck_count=1'
response = requests.get(url=token_url)
print(response.status_code)
resp = response.json()
deck_id=resp['deck_id']
print(deck_id)
token_url1 = base_url +"api/deck/"+deck_id+ "/draw/?count=2"
response1 = requests.get(url=token_url1)
print(response1.status_code)
resp = response1.json()
print(resp['cards'][0]['suit'])
