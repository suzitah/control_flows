def calculate_discount(price,discount_percent):
    price=float(price)
    discount_percent=float(discount_percent)

    if discount_percent>=20:
        price=price*0.8
        return price
    else:
        return price

new_price=input("Please enter the original price: ")
discount=input("please enter the discount given: ")
discounted_price= calculate_discount(new_price,discount)
print("The discounted price is",discounted_price)