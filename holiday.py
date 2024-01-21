# this is a program that calculates total cost of the holiday based on users input
print("Welcome to your holiday planner!")
print()
# ask user to input holiday destination
city_flight = input("Where would you like to go?\nPlease choose from following options:\nLondon\nNew York\nTakyo\nBeijing\nLos Angeles\nParis\n").capitalize() 
# flight prices based on destination
cities_flight_cost = {                     
        "London":175,
        "New York":250,
        "Tokyo":375,
        "Beijing":400,
        "Los Angeles":245,
        "Paris":175
}
# ask user for number of nights
num_nights = int(input("Please enter the number of nights you are planning to stay at the hotel: "))
# ask user for number of days of hire car 
rental_days = int(input("Please enter the number of days you will need your hired car for: "))
# function to calculate hotel cost
def hotel_cost(num_nights):
    cost_num_days_hot_stay = num_nights * 175
    return cost_num_days_hot_stay
# function to calculate flight cost based on users input
def plane_cost(city_flight):
    if city_flight in cities_flight_cost:
        return cities_flight_cost[city_flight]
# function to calculate car rental
def car_rental(rental_days):
    cost_days_car_rental = rental_days * 65
    return cost_days_car_rental
# function to calculate total holiday cost
def holiday_cost(total_flight, total_hotel, total_car):
    total_holiday_cost = (total_flight + total_hotel + total_car)
    return total_holiday_cost
print()
print("<><><><><><><><><><><><><><><><><><>")
print()
# print holiday details based on users input
print(f"Your holiday details:\nFlying from:       {city_flight}\nNumber of nights:{num_nights:3}\nCar hire days:{rental_days:6}")
# call functions to calculate flight  hotel and car rental costs
total_flight = plane_cost(city_flight)
total_hotel = hotel_cost(num_nights)
total_car = car_rental(rental_days)
total_holiday = holiday_cost(total_flight, total_hotel, total_car)
print()
print("<><><><><><><><><><><><><><><><><><>")
print()
# print total holiday cost
print("Your holiday total is", total_holiday, "£")
print()
