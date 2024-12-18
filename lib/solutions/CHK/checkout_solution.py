# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_map = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    discount = {
        'A': {
            'quantity': 3,
            'amount': 20
        },
        'B': {
            'quantity': 2,
            'amount': 15
        }
    }

    checkout_balance = 0
    checkout_map = {}
    for sku in skus:
        # Handle invalid cases.
        if sku not in skus:
            return -1
        
        checkout_balance += price_map[sku]

        if sku not in checkout_map:
            checkout_map[sku] = 1
        else:
            checkout_map[sku] += 1
    
    #Apply discount
    for sku, c_quantity in checkout_map.items():
        if sku in discount and c_quantity >= discount[sku]["quantity"]:
            checkout_balance = checkout_balance - (c_quantity // discount[sku]["quantity"] * discount[sku]["amount"])
    
    return checkout_balance





