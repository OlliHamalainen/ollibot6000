# ollibot6000 - Telegram bot made with python
demo for codebootcamp2021


## bot commands and what they do

`/help`
- shows all following commands

`/hello`
- Greets user with "hi there, I'm ollibot6000"
    
`/dog`
- Sends user a random dog image using https://dog.ceo/api/breeds/image/random
    
`/news`
- Sends user a headline and image using https://newsapi.org/
    
`/weather`
- gives user information about weather in kuopio using https://openweathermap.org/api
    
`/game`
- starts rock paper scissors game with custom buttons.


**to make bot work, you must install pyTelegramBotAPI**
```
pip install pyTelegramBotAPI

```
also update python to version 3.9  
**then replace following variables with your api keys**    
bot_token = ~~config.YOUR_TELEGRAMBOT_API_TOKEN~~  (key aquired from telegrams botfather)  
newsapikey = ~~config.YOUR_NEWSAPI_KEY~~  (https://newsapi.org/)  
apikey = ~~config.YOUR_OPENWEATHER_API_KEY~~  (https://openweathermap.org/api)  


## run code with
```
python app.py
```
