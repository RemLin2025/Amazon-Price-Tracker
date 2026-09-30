import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
from product_data import ProductData, PriceType

load_dotenv()
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
account_sid = os.getenv("ACCOUNT_SID")
user_agent = os.getenv("USER_AGENT")
URL = os.getenv("URL")

headers = {
    "User-Agent": user_agent,
    "Accept-Language": "en-US,en;q=0.9",
    }

response = requests.get(URL, headers=headers)
response.raise_for_status()
product_text = response.text

product = ProductData(product_text)

# my_number = os.environ.get("MY_NUMBER")
# from_number = os.environ.get("FROM_NUMBER")
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#     to=my_number,
#     from_=from_number,
#     body="The ",
# )