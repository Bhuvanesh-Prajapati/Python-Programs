#function to categorise vahicles based on the num_of_tyres it has
def vehicle(num_of_tyres):
    if num_of_tyres > 1 & num_of_tyres < 5:
        if num_of_tyres == 4:
            print("its a car")
        elif num_of_tyres == 3:
            print("its a rickshaw")
        elif num_of_tyres == 2:
            print("its a bike")
    else:
            print("not valid")

vehicle(1)
