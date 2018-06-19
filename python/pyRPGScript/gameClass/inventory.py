class Items:
    def __init__(self, name, typeItem, description, deal, qty):
        self.deal = deal
        self.description = description
        self.type = typeItem
        self.name = name
        self.qty = qty

    def take_qty(self, cost):
        self.qty -= cost
        if self.qty < 0:
            self.qty = 0
