class publisher:
    def __init__(self):
        self.name=input("Enter Publisher Name")
class book(publisher):
    def __init__(self):
        super().__init__()
        self.author=input("Enter Author Name")
        self.title=input("Enter Title")
class python(book):
    def __init__(self,):
        super().__init__()
        self.page=input("Enter thee pages")
    def display(self):
        print("Publisher", self.name)
        print("Author: ", self.author)
        print("Title: ", self.title)
        print("Number of pages: ", self.page)

obj=python()
obj.display()
