import uuid
import numpy as np


# Represents the insurance agent
class Agent:
    def __init__(self, name, address):
        self.ID= str(uuid.uuid1())
        self.name = name
        self.address = address
        self.customers = []
        self.payments = []

    # convert object o JSON
    def serialize(self):
        return {
            'id': self.ID,
            'name': self.name,
            'address': self.address,
            'customers': [h.serialize() for h in self.customers]
        }

    #
    def addCustomertoAgent(self, customer):
        self.customers.append(customer)

    def addPayment(self, payment):
        self.payments.append(payment)

    def getCustomers(self):
        return list(self.customers)

    def calculatePerformance(self):
        '''
        Takes the difference between each agents customers sum of payments and the approved claim amounts.
        Result is then p
        '''


        customerpayments_sum = sum([float(p.amount_received) for h in self.customers for p in h.getPayments()])
        customerclaims_sum =  sum([float(cl.amount_covered) for h in self.customers for cl in h.getClaims()])

        total = customerpayments_sum - customerclaims_sum

        if total < 1:
            total = 1

        return self, np.log10(total)


    # serialize for listing all claims per agent
    def claim_serialize(self):
        return {
            'agent_id': self.ID,
            'claims': [cl.serialize() for h in self.customers for cl in h.getClaims()]
        }


    # serialize for calculated revenue
    def revenue_serialize(self):
        return {
            'agent_id': self.ID,
            'payments': [cl.serialize() for h in self.customers for cl in h.getPayments()]
        }


    # serialize for ranking of agents
    def performance_serialize(self, metric):
        return {
            'agent_id': self.ID,
            'name': self.name,
            'performance_metric': metric
        }

