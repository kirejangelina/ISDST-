import pytest
from parser import normalize_news

def test_normalize_valid_data():
    raw = {"title": "Привет мир", "date": "2023-10-25", "source": "RBC"}
    result = normalize_news(raw)
    assert result["title"] == "Привет мир"
    assert result["date"] == "2023-10-25"
    assert result["source"] == "rbc"

def test_empty_title():
    # Тест на пустой заголовок (требование задания)
    raw = {"title": "   ", "date": "2023-10-25", "source": "Lenta"}
    result = normalize_news(raw)
    assert result["title"] == "Без названия"

def test_broken_date():
    # Тест на битую дату (требование задания)
    raw = {"title": "Новость", "date": "32.13.2023", "source": "TASS"}
    result = normalize_news(raw)
    assert result["date"] == "1970-01-01" # Отдаем дефолт

def test_alternative_date_format():
    # Проверка другого формата даты
    raw = {"title": "Новость", "date": "25.10.2023", "source": "TASS"}
    result = normalize_news(raw)
    assert result["date"] == "2023-10-25"
