import telebot

bot = telebot.TeleBot('6893368619:AAHAktAFwfKWEoz6tBPklIv7zu7g1e4bmGw')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'привет, напиши /sec , если хочешь узнать секрет!', parse_mode='Markdown')


@bot.message_handler(commands=['/sec'])
def main(message):
    bot.send_message(message.chat.id, 'секреты не раскрываются', parse_mode='Markdown')


@bot.message_handler(commands=['/run'])
def main(message):
    bot.send_message(message.chat.id, 'run out of your house there are ghosts!!! \nrun out of your house there are ghosts!!!', parse_mode = 'Markdown')

@bot.message_handler(commands=['/food'])
def main(message):
        bot.send_message(message.chat.id, 'сегодня я съел сосиску в тесте...', parse_mode='Markdown')

@bot.message_handler(commands=['/sad'])
def main(message):
        bot.send_message(message.chat.id, 'я получил 2 по истории...', parse_mode='Markdown')
        bot.send_message(message.chat.id, 'но это не повод расстраиваться, ведь можно посмотреть новое видео [мистербиста](https: // www.youtube.com / @ MrBeast)', parse_mode='Markdown')

@ bot.message_handler(commands=['/sry'])
def main(message):
        bot.send_message(message.chat.id, 'у меня закончились идеи для ответов...', parse_mode='Markdown')

bot.infinity_polling()