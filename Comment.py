class Comment:
	def __init__(self, author_id, comment_id, post_id, text):
		self.__author_id = author_id
		self.__comment_id = comment_id
		self.__post_id = post_id
		self.__text = text
		self.__time = None