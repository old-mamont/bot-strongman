import telebot
from telebot import types
from Config import token
from models import Base_SQL
from sportsman import *

def verification_user(user : dict):
    """Проверка на нового пользователя"""
    ls_id_users = Base_SQL.show("SELECT id FROM User")
    if not (user.id,) in ls_id_users:
        request = """INSERT INTO User (id, first_name, last_name) VALUES ( %s, %s, %s )"""
        data = [(user.id, user.first_name, str(user.last_name))]
        Base_SQL.write(request, data)
        print(f"Произошла запись пользователя: {user.id}, погоняло {user.first_name}")
    else:
        print(f"Пользователь {user.first_name} уже в базе")
        


# Создание объекта бота
bot = telebot.TeleBot(token())

def keyboard_menu(message, id = False):
    # Сделать генератор кнопок? С помощью генератора списка
    if id == False:
        markup = types.ReplyKeyboardMarkup(True)
        item1 = types.KeyboardButton("Профиль")
        item2 = types.KeyboardButton("Пользоваетельский запрос")
        item3 = types.KeyboardButton("Планы тренеровок")
        item4 = types.KeyboardButton("Сообщество")
        item5 = types.KeyboardButton("Трекер")
        markup.add(item1, item2, item3, item4, item5)
        bot.send_message(message.chat.id, "Выберите кнопку из меню.", reply_markup=markup)
    
    else:
        markup = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton("Погода", callback_data="get_weather")
        btn_2 = types.InlineKeyboardButton("Кнопка_2", callback_data="get_weather")
        markup.add(btn_1, btn_2)
        bot.send_message(message.chat.id, "Выберите кнопку из меню.", reply_markup=markup)
        


@bot.message_handler(commands = ["start"])
def start(message ):
    # verification_user(message.from_user)
    keyboard_menu(message)

    # bot.send_message(message.chat.id, "Выберите кнопку из меню.", reply_markup=markup)





def get_weather(message):
    keyboard_menu(message, id=True)

def User_Request(message):
    bot.reply_to(message, f"Ваш запрос '{message.text}'.")



@bot.message_handler(commands = ["get_city"])
def get_city(message):
    
    # markup = types.InlineKeyboardMarkup()
    # btn = types.InlineKeyboardButton("Кнопка", callback_data="key",request_location=True)
    # markup.add(btn)

    markup = types.ReplyKeyboardMarkup()
    btn = types.KeyboardButton("Трекер", request_location=True)
    markup.add(btn)

    bot.send_message(message.chat.id, text="Введите город.",reply_markup=markup)
    # цепочка вызова
    # bot.register_next_step_handler(message, key,)




@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Профиль":
        markup = types.ReplyKeyboardMarkup(True)
        btn_telehon = types.KeyboardButton("Свой телефон", request_contact=True)
        btn_geo = types.KeyboardButton("Геопозиция", request_location=True)
        btn_back = types.KeyboardButton("Назад" )
        markup.add(btn_back, btn_geo, btn_telehon)
        bot.send_message(message.chat.id, "Профиль", reply_markup=markup)
    
    elif message.text == "Назад":
        keyboard_menu(message)
    
    elif message.text == "Трекер":
        get_weather(message)
    
    elif message.text == "Пользоваетельский запрос":
        bot.send_message(message.chat.id, "Введите запрос.")
        bot.register_next_step_handler(message, User_Request,)
        




#  Обработка нажатий на кнопки осуществляется в функции callback_handler, 
#  которая реагирует на колбэки при нажатиях на кнопки InlineKeyboardButton.
@bot.callback_query_handler(func= lambda callback: True)
def callback_message(callback):
    if callback.data == 'get_location':
        bot.send_message(callback.message.chat.id, 'Please share your location', reply_markup=types.ReplyKeyboardRemove())
        print(callback)
    elif callback.data == "get_weather":
        wae_data = Weather.get_weather_city()
        bot.send_message(callback.message.chat.id,f"Погода в {wae_data["name"]}: \nТемпература: {wae_data["main"]["temp"]}°\nСкорость ветра: {wae_data["wind"]["speed"]} м\с")



bot.polling()


