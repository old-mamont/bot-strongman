
import telebot
from telebot import types
from Token import token
from models import verification_user



bot = telebot.TeleBot(token())

@bot.message_handler(commands=["start"]) 
def start(message):
    bot.send_message(message.from_user.id, "Команды:\n/start\n/button")
    print(verification_user(message.from_user))



@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Профиль")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)



@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Профиль":
        bot.send_message(message.chat.id,"Мой профиль ⚙️\n" )
        bot.send_message(message.chat.id, message.from_user )

bot.polling(none_stop=True, interval=0)