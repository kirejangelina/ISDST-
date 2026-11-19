import pytest
from converter.units import UnitConverter

def test_length_m_to_cm():
    assert UnitConverter.convert_length(1, 'm', 'cm') == pytest.approx(100.0)

def test_length_inch_to_mm():
    assert UnitConverter.convert_length(1, 'inch', 'mm') == pytest.approx(25.4)

def test_mass_kg_to_g():
    assert UnitConverter.convert_mass(1, 'kg', 'g') == pytest.approx(1000.0)

def test_mass_lb_to_kg():
    assert UnitConverter.convert_mass(1, 'lb', 'kg') == pytest.approx(0.45359237, rel=1e-5)

def test_invalid_unit():
    with pytest.raises(ValueError):
        UnitConverter.convert_length(1, 'm', 'parsec')
