class Category:
  def __init__(self, name):
    self.name = name
    self.total = 0.0

  def deposit(self, amount):
    self.total += amount

  def withdraw(self, amount):
    self.total -= amount

  def get_balance(self):
    return self.total
    
  def transfer(self, amount, instance):
    if amount > self.total:
      return False

    self.withdraw(amount)
    instance.deposit(amount)
    return True

  def check_funds(self):
    pass
food = Category("Food")
entertainment =  Category("Entertainment")
food.deposit(100)
food.transfer(25, entertainment)
print(food.get_balance())
print(entertainment.get_balance())



def create_spend_chart(categories):
  pass