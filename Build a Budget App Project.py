class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0.0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.balance

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            description = entry["description"][:23]
            amount = f"{entry['amount']:.2f}"[:7]
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.balance:.2f}"
        return title + items + total


def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    spendings = []

    for category in categories:
        total_spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spendings.append(total_spent)

    total = sum(spendings)
    percentages = [int(spending / total * 100) // 10 * 10 for spending in spendings]

    chart = ""
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "|"
        for percent in percentages:
            chart += " o " if percent >= i else "   "
        chart += " \n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)
    padded_names = [name.ljust(max_length) for name in names]

    for i in range(max_length):
        line = "     "
        for name in padded_names:
            line += name[i] + "  "
        if i < max_length - 1:
            line += "\n"
        chart += line

    return title + chart


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")

food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([business, food, entertainment]))