# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


import datetime
t = datetime.datetime.now()
print(type(t))
print(t)
#print("STARTED AT: " + t)
print(t.strftime("%Y-%m-%d %I:%M %p"))

#
# INFO CAPTURE / INPUT
#

subtotal_price = 0
selected_ids = []

while True:
    selected_id = input("Please input a product identifier: ") #> "9" this is a string version 
    #> "DONE"
    if selected_id == "DONE":
        break
    else:
        """ matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0]
        total_price = total_price + matching_product["price"]
        print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"])) """
        selected_ids.append(selected_id)

#
# INFO DISPLAY / OUTPUT
#
 
#print(selected_ids)

#print receipt

print("---------------------------")
print("JOSIE'S GROCERIES")
print("WWW.JOSIE'S-GROCERIES.COM")
print("---------------------------")
print("CHECKOUT AT: " + t.strftime("%Y-%m-%d %I:%M %p"))
print("---------------------------")

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    subtotal_price = subtotal_price + matching_product["price"]
    print("SELECTED PRODUCT: " + matching_product["name"] + " (" + to_usd(matching_product["price"])+ ")")

tax_rate = 0.06 # constant tax rate for DC

tax = subtotal_price * tax_rate
total_price = subtotal_price + tax

""" x = 1

running_total = 0

while x < 5: # todo: restore infinite looping condition
    # todo: ask the user to input a product id
    selected_id = 1 # input("Please select a product id (1-20)")
    #product = {
    #    "id":1, 
    #    "name": "Chocolate Sandwich Cookies", 
    #    "department": "snacks", 
    #    "aisle": "cookies cakes", 
    #    "price": 3.50
    #}
    matching_products = [p for p in products if p["id"] == selected_id]
    product = matching_products[0]
    price = product["price"] #4.95 # todo: lookup actual price of the scanned/selected product
    running_total = running_total + price
    x = x + 1 """

print("---------------------------")
print("SUBTOTAL: " + to_usd(subtotal_price))
print("TAX: " + to_usd(tax))
print("TOTAL: " + to_usd(total_price))
print("---------------------------")
print("THANKS FOR SHOPPING AT JOSIE'S GROCERIES!")
print("---------------------------")
