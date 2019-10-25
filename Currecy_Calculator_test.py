# Testing the functionality of Currecy_Calculator using pytest
import requests

from Currecy_Calculator import CurrecyCalculator

cc = CurrecyCalculator()
rate = requests.get("https://api.exchangeratesapi.io/latest")
datarate = rate.json()
pln = datarate['rates']['PLN']
usd = datarate['rates']['USD']


def test_currecycalculator_initialization():
    assert cc


def test_api():
    assert cc.PLN == pln


def test_euro_to_pln():
    assert cc.euro_to_pln(20) == pln * 20


def test_pln_to_euro():
    assert cc.pln_to_euro(25) == 25 / pln


def test_euro_to_usd():
    assert cc.euro_to_usd(18) == usd * 18


def test_usd_to_euro():
    assert cc.usd_to_euro(5) == 5 / usd


def test_pln_to_usd():
    assert cc.pln_to_usd(168) == 168 / pln * usd


def test_usd_to_pln():
    assert cc.usd_to_pln(245) == 245 / usd * pln
