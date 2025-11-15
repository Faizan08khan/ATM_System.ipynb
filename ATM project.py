# ATM_System.ipynb
ATM sytem using oops (Python) : )
class Atm():
  def __init__(self):
    self.pin=None
    self.accountnumber=8889733444
    self.balance=50000
    self.menu()
  def menu(self):
    user_input=input("""Hello User, How would you like to proceed?
       1. Enter 1 to Withdrawl
       2. Enter 2 to deposit
       3. Enter 3 to check balance
       4. Enter 4 to Generate Pin
       5. Enter 5 to exit""")
    if user_input=="1":
      self.withdrawl()
    elif user_input=="2":
      self.credited()
    elif user_input=="3":
      self.checkbalance()
    elif user_input=="4":
      self.generate_pin()
    elif user_input=="5":
      print("Thank you")
      exit()
    else:
      print("bye")
      self.menu()

  def generate_pin(self):  #No incapsulation here
    self.pin=input("Enter a pin")  #for it we can put _ _ in self.__pin=xxx
    print("Pin set successfully")
    self.menu()

  def credited(self):
    if self.pin is None:
      print("Please set a PIN first!")
      self.menu()
      return
    user_input=input("Enter your pin")
    if user_input==self.pin:
      try:
        a=int(input("Enter the amount"))
        if a<=0:
          print("Amount must be positive")
        else:
          self.balance=self.balance+a
          print("Money credited to your account number")
          print("Now Your balance is",self.balance)
      except ValueError:
        print("Invalid amount entered")
      self.menu()
    else:
      print("Invalid pin")
      self.menu()

  def withdrawl(self):
    if self.pin is None:
      print("Please set a PIN first!")
      self.menu()
      return
    user_input=input("Enter your pin")
    if user_input==self.pin:
      try:
        a=int(input("Enter the amount"))
        if a<=0:
          print("Amount must be positive")
        elif a>self.balance:
          print("Insufficient balance")
        else:
          self.balance=self.balance-a
          print("Withdrawal successful")
          print("Now Your balance is",self.balance)
      except ValueError:
        print("Invalid amount entered")
      self.menu()
    else:
      print("Invalid pin")
      self.menu()


  def checkbalance(self):
    if self.pin is None:
      print("Please set a PIN first!")
      self.menu()
      return
    user_input=input("Enter your pin")
    if user_input==self.pin:
     print("Your balance is",self.balance)
     self.menu()
    else:
      print("Invalid pin")
      self.menu()

if __name__ == "__main__":
    atm = Atm()

