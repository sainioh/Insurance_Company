import uuid


# Using inheritance to support future expansion of different kind of payments for the company

class Payment:
    def __init__(self, date,amount_received):
        self.date = date
        self.amount_received = amount_received




class InPayment(Payment):
    def __init__(self,date,customer_id,amount_received):
        self.date = date
        self.customer_id = customer_id
        self.amount_received = amount_received


    def serialize(self):
        return {
            'date': self.date,
            'customer_id': self.customer_id,
            'amount_received': self.amount_received
        }



class OutPayment(Payment):
    def __init__(self,date,agent_id,amount_sent):
        self.date = date
        self.agent_id = agent_id
        self.amount_sent = amount_sent


    def serialize(self):
        return {
            'date': self.date,
            'agent_id': self.agent_id,
            'amount_sent': self.amount_sent
        }