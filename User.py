import hashlib
import os

class User:
	def __init__(self, user_id, user_name, login, password):
		self.__user_id = user_id
		self.__user_name = user_name
		self.__login = login
		self.__salt, self.__password_hash = self.__hash_password(password)
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

	def get_login(self):
		return self.__login
	
	def get_user_name(self):
		return self.__user_name
	
	def get_user_id(self):
		return self.__user_id
	
	#проверяем
	def check_password(self, password):
		test_hash = hashlib.pbkdf2_hmac(
			'sha256',
			password.encode('utf-8'),
			salt,
			100 # количество прогонов
			)
		return test_hash == self.__password_hash