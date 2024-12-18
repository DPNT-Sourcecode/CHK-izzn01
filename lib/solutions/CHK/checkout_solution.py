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
        ],
        'F': [
            (1, 10)
        ],
        'G': [
            (1, 20)
        ],
        'H': [
            (10, 80),
            (5, 45),
            (1, 10)
        ],
        'I': [
            (1, 35)
        ],
        'J': [
            (1, 60)
        ],
        'K': [
            (2, 120),
            (1, 70)
        ],
        'L': [
            (1, 90)
        ],
        'M': [
            (1, 15)
        ],
        'N': [
            (1, 40)
        ],
        'O': [
            (1, 10)
        ],
        'P': [
            (5, 200),
            (1, 50)
        ],
        'Q': [
            (3, 80),
            (1, 30)
        ],
        "R": [
            (1, 50)
        ],
        'S': [
            (1, 20)
        ],
        'T': [
            (1, 20)
        ],
        'U': [
            (1, 40)
        ],
        'V': [
            (3, 130),
            (2, 90),
            (1, 50),
        ],
        'W': [
            (1, 20),
        ],
        'X': [
            (1, 17)
        ],
        'Y': [
            (1, 20)
        ],
        'Z': [
            (1, 21)
        ]
    }

    free_item_map = {
        'B': ('E', 2,),
        'F': ('F', 2,),
        'M': ('N', 3),
        'Q': ('R', 3),
        'U': ('U', 3),
    }

    # ordered by price
    group_offers = [
        'Z', 'Y', 'S', 'T', 'X'
    ]

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
    
    # calculate group offers and adjust prices

    can_claim_offers = sum([items_counter.get(i, 0) for i in group_offers]) // 3
    checkout_balance = can_claim_offers * 45 

    total_offer_claimed = can_claim_offers * 3
    for item in group_offers:
        if total_offer_claimed == 0:
            break
        
        if item in items_counter:
            s_value = min(items_counter[item], total_offer_claimed)
            items_counter[item] = items_counter[item] - s_value
            total_offer_claimed -= s_value

    # calculate price
    for sku, quantity in items_counter.items():
        current_quantity = quantity

        # handle free y if number of x
        if sku in free_item_map:
            needed_sku, needed_quantity = free_item_map[sku]
            if needed_sku != sku:
                current_quantity -= items_counter.get(needed_sku, 0) // needed_quantity
            else:
                # Must of the same free item in the cart
                current_quantity -= items_counter.get(needed_sku, 0) // (needed_quantity + 1)
        
        for price_tier in price_map[sku]:
            quantity_for_cur_price_tier = current_quantity // price_tier[0]
            checkout_balance += price_tier[1] * quantity_for_cur_price_tier
            
            # calculate remaining quantity
            current_quantity -= quantity_for_cur_price_tier * price_tier[0]

    return checkout_balance


