# Bank Account
class Account():

    def __init__(self,owner,balance):

        self.owner = owner
        self.balance = balance

    ## string representation of attributes of the class
    def __str__(self):
        return (f'{self.owner}, you have ${self.balance} in your bank account.')

    ## to deposit amount in account
    def deposit(self,amt1):
        self.balance = self.balance + amt1
        print(f'You just deposited ${amt1} in your account.')
        print(f'Now you have ${self.balance} in your account')

    ## to withdraw ammount from the account
    def withdrawl(self,amt2):
        if amt2 <= self.balance:
            self.balance = self.balance - amt2
            print('You have withdrawl ${amt} from your account'.format(amt=amt2))
            print(f'Your reamining balance is {self.balance}')
        else:
            print(f'You don\'t have enough balance in your account, Your account balance is ${self.balance}')

ac = Account('Bhuvanesh',1000)
print(ac)
ac.deposit(500)
ac.withdrawl(100)
ac.withdrawl(2000)
