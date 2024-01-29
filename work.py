class person:
    def __init__(self):
        self.name = input('Enter the name:')
        self.code = int(input('Enter the code'))

    def display(self):
        print("name is", self.name)
        print("code is", self.code)

class account(person):
    def __init__(self):
        super().__init__()
        self.pay = int(input('Enter the payment:'))

    def display(self):
        super().display()
        print("payment is", self.pay)

class admin(person):
    def __init__(self):
        super().__init__()
        self.exp = int(input('Enter the experience year:'))

    def display(self):
        super().display()
        print("experience is", self.exp)

class employee(account, admin):
    def __init__(self):
        super().__init__()

a = employee()
a.display()
