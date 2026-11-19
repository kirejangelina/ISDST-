class UnitConverter:
    LENGTH_FACTORS = {
        'm': 1.0, 'cm': 0.01, 'mm': 0.001, 'km': 1000.0, 'inch': 0.0254, 'ft': 0.3048
    }
    MASS_FACTORS = {
        'kg': 1.0, 'g': 0.001, 'mg': 0.000001, 'lb': 0.45359237, 'oz': 0.028349523125
    }

    @staticmethod
    def convert_length(value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in UnitConverter.LENGTH_FACTORS:
            raise ValueError(f"Неизвестная единица длины: {from_unit}")
        if to_unit not in UnitConverter.LENGTH_FACTORS:
            raise ValueError(f"Неизвестная единица длины: {to_unit}")
        return (value * UnitConverter.LENGTH_FACTORS[from_unit]) / UnitConverter.LENGTH_FACTORS[to_unit]

    @staticmethod
    def convert_mass(value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in UnitConverter.MASS_FACTORS:
            raise ValueError(f"Неизвестная единица массы: {from_unit}")
        if to_unit not in UnitConverter.MASS_FACTORS:
            raise ValueError(f"Неизвестная единица массы: {to_unit}")
        return (value * UnitConverter.MASS_FACTORS[from_unit]) / UnitConverter.MASS_FACTORS[to_unit]
