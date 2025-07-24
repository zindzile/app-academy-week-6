
#create a shopping cart program that will continuously ask the user for food product and the price of that product
#have an exit clause if the user wishes to stop adding more things to their cart
#At the end show the food items and the total cost the user

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {food}:R"))
        foods.append(food)
        prices.append(price)
        
print("----- Your Cart -----")      

for food in foods:
    print(food, end= " ") 
    
for price in prices:
    total += price
    
print("\n")
print(f"your total is: R{total}")