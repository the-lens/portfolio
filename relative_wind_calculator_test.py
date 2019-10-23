#Testing the fuctionality of realtive wind calculator
import pytest

from relative_wind_calculator import RelativeWindCalculator

def test_realativewindcalculator_initialization():
    rwc = RelativeWindCalculator()
    assert rwc

def test_number1():
    rwc = RelativeWindCalculator()
    rwc.windcalculator(90,50)
    assert rwc.relative == -40

def test_number2():
    rwc = RelativeWindCalculator()
    rwc.windcalculator(190,230)
    assert rwc.relative == 40

def test_number3():
    rwc = RelativeWindCalculator()
    rwc.windcalculator(0,230)
    assert rwc.relative == -130

def test_letter_wh():
    rwc = RelativeWindCalculator()
    with pytest.raises(Exception):
        rwc.inputnumbers('a',230)

def test_letter_ph():
    rwc = RelativeWindCalculator()
    with pytest.raises(Exception):
        rwc.inputnumbers(230,'ab')

def test_letter_wh_ph():
    rwc = RelativeWindCalculator()
    with pytest.raises(Exception):
        rwc.inputnumbers('xx','ab')

def test_handling():
    rwc = RelativeWindCalculator()
    with pytest.raises(Exception):
        rwc.inputnumbers(440,20)

def test_handling2():
    rwc = RelativeWindCalculator()
    with pytest.raises(Exception):
        rwc.inputnumbers(20,361)

def test_handling3():
    rwc = RelativeWindCalculator()
    with pytest.raises(Exception):
        rwc.inputnumbers(-40,20)

def test_handling4():
    rwc = RelativeWindCalculator()
    with pytest.raises(Exception):
        rwc.inputnumbers(-40,-420)
