from bs4 import BeautifulSoup
import requests

LOWEST_ELEMENT_INDEX = 1
CUTOFF_STRING = 3

class CamelScraper:
    def __init__(self, url: str, headers: dict[str, str]):
        self.url = url
        self.headers = headers
        self.soup = BeautifulSoup(self.fetch_html(), 'html.parser')

    def fetch_html(self) -> str:
        """Fetches the HTML of the Camel page."""
        response = requests.get(self.url, headers=self.headers)
        response.raise_for_status()
        return response.text

    def get_lowest_price(self):
        total_price_element = self.soup.select("tr.pt.amazon.on td")
        total_price_data = total_price_element[LOWEST_ELEMENT_INDEX].text.strip()
        cutoff = total_price_data.index(".") + CUTOFF_STRING
        total_price = total_price_data[:cutoff]
        return total_price

    def get_lowest_price_date(self):
        total_price_element = self.soup.select("tr.pt.amazon.on td")
        total_price_data = total_price_element[LOWEST_ELEMENT_INDEX].text.strip()
        cutoff = total_price_data.index(".") + CUTOFF_STRING
        price_date = total_price_data[cutoff:]
        return price_date.strip().replace("(", "").replace(")", "")