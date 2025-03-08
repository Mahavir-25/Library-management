from userlogin import User  # Importing the User class for login/signup functionality

class Library(User):  
    def __init__(self):
        super().__init__()  # Initialize User class attributes
        # Dictionary storing books with their details
        self.books = {
            1: {"title": "Pride and Prejudice", "owner": "Jane Austen", "price": 250, "year": 1813},
            2: {"title": "The Fault in Our Stars", "owner": "John Green", "price": 300, "year": 2012},
            3: {"title": "2 States", "owner": "Chetan Bhagat", "price": 200, "year": 2009}
        }
        self.purchased_books = {}  # Dictionary to store purchased books for each user
        self.current_student = None  # To keep track of the logged-in user
        self.current_user = None  # Duplicate variable, but kept for consistency

    def display_books(self):
        """Displays the available books in the library"""
        print(f"{'ID':>5}{'Title':>35}{'Owner':>20}{'Price':>10}{'Year':>10}")
        print("=" * 80)
        for book_id, details in self.books.items():
            print(f"{book_id:>5}{details['title']:>35}{details['owner']:>20}{details['price']:>10}{details['year']:>10}")

    def buy_book(self):
        """Allows a logged-in user to purchase a book"""
        if not self.current_student:
            print("Please login first to buy a book.")
            return

        self.display_books()  # Show available books
        try:
            ch = int(input("Enter the ID of the book you want to buy: "))
            qty = int(input("Enter the quantity of books: "))

            if ch in self.books:  # Check if book exists
                total_price = self.books[ch]['price'] * qty
                print(f"You have purchased {qty} copies of '{self.books[ch]['title']}' for {total_price}.")

                # Add purchased book to user's record
                if self.current_student not in self.purchased_books:
                    self.purchased_books[self.current_student] = []

                self.purchased_books[self.current_student].append({"id": ch, **self.books[ch]})

                # Remove book from available stock
                del self.books[ch]
                print("Thanks for your purchase!")

            else:
                print("Invalid book ID. Please try again.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    def return_book(self):
        """Allows a logged-in user to return a book"""
        if not self.current_student:
            print("Please login first before returning a book.")
            return

        if self.current_student not in self.purchased_books or not self.purchased_books[self.current_student]:
            print("You have no books to return.")
            return

        print(f"{'ID':>5}{'Title':>35}{'Owner':>20}{'Price':>10}{'Year':>10}")
        print("=" * 80)

        # Display purchased books
        for book in self.purchased_books[self.current_student]:
            print(f"{book['id']:>5}{book['title']:>35}{book['owner']:>20}{book['price']:>10}{book['year']:>10}")

        try:
            rtn = int(input("Enter the Book ID of the book you want to return: "))
            for book in self.purchased_books[self.current_student]:
                if book['id'] == rtn:
                    self.books[book['id']] = book  # Add the book back to available books
                    self.purchased_books[self.current_student].remove(book)
                    print("\nReturn successful! Thank you for returning the book.")
                    return

            print("Invalid Book ID. Please try again.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    def user_profile(self):
        """Displays the user's profile and purchased books"""
        if not self.current_student:
            print("Please login first to view your profile.")
            return

        print(f"\n--- {self.current_student}'s Profile ---")
        print("Purchased Books:")
        if self.current_student in self.purchased_books and self.purchased_books[self.current_student]:
            for book in self.purchased_books[self.current_student]:
                print(f"- {book['title']} by {book['owner']} ({book['year']}) - ₹{book['price']}")
        else:
            print("No books purchased yet.")

    def main_menu(self):
        """Displays the main menu and handles user choices"""
        while True:
            print("\n--- Library Management System ---")
            print("1. Signup")
            print("2. Login")
            print("3. Display All Books")
            print("4. Buy a Book")
            print("5. Return a Book")
            print("6. View Profile")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.signup()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.display_books()
            elif choice == '4':
                self.buy_book()
            elif choice == '5':
                self.return_book()
            elif choice == '6':
                self.user_profile()
            elif choice == '7':
                print("Goodbye! Have a great day!")
                break
            else:
                print("Invalid choice! Please try again.")
