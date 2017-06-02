"""Classes for melon orders."""
import random

class AbstractMelonOrder(object):
    """docstring for AbstractMelonOrder"""

    def __init__(self, species, qty, order_type, tax):

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_base_price(self):
        base_price = random.choice(range(5,10))
        return base_price * 1.5 if self.species == "Christmas" else base_price

    def get_total(self):
        """Calculate price, including tax."""

        # if self.species == "Christmas":
        #    base_price = 5 * 1.5
        # else:
        #     base_price = 5
        base_price = self.get_base_price()

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(DomesticMelonOrder, self).__init__(species, qty, order_type = "domestic", tax = 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super(InternationalMelonOrder, self).__init__(species, qty, order_type = "international", tax = 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price, including tax."""

        total = super(InternationalMelonOrder, self).get_total()

        fl_fee = 3 if self.qty < 10 else 0 # calculating flax fee if applicable

        return total + fl_fee

class GovernmentMelonOrder(AbstractMelonOrder):
    """docstring for GovernmentMelonOrder"""

    def __init__(self, species, qty):
            """Initialize melon order attributes."""

        super(GovernmentMelonOrder, self).__init__(species, qty, order_type = "government", tax = 0)
 
    passed_inspection = False

    def mark_inspection(self, passed):

        if passed:
            self.passed_inspection = True
