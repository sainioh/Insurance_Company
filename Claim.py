import uuid

class Claim:
    def __init__(self, date, incident_description, claim_amount):
        self.date = date
        self.incident_description = incident_description
        self.claim_amount = claim_amount

