import uuid

class Claim:
    def __init__(self, date, incident_description, claim_amount):
        self.ID = str(uuid.uuid1())
        self.date = date
        self.incident_description = incident_description
        self.claim_amount = claim_amount
        self.status = 'unprocessed'
        self.amount_covered = 0

    # convert object o JSON
    def serialize(self):
        return {
            'id': self.ID,
            'date': self.date,
            'incident_description': self.incident_description,
            'claim_amount': self.claim_amount,
            'status': self.status,
            'amount_covered': self.amount_covered
        }


    def changeStatus(self, covered):
        '''
        Changes the status of Claim based on the parameter "covered". If it matches the claim amount the status is set
        to "FULLY COVERED", otherwise if covered is lower than claimed amount status is set to "PARTLY COVERED".
        Finally if covered is set to zero, the status is set to "REJECTED".
        Default value for claim status is "unprocessed" and zero for the amount_covered until the agent/company has
        reviewed the claim.
        :param covered:
        :return:
        '''
        covered = int(covered)
        self.amount_covered = covered
        if (covered > 0 and covered < int(self.claim_amount)):
            self.status = "PARTLY COVERED"
        elif (covered >= int(self.claim_amount)):
            self.status = "FULLY COVERED"
        else:
            self.status = "REJECTED"