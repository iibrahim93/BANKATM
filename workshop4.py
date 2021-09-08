class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin 
        self.password = password

    def get_name(self):
        """ 
        This function gets the name of the initialized User
        """
        return self.name

    def get_pin(self):
        """
        this function gets the pin of the initialized User
        """
        return self.pin

    def get_passowrd(self):
        """
        this function gets the password of the initialized User
        """
        return self.password
    
    def change_name(self, name):
        """
        this function changes the name of the initialized User
        """
        self.name = name

    def change_pin(self, pin):
        """
        this function changes the pin of the initialized User
        """
        self.pin = pin 

    def change_password(self, password):
        """
        this function changes the password of the initialized User
        """
        self.password = password

class BankUser(User):
    #Initializes a bankuser
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0 

    def get_balance(self):
        """
        This function gets the balance of the bank user
        """
        return self.balance

    def show_balance(self):
        """
        This function shows the balance of the bank user
        """
        print(self.balance)

    def withdraw(self, amount):
        """
        This function allows the a bankuser withdraw money from their account
        """
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """
        This function allows the a bankuser withdraw money from their account
        """
        self.balance += amount
        return self.balance

    def transfer_money(self, amount, target_user):
        """
        This function allows the a bankuser send money
        to another user
        """
        print(f"You are transferring ${amount} to {target_user.name}")
        print("Authentication required")
        if self.pin == input("Enter your pin: "):
            print("Transfer authorized")
            print(f"Transferring ${amount} to {target_user.name}")
            self.withdraw(amount)
            target_user.deposit(amount)
            return True
        else:
            print("INVALID pin. Transaction cancelled")
            return False

    def request_money(self, amount, target_user):
        """
        This function allows the a bankuser request money from their account
        """
        print(f"You are requesting ${amount} from {target_user.name}")
        print("User Authentication required....")
        if target_user.pin == input(f"Enter {target_user.name} pin: "):
            password = input("Enter your password: ")
            if password == self.password:
                target_user.withdraw(amount)
                self.deposit(amount)
                print("Request authorized")
                print(f"{target_user.name} sent ${amount}")
                return True
            else:
                print("INVALID password. Transaction cancelled")
        else:
            print("INVALID pin. Transaction cancelled")
            return False

        

    
    



        

""" Driver Code for task 1"""
user1 = User("Bob",1234, "password")
# print(user1.get_name(), user1.get_pin(), user1.get_passowrd())

"""Driver Code for Task 2"""
user1.change_name("Bobby")
user1.change_pin(4321)
user1.change_password("newpassword")
print(user1.get_name(), user1.get_pin(), user1.get_passowrd())

""" Driver Code for Task 3"""
bankuser1 = BankUser("Bob", "1234", "password")
print(bankuser1.get_name(), bankuser1.get_pin(), bankuser1.get_passowrd(), bankuser1.get_balance())


""" Driver Code for Task 4"""
bankuser1 = BankUser("Bob", "1234", "password")
bankuser2 = BankUser("Alice", "123", "newpassword")
print(f"{bankuser1.get_name()} has an account of {bankuser1.get_balance()}")
bankuser1.deposit(100)
print(f"{bankuser1.get_name()} has an account of {bankuser1.get_balance()}")
bankuser1.withdraw(20)
print(f"{bankuser1.get_name()} has an account of {bankuser1.get_balance()}")


""" Driver Code for Task 5"""
bankuser2.deposit(5000)
print(bankuser2.get_name(), "has a balance of : $", bankuser2.get_balance())
print(bankuser1.get_name(), "has a balance of : $", bankuser1.get_balance(), "\n")

if bankuser2.transfer_money(500,bankuser1) == True:
    print(bankuser2.get_name(), "has a balance of : $", bankuser2.get_balance())
    print(bankuser1.get_name(), "has a balance of : $", bankuser1.get_balance(), "\n")

    bankuser2.request_money(250, bankuser1)
    print(bankuser2.get_name(), "has a balance of : $", bankuser2.get_balance())
    print(bankuser1.get_name(), "has a balance of : $", bankuser1.get_balance())
else:
    print(bankuser2.get_name(), "has a balance of : $", bankuser2.get_balance())
    print(bankuser1.get_name(), "has a balance of : $", bankuser1.get_balance())




