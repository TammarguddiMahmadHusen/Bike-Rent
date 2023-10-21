from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name)

class Bike:
    def __init__(self, bike_id, is_available=True):
        self.bike_id = bike_id
        self.is_available = is_available

class BikeRental:
    def __init(self, inventory):
        self.inventory = inventory

    def rent_bike(self, bike_id):
        bike = self.get_bike(bike_id)
        if bike:
            if bike.is_available:
                bike.is_available = False
                return f"Rented bike with ID {bike_id}"
            else:
                return f"Bike with ID {bike_id} is already rented."
        else:
            return f"Bike with ID {bike_id} does not exist in our inventory."

    def return_bike(self, bike_id):
        bike = self.get_bike(bike_id)
        if bike:
            if not bike.is_available:
                bike.is_available = True
                return f"Returned bike with ID {bike_id}"
            else:
                return f"Bike with ID {bike_id} is already available."
        else:
            return f"Bike with ID {bike_id} does not exist in our inventory."

    def get_bike(self, bike_id):
        for bike in self.inventory:
            if bike.bike_id == bike_id:
                return bike
        return None

    def display_inventory(self):
        return [{"bike_id": bike.bike_id, "status": "Available" if bike.is_available else "Rented"} for bike in self.inventory]

# Create some bike objects and add them to the inventory
bike1 = Bike(1)
bike2 = Bike(2)
bike3 = Bike(3)
inventory = [bike1, bike2, bike3]
rental_system = BikeRental(inventory)

@app.route('/')
def home():
    return render_template('index.html', inventory=rental_system.display_inventory())

@app.route('/rent', methods=['POST'])
def rent():
    bike_id = int(request.form['bike_id'])
    message = rental_system.rent_bike(bike_id)
    return message

@app.route('/return', methods=['POST'])
def return_bike():
    bike_id = int(request.form['bike_id'])
    message = rental_system.return_bike(bike_id)
    return message

if __name__ == "__main__":
    app.run(debug=True)
