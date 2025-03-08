class User:
	def __init__(self):
		self.user={}
		self.current_student= None
		self.parcheshed_book={}
	def signup(self):
		username=input("Username:")
		if username in self.user:
			print("user id alredy exist:")
			return False
		password=input("Password:")
		self.user[username]=password
		self.parcheshed_book[username]=[]
		print("User signup succesfully ")
		self.login()
		return True
	def login(self):
		print("----------login details----------")
		username=input("username:")
		password=input("Password:")
		if username in self.user and self.user[username]==password:
			self.current_student=username
			print("login succesfully welcome",username)
			return True
		else:
			print("invalid username or password please check or login")
			return False
	