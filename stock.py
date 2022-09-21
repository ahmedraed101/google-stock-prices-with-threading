from threading import Thread
import requests
from bs4 import BeautifulSoup as BS


class Stock(Thread):
    def __init__(self, symbol: str) -> None:
        super().__init__()
        self.symbol = symbol
        self.url = f"https://www.google.com/search?q={self.symbol}+stocks"
        self.price = None
        self.currency = None

    def run(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BS(response.text, "html.parser")
            div = soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"})
            price_text = div.text.split(" ")[0]
            if price_text:
                try:
                    self.price = float(
                        price_text.replace("٬", "").replace("٫", ".")
                    )
                except ValueError:
                    self.price = None
            currency = (
                soup.find("div", {"class": "BNeawe uEec3 AP7Wnd"})
                .text.split("·")[1]
                .split(" ")[3]
            )
            if currency:
                self.currency = currency

    def __str__(self):
        return f"{self.symbol}\t{self.price}\t\t{self.currency}"
