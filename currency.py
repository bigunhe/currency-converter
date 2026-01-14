import requests
import os

API_KEY = os.getenv("FREECURRENCY_API_KEY")
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES = ["USD", "GBP", "AUD", "CAD", "EUR"]


def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid Currency")
        return None


while True:
    base = input("Enter a currency to convert to, (q to quit): ").upper()

    if base == "Q":
        break

    if base not in CURRENCIES:
        print("That currency is not available to convert. Try another one...")
        continue

    data = convert_currency("CAD")

    if not data:
        continue

    del data[base]

    for ticker, value in data.items():
        print(f"{ticker}: {value}")


# you can develop this adding an interface (web/desktop)
# you can use this to convert amounts multiplying the amount by values obtained here
