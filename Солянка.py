import hashlib
import os
import datetime

class User:
	def __init__(self, user_id, user_name, login, password):
		self.__user_id = user_id
		self.__user_name = user_name
		self.__login = login
		self.__salt, self.__password_hash = self._hash_password(password)
		self.__comment_ids = set() #все комменты
		self.__like_ids = set() #все лайки
		self.__friends_ids = set() #все друзья
		self.__posts_ids = set() #все посты

	#хэширование
	def _hash_password(self, password):
		salt = os.urandom(32) #создание соли
		password_hash = hashlib.pbkdf2_hmac( #создание хэша
			'sha256',
			password.encode('utf-8'),
			salt,
			100 # количество прогонов
			)
		return salt, password_hash

	def get_user_id(self):
		return self.__user_id
	
	def get_login(self):
		return self.__login
	
	def get_user_name(self):
		return self.__user_name
	
	#проверяем
	def check_password(self, password):
		test_hash = hashlib.pbkdf2_hmac(
			'sha256',
			password.encode('utf-8'),
			self.__salt,
			100 # количество прогонов
			)
		return test_hash == self.__password_hash
	
	def add_friend(self, friend_id):
		if (friend_id == self.__user_id):
			print("Ты дурак? Заведи себе друзей уже.")
			return
		else:
			self.__friends_ids.add(friend_id)
			print("Ура, ты не одинок")


class Post:
	def __init__(self, post_id, author_id, author_name, time, likes):
		self.__post_id = post_id
		self.__author_id = author_id
		self.__author_name = author_name
		self.__time = datetime.datetime.now() #мы создадим метод для назначения времени
		self.__likes = likes
		self.__comments = []

class TextPost(Post):
	def __init__(self, post_id, author_id, author_name, text, time, likes, topic):
		super().__init__(post_id, author_id, author_name, time, likes)
		self.__topic = topic
		self.__text = text

class VideoPost(Post):
	def __init__(self, post_id, author_id, author_name, video, time, likes, duration):
		super().__init__(post_id, author_id, author_name, time, likes, duration)
		self.__duration = duration
		self.__video = video

class ImagePost(Post):
	def __init__(self, post_id, author_id, author_name, image, time, likes, caption):
		super().__init__(post_id, author_id, author_name, time, likes, caption)
		self.__caption = caption
		self.__image = image



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
					return user
				else:
					print("Неверный пароль")
					return None
		
		print("Нет пользователя с таким логином")
		return None 
	
	def add_friendship(self, user_id_1, user_id_2):
		if user_id_1 in self.__users and user_id_2 in self.__users:
			user1 = self.__users[user_id_1]
			user2 = self.__users[user_id_2]
			user1.add_friend(user_id_2)
			user2.add_friend(user_id_1)
			print("#вы друзья")
		else:
			print("Один из пользователей твоя шиза.")

start = SocialStructure()

user_id_1 = start.registration("karri", "mail@mail.ru", "1234a")
user_id_2 = start.registration("name2", "89228177877", "1234a")

user_3 = start.login("mail@mail.ru", "1234a")
user_4 = start.login("mail@mail.ru", "1234")

user_5 = start._SocialStructure__users[user_id_1]
user_6 = start._SocialStructure__users[user_id_2]

print("Друзья Karry:", user_5._User__friends_ids)
print("Друзья Alex:", user_6._User__friends_ids)




