import re
from datetime import datetime
from typing import Dict, Any, Optional

def normalize_news(raw_news: Dict[str, Any]) -> Dict[str, Any]:
    """
    Нормализует запись новости.
    Приводит дату к ISO формату (YYYY-MM-DD), чистит title от лишних пробелов,
    и обрабатывает пустые значения.
    """
    # 1. Нормализация Title
    raw_title = raw_news.get("title", "")
    # Убираем лишние пробелы и переносы строк
    clean_title = re.sub(r'\s+', ' ', str(raw_title)).strip()
    if not clean_title:
        clean_title = "Без названия"

    # 2. Нормализация Date
    raw_date = raw_news.get("date", "")
    clean_date = "1970-01-01" # Дефолтная дата, если битая
    if raw_date:
        # Пробуем распарсить разные форматы
        for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%Y/%m/%d"):
            try:
                parsed_date = datetime.strptime(str(raw_date).strip(), fmt)
                clean_date = parsed_date.strftime("%Y-%m-%d")
                break
            except ValueError:
                continue

    # 3. Нормализация Source
    raw_source = raw_news.get("source", "")
    clean_source = str(raw_source).strip().lower()
    if not clean_source:
        clean_source = "unknown"

    return {
        "title": clean_title,
        "date": clean_date,
        "source": clean_source
    }
