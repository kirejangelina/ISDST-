def create_journal(total_lessons):
    if total_lessons <= 0:
        raise ValueError("Количество занятий должно быть положительным")
    return {"lessons": total_lessons, "students": {}}


def add_student(journal, name):
    if name in journal["students"]:
        print(f"Студент '{name}' уже есть в журнале")
        return False
    journal["students"][name] = [None] * journal["lessons"]
    return True


def mark_lesson(journal, name, lesson_index, present):
    if name not in journal["students"]:
        print(f"Студент '{name}' не найден")
        return False
    if not (0 <= lesson_index < journal["lessons"]):
        print(f"Неверный номер занятия: {lesson_index + 1}")
        return False
    journal["students"][name][lesson_index] = present
    return True


def attendance_percent(journal, name):
    marks = journal["students"].get(name)
    if marks is None:
        print(f"Студент '{name}' не найден")
        return 0.0
    marked = [m for m in marks if m is not None]
    if not marked:
        return 0.0
    return 100.0 * sum(1 for m in marked if m) / len(marked)


def group_average_percent(journal):
    if not journal["students"]:
        return 0.0
    percents = [attendance_percent(journal, n) for n in journal["students"]]
    return sum(percents) / len(percents)


def truants(journal, threshold):
    return [
        n for n in journal["students"] if attendance_percent(journal, n) < threshold
    ]


def perfect_attendees(journal):
    result = []
    for name, marks in journal["students"].items():
        marked = [m for m in marks if m is not None]
        if marked and all(marked):
            result.append(name)
    return result


def print_journal(journal):
    if not journal["students"]:
        print("Журнал пуст")
        return
    header = (
        "Студент".ljust(15)
        + " | "
        + " ".join(f"З{i + 1}".rjust(3) for i in range(journal["lessons"]))
        + " | %"
    )
    print(header)
    print("-" * len(header))
    for name, marks in journal["students"].items():
        cells = " ".join(
            (" + " if m is True else " - " if m is False else " . ").rjust(3)
            for m in marks
        )
        print(f"{name:<15} | {cells} | {attendance_percent(journal, name):.1f}")


if __name__ == "__main__":
    journal = create_journal(total_lessons=5)

    for name in ["Иванов", "Петров", "Сидорова", "Козлов"]:
        add_student(journal, name)

    mark_lesson(journal, "Иванов", 0, True)
    mark_lesson(journal, "Петров", 0, True)
    mark_lesson(journal, "Сидорова", 0, True)
    mark_lesson(journal, "Козлов", 0, False)

    mark_lesson(journal, "Иванов", 1, True)
    mark_lesson(journal, "Петров", 1, False)
    mark_lesson(journal, "Сидорова", 1, True)
    mark_lesson(journal, "Козлов", 1, False)

    mark_lesson(journal, "Иванов", 2, True)
    mark_lesson(journal, "Петров", 2, False)
    mark_lesson(journal, "Сидорова", 2, True)
    mark_lesson(journal, "Козлов", 2, True)

    mark_lesson(journal, "Иванов", 3, True)
    mark_lesson(journal, "Петров", 3, True)
    mark_lesson(journal, "Сидорова", 3, True)
    mark_lesson(journal, "Козлов", 3, False)

    print("=== Журнал ===")
    print_journal(journal)

    print(f"\nСредняя посещаемость группы: {group_average_percent(journal):.1f}%")

    print("\nПрогульщики (< 60%):")
    for n in truants(journal, 60):
        print(f"  {n}: {attendance_percent(journal, n):.1f}%")

    print("\nНе пропускали ни одного занятия:")
    for n in perfect_attendees(journal):
        print(f"  {n}")

    print("\n=== Проверка ошибок ===")
    mark_lesson(journal, "Неизвестный", 0, True)
    mark_lesson(journal, "Иванов", 99, True)
    add_student(journal, "Иванов")
