from  mysql.connector import *


class Base_SQL():
    def __init__(self) -> None:
        pass
    
    def create_connection():
        """Подключение к БД"""
        connection = connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bot-sport-bd"
        )
        return connection
        
    def show(request : str) -> list:
        """  Принимает sql запрос. Возращает список значений """
        connection = Base_SQL.create_connection()
        with connection.cursor() as cursor:
            cursor.execute(request) # чтение
            result = cursor.fetchall()
        connection.close()  # Закрытие соединения
        return result
    
    def write(request : str, data : list):
        """request - sql запрос. data - данные для записи, формат: [(user.id, user.first_name, str(user.last_name))]"""
        connection = Base_SQL.create_connection()
        with connection.cursor() as cursor:
            cursor.executemany(request, data)
            connection.commit()
        connection.close()

    
    



















# Установите соединение с базой данных
# def create_connection():
#     connection = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="",
#         database="bot-sport-bd"
#     )
#     return connection


# base = create_connection()
# cursor = base.cursor()
# query = ("SELECT * FROM User")
# cursor.execute(query)

# print(cursor)
# for i in cursor:
#   print(i)





# def verification_user(user : dict) -> bool :
#     """ Авторизация пользователя
#     Принимает юзера. Отдаёт true если найден id, иначе записывает id"""
#     with open("User.txt", "r+") as file:
#         us_id = str(user.id)
#         if not us_id + "\n" in file.readlines():
#             file.write(us_id + "\n")
#             return False
#         return True



        
    



    
    






