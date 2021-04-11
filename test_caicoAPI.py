import pytest
from CaicoAPI import *
from InsuranceCompany import *
from Customer import *
from Claim import *
from Payment import *
from Agent import *

@pytest.fixture
def customers():
    return [Customer("Customer A", "street A"), Customer("Customer B", "street B"), Customer("Customer C", "street C")]

@pytest.fixture
def agents():
    return [Agent("Agent X", "street X"), Customer("Agent Y", "street Y"), Agent("Agent Z", "street Z")]

def test_addCustomertoAgent(customers, agents):
    c1 = customers[0]
    a1 = agents[0]

    assert c1 not in a1.customers
    a1.addCustomertoAgent(c1)
    assert c1 in a1.customers

