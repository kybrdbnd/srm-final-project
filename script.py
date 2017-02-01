import quandl
import requests
import matplotlib.pyplot as plt

# variables declare
high_array = []
date_array = []
quandl.ApiConfig.api_key = 'Hqu7HLNnBU4bxBU4jLaZ'

# functions declaration


def plot_graph(date, high, start_date, end_date):
    # print("hello")
    plt.xlabel("Year")
    plt.ylabel("High Value")
    title = "High Value from {} to {}".format(start_date, end_date)
    plt.title(title)
    plt.plot(date, high)
    plt.savefig("test.png")
    # plt.axis([0, date_array, 0, high_array])
    plt.show()


# script code
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
            high_array.append(data[1])
            date_array.append(data[0])
            print("{}\t{}\t{}\n".format(data[0], data[1], data[2]))
        plot_graph(date_array, high_array, user_start_date, user_end_date)
    except Exception:
        print("Please Enter the dates in correct format")
except Exception:
    print("Check your Internet Connection")
