def calculate_discounted_price(price, discount):
    try:
        price= float(price)
        discount= float(discount)
        if price < 0 or discount < 0:
            raise ValueError('El precio y el descuento deben ser valores positivos')
    
        result= price -(price * discount)
        return result
    except ValueError:
        raise TypeError('El precio y el descuento deben ser números')

    


result= calculate_discounted_price(-50,'a')

print(result)