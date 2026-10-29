class Student:
    def __init__(self, name, lessons):
        self.name = name
        self.marks = [None] * lessons

    def mark(self, lesson_index, present):
        self.marks[lesson_index] = present

    def attendance_percent(self):
        marked = [m for m in self.marks if m is not None]
        if not marked:
            return 0.0
        return 100.0 * sum(1 for m in marked if m) / len(marked)

    def is_perfect(self):
        marked = [m for m in self.marks if m is not None]
        return bool(marked) and all(marked)

    def __str__(self):
        cells = " ".join(
            (" + " if m is True else " - " if m is False else " . ").rjust(3)
            for m in self.marks
        )
        return f"{self.name:<15} | {cells} | {self.attendance_percent():.1f}"


class Journal:
    def __init__(self, total_lessons):
        if total_lessons <= 0:
            raise ValueError("Количество занятий должно быть положительным")
        self.total_lessons = total_lessons
        self.students = {}

    def add_student(self, name):
        if name in self.students:
            print(f"Студент '{name}' уже есть в журнале")
            return False
        self.students[name] = Student(name, self.total_lessons)
        return True

    def mark(self, name, lesson_index, present):
        if name not in self.students:
            print(f"Студент '{name}' не найден")
            return False
        if not (0 <= lesson_index < self.total_lessons):
            print(f"Неверный номер занятия: {lesson_index + 1}")
            return False
        self.students[name].mark(lesson_index, present)
        return True

    def group_average_percent(self):
        if not self.students:
            return 0.0
        percents = [s.attendance_percent() for s in self.students.values()]
        return sum(percents) / len(percents)

    def truants(self, threshold):
        return [s for s in self.students.values() if s.attendance_percent() < threshold]

    def perfect_attendees(self):
        return [s for s in self.students.values() if s.is_perfect()]

    def print_all(self):
        if not self.students:
            print("Журнал пуст")
            return
        header = (
            "Студент".ljust(15)
            + " | "
            + " ".join(f"З{i + 1}".rjust(3) for i in range(self.total_lessons))
            + " | %"
        )
        print(header)
        print("-" * len(header))
        for s in self.students.values():
            print(s)


if __name__ == "__main__":
    journal = Journal(total_lessons=5)

    for name in ["Иванов", "Петров", "Сидорова", "Козлов"]:
        journal.add_student(name)

    journal.mark("Иванов", 0, True)
    journal.mark("Петров", 0, True)
    journal.mark("Сидорова", 0, True)
    journal.mark("Козлов", 0, False)

    journal.mark("Иванов", 1, True)
    journal.mark("Петров", 1, False)
    journal.mark("Сидорова", 1, True)
    journal.mark("Козлов", 1, False)

    journal.mark("Иванов", 2, True)
    journal.mark("Петров", 2, False)
    journal.mark("Сидорова", 2, True)
    journal.mark("Козлов", 2, True)

    journal.mark("Иванов", 3, True)
    journal.mark("Петров", 3, True)
    journal.mark("Сидорова", 3, True)
    journal.mark("Козлов", 3, False)

    print("=== Журнал ===")
    journal.print_all()

    print(f"\nСредняя посещаемость группы: {journal.group_average_percent():.1f}%")

    print("\nПрогульщики (< 60%):")
    for s in journal.truants(60):
        print(f"  {s.name}: {s.attendance_percent():.1f}%")

    print("\nНе пропускали ни одного занятия:")
    for s in journal.perfect_attendees():
        print(f"  {s.name}")

    print("\n=== Проверка ошибок ===")
    journal.mark("Неизвестный", 0, True)
    journal.mark("Иванов", 99, True)
    journal.add_student("Иванов")
