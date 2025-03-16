
class Item:

    def __init__(self, timestamp, name, description, image, categoryIDs, price, quantity, meta):
        self.timestamp = timestamp
        self.name = name
        self.description = description
        self.image = image
        self.categoryIDs = categoryIDs
        self.price = price
        self.quantity = quantity
        self.meta = meta
