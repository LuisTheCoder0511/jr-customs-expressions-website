

def add(data, status):

    name: str = data['name']
    image = data['image']
    price = data['price']
    quantity = data['quantity']

    if len(name) == 0:
        return "name required"
    elif name.isspace():
        return "name empty"
    elif name.__contains__("null"):
        return "name error"

    elif not image:
        return "image required"

    elif not price:
        return "price required"
    elif price == 0:
        return "price free"

    elif not quantity:
        return "quantity required"
    elif quantity == 0:
        return "quantity 0"

    return status
