class Bill:

    def __init__(self, amount, month, year):
        self.amount = amount
        self.month = month
        self.year = year


class Flatmate:

    def __init__(self, name, days_in_flat):
        self.name = name
        self.days_in_flat = days_in_flat

    def pays(self, bill_result, flatmate):
        """
        return a bill result for each flatmate
        """
        weight = self.days_in_flat / (flatmate.days_in_flat + self.days_in_flat)
        return round(bill_result * weight, 1)
