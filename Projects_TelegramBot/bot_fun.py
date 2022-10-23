import telebot, time, os

bot = telebot.TeleBot(os.environ['BOT_TOKEN'])
CHANNEL_NAME = '@адрес_telegram_канала'
# Загружаем список шуток
f = open('data/fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()

for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke)
    # Делаем паузу в один час
    time.sleep(3600)
bot.send_message(CHANNEL_NAME, "Шутки закончились :-(")
