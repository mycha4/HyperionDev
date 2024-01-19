# program that calculates total stock worth in my cafe
# cafe menu
menu = ["Breakfast wrap","Toast with jam","Bagel with cream cheese","Ham and cheese melt","Black coffee","White coffee", "Orange juice","Tea"]
# cafe stock
stock = {
        "Breakfast wrap": 5,
        "Toast with jam": 6,
        "Bagel with cream cheese": 10,
        "Ham and cheese melt": 8,
        "Black coffee": 10,
        "White coffee": 10,
        "Orange juice": 6,
        "Tea": 11,
         }
# cafe prices per item         
price = {
        "Breakfast wrap": 6.50,
        "Toast with jam": 4,
        "Bagel with cream cheese": 4.50,
        "Ham and cheese melt": 3.50,
        "Black coffee": 2.50,
        "White coffee": 2.50,
        "Orange juice": 4,
        "Tea": 2.50,
         }
# total stock worth calculation
total_stock = {key: stock[key] * price[key] for key in menu}
total_stock_sum = sum(total_stock.values())
print("Total stock value is ",total_stock_sum, "£")
