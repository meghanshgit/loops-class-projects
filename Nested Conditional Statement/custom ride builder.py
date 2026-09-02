print("====================================")

print(" Welcome to Ride Builder! ")

print("====================================")

print()

print("pick your vehicle")
print("1 - bike")
print("2 - car")
print()

choice=int(input("enter 1 or 2 : "))
print()
if choice==1:
    print("pick your bike type")
    print("1 - scooter")
    print("2 - mountain bike")

    bike_type=int(input("enter 1 or 2"))
    if bike_type==1:
        print("you picked scooty")
        print("top speed : 80 km/h")
        print("best for : city roads")
    elif bike_type==2:
        print("You picked : Mountain Bike")
        print("Top speed : 40 km/h")
        print("Best for : Off-road trails")

    else:
        print("Invalid choice.")

        print("Please enter 1 for Scooty or 2 for  Mountain Bike.")


elif choice==2:
    print("Step 2: Pick your car type")
    print(" 1 - Sedan")
    print(" 2 - SUV")
    print()
    car_type = int(input("Enter 1 or 2: "))

    print()

    if car_type==1:
        print("You picked : Sedan")
        print("Seats : 5 passengers")
        print("Best for : Family trips")

    elif car_type==2 :
        print("You picked : SUV")
        print("Seats : 7 passengers")
        print("Best for : Off-road adventures")

    else:
        print("Invalid choice.")
        print("Please enter 1 for SUV or 2 for Sedan") 

else:
    print("That was not a valid choice.")

    print("Please enter 1 for Bike or 2 for Car.")