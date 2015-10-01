"""This file should have our melon-type classes in it."""

class MelonOrder(object):
    species = None
    color = None
    imported = None
    shape = None
    seasons = []

    def get_base_price(self):
        """Calculate price, given a number of melons ordered."""

        base_price = 5.00
        return base_price


class WatermelonOrder(MelonOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        
        base_price = self.get_base_price()

        total = base_price * qty   # TODO, calculate the real amount!

        if self.imported == True:
            total *= 1.5

        if self.shape == "square":
            total *= 2

        if qty >= 3:
            total *= 0.75

        return total


class CantaloupeOrder(MelonOrder):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_price = self.get_base_price()

        total = base_price * qty   # TODO, calculate the real amount!

        if self.imported == True:
            total *= 1.5

        if self.shape == "square":
            total *= 2

        if qty >= 5:
            total *= 0.50

        return total


class CasabaOrder(MelonOrder):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_price = self.get_base_price() + 1.00
        total = base_price * qty   # TODO, calculate the real amount!

        if self.imported == True:
            total *= 1.5

        if self.shape == "square":
            total *= 2

        return total

class SharlynOrder(MelonOrder):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_price = self.get_base_price()

        total = base_price * qty   # TODO, calculate the real amount!

        if self.imported == True:
            total *= 1.5

        if self.shape == "square":
            total *= 2

        return total


class SantaClausOrder(MelonOrder):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_price = self.get_base_price()

        total = base_price * qty   # TODO, calculate the real amount!

        if self.imported == True:
            total *= 1.5

        if self.shape == "square":
            total *= 2

        return total


class ChristmasOrder(MelonOrder):
    species = "ChristmasOrder"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_price = self.get_base_price()

        total = base_price * qty   # TODO, calculate the real amount!

        if self.imported == True:
            total *= 1.5

        if self.shape == "square":
            total *= 2

        return total


class HornedMelonOrder(MelonOrder):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_price = self.get_base_price()

        total = base_price * qty   # TODO, calculate the real amount!

        if self.imported == True:
            total *= 1.5

        if self.shape == "square":
            total *= 2

        return total


class XiguaOrder(MelonOrder):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_price = self.get_base_price()

        total = base_price * qty   # TODO, calculate the real amount!

        if self.imported == True:
            total *= 1.5

        if self.shape == "square":
            total *= 2

        return total


class OgenOrder(MelonOrder):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        base_price = self.get_base_price() + 1.00
        total = base_price * qty   # TODO, calculate the real amount!

        if self.imported == True:
            total *= 1.5

        if self.shape == "square":
            total *= 2

        return total