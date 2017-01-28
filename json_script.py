import requests
API_KEY = "Hqu7HLNnBU4bxBU4jLaZ"
url = "https://www.quandl.com/api/v3/datasets/NSE/BHARTIARTL.json?column_index=2&start_date=2015-12-31&end_date=2016-12-31&collapse=monthly&api_key=Hqu7HLNnBU4bxBU4jLaZ"
# print(url)
data = requests.get(url)
parsed_data = data.json()
# print(parsed_data)
# print(len(parsed_data['dataset']))
print("Name: {}\n".format(parsed_data['dataset']['name']))
print("Date\t\tHigh")
print("------------------------------------")
for data in parsed_data['dataset']['data']:
    print ("{}\t{}".format(data[0], data[1]))
# print(parsed_data['dataset']['data'])
