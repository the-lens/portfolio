#This program calculate actual currency EUR, USD and PLN. It can be used to convert to all ways form EURO TO PLN or PLN TO USD etc.
#It using a pubic API and REST API technology 
import requests


class CurrecyCalculator(object):

    def __init__(self):
        rate = requests.get("https://api.exchangeratesapi.io/latest")
        datarate = rate.json()
        self.PLN = datarate['rates']['PLN']
        self.USD = datarate['rates']['USD']
        self.EUR = 0
        self.finalprice = 0

    def euro_to_pln(self, euro):
        return self.PLN * euro

    def pln_to_euro(self, pln):
        return pln / self.PLN

    def euro_to_usd(self, usd):
        return self.USD * usd

    def usd_to_euro(self, usd):
        return usd / self.USD

    def pln_to_usd(self, pln):
        return pln / self.PLN * self.USD

    def usd_to_pln(self, usd):
        return usd / self.USD * self.PLN
