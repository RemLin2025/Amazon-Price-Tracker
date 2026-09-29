from bs4 import BeautifulSoup

class ProductData:
    def __init__(self, text: str):
        self.soup = BeautifulSoup(text, "html.parser")
        self.price = self.find_price()


    def find_price(self) -> float:
        whole_price_element = self.soup.select_one("span.a-price-whole")
        fraction_price_element = self.soup.select_one("span.a-price-fraction")

        if whole_price_element is not None and fraction_price_element is not None:
            whole_price = whole_price_element.text.strip()
            fraction_price = fraction_price_element.text.strip()
            total_price = float(whole_price + fraction_price)
            return total_price

        raise Exception('Failed to find price')

