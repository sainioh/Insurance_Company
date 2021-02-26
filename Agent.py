import uuid
# Represents the insurance agent
class Agent:
    def __init__(self, name, address):
        self.ID= str(uuid.uuid1())
        self.name = name
        self.address = address

    # convert object o JSON
    def serialize(self):
        return {
            'id': self.ID,
            'name': self.name,
            'address': self.address
        }