"""Restaurant rating lister."""


# put your code here
def show_restaurant_rating(filename):

    file = open(filename)
    restaurant_rating = {}

    for line in file:
        line = line.rstrip()
        name_rating = line.split(":")
        restaurant_rating[name_rating[0]] = name_rating[1]

    sorted_name = sorted(restaurant_rating)

    for name in sorted_name :
        print(f"{name} is rated at {restaurant_rating[name]}.")



def add_rating():
    restaurant_name = input("What is the restaurant name? ")
    restaurant_rating = input(f"What is {restaurant_name}'s rating? ")

    return tuple(restaurant_name,restaurant_rating)




