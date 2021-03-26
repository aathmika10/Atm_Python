class atm:
    def __init__(self,card_number, pin_number):
        self.pin_number=pin_number
        self.card_number=card_number

    def cashWithdrawel(self,amount):
        print("The amount withdrawed is "+ amount)

    def balanceEnquiry(self):
        print("The balance left = 20000 ")

def main():
    cardNumber=input("enter your card number: ")
    pinNumber=input("Enter your pin number: ")

    person1= atm(cardNumber,pinNumber)
    person1.cashWithdrawel(input("Enter amount to be withdrawed: "))
    person1.balanceEnquiry()

main()