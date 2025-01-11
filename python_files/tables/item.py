def __blueprint__():
    return f'''
        code VARCHAR UNIQUE, 
        name VARCHAR, 
        description VARCHAR, 
        price FLOAT, 
        quantity INTEGER, 
        item_type VARCHAR 
        '''


def __keys__():
    return "code, name, description, price, quantity, item_type"


class Item:

    def __init__(self, code, name, description, price, quantity, item_type):
        self.code = code
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.item_type = item_type

    def __values__(self):
        return self.code, self.name, self.description, self.price, self.quantity, self.item_type

    def __repr__(self):
        return f'<Item> {self.name}'
