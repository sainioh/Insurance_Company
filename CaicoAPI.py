from flask import Flask, request, jsonify
from InsuranceCompany import *
from Customer import *
from Claim import *
from Payment import *

app = Flask(__name__)

# Root object for the insurance company
company = InsuranceCompany("Be-Safe Insurance Company")


# Add a new customer (parameters: name, address).
@app.route("/customer", methods=["POST"])
def addCustomer():
    # parameters are passed in the body of the request
    cid = company.addCustomer(request.args.get('name'), request.args.get('address'))
    return jsonify(f"Added a new customer with ID {cid}")


# Return the details of a customer of the given customer_id.
@app.route("/customer/<customer_id>", methods=["GET"])
def customerInfo(customer_id):
    c = company.getCustomerById(customer_id)
    if (c != None):
        return jsonify(c.serialize())
    return jsonify(
        success=False,
        message="Customer not found")


# Add a new car (parameters: model, numberplate).
@app.route("/customer/<customer_id>/car", methods=["POST"])
def addCar(customer_id):
    c = company.getCustomerById(customer_id)
    if (c != None):
        car = Car(request.args.get('model'), request.args.get('number_plate'), request.args.get('motor_power'), request.args.get('year'))
        c.addCar(car)
    return jsonify(
        success=c != None,
        message="Customer not found")



@app.route("/customer/<customer_id>", methods=["DELETE"])
def deleteCustomer(customer_id):
    result = company.deleteCustomer(customer_id)
    if (result):
        message = f"Customer with id{customer_id} was deleted"
    else:
        message = "Customer not found"
    return jsonify(
        success=result,
        message=message)



@app.route("/customers", methods=["GET"])
def allCustomers():
    return jsonify(customers=[h.serialize() for h in company.getCustomers()])




# ----------------AGENTS ---------------------



# Add a new Agent (parameters: name, address).
@app.route("/agent", methods=["POST"])
def addAgent():
    # parameters are passed in the body of the request
    a_id = company.addAgent(request.args.get('name'), request.args.get('address'))
    return jsonify(f"Added a new Agent with ID {a_id}")



@app.route("/agents", methods=["GET"])
def allAgents():
    '''
    Gets the serialized information of agents from list of all agents
    :return:
    '''
    return jsonify(agents=[h.serialize() for h in company.getAgents()])



@app.route("/agent/<agent_id>", methods=["GET"])
def agentInfo(agent_id):
    '''
    Gets the corresponding Agent information based on the parameter agent_id.
    :param agent_id:
    :return:
    '''
    a = company.getAgentById(agent_id)
    if (a != None):
        return jsonify(a.serialize())
    return jsonify(
        success=False,
        message="Customer not found")



@app.route("/agent/<agent_id>/<customer_id>", methods=["POST"])
def assignCustomertoAgent(agent_id, customer_id):
    '''
    Assigns created customer to agent who will be representing that customer by calling method Customer method
    "addCustomertoAgent()".
    :param agent_id:
    :param customer_id:
    :return:
    '''
    c = company.getCustomerById(customer_id)
    a = company.getAgentById(agent_id)

    if (c != None and a != None):
        a.addCustomertoAgent(c)

    return jsonify(agents=[h.serialize() for h in company.getAgents()])  # REMOVE AFTER TEST



@app.route("/agent/<agent_id>", methods=["DELETE"])
def deleteAgent(agent_id):
    '''
    Deletes agent by calling InsuranceCompany method "deleteAgent", where the agents all customers will be transferred
    to the agent who has been working in the company longest (first in list of agents).
    :param agent_id:
    :return:
    '''
    result = company.deleteAgent(agent_id)
    if (result):
        message = f"Customer with id{agent_id} was deleted"
    else:
        message = "Agent not found"
    return jsonify(
        success=result,
        message=message)



# ----------------CLAIMS---------------------



@app.route("/claims/<customer_id>/file", methods=["POST"])
def addClaim(customer_id):
    '''
    Creates new Claim object and adds it to both InsuranceCompany list of all claims and the corresponding
    Customer-objects list of claims.
    :param customer_id:
    :return:
    '''
    c = company.getCustomerById(customer_id)
    if (c != None):
        claim = Claim(request.args.get('date'), request.args.get('incident_description'), request.args.get('claim_amount'))
        c.addClaim(claim)
        company.addClaim(claim)
    return jsonify(
        success=c != None,
        message="Customer not found")



@app.route("/claims/<claim_id>", methods=["GET"])
def claimInfo(claim_id):
    '''
    Gets information on single Claim object based on the claim_id.
    '''
    cl = company.getClaimById(claim_id)
    if (cl != None):
        return jsonify(cl.serialize())
    return jsonify(
        success=False,
        message="Claim not found")



@app.route("/claims", methods=["GET"])
def allClaims():
    '''
    Serializes all claims stored in InsuranceCompany class and calling method "getClaims()"
    :return:
    '''
    return jsonify(claims=[cl.serialize() for cl in company.getClaims()])



@app.route("/claims/<claim_id>/status", methods=["PUT"])
def putClaimStatus(claim_id):
    '''
    Adds status to the claim with claim_id. Calls Claim method "changeStatus()" to choose which status to apply.
    :param claim_id: generated id of the claim
    :return:
    '''
    cl = company.getClaimById(claim_id)
    covered = request.args.get('approved_amount')
    if (cl != None):
        cl.changeStatus(covered)    # Sets certain status based on approved_amount

    return jsonify(
        success=False,
        message="Claim not found")



# ----------------PAYMENTS---------------------



@app.route("/payment/in", methods=["POST"])
def addPaymentIn():
    '''
    Adds an in-payment made by customer. For making statistical analysis simpler the payment class is added to both
    InsuranceCompany list of all payments and the payment list of Customer class.
    '''

    payment = InPayment(request.args.get('date'), request.args.get('customer_id'), request.args.get('amount_received'))

    p = company.getCustomerById(payment.customer_id)    #get customer object by given id
    if (p != None):
        p.addPayment(payment)
        company.addPayment(payment)
    return jsonify(
        success= p != None)



@app.route("/payment/out", methods=["POST"])
def addPaymentOut():
    '''
    Adds an out-payment to an Agent. For making statistical analysis simpler the payment class is added to both
    InsuranceCompany list of all payments and the payment list of Agent class.
    I was not sure whether amount sent was supposed to be calculated or if it is
    an output of the program user.
    '''

    payment = OutPayment(request.args.get('date'), request.args.get('agent_id'), request.args.get('amount_sent'))

    p = company.getAgentById(payment.agent_id)
    if (p != None):
        p.addPayment(payment)
        company.addPayment(payment)
    return jsonify(
        success= p != None)



@app.route("/payments", methods=["GET"])
def allPayments():
    '''
    Serializes all the company payments stored inside InsuranceCompany class
    '''
    return jsonify(payments=[cl.serialize() for cl in company.getPayments()])



# ----------------STATS---------------------



@app.route("/stats/claims", methods=["GET"])
def allClaimsByAgent():
    '''

    Calls InsuranceCompany method "getClaimsPerAgent()" which serializes, together with Agent method "claim_serialize()",
    the list of all claims grouped by each agent.

    '''
    return jsonify(ClaimsByAgent = company.getClaimsPerAgent())



@app.route("/stats/revenues", methods=["GET"])
def allRevenues():

    '''
    Calls InsuranceCompany method "getRevenue()" which serializes, together with Agent method "revenue_serialize()",
    the list of all in-payments grouped by each agent.
    '''

    return jsonify(revenueByAgent = company.getRevenue())



@app.route("/stats/agents", methods=["GET"])
def allAgentsPerformance():

    '''
    Calculates the performance metric for agents by calling InsuranceCompany method "getAgentPerformance".
    '''

    return jsonify(agentPerformance = company.getAgentPerformance())




###DO NOT CHANGE CODE BELOW THIS LINE ##############################
@app.route("/")
def index():
    return jsonify(
        success=True,
        message="Your server is running! Welcome to the Insurance Company API.")


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers[
        'Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE"
    return response


if __name__ == "__main__":
    app.run(debug=True, port=5000)