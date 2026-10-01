from bs4 import BeautifulSoup
from enum import Enum
import requests


class PriceType(Enum):
    """Represents a parent css element to get targeted price type."""
    def __add__(self, other):
        return self.value + other
    DEAL = "#primeSavingsUpsellAccordionRow"
    REGULAR = "#newAccordionRow_1"
    USED = "#usedAccordionRow"


class AmazonScraper:
    def __init__(self, url: str, headers: dict[str, str]):
        self.url = url
        self.headers = headers
        self.soup = BeautifulSoup(self.fetch_html(), "html.parser")

    def fetch_html(self) -> str:
        """Fetches the HTML of the Amazon page."""
        response = requests.get(self.url, headers=self.headers)
        response.raise_for_status()
        return response.text

    def get_price(self, price_type: PriceType) -> float:
        """Returns the full price of the product depending on the price type."""
        whole_price_element = self.soup.select_one(price_type + " span.a-price-whole")
        fraction_price_element = self.soup.select_one(price_type + " span.a-price-fraction")

        if whole_price_element is not None and fraction_price_element is not None:
            whole_price = whole_price_element.text.strip()
            fraction_price = fraction_price_element.text.strip()
            total_price = whole_price + fraction_price
            return float(total_price)

        print("Failed to find price")
        raise Exception('Failed to find price')

    def get_name(self) -> str:
        title_element = self.soup.select_one("#productTitle")
        return title_element.text.strip()


