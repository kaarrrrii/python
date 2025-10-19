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