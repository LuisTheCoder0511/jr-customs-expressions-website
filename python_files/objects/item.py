
class Item:

    def __init__(self, name, description, image, categoryIDs, price, quantity, meta):
        self.ID = 0
        self.name = name
        self.description = description
        self.image = image
        self.categoryIDs = categoryIDs
        self.price = price
        self.quantity = quantity
        self.meta = meta

    def __set_id__(self, ID):
        self.ID = ID
