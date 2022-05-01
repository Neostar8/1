import telebot
from config import keys,TOKEN
from extensions import APIException,MoneyConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message:telebot.types.Message):
    text='Привет, я Бот-Конвертер валют. Чтобы начать работу, введите команду боту в следующем формате: \n<Имя валюты цену которой хотите узнать>' \
    ' \n<Имя валюты в которой надо узнать цену первой валюты> ' \
    '<Количество первой валюты>  \
    \nУвидеть список доступных валют можно с помощью команды /values \
    \nУсловия ввода команды я могу напомнить в команде /help'
    bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = 'Следующий формат: \n<Имя валюты цену которой хотите узнать>' \
    ' \n<Имя валюты в которой надо узнать цену первой валюты> ' \
    '<Количество первой валюты>' \
    '\nУвидеть список доступных валют можно с помощью команды /values'

    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты'
    for key in keys.keys():
        text ='\n'.join((text,key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Слишком много переменных.')

        base, quote, amount = values
        total_base = MoneyConverter.get_price(base,quote,amount)
    except APIException as error:
        bot.reply_to(message, f'Ошибка пользователя.\n{error}')
    except Exception as error:
        bot.reply_to(message, f'Не удалось обработать команду.\n{error}')
    else:
        text=f'{amount} {base} в {quote} = {float(total_base)*int(amount)}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)