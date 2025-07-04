class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    
        print(f"Current balance on the account is ${self.balance}")


    def add_money(self):
        while True: 
            try: 
                amount = int(input("How much money do you want to add?: "))

                self.balance += amount
                more_money = input("Do you want to add more money? (yes/no): ")
                if more_money.lower() != 'yes':
                    break
            except ValueError:
                print("The value entered is invalid. Please enter a number.")
            

        print(f"New balance on the account is ${self.balance}")


    def subtract_money(self):
        while True:
            try:
                amount = int(input("How much money do you want to subtract?: "))

                self.balance -= amount
                less_money = input("Do you want to subtract more money? (yes/no): ")
                if less_money.lower() != 'yes':
                    break
            except ValueError:
                print("The value entered is invalid. Please enter a number.")



        print(f"New balance on the account is ${self.balance}")



class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        self.min_balance = min_balance
        super().__init__(balance)
        print(f"Minimum amount allowed on this account is ${min_balance}")


    def transactions(self):
        while True:
            try: 
                operation = int(input("""Choose an option:
                1. Add money
                2. Subtract money
                3. Exit
                    """))
                if operation == 1:
                    self.add_money()
                elif operation == 2:
                    self.subtract_money()
                    if self.balance < self.min_balance:
                        print(f"You have reached the minimum amount allowed for this account, which is ${self.min_balance}")
                        break
                elif operation == 3:
                    break
            except ValueError:
                print("Invalid option. You need to choose an option between 1, 2 or 3.")
        
        
        print(f"Your final balance is: ${self.balance}")
        print("Thank you for using our bank")
    
my_account = SavingsAccount(1000, 200)

my_account.transactions()
