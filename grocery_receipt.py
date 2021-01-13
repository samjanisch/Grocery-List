#Grocery List Price Calculator
import random

store_options = {"Bread": 2.99, "Turkey": 3.99, "Apple": 1.00, "Onion": 0.50,
                 "Olive Oil": 5.00, "Flank Steak": 12.00, "Salmon": 8.00,
                 "Bag of Pretzel": 1.99}
total = 0

for key in store_options:
    num_of_items = random.randrange(0, 5)
    price_of_item = (store_options[key] * num_of_items)
    total += price_of_item
    print("Your list contains " + str(num_of_items)+ " " + key +
          " at a price of " + str(price_of_item))

    
print("The total cost of your shopping trip is " + str(total))
