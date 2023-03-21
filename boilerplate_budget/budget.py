class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self) -> str:
        name_length = len(self.name)

        start_length = round((30 - name_length) / 2)
        first_line = "*" * start_length + self.name + "*" * (30 - start_length - name_length)

        def line(dictionary):
            len_of_desc = len(dictionary["description"])
            amount_str = str('%.2f' % dictionary["amount"])
            desc = dictionary["description"]

            len_of_amount = len(amount_str)

            if len_of_amount > 7:
                amount_str = amount_str[:7]
                len_of_amount = 7
            if len_of_desc > 23:
                desc = desc[0:23]
                len_of_desc = 23

            the_line = desc + " " * (30 - len_of_amount - len_of_desc) + amount_str
            return the_line

        total_amt = '%.2f' % self.get_balance()

        return first_line + '\n' + '\n'.join(map(
            line, self.ledger)) + '\n' + f'Total: {total_amt}'

    def deposit(self, amount, description=""):
        deposit_object = {"amount": amount, "description": description}
        self.ledger.append(deposit_object)

    def get_balance(self):
        current_balance = 0
        for i in range(len(self.ledger)):
            current_balance += self.ledger[i]["amount"]
        return current_balance

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            withdraw_object = {"amount": -amount, "description": description}
            self.ledger.append(withdraw_object)
            return True
        else:
            return False

    def transfer(self, amount, category):
        if not self.withdraw(amount, f'Transfer to {str(category.name)}'):
            return False
        else:
            category.deposit(amount, f'Transfer from {str(self.name)}')
        return True


def create_spend_chart(categories):
    category_list = []
    spend_amount = []
    total_amount = 0
    for category in categories:
        category_list.append(category.name)

        amount = 0
        for i in category.ledger:
            if i["amount"] < 0:
                amount += abs(i["amount"])
        spend_amount.append(amount)
        total_amount += amount
    percent_amount = [int((((works_amount / total_amount) * 10) // 1) * 10) for works_amount in spend_amount]
    line = "Percentage spent by category\n"

    for value in reversed(range(0, 101, 10)):
        if value == 0:
            string = "  " + str(value) + "|"
        elif value < 100:
            string = " " + str(value) + "|"
        else:
            string = str(value) + "|"
        for i in percent_amount:
            if i >= value:
                string += " o "
            else:
                string += "   "

        line += string + ' \n'

    dash_length = len(spend_amount) * 3 + 1
    line += "    " + "-" * dash_length + '\n'

    longest_str = max(category_list, key=len)
    longest_str_num = len(longest_str)

    for value in range(0, longest_str_num):
        line += "    "
        number = 1
        for category in category_list:

            if len(category) > value:

                line += (" " + category[value] + " ")
                if number == len(category_list):
                    line += " "
            else:
                line += "   "

            number += 1
        line += "\n"
    line = line.rstrip()
    line += "  "

    return line
