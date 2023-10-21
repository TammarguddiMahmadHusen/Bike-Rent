class Bike:
    def __init__(self, bike_id, is_available=True):
        self.bike_id = bike_id
        self.is_available = is_available

class BikeRental:
    def __init__(self, inventory):
        self.inventory = inventory

    def rent_bike(self, bike_id):
        bike = self.get_bike(bike_id)
        if bike:
            if bike.is_available:
                bike.is_available = False
                print(f"Rented bike with ID {bike_id}")
            else:
                print(f"Bike with ID {bike_id} is already rented.")
        else:
            print(f"Bike with ID {bike_id} does not exist in our inventory.")

    def return_bike(self, bike_id):
        bike = self.get_bike(bike_id)
        if bike:
            if not bike.is_available:
                bike.is_available = True
                print(f"Returned bike with ID {bike_id}")
            else:
                print(f"Bike with ID {bike_id} is already available.")
        else:
            print(f"Bike with ID {bike_id} does not exist in our inventory.")

    def get_bike(self, bike_id):
        for bike in self.inventory:
            if bike.bike_id == bike_id:
                return bike
        return None

    def display_inventory(self):
        print("Bike Inventory:")
        for bike in self.inventory:
            status = "Available" if bike.is_available else "Rented"
            print(f"Bike ID: {bike.bike_id} - Status: {status}")

def main():
    # Create some bike objects and add them to the inventory
    bike1 = Bike(1)
    bike2 = Bike(2)
    bike3 = Bike(3)
    inventory = [bike1, bike2, bike3]

    rental_system = BikeRental(inventory)

    while True:
        print("\n1. Rent a bike")
        print("2. Return a bike")
        print("3. Display bike inventory")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            bike_id = int(input("Enter the bike ID you want to rent: "))
            rental_system.rent_bike(bike_id)
        elif choice == '2':
            bike_id = int(input("Enter the bike ID you want to return: "))
            rental_system.return_bike(bike_id)
        elif choice == '3':
            rental_system.display_inventory()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
