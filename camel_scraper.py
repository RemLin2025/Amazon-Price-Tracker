from bs4 import BeautifulSoup
import requests

LOWEST_ELEMENT_INDEX = 1
AVERAGE_ELEMENT_INDEX = 4
PRICE_DECIMAL_CUTOFF_OFFSET = 3
DOLLAR_SYMBOL_CUTOFF = 1

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

    def get_lowest_price(self) -> float:
        total_price_element = self.soup.select("tr.pt.amazon.on td")
        total_price_data = total_price_element[LOWEST_ELEMENT_INDEX].text.strip()
        cutoff = total_price_data.index(".") + PRICE_DECIMAL_CUTOFF_OFFSET
        total_price = total_price_data[DOLLAR_SYMBOL_CUTOFF:cutoff]
        return round(float(total_price), 2)

    def get_average_price(self) -> float:
        total_price_element = self.soup.select("tr.pt.amazon.on td")
        total_price_data = total_price_element[AVERAGE_ELEMENT_INDEX].text.strip()
        cutoff = total_price_data.index(".") + PRICE_DECIMAL_CUTOFF_OFFSET
        total_price = total_price_data[DOLLAR_SYMBOL_CUTOFF:cutoff]
        return round(float(total_price), 2)

    def get_lowest_price_date(self):
        total_price_element = self.soup.select("tr.pt.amazon.on td")
        total_price_data = total_price_element[LOWEST_ELEMENT_INDEX].text.strip()
        cutoff = total_price_data.index(".") + PRICE_DECIMAL_CUTOFF_OFFSET
        price_date = total_price_data[cutoff:]
        return price_date.strip().replace("(", "").replace(")", "")