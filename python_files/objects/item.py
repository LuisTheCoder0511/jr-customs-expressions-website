from python_files.objects.metadata import Metadata


class Item:

    def __init__(self, item_id, name, description, price, quantity, initial_date, metadata: Metadata):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.initial_date = initial_date
        self.metadata = metadata
