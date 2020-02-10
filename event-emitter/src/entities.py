from uuid import uuid4

from random import seed, random, choice

seed()


def get_price():
    return round(random(), 2) * 10000


def get_vehicle():
    colors = ['red', 'blue', 'black', 'white', 'yellow', 'orange', 'grey']
    makes = ['mazda', 'hyundai', 'ford', 'kia', 'honda', 'jeep']
    ages = ['one year', 'two year', 'three year', 'ten year']
    conditions = ['perfect', 'good', 'very good', 'ok', 'poor', 'very poor']

    return {
        'vehicle_description': "{0} old {1} {2} in {3} condition".format(choice(ages), choice(colors), choice(makes),
                                                                         choice(conditions)),
        'vehicle_id': uuid4()
    }


auction_sites = [
    {
        'auction_site': 'toronto north',
        'auction_site_id': uuid4(),
    },
    {
        'auction_site': 'toronto south',
        'auction_site_id': uuid4(),
    },
    {
        'auction_site': 'burlington',
        'auction_site_id': uuid4(),
    },
    {
        'auction_site': 'vaughn',
        'auction_site_id': uuid4(),
    },
    {
        'auction_site': 'scarborough',
        'auction_site_id': uuid4(),
    }
]

online_auction_details = [
    {
        'seller_id': uuid4(),
        'auction_id': uuid4(),
    },
    {
        'seller_id': uuid4(),
        'auction_id': uuid4(),
    },
    {
        'seller_id': uuid4(),
        'auction_id': uuid4(),
    },
    {
        'seller_id': uuid4(),
        'auction_id': uuid4(),
    },
    {
        'seller_id': uuid4(),
        'auction_id': uuid4(),
    }
]

users = [
    {
        'buyer_name': 'alex',
        'buyer_id': uuid4(),
    },
    {
        'buyer_name': 'abi',
        'buyer_id': uuid4(),
    },
    {
        'buyer_name': 'farhan',
        'buyer_id': uuid4(),
    },
    {
        'buyer_name': 'ricardo',
        'buyer_id': uuid4(),
    },
    {
        'buyer_name': 'abinaya',
        'buyer_id': uuid4(),
    },
    {
        'buyer_name': 'masoud',
        'buyer_id': uuid4(),
    },
]

purchases = []


def get_live_auction_purchase_event():
    purchase_data = {
        **get_vehicle(),
        **choice(users),
        **choice(auction_sites),
        'purchase_id': uuid4()
    }

    purchases.append(purchase_data)

    return purchase_data


def get_online_auction_purchase_event():
    purchase_data = {
        **get_vehicle(),
        **choice(users),
        **choice(online_auction_details),
        'purchase_id': uuid4()
    }

    purchases.append(purchase_data)

    return purchase_data


def get_payment_made_event():
    if not len(purchases):
        return False
    else:
        purchase = choice(purchases)
        return {
            'amount': round(random(), 2) * 10,
            'purchase_id': purchase['purchase_id'],
            'user_id': purchase['buyer_id']
        }
