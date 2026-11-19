"""
Standard discount: any weight 6%
Seasonal discount: any weight 12%
Weight discount: 10 >= weight 6%
                 weight > 10 18%
"""
from enum import Enum, auto

class DiscountType(Enum):
    STANDARD = auto()
    SEASONAL = auto()
    WEIGHT = auto()


def get_discounted_price(cart_weight, price, discount_type):
    if discount_type == DiscountType.STANDARD:
        rate = 0.06
    elif discount_type == DiscountType.SEASONAL:
        rate = 0.12
    elif discount_type == DiscountType.WEIGHT:
        rate = 0.06 if cart_weight <= 10 else 0.18
    else:
        raise ValueError(f"Unknown discount type: {discount_type}")

    return price * (1 - rate)

print(get_discounted_price(9, 100, DiscountType.WEIGHT))
