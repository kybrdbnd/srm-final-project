import quandl

quandl.ApiConfig.api_key = 'Hqu7HLNnBU4bxBU4jLaZ'
data = quandl.get(["NSE/BHARTIARTL.2", "NSE/BHARTIARTL.3"],
                  start_date="2016-10-31", end_date="2016-12-31")
print(data)
