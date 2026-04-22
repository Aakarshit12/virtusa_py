class Expense:
    def __init__(self,date,category,amt,desc):
        self.date=date
        self.category=category
        self.amount=amt
        self.description=desc
    def to_dict(self):
        return {
            'date': self.date,
            'category': self.category,
            'amount': self.amount,
            'description': self.description
        }
    def __str__(self):
        return "[" + self.date + "] " + self.category + " - Rs." + str(self.amount)