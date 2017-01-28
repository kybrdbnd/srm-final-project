import requests
url = "https://gist.githubusercontent.com/anonymous/bf80cd113fcee17a09aa25475f5cd70a/raw/c51985094b58ca4ce98b3c73a086d313093ce7cd/blob.json"
data = requests.get(url)
parsed_data = data.json()
print(parsed_data['name'])
