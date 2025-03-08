class User:
    def __init__(self):
        # Dictionary to store user credentials (username as key and password as value)
        self.user = {}
        # Variable to keep track of the currently logged-in user
        self.current_student = None
        # Dictionary to store purchased books for each user
        self.parcheshed_book = {}

    def signup(self):
        """Method for user signup (registration)"""
        username = input("Username: ")

        # Check if the username already exists
        if username in self.user:
            print("User ID already exists.")
            return False

        password = input("Password: ")

        # Store the username and password in the dictionary
        self.user[username] = password

        # Initialize an empty list for storing purchased books of the user
        self.parcheshed_book[username] = []

        print("User signup successfully.")

        # Automatically log in the user after successful signup
        self.login()
        return True

    def login(self):
        """Method for user login"""
        print("---------- Login Details ----------")

        username = input("Username: ")
        password = input("Password: ")

        # Check if username exists and password matches
        if username in self.user and self.user[username] == password:
            self.current_student = username  # Set the current logged-in user
            print("Login successful. Welcome", username)
            return True
        else:
            print("Invalid username or password. Please check and try again.")
            return False
