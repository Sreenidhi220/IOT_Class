#Aum Amriteshwaryai Namah
#Class Exercise no. 8: OOP and POP illustration

# Suppose we want to model a bank account with support for 'deposit' and 'withdraw' operations.
# One way to do that is by Procedural Programming

# balance = 0

# def deposit(amount):
#     global balance
#     balance += amount
#     return balance

# def withdraw(amount):
#     global balance
#     balance -= amount
#     return balance

#The above example is good enough only if we want to have just a single account. 
#Things start getting complicated if we want to model multiple accounts.

# Have multiple accounts as list or dictionary or separate variables?

def deposit(name, amount):
    Accounts[name] += amount
    return Accounts[name]


def withdraw(name, amount):
    Accounts[name] -= amount
    return balance

Accounts = {}
Accounts["Arya"] = 2000
Accounts["Swathi"] = 2000
Accounts["Urmila"] = 2000

print("Arya's balance is %d" % deposit("Arya", 200))


class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

Arya = BankAccount()
Swathi = BankAccount()
Urmila = BankAccount()
Swathi.deposit(400)
Urmila.deposit(700)

print(Urmila.balance)

#Referece :https://anandology.com/python-practice-book/object_oriented_programming.html
