# main.py
from typing import Dict, List


def mark(attendance: Dict[str, List[bool]], student: str, present: bool) -> None:
    if student not in attendance:
        attendance[student] = []
    attendance[student].append(present)


def attendance_percent(attendance: Dict[str, List[bool]], student: str) -> float:
    marks = attendance.get(student)
    if not marks:
        raise ValueError("no marks")
    return 100.0 * sum(1 for m in marks if m) / len(marks)


def truants(attendance: Dict[str, List[bool]], threshold: float) -> List[str]:
    result = []
    for student, marks in attendance.items():
        if not marks:
            continue
        pct = 100.0 * sum(1 for m in marks if m) / len(marks)
        if pct < threshold:
            result.append(student)
    return sorted(result)


def perfect_attendance(attendance: Dict[str, List[bool]]) -> List[str]:
    return sorted(
        s for s, marks in attendance.items() if marks and all(marks)
    )
