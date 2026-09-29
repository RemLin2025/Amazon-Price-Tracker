import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

USER_AGENT = os.environ.get("USER_AGENT")
headers = {
    'User-Agent': USER_AGENT,
    }

response = requests.get(URL, headers=headers)
response.raise_for_status()
response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")
