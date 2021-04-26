class Category:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount
        return "You made a {} deposit for this {} category".format(amount, self.category)

    def withdraw(self, amount):
        self.amount -= amount
        return "You have withdrawn {} from the {} category, balance is now {}".format(amount, self.category,
                                                                                      self.amount)

    def check_balance(self, amount):
        if amount < self.amount:
            return True
        return False

    def category_balance(self):
        return "Your category balance is now: {}".format(self.amount)

    def transfer(self, amount, cat):
        #transfer between two instantiated class
        cat.amount += amount
        return "${} is transferred fron {} to {}".format(amount,self.category,cat.category)
        
        #print("The current balance in {} is now {}".format(self.category, self.amount))


food_category = Category("Food", 1000)
clothing_category = Category("Clothing", 500)
car_category = Category("Car Expenses", 200)
utilities_category = Category("Utilities", 500)
entertainment_category = Category("Entertainment", 200)

print(food_category.withdraw(200))
print(food_category.check_balance(500))
print(food_category.category_balance())
print(food_category.transfer(600,utilities_category))

print(food_category.transfer(50, car_category))
