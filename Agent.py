import uuid


# Represents the insurance agent
class Agent:
    def __init__(self, name, address):
        self.ID= str(uuid.uuid1())
        self.name = name
        self.address = address
        self.customers = []

    # convert object o JSON
    def serialize(self):
        return {
            'id': self.ID,
            'name': self.name,
            'address': self.address,
            'customers': [{'name': h.name} for h in self.customers]
        }

    def addCustomertoAgent(self, customer):
        self.customers.append(customer)
        return None

