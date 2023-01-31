import openai
import googletrans
import telebot
from googletrans import Translator
from telebot import types

openai.api_key = "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"
translator = Translator(service_urls=['translate.google.com'])

bot = telebot.TeleBot("5640041523:AAGwve4jt4aIDYE5NWok-vFpaJGNSBqnzDQ")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Включить перевод", "Выключить перевод")
    bot.send_message(chat_id=message.chat.id, text="Привет! Добро пожаловать в ChatGPT с возможностью русского ввода!", reply_markup=markup)

@bot.message_handler(commands=['stop_bot'])
def stop_bot(message):
    bot.stop_polling()

@bot.message_handler(func=lambda message: message.text == "Включить перевод")
def enable_translation(message):
    bot.reply_to(message, "Перевод включен.")
    global translate_enabled
    translate_enabled = True

@bot.message_handler(func=lambda message: message.text == "Выключить перевод")
def disable_translation(message):
    bot.reply_to(message, "Перевод выключен.")
    global translate_enabled
    translate_enabled = False


@bot.message_handler(content_types=["text"])
def handle_text(message):
    global translate_enabled
    translate_enabled = False

    user_input = message.text

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    if translate_enabled and "```" not in response:
        response_translated = translator.translate(response, dest='ru').text
        bot.reply_to(message, response_translated)
    else:
        bot.reply_to(message, response)

bot.polling()


