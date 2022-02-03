import requests
from bs4 import BeautifulSoup
import config



def get_uah_exchange():

    full_page = requests.get(config.DOLLAR_UAH, headers=config.ne_bot)
    soup = BeautifulSoup(full_page.content, "html.parser")
    convert = soup.findAll("span", {"class": "DFlfde", "data-precision": 2})
    text = f"Сurrently exchange rate USD {convert[0].text}\n"
    full_page = requests.get(config.EURO_UAH, headers=config.ne_bot)
    soup1 = BeautifulSoup(full_page.content, "html.parser")
    convert1 = soup1.findAll("span", {"class": "DFlfde", "data-precision": 2})
    text += f"Сurrently exchange rate EURO {convert1[0].text}"
    return text

print(get_uah_exchange())