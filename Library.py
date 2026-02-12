import logging
logging.basicConfig(
    filename="books.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LibraryBook:

    fine_per_day = 10

    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_issued = False
        self.days_issued = 0

    def issue_book(self, days):
        if self.is_issued==False and days > 0:
            self.is_issued = True
            self.days_issued = days
            logging.info("the book is issued for %d days",days)
        else:
            logging.info("Book is already issued or invalid days")

    def return_book(self):
        if self.is_issued:
            logging.info("Book returned successfully")
            self.is_issued = False
        
    def calculate_fine(self, allowed_days):
        if self.days_issued > allowed_days:
            late_days = self.days_issued - allowed_days
            fine = late_days * LibraryBook.fine_per_day
            logging.info("the book is late by %d days",late_days)
            logging.info("Fine Amount is %d", fine)
        else:
            logging.info("No fine. Book returned on time.")

    @classmethod
    def update_fine_per_day(cls, new_fine):
        cls.fine_per_day = new_fine
        logging.info("Fine per day updated to %d", cls.fine_per_day)

b1 = LibraryBook("Secret Alchemist", "Author", 101)

b1.issue_book(10)
b1.calculate_fine(7)
b1.return_book()

LibraryBook.update_fine_per_day(20)

b1.issue_book(12)
b1.calculate_fine(7)