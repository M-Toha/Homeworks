## Practice

#1. Write a Python class named Circle constructed by a radius and two methods
# which will compute the area and the perimeter of a circle.
import math
class Circle:
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self):
        return math.pi*self.radius ** 2
    
    def perimeter(self):
        return math.pi*self.radius * 2
    
cir = Circle(1)
print(f'Area: {cir.area()}\nPerimeter: {cir.perimeter()}')

# 2. Write a Python program to crate two empty classes, Student and Marks. 
# Now create some instances and check whether they are instances of the said classes or not. 
# Also, check whether the said classes are subclasses of the built-in object class or not.

class Student:
    pass

class Marks:
    pass

John = Student()
F = Marks()

assert isinstance(John, Student) == True
assert isinstance(F, Marks) == True
assert isinstance(John, object) == True
assert isinstance(F, object) == True
'''
3. A Bank
    1. Using the Account class as a base class, write two derived classes called SavingsAccount and CurrentAccount. 
    A SavingsAccount object, in addition to the attributes of an Account object, 
    should have an interest attribute and a method which adds interest to the account. 
    A CurrentAccount object, in addition to the attributes of an Account object, 
    should have an overdraft limit attribute.

    2. Now create a Bank class, an object of which contains an array of Account objects. 
    Accounts in the array could be instances of the Account class, the SavingsAccount class, 
    or the CurrentAccount class. Create some test accounts (some of each type).

    3. Write an update method in the Bank class. It iterates through each account, 
    updating it in the following ways: Savings accounts get interest added (via the method you already wrote); 
    CurrentAccounts get a letter sent if they are in overdraft. (use print to 'send' the letter).

    4. The Bank class requires methods for opening and closing accounts, 
    and for paying a dividend into each account.
'''
class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number
    
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'
    
my_account = Account(3000, 342)
new_account = Account.create_account(432)
print(my_account)
print(new_account)

class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest: float):
        super().__init__(balance, account_number)
        self._interest = interest

    def add_interest(self):
        self._balance = round(self._balance*(1 + self._interest), 2)
      
        
class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit: int):
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit

save_account = SavingsAccount(1214, 343, 0.11)
save_account.add_interest()
print(save_account)

cur_account = CurrentAccount(3200, 344, 5000)
cur_account1 = CurrentAccount(-7000, 345, 5000)
class Bank:
    def __init__(self, accounts: list[Account]):
        self._accounts = accounts

    def get_accounts(self):
        for acc in self._accounts:
            print(acc)

    def update_accounts(self):
        for acc in self._accounts:
            if isinstance(acc, SavingsAccount):
                acc.add_interest()
            elif isinstance(acc, CurrentAccount):
                if acc._balance + acc._overdraft_limit < 0:
                    print(f' Dear account number {acc._account_number} owner, you are in overdraft')

    def open_account(self, newacc: Account):
        self._accounts.append(newacc)

    def close_account(self, acc: Account):
        self._accounts.remove(acc)
 
mybank = Bank([my_account, save_account, cur_account])
print(mybank.get_accounts())
mybank.open_account(cur_account1)
print(mybank.get_accounts())
mybank.update_accounts()
mybank.close_account(my_account)
print(mybank.get_accounts())








