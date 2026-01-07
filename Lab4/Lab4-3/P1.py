from datetime import datetime

class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self._id = item_id
        self.__checked_out = False
    
    def get_status(self):
        return "Checked out" if self.__checked_out else "Available"
    
    def check_out(self):
        # if checked_out is False (item still in lib)
        if not self.__checked_out:
            self.__checked_out = True
            return True
        # can't check out if item not in lib
        return False
    
    def return_item(self):
        if self.__checked_out:
            self.__checked_out = False
            return True
        return False

# implement 3 classes here
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
        self.pages_count = 0

    def set_pages_count(self, pages):
        self.pages_count = pages

    def display_info(self):
        print(
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Pages: {self.pages_count}\n"
            f"Status: {self.get_status()}"
        )
class TextBook(Book):
    def __init__(self, title, item_id, author, subject, grade_level):
        super().__init__(title, item_id, author)
        self.subject = subject
        self.grade_level = grade_level

    def display_course_info(self):
        print(
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Pages: {self.pages_count}\n"
            f"Subject: {self.subject}\n"
            f"Grade Level: {self.grade_level}\n"
            f"Status: {self.get_status()}"
        )

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

        now = datetime.now()
        self.month = now.month
        self.year = now.year

    def display_issue(self):
        print(
            f"Title: {self.title}\n"
            f"Issue: {self.issue_number}\n"
            f"Date: {self.month}/{self.year}\n"
            f"Status: {self.get_status()}"
        )

# Test your code:
# This is just an example. You should test a lot more than this.
print("<===========[book]===========>")
book = Book("Harry Potter", "B001", "J.K. Rowling")
book.set_pages_count(350)
book.display_info()
print("<============================>")
print()

print("<=========[CheckOut]=========>")
book.check_out()
book.display_info()
print("<============================>")
print()

print("<==========[Return]==========>")
book.return_item()
book.display_info()
print("<============================>")
print()

print("<=========[TextBook]=========>")
textbook = TextBook("In a range of time", "T001", "Kittikawin", "History", "Highschool")
textbook.set_pages_count(500)
textbook.display_course_info()
print("<============================>")
print()

print("<=========[Magazine]=========>")
mag = Magazine("TIME", "M001", 202)
mag.display_issue()
print("<============================>")



