# Лабораторная работа 6
# Задача 13: Конвертер единиц (длина/масса)

**Студент:** Кирей А.В.

## Постановка задачи
Набор конверсий с тестами точности (допуск погрешности). CI; CD — публикация справочной таблицы на Pages.

## Как устроен CI/CD
Пайплайн настроен через GitHub Actions (`.github/workflows/ci-cd.yml`).

1. **CI (Continuous Integration):** Запускается при `push` и `pull_request` в `main`. Устанавливает зависимости и запускает тесты `pytest`.
2. **CD (Continuous Deployment):** Если тесты прошли и пуш был в `main`, публикует папку `docs/` на GitHub Pages.

## Как запустить тесты локально
```bash
pip install -r requirements.txt
pytest tests/
