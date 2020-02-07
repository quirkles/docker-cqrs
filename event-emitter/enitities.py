from uuid import uuid4

from random import seed, random, choice

seed()

def get_price():
    return round(random() , 2) * 10000

def get_vehicle():
    colors = ['red', 'blue', 'black', 'white', 'yellow', 'orange', 'grey']
    makes = ['mazda', 'hyundai', 'ford', 'kia', 'honda', 'jeep']
    ages = ['one year', 'two year', 'three year', 'ten year']
    conditions = ['perfect', 'good', 'very good', 'ok', 'poor', 'very poor']

    return {
        'description': "{0} old {1} {2} in {3} condition".format(choice(ages), choice(colors), choice(makes), choice(conditions)),
        'id': uuid4()

auction_sites = [
    {
        'name': 'toronto north',
        'id': uuid4(),
    },
    {
        'name': 'toronto south',
        'id': uuid4(),
    },
    {
        'name': 'burlington',
        'id': uuid4(),
    },
    {
        'name': 'vaughn',
        'id': uuid4(),
    },
    {
        'name': 'scarborough',
        'id': uuid4(),
    }
]

users = [
    {
        'name': 'alex',
        'id': uuid4(),
    },
    {
        'name': 'abi',
        'id': uuid4(),
    },
    {
        'name': 'farhan',
        'id': uuid4(),
    },
    {
        'name': 'ricardo',
        'id': uuid4(),
    },
    {
        'name': 'abinaya',
        'id': uuid4(),
    },
    {
        'name': 'masoud',
        'id': uuid4(),
    },
]

def get_live_auction_purchase_event():
    return {
        'vehicle_id': uuid4(),
        'description': get_description(),
        'price': get_price()
    }
print(live_auctions)