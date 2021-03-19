from Customer import *
from Agent import *


class InsuranceCompany:
    def __init__(self, name):
        self.name = name  # Name of the Insurance company
        self.customers = []  # list of customers
        self.agents = []  # list of agents
        self.claims = []   # list of claims

    def getCustomers(self):
        return list(self.customers)

    def getAgents(self):
        return list(self.agents)

    def getClaims(self):
        return list(self.claims)

    def addCustomer(self, name, address):
        c = Customer(name, address)
        self.customers.append(c)
        return c.ID

    def addAgent(self, name, address):
        a = Agent(name, address)
        self.agents.append(a)
        return a.ID

    def addClaim(self, claim):
        self.claims.append(claim)


    def getCustomerById(self, id_):
        for d in self.customers:
            if (d.ID == id_):
                return d
        return None

    def getAgentById(self, id_):
        for d in self.agents:
            if (d.ID == id_):
                return d
        return None

    def getClaimById(self, id_):
        for cl in self.claims:
            if cl.ID == id_:
                return cl


    def deleteCustomer(self, customer_id):
        c = self.getCustomerById(customer_id)
        self.customers.remove(c)

    def deleteAgent(self, agent_id):
        a = self.getAgentById(agent_id)
        if a.customers:
            customerlist = a.customers
            self.agents.remove(a)
            for i in customerlist:
                self.agents[0].addCustomertoAgent(i)
            return True
        else:
            self.agents.remove(a)
            return True

        return False
