# Currency Converter

A small script that fetches latest currency exchange rates using FreeCurrencyAPI and shows rates for a small set of currencies.

## Overview

This project demonstrates how to request the latest exchange rates from FreeCurrencyAPI and use those rates to perform simple conversions. It's a minimal, local script (not a web server) that uses the `requests` library.

## Endpoint used

The script calls the FreeCurrencyAPI "latest" endpoint:

```
GET https://api.freecurrencyapi.com/v1/latest
```

Query parameters:
- `apikey` (required) — your API key for FreeCurrencyAPI
- `base_currency` (optional) — the base currency to compare against (e.g., `CAD`)
- `currencies` (optional) — comma-separated list of currency tickers to return (e.g., `USD,GBP,EUR`)

Full example request URL:

```
https://api.freecurrencyapi.com/v1/latest?apikey=YOUR_KEY&base_currency=CAD&currencies=USD,GBP,EUR
```

Example response (trimmed):

```json
{
  "data": {
    "USD": 0.73,
    "GBP": 0.57,
    "EUR": 0.66
  }
}
```

The script reads `data` from the response and uses those numeric values as rates relative to the requested `base_currency`.

## How to use

1. Install requirements:

```bash
pip install requests
```

2. Edit `currency.py` and set your API key. For security, prefer an environment variable instead of hardcoding:

```python
import os
API_KEY = os.getenv('FREECURRENCY_API_KEY')
```

3. Run the script interactively:

```bash
python currency.py
```

The script prompts for a target currency and prints the exchange rates for the configured currency list.

### Using the conversion function in code

The project exposes a small helper `convert_currency(base)` which returns a dictionary of rates for the configured `CURRENCIES` list. Example usage:

```python
from currency import convert_currency
rates = convert_currency('CAD')
# rates is a dict like {"USD": 0.73, "GBP": 0.57, ...}
amount_in_cad = 100
amount_in_usd = amount_in_cad * rates['USD']
```

## Configurable currencies

The script uses a `CURRENCIES` list (default: `USD, GBP, AUD, CAD, EUR`). Modify this list to request different currencies from the API.

## Notes & recommendations

- Do not commit API keys to git. Use environment variables or a .env file (and add it to `.gitignore`).
- The example uses the public FreeCurrencyAPI `latest` endpoint; review the API provider docs for rate limits and account restrictions.


