import requests
import os
from PIL import Image
from dotenv import load_dotenv
import datetime as dt
date = dt.date.today()

load_dotenv('C:/Users/maxwe/OneDrive/Desktop/.env')

# look up company ticker by name
# Only allowed 5 per day unless pay $5 for 100k
searchItem = 'Tesla'

lookup_url = "https://stock-ticker-security-and-company-search-database.p.rapidapi.com/all_search"
lookup_company_headers = {
    'x-rapidapi-host': "stock-ticker-security-and-company-search-database.p.rapidapi.com",
    'x-rapidapi-key': os.getenv('rapidapiKey')
}

lookup_params = {
    "security": searchItem,
    "result_type": "short",
    "exchange": "NASDAQ"
}
# Todo- add if response == 4** that was an invalid search
lookup_company_response = requests.get(url=lookup_url, headers=lookup_company_headers, params=lookup_params)
lookup_company_response.raise_for_status()
ticker_symbol = lookup_company_response.json()['ticker']

# Stock api for daily prices
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': ticker_symbol,
    'apikey': os.getenv('stockKey')
}

stock_response = requests.get('https://www.alphavantage.co/query')
stock_response.raise_for_status()


# News
news_params = {
    'apiKey': os.getenv('newskey'),
    'q': searchItem,
    'from': date,
    'sortBy': 'popularity'
}

# api call for news, searchItem would be the company
news_response = requests.get('https://newsapi.org/v2/everything', params=news_params)
news_response.raise_for_status()
news_response.json()

# Example of how to use Pil's Image to read image data
# img = Image.open(response.content)