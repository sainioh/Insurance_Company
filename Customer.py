import uuid


# Represents the customer of the car insurance company
class Customer:
    def __init__(self, name, address):
        self.ID = str(uuid.uuid1())
        self.name = name
        self.address = address
        self.cars = []  # List of cars
        self.claims = []  # list of claims
        self.payments = []


    def addCar(self, car):
        self.cars.append(car)


    def addClaim(self, claim):
        self.claims.append(claim)


    def addPayment(self, payment):
        self.payments.append(payment)

    def getClaims(self):
        return list(self.claims)


    def getPayments(self):
        return list(self.payments)


    # convert object o JSON
    def serialize(self):

        return {
            'id': self.ID,
            'name': self.name,
            'address': self.address,
            'cars': [{'name':h.name, 'number_plate': h.number_plate, 'motor_power': h.motor_power, 'year': h.year} for h in self.cars]
        }


class Car:
    def __init__(self, model_name, number_plate, motor_power, year):
        self.name = model_name
        self.number_plate = number_plate
        self.motor_power = motor_power
        self.year = year