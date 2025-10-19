import hashlib
import os
import binascii

class User:
	def __init__(self, user_id, user_name, login, password):
		self.__user_id = user_id
		self.__user_name = user_name
		self.__login = login
		self.__password = password
		self.__comment_ids = set() #все комменты
		self.__like_ids = set() #все лайки
		self.__friends_ids = set() #все друзья
		self.__posts_ids = set() #все посты
	
	def get_login(self):
		return self.__login
	
	def get_user_name(self):
		return self.__user_name
	
	def get_user_id(self):
		return self.__user_id
	
	def check_password(self, password):
		return self.__password == password


class Post:
	def __init__(self, post_id, author_id, author_name, content, time, comment_id, likes):
		self.__post_id = post_id
		self.__author_id = author_id
		self.__author_name = author_name
		self.__content = content
		self.__time = None #мы создадим метод для назначения времени
		self.__comment_id = comment_id 
		self.__likes = likes

class Comment:
	def __init__(self, author_id, comment_id, post_id, text):
		self.__author_id = author_id
		self.__comment_id = comment_id
		self.__post_id = post_id
		self.__text = text
		self.__time = None

class Like:
	def __init__(self, like_id, user_id):
		self.__like_id = like_id
		self.__user_id = user_id
		self.__time = None

class SocialStructure:
	def __init__(self):
		self.__users = {}
		self.__posts = []
		self.__next_user_id = 1

	def registration(self, user_name, login, password):
		#создание экземпляра класса
		user_id = self.__next_user_id # создание id пользователя
		user = User(user_id, user_name, login, password) #создание самого пользователя
		#закидывание в систему
		self.__users[user_id] = user # сохранение в систему класса
		self.__next_user_id += 1
		#возвращаем айди для последующей генерации
		print("Создан: " + user_name + " " +str(user_id))
		return user_id
	
	def login(self, login, password):
		for user in self.__users.values():
			if user.get_login() == login:
				
				if user.check_password(password):
					print("Успешный вход")
					return User
				else:
					print("Неверный пароль")
					return None
		
		print("Нет пользователя с таким логином")
		return None 

start = SocialStructure()

user_1 = start.registration("karri", "mail@mail.ru", "1234a")
user_2 = start.registration("name2", "89228177877", "1234a")

user = start.login("mail@mail.ru", "1234a")
user_3 = start.login("mail@mail.ru", "1234")


