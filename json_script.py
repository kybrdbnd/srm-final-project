import requests
API_KEY = "Hqu7HLNnBU4bxBU4jLaZ"
url = "https://www.quandl.com/api/v3/datasets/NSE/BHARTIARTL.json?api_key={0}".format(
    API_KEY
)
# print(url)
data = requests.get(url)
parsed_data = data.json()
print(parsed_data)
