import gspread
import telebot


gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('11Opwm97cjjt215dt3yeswRf7QlpQm5z34MBcI76mGEM')
# print(sh.sheet1.get('A1:B1'))
# урл на таблицу 11Opwm97cjjt215dt3yeswRf7QlpQm5z34MBcI76mGEM

bot_token = '5643270177:AAF_-UPZAkE7K1X_88FLkOFOZjRMnMLCmvo'
bot = telebot.TeleBot(bot_token)

name = ''
mood = ''

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я маленький бот;) Рад буду записывать данные в таблицу. Как Вас зовут? ')

@bot.message_handler(func=lambda m:True)
def add_name(message):
    global name
    name = message.text

    bot.send_message(message.from_user.id, 'Какое у Вас настроение?')
    bot.register_next_step_handler(message, add_moon)

def add_moon(message):
    global mood
    mood = message.text

    bot.send_message(message.from_user.id, 'Спасибо, данные отправлены. Всего хорошего!!!')
    bot.register_next_step_handler(message, send_to_sheet)

def send_to_sheet(message):
    lst = gc.open_by_key('11Opwm97cjjt215dt3yeswRf7QlpQm5z34MBcI76mGEM')
    lst.sheet1.append_row([name, mood])




bot.polling(none_stop=True)