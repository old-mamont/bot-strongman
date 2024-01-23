# import mysql.connector
# # Установите соединение с базой данных
# def create_connection():
#     connection = mysql.connector.connect(
#         host="mysql74.hostland.ru",
#         user="host1630433_tbotbase",
#         password="vwwlPmQR",
#         database="host1630433_tbotbase"
#     )
#     return connection

# base = create_connection()
# print(base)




def verification_user(user : dict) -> bool :
    """ Авторизация пользователя
    Принимает юзера. Отдаёт true если найден id, иначе записывает id"""
    with open("User.txt", "r+") as file:
        us_id = str(user.id)
        if not us_id + "\n" in file.readlines():
            file.write(us_id + "\n")
            return False
        return True


   
        
    



    
    






