import quandl
import requests
quandl.ApiConfig.api_key = 'Hqu7HLNnBU4bxBU4jLaZ'

try:
    url = "https://www.quandl.com/api/v3/datasets/NSE/BHARTIARTL/metadata.json"
    try:
        meta_data = requests.get(url)
        parsed_meta_data = meta_data.json()
        print("Name: {}".format(parsed_meta_data['dataset']['name']))
        user_start_date = input("Enter the start date(YYYY-MM-DD):")
        user_end_date = input("Enter the end date(YYYY-MM-DD):")
        searched_data = quandl.get(["NSE/BHARTIARTL.2", "NSE/BHARTIARTL.3"],
                                   start_date=user_start_date,
                                   end_date=user_end_date,
                                   collapse="monthly",
                                   returns="numpy")
        print("Date\t\t\tHigh\tLow\t")
        print("----------------------------------")
        for data in searched_data:
            print("{}\t{}\t{}\n".format(data[0], data[1], data[2]))
    except Exception:
        print("Please Enter the dates in correct format")
except Exception:
    print("Check your Internet Connection")
