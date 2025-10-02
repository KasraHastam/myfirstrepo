def total_package(cart, prices):
    total_price = 0
    for item in  cart:
        count = cart[item]
        product_price = prices[item]
        total_price = total_price + (count * product_price)
        return total_price
    
    cart = {"Apple": 3 , "Banana": 5 , "Orange": 2}
    prices = {"Apple": 1.5 , "Banana": 0.5 , "Orange": 1.25}

    print("Your total is: ", total_package(cart , prices))