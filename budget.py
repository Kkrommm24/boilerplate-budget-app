class Category:

  def __init__(self, name):
    self.name = name
    self.total = 0.0
    self.ledger = []

  def deposit(self, amount, description):
    self.total += amount
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description):
    can_withdraw = self.check_funds(amount)
    if can_withdraw:
      self.total -= amount
      self.ledger.append({"amount": -amount, "description": description})
    return can_withdraw

  def get_balance(self):
    return self.total

  def transfer(self, amount, instance):
    canTransfer = self.check_funds(amount)
    if canTransfer:
      self.withdraw(amount, f"Transfer to {instance.name}")
      instance.deposit(amount, f"Transfer to {self.name}")
    return canTransfer

  def check_funds(self, amount):
    if amount > self.total:
      return False
    return True


food = Category("Food")
entertainment = Category("Entertainment")
food.deposit(100, "something")
food.transfer(25, entertainment)
food.withdraw(20, "beans")
print(food.ledger)
print(entertainment.ledger)
print(food.get_balance())
print(entertainment.get_balance())


def create_spend_chart(categories):
  pass
