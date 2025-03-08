from userlogin import User

class Laibrary(User):
    def __init__(self):
        super().__init__()
        self.books = {
            1: {"title": "Pride and Prejudice", "owner": "Jane Austen", "price": 250, "year": 1813},
            2: {"title": "The Fault in Our Stars", "owner": "John Green", "price": 300, "year": 2012},
            3: {"title": "2 States", "owner": "Chetan Bhagat", "price": 200, "year": 2009}
        }
        self.purchased_books = {}  # Store purchased books per student
        self.current_student = None
        self.current_user = None

    def display_books(self):
        print(f"{'ID':>5}{'Title':>35}{'Owner':>20}{'Price':>10}{'Year':>10}")
        print("=" * 80)  
        for book_id, details in self.books.items():
            print(f"{book_id:>5}{details['title']:>35}{details['owner']:>20}{details['price']:>10}{details['year']:>10}")

    def buy_book(self):
        if not self.current_student:
            print("Please login first to buy a book.")
            return

        self.display_books()
        try:
            ch = int(input("Enter the ID of the book you want to buy: "))
            qty = int(input("Enter the quantity of books: "))

            if ch in self.books:
                total_price = self.books[ch]['price'] * qty
                print(f"You have purchased {qty} copies of '{self.books[ch]['title']}' for {total_price}.")

                if self.current_student not in self.purchased_books:
                    self.purchased_books[self.current_student] = []

                self.purchased_books[self.current_student].append({"id": ch, **self.books[ch]})

                del self.books[ch]
                print("Thanks for your purchase!")

            else:
                print("Invalid book ID. Please try again.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")
    def return_book(self):
        if not self.current_student:
            print("Please login first brfor return book")
            return
        print(f"{'ID':>5}{'Title':>35}{'Owner':>20}{'Price':>10}{'Year':>10}")
        print("=" * 80)
        for book in self.purchased_books[self.current_student]:
            print(f"{book['id']:>5}{book['title']:>35}{book['owner']:>20}{book['price']:>10}{book['year']:>10}")

        rtn = int(input("Which book do you want to return (Enter Book ID): "))
        for book in self.purchased_books[self.current_student]:
            if book['id'] == rtn:
                self.books[book['id']]=book
                self.purchased_books[self.current_student].remove(book)
                print("\n\n\n\nRETRN SUCESSFULLY BRO...............")

                break





    def user_profile(self):
        if not self.current_student:
            print("Please login first to view your profile.")
            return

        print(f"\n--- {self.current_user}'s Profile ---")
        print("Purchased Books:")
        if self.current_student in self.purchased_books and self.purchased_books[self.current_student]:
            for book in self.purchased_books[self.current_student]:
                print(f"- {book}")
        else:
            print("No books purchased yet.")

    def main_menu(self):
        while True:
            print("\n--- Library Management System ---")
            print("1. Signup")
            print("2. Login")
            print("3. Display All Books")
            print("4. Buy a Book")
            print("5. return a Book")
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
                print("duua oo me yaad rakha good bye!!!!")
                break
            else:
                print("Invalid choice! Please try again.")
