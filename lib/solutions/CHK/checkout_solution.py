# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_map = {
        'A': [
            (5, 200,),
            (3, 130,),
            (1, 50,),
        ],
        'B': [
            (2, 45,),
            (1, 30,)
        ],
        'C': [
            (1, 20)
        ],
        'D': [
            (1, 15)
        ],
        'E': [
            (1, 40)
        ]
    }

    free_item_map = {
        'B': ('E', 2)
    }

    items_counter = {}
    for sku in skus:
        # Handle invalid cases.
        if sku not in price_map:
            return -1
        
        if sku not in items_counter:
            items_counter[sku] = 1
        else:
            items_counter[sku] += 1

    checkout_balance = 0
    
    # calculate price

    for sku, quantity in items_counter.items():
        current_quantity = quantity

        # handle free y if number of x
        if sku in free_item_map:
            needed_sku, needed_quantity = free_item_map[sku]
            current_quantity -= items_counter.get(needed_sku, 0) // needed_quantity
        
        for price_tier in price_map[sku]:
            quantity_for_cur_price_tier = current_quantity // price_tier[0]
            checkout_balance += price_tier[1] * quantity_for_cur_price_tier
            
            # calculate remaining quantity
            current_quantity -= quantity_for_cur_price_tier * price_tier[0]

    return checkout_balance



