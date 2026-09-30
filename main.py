import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
from amazon_scraper import AmazonScraper, PriceType
from camel_scraper import CamelScraper

load_dotenv()
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
account_sid = os.getenv("ACCOUNT_SID")
user_agent = os.getenv("USER_AGENT")
amazon_url = os.getenv("AMAZON_URL")
camel_url = os.getenv("CAMEL_URL")

headers = {
    "User-Agent": user_agent,
    "Accept-Language": "en-US,en;q=0.9",
    }

amazon = AmazonScraper(amazon_url, headers)
camel = CamelScraper(camel_url, headers)
price = amazon.get_price(PriceType.DEAL)
lowest_price = camel.get_lowest_price()
lowest_price_date = camel.get_lowest_price_date()



# my_number = os.environ.get("MY_NUMBER")
# from_number = os.environ.get("FROM_NUMBER")
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#     to=my_number,
#     from_=from_number,
#     body="The ",
# )