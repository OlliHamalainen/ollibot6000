import telebot
import time
from random import randint
import json
import requests
import re
from flask import Flask, request
import os
# POWERSHELL --> pip install pyTelegramBotAPI
# botname --> olli6000bot
# run code command --> python ollibot.py
YOUR_TELEGRAMBOT_API_TOKEN = '1650853956:AAFnatrD9QzhJGlLfTrpXEJVqcDm-NNGDaw'

# change bot token to your own
bot_token = YOUR_TELEGRAMBOT_API_TOKEN
bot = telebot.TeleBot(token=bot_token)
botname = bot.get_me().first_name
server = Flask(__name__)


@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "hi there, I'm {}".format(botname))


@ bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(
        message, 'you can use following commands: /hello, /game, /weather, /dog, /news')


# start of random dog code
dog_url = 'https://dog.ceo/api/breeds/image/random'
dogresponse = requests.get(dog_url)


@ bot.message_handler(commands=['dog'])
def send_dog(message):
    dogresponse = requests.get(dog_url)
    x = dogresponse.json()
    dog = x['message']
    bot.reply_to(
        message, '{}'.format(dog))


@server.route('/' + bot_token, methods=['POST'])
def getMessage(message):
    bot.process_new_updates([telebot.types.Update.de_json(
        requests.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://ollibot6000.herokuapp.com/' + bot_token)
    return "!", 200


if __name__ == "_main_":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
