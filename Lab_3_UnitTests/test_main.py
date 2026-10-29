import pytest
from main import mark, attendance_percent, truants, perfect_attendance

def test_mark_new_student():
    data = {}
    mark(data, "Иванов", True)
    assert data == {"Иванов": [True]}

    mark(data, "Иванов", False)
    assert data == {"Иванов": [True, False]}


def test_attendance_percent_valid():
    data = {"Иванов": [True, True, False, True]}  # 3 из 4 = 75%
    assert attendance_percent(data, "Иванов") == 75.0


def test_attendance_percent_zero():
    data = {"Петров": [False, False, False]}
    assert attendance_percent(data, "Петров") == 0.0


def test_attendance_percent_empty():
    with pytest.raises(ValueError):
        attendance_percent({"Сидорова": []}, "Сидорова")
    
    with pytest.raises(ValueError):
        attendance_percent({}, "Неизвестный")


def test_truants():
    data = {
        "Отличник": [True, True, True],      # 100%
        "Хорошист": [True, True, False],     # 66.6%
        "Двоечник": [False, False, True],    # 33.3%
        "Пустой": []                         # Пустой список (пропускается)
    }
    
    assert truants(data, 60.0) == ["Двоечник"]
    
    assert truants(data, 80.0) == ["Двоечник", "Хорошист"]


def test_perfect_attendance():
    data = {
        "Отличник": [True, True],
        "Хорошист": [True, False],
        "Пустой": [],
        "Еще_отличник": [True]
    }
    assert perfect_attendance(data) == ["Еще_отличник", "Отличник"]
