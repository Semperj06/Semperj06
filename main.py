import config
import datetime
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
from pycoingecko import CoinGeckoAPI


bot = telebot.TeleBot(config.Token)
now = datetime.datetime.now()
coin_g = CoinGeckoAPI()


@bot.message_handler(commands=(["start"]))
def greetings(message):
    """При запуске бота и при вводе команды start здороваемся с пользователем и перенаправляем на функцию make_keyboard"""
    txt = f"Hello {message.from_user.first_name}, to find out the current rate or top coins, select the appropriate menu🐐🐐🐐"
    greeting = bot.send_message(message.chat.id, txt)
    bot.register_next_step_handler(greeting, make_keyboard)


@bot.message_handler(commands=(["menu"]))
def make_keyboard(message):
    """Создаем пользовательскую клавиатуру выводим ее и следующим шагом перенаправляем на функцию send_message"""
    item1 = types.KeyboardButton("Crypto")
    item2 = types.KeyboardButton("Top")
    item3 = types.KeyboardButton("Uah")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(item1, item2, item3)
    msg = bot.send_message(message.chat.id, "Choose what interests you ;)",  reply_markup=markup)
    bot.register_next_step_handler(msg, send_message)


@bot.message_handler(content_types=["text"])
def send_message(message):
    """Проверка если пользователь выбирает команду с клавиатуры или пишет ключевое слово то запускаем соответствующею
    функцию, если по такому слову не реализована функция то вывожу подсказку с командой меню"""
    if message.text.lower() == "crypto":
        """Запускаем функцию crypto и прячем клавиатуру"""
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, crypto(), reply_markup=markup)
    elif message.text.lower() == "uah":
        """Запускаем функцию get_uah_exchange"""
        bot.send_message(message.chat.id, f"updated in ({now})")
        bot.send_message(message.chat.id, get_uah_exchange())
    elif message.text.lower() == "top":
        """Запускаем функцию get_top"""
        bot.send_message(message.chat.id, "Top-7 search coins on CoinGecko in the last 24 hours")
        bot.send_message(message.chat.id, get_top())
    else:
        """Выводим сообщение подсказку с командой для открытия меню клавиатуры"""
        bot.send_message(message.chat.id, "See what the bot can do enter the command /menu")
        f = open(str(message.from_user.first_name)+'.txt', 'a', encoding="utf-8")
        f.write(f"(ID = {message.chat.id})Name = {message.from_user.first_name}, {message.text}--{now}\n")
        f.close()


def crypto():
    """Передаю список монет и валюту параметром в get_price и  через цикл формирую строку """
    text = ""
    price = coin_g.get_price(ids=config.list_of_cripto, vs_currencies='usd, uah')
    for i in price:
        text += f"{i.title()} -> (usd {price[i]['usd']}), (uah {price[i]['uah']})_._._._._🐐\n"
        text += "\n"
    return text


def get_top():
    """Делаем запрос к словарю и получаем топ монет по популярности поиска за последние 24 часа"""
    coin_name = []
    text = ""
    for i in range(7):
        coin_name.append(coin_g.get_search_trending()['coins'][i]["item"]["name"])
    for i in coin_name:
        text += f"{i}_._._._._🐐\n"
        text += "\n"
    return text


def get_uah_exchange():
    """С гугла запрашиваем текущий курс гривны к доллару и евро"""
    full_page = requests.get(config.DOLLAR_UAH, headers=config.ne_bot)
    soup = BeautifulSoup(full_page.content, "html.parser")
    convert = soup.findAll("span", {"class": "DFlfde", "data-precision": 2})
    text = f"Сurrently exchange rate USD --> {convert[0].text}_._._._._🐐\n"
    full_page = requests.get(config.EURO_UAH, headers=config.ne_bot)
    soup1 = BeautifulSoup(full_page.content, "html.parser")
    convert1 = soup1.findAll("span", {"class": "DFlfde", "data-precision": 2})
    text += f"Сurrently exchange rate EURO --> {convert1[0].text}_._._._._🐐"
    return text


if __name__ == '__main__':
    bot.polling(none_stop=True)
