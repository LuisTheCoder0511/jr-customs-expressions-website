
class Cart:

    def __init__(self, ItemIDs):
        self.ID = 0
        self.ItemIDs = ItemIDs

    def __set_id__(self, ID):
        self.ID = ID
