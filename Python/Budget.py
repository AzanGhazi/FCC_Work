class Category:
    def __init__(self, category):
       self.category = category
       self.ledger = []

    def deposit(self, amount, description=""):
        obj = {"amount": amount, "description": description}
        self.ledger.append(obj)
    
    def withdraw(self, amount, description=""):
        obj = {"amount": -amount, "description": description}
        if self.check_funds( amount):
            self.ledger.append(obj)
            return True
        else:
            return False
    
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance
    
    def transfer(self, amount, budget_cat):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to "+budget_cat.category)
            budget_cat.deposit(amount, "Transfer from "+self.category)
            return True
        return False

    def check_funds(self, amount):
        bal = self.get_balance()
        
        if amount > bal:
            return False
        else:
            return True

    def __str__(self):
        return_str = self.category.center(30, "*") + '\n'
        for item in self.ledger:
            return_str += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"
        return_str += "Total: "+str(self.get_balance())
        return return_str

def create_spend_chart(categories):
    spend = []
    for cat in categories:
        cost = 0
        for item in cat.ledger:
            if item['amount'] < 0:
                cost += abs(item['amount'])
        spend.append(cost)
    total_spend = sum(spend)
    percentage = [i/total_spend * 100 for i in spend]
    
    chart_string = "Percentage spent by category"
    for i in range(100, -1, -10):
        chart_string += "\n" + str(i).rjust(3) + "|"
        for item_per in percentage:
            if item_per > i:
                chart_string += " o "
            else:
                chart_string += "   "
        chart_string += " "
    chart_string += "\n    ----------"
    
    cat_lens = [len(cat.category) for cat in categories]
    max_len = max(cat_lens)
    
    for space in range(max_len):
        chart_string += "\n    "
        for cat in range(len(categories)):
            if space < cat_lens[cat]:
                chart_string += " " + categories[cat].category[space] + " "
            else:
                chart_string += "   "
        chart_string += " "
    print(chart_string)
    return chart_string

