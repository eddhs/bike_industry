from bike_industry import Wheel, Frame, Bicycle, Bicycle_Shop, Customer

#wheel types
Bones = Wheel("Bones", 3, 15)
Spitfire = Wheel("Spitfire", 4, 25)
Better = Wheel("Better", 5, 35)

#frame types
Aluminum = Frame("Aluminum", 10, 100)
Carbon = Frame("Carbon", 5, 250)
Steel = Frame("Steel", 15, 70)

#bike models
Alienware = Bicycle("Alienware", Bones, Aluminum)
PlanB = Bicycle("PlanB", Spitfire, Carbon)
Deathwish = Bicycle("Deathwish", Better, Steel)
Almost = Bicycle("Almost", Bones, Carbon)
Enjoi = Bicycle("Enjoi", Spitfire, Steel)
DGK = Bicycle("DGK", Better, Aluminum)

#bike shop name and inventory with 20% markup
Active_Bike_Shop = Bicycle_Shop("Active Bike Shop", {Alienware: 4, PlanB: 5, Deathwish: 6, Almost: 10, Enjoi: 15, DGK: 8}, .2)

#Customer names and budgets
Roger = Customer("Roger", 200)
Eric = Customer("Eric", 500)
Kyle = Customer("Kyle", 1000)
customers = [Roger, Eric, Kyle]

for customer in customers:
    print ("{0} Current Inventory for {1}".format(Active_Bike_Shop,customer.customer_name))
    Active_Bike_Shop.print_inventory(customer.budget)
    print ("")
    
print ("{0} Total Starting Inventory".format(Active_Bike_Shop.shop_name))
Active_Bike_Shop.print_inventory()
print ("")

Active_Bike_Shop.reset_profit_balance()
bicycle_purchases = {Roger: PlanB, Eric: Almost, Kyle: DGK}
print ("Bicycle Purchases")
for customer in bicycle_purchases:
    bicycle_sold = bicycle_purchases[customer]
    customer.purchase_bicycle(bicycle_sold, Active_Bike_Shop.bicycle_selling_price(bicycle_sold))
    Active_Bike_Shop.sell_bicycle(bicycle_sold)
    print ("")
    
print ("{0} Total Ending Inventory".format(Active_Bike_Shop.shop_name))
Active_Bike_Shop.print_inventory()
print ("")
print ("{0} Total Profit = ${1}".format(Active_Bike_Shop.shop_name, Active_Bike_Shop.profit_balance))



