import quandl

quandl.ApiConfig.api_key = 'Hqu7HLNnBU4bxBU4jLaZ'
data = quandl.get_table("ZACKS/FC", ticker="MSFT")
print(data)
