from Customer import *
from Agent import *


class InsuranceCompany:
    def __init__(self, name):
        self.name = name  # Name of the Insurance company
        self.customers = []  # list of customers
        self.agents = []  # list of agents
        self.claims = []   # list of claims
        self.payments = [] # list of payments

    def getCustomers(self):
        return list(self.customers)



    def getAgents(self):
        return list(self.agents)



    def getClaims(self):
        return list(self.claims)



    def getPayments(self):
        return list(self.payments)



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



    def addPayment(self, payment):
        self.payments.append(payment)



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



    def getClaimsPerAgent(self):
        '''
        Gets the list of all Agents, calls the Agent method "claim_serialize()" which goes through each Agents customer
        and their claim.
        :return:  Serialized information of all agents and their customers claims
        '''
        ags = [ag for ag in self.getAgents()]
        claimbyagent = [a.claim_serialize() for a in ags]

        return claimbyagent



    def getRevenue(self):
        '''
        Gets the list of all Agents, calls the Agent method "revenue_serialize()" which gets every Agents customers
        in-payments and serializes the information.
        :return: Serialized information of all agents and their customers in-payments
        '''
        ags = [ag for ag in self.getAgents()]
        revenuebyagent = [a.revenue_serialize() for a in ags]

        return revenuebyagent



    def getAgentPerformance(self):

        '''
            Calls Agent method "calculatePerformance" to get an agent rating, sorts and serializes the agent list so that
            better performing agents are first.
        '''
        performancelist = []
        ags = [ag for ag in self.getAgents()]   # list of all agents

        for a in ags:
            performancelist.append(a.calculatePerformance())    # stores agent object and the rating as tuple

        performancelist = sorted(performancelist, key=lambda x: x[1], reverse=True) # sorts the list descending order
        ranked_agents = [ag[0].performance_serialize(ag[1]) for ag in performancelist]  # serializes each agent

        return ranked_agents



    def deleteCustomer(self, customer_id):
        c = self.getCustomerById(customer_id)
        self.customers.remove(c)



    def deleteAgent(self, agent_id):
        '''
        If agent is deleted, the function moves the agents customers to the agent who has been working in the company
        longest (first position in list of agents).
        :param agent_id:
        :return:
        '''
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
