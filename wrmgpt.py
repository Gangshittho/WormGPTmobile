import telebot
import requests

API_TOKEN = '7184724613:AAFvjXsBdrncybOq6nZ0AIMJJgJRiAJsIxk'
URL = "https://dev-gpts.pantheonsite.io/wp-admin/js/apis/WormGPT.php"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "who are you? WormGPT .")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    data = {
        "text": message.text,
        "api_key": "openai-api-key",
        "temperature": 0.9
    }
    response = requests.post(URL, json=data).json()
    text = response["choices"][0]["message"]["content"]
    bot.reply_to(message, text,parse_mode='markdown')

bot.polling()
