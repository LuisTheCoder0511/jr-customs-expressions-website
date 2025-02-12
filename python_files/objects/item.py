
class Item:

    def __init__(self, name, description, categoryID, price, quantity, meta):
        self.ID = 0
        self.name = name
        self.description = description
        self.categoryID = categoryID
        self.price = price
        self.quantity = quantity
        self.meta = meta

    def __set_id__(self, ID):
        self.ID = ID
