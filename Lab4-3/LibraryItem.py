from datetime import datetime

class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self._id = item_id
        self._checked_out = False
    
    def get_status(self):
        return "Checked out" if self._checked_out else "Available"
    
    def check_out(self):
        # if checked_out is False (item still in lib)
        if not self._checked_out:
            self._checked_out = True
            return True
        # can't check out if item not in lib
        return False
    
    def return_item(self):
        if self._checked_out:
            self._checked_out = False
            return True
        return False
        
    def display_info(self):
        print(f"Title: {self.title}\n"
              f"ID : {self._id}\n"
              f"Status: {self.get_status()}")

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
            f"Status: {self.get_status()}\n"
            f"Author: {self.author}\n"
            f"Pages: {self.pages_count}"
        )
class TextBook(Book):
    def __init__(self, title, item_id, author, subject, grade_level):
        super().__init__(title, item_id, author)
        self.subject = subject
        self.grade_level = grade_level

    def display_info(self):
        super().display_info()
        print(
            f"Subject: {self.subject}\n"
            f"Grade Level: {self.grade_level}"
        )

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

        now = datetime.now()
        self.month = now.month
        self.year = now.year

    def display_info(self):
        super().display_info()
        print(
            f"Issue: {self.issue_number}\n"
            f"Date: {self.month}/{self.year}"
        )
