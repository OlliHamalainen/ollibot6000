import telebot
import time
from random import randint
import json
import requests
import re
import config

bot_token = config.YOUR_TELEGRAMBOT_API_TOKEN
newsapikey = config.YOUR_NEWSAPI_KEY
apikey = config.YOUR_OPENWEATHER_API_KEY

bot = telebot.TeleBot(token=bot_token)
botname = bot.get_me().first_name


@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "hi there, I'm {}".format(botname))


@ bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(
        message, 'you can use following commands: /hello, /game, /weather, /dog, /news')


# start of random dog code------------------------------
dog_url = 'https://dog.ceo/api/breeds/image/random'
dogresponse = requests.get(dog_url)


@ bot.message_handler(commands=['dog'])
def send_dog(message):
    dogresponse = requests.get(dog_url)
    x = dogresponse.json()
    dog = x['message']
    bot.reply_to(
        message, '{}'.format(dog))


# start of news--------------------------

news_url = ('http://newsapi.org/v2/top-headlines?'
            'country=us&'
            'apiKey={}'.format(newsapikey))


@ bot.message_handler(commands=['news'])
def send_news(message):
    newsresponse = requests.get(news_url)
    w = newsresponse.json()
    nmain = w['articles']
    ncontent = nmain[randint(0, 10)]
    ntitle = ncontent['title']
    nimg = ncontent['urlToImage']
    bot.reply_to(
        message, '{}\n {}'.format(ntitle, nimg))


# start of weather code -------------------------
cityid = 'Kuopio'
weather_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(
    cityid, apikey)

f = requests.get(weather_url)
y = f.json()
main = y['main']
temperature = main['temp'] - 273.15
location = y['name']
description = y['weather'][0]['description']


@ bot.message_handler(commands=['weather'])
def send_weather(message):
    bot.reply_to(
        message, '{}\n {}°C\n {}'.format(location, temperature, description))


# start of game ------------------------------------------

t = ["rock", "paper", "scissors"]
computer = t[randint(0, 2)]


@bot.message_handler(commands=['game'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(
        text='Rock', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(
        text='Paper', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(
        text='Scissors', callback_data=5))
    bot.send_message(
        message.chat.id, text="Let's play advanced rps-game", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(
        callback_query_id=call.id, text='Answer accepted!')

    if call.data == computer:
        answer == 'Tie'

    elif call.data == '3':
        callback_data_string = 'rock'
        if computer == 'rock':
            answer = 'tie with your {} againts my {}'.format(
                callback_data_string, computer)
        elif computer == 'paper':
            answer = 'I won! Your {} had no change against my {}'.format(
                callback_data_string, computer)
        elif computer == 'scissors':
            answer = 'you won! your {} beat my {} with ease'.format(
                callback_data_string, computer)

    elif call.data == '4':
        callback_data_string = 'paper'
        if computer == 'paper':
            answer = 'tie with your {} againts my {}'.format(
                callback_data_string, computer)
        elif computer == 'scissors':
            answer = 'I won! Your {} had no change against my {}'.format(
                callback_data_string, computer)
        elif computer == 'rock':
            answer = 'you won! your {} beat my {} with ease'.format(
                callback_data_string, computer)

    elif call.data == '5':
        callback_data_string = 'scissors'
        if computer == 'scissors':
            answer = 'tie with your {} againts my {}'.format(
                callback_data_string, computer)
        elif computer == 'rock':
            answer = 'I won! Your {} had no change against my {}'.format(
                callback_data_string, computer)
        elif computer == 'paper':
            answer = 'you won! your {} beat my {} with ease'.format(
                callback_data_string, computer)

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(
        call.message.chat.id, call.message.message_id)


bot.polling()
