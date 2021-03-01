from Customer import *
from Agent import *


class InsuranceCompany:
    def __init__(self, name):
        self.name = name  # Name of the Insurance company
        self.customers = []  # list of customers
        self.agents = []  # list of dealers

    def getCustomers(self):
        return list(self.customers)

    def addCustomer(self, name, address):
        c = Customer(name, address)
        self.customers.append(c)
        return c.ID

    def addAgent(self, name, address):
        a = Agent(name, address)
        self.agents.append(a)
        return a.ID

    def getCustomerById(self, id_):
        for d in self.customers:
            if (d.ID == id_):
                return d
        return None

    def deleteCustomer(self, customer_id):
        c = self.getCustomerById(customer_id)
        self.customers.remove(c)