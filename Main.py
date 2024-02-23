import os,sys
from requests import get
from pprint import PrettyPrinter
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

BASE_URL = "https://api.apilayer.com/currency_data/"
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    print("The API key could not be read.")
    sys.exit(1)

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"list?apikey={API_KEY}"
    data = get(BASE_URL+endpoint).json()
    for key,value in data["currencies"].items():
        print(f"{key}:{str(value)}")


def exchange_rate(currency1, currency2):
    endpoint = f"live?source={currency1}&currencies={currency2}&apikey={API_KEY}"
    url = BASE_URL + endpoint 
    response = get(url)
    if response.status_code != 200:
        print("There was a problem connecting to the API.")
        sys.exit(1)

    data = response.json()
    if "quotes" not in data:
        print("Incorrect currencies. Check the values entered.")
        return
    lists = list(data["quotes"].items())
    printer.pprint(f"{lists[0][0]} is {lists[0][1]} | DATE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")



get_currencies()
currency1 = input("What is basic currency?")
currency2 = input("Which you want to convert?")
exchange_rate(currency1,currency2)


