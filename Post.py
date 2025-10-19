class Post:
	def __init__(self, post_id, author_id, author_name, content, time, comment_id, likes):
		self.__post_id = post_id
		self.__author_id = author_id
		self.__author_name = author_name
		self.__content = content
		self.__time = None #мы создадим метод для назначения времени
		self.__comment_id = comment_id 
		self.__likes = likes