class Bicycle_Part(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

class Wheel(Bicycle_Part):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

class Frame(Bicycle_Part):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

class Bicycle(object):
    def __init__(self, model, wheel_type, frame_type):
        self.model = model
        self.wheel_type = wheel_type
        self.frame_type = frame_type

    wheel_count = 2

    def calc_value(self, attribute):
        return (getattr(self.wheel_type, attribute) * 2) + getattr(self.frame_type, attribute)

    def weight(self):
        return self.calc_value("weight")

    def cost(self):
        return self.calc_value("cost")

class Bicycle_Shop(object):
    def __init__(self, shop_name, bicycle_inventory = {}, bicycle_markup = 0.0):
        self.shop_name = shop_name
        self.bicycle_inventory = bicycle_inventory
        self.bicycle_markup = bicycle_markup
        self.profit_balance = 0
        
    def bicycle_selling_price(self, bicycle): 
        return int(bicycle.cost() + round(bicycle.cost() * self.bicycle_markup,0))
        
    def sell_bicycle(self, bicycle):
        if self.bicycle_inventory[bicycle] > 0:
            bicycle_profit = self.bicycle_selling_price(bicycle) - bicycle.cost()
            self.profit_balance += bicycle_profit
            self.bicycle_inventory[bicycle] -= 1
            print ("{0} has successfully sold a {1} for ${2}.".format(self.shop_name, bicycle.model, bicycle_profit))
        else:
            print ("{0} bicycle is not in stock to sell.".format(bicycle))
    
    def reset_profit_balance (self):
        self.profit_balance = 0
    
    def print_inventory(self, selling_price_limit = 9999):
        print ("Name     Count    Selling Price")
        for bicycle in self.bicycle_inventory:
            bicycle_selling_price = self.bicycle_selling_price(bicycle)
            if bicycle_selling_price < selling_price_limit:
                print ("{0}    {1}    ${2}".format(bicycle.model, self.bicycle_inventory[bicycle], bicycle_selling_price))
                
class Customer(object):
    def __init__(self, customer_name, budget, bicycle = None):
        self.customer_name = customer_name
        self.budget = budget
        self.bicycle = bicycle
    def purchase_bicycle(self, bicycle, bicycle_cost):
        self.bicycle = bicycle
        self.budget -= bicycle_cost
        print ("Thank you {0}, you bought a {1} for ${2}. You have ${3} left in your budget.".format(self.customer_name, bicycle.model, bicycle_cost, self.budget))