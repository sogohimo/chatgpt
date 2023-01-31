# import openai
# import googletrans
# import telebot
# from googletrans import Translator

# openai.api_key = "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"
# translator = Translator(service_urls=['translate.google.com'])

# bot = telebot.TeleBot("5640041523:AAGwve4jt4aIDYE5NWok-vFpaJGNSBqnzDQ")

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.reply_to(message, "Hi, I am a chatbot powered by OpenAI's GPT-3. How can I help you today?")

# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     user_input = message.text

#     user_input_translated = translator.translate(user_input, dest='en').text

#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=user_input_translated,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     ).choices[0].text

#     response_translated = translator.translate(response, dest='ru').text

#     bot.reply_to(message, response_translated)

# bot.polling()



#____________________________________



# import openai
# import googletrans
# import telebot
# from googletrans import Translator

# openai.api_key = "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"
# translator = Translator(service_urls=['translate.google.com'])

# bot = telebot.TeleBot("5640041523:AAGwve4jt4aIDYE5NWok-vFpaJGNSBqnzDQ")

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.reply_to(message, "Hi, I am a chatbot powered by OpenAI's GPT-3. How can I help you today?")

# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     user_input = message.text

#     user_input_translated = translator.translate(user_input, dest='en').text

#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=user_input_translated,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     ).choices[0].text

#     response_translated = translator.translate(response, dest='ru').text

#     if '```' in response_translated:
#         code_start = response_translated.index('```')
#         code_end = response_translated.rindex('```')
#         code = response_translated[code_start+3:code_end]
#         bot.send_message(chat_id=message.chat.id, text=code, parse_mode='Markdown')
#         response_translated = response_translated[:code_start] + response_translated[code_end+3:]

#     bot.reply_to(message, response_translated)

# bot.polling()


#_______________________ГОТОВ ТИПА


# import openai
# import googletrans
# import telebot
# from googletrans import Translator

# openai.api_key = "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"
# translator = Translator(service_urls=['translate.google.com'])

# bot = telebot.TeleBot("5640041523:AAGwve4jt4aIDYE5NWok-vFpaJGNSBqnzDQ")

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.reply_to(message, "Hi, I am a chatbot powered by OpenAI's GPT-3. How can I help you today?")

# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     user_input = message.text

#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=user_input,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     ).choices[0].text

#     if "```" not in response:
#         response_translated = translator.translate(response, dest='ru').text
#         bot.reply_to(message, response_translated)
#     else:
#         bot.reply_to(message, response)

# bot.polling()



# ____________Две кнопки
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


