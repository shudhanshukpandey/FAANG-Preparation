"""Aggregation: Weak whole-part relationship where parts survive the destruction of the whole."""

from typing import List


class Professor:
    def __init__(self, emp_id: str, name: str) -> None:
        self.emp_id = emp_id
        self.name = name

    def __repr__(self) -> str:
        return f"Professor({self.name})"


class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.professors: List[Professor] = []

    def add_professor(self, professor: Professor) -> None:
        self.professors.append(professor)

    def list_faculty(self) -> List[str]:
        return [p.name for p in self.professors]


if __name__ == "__main__":
    prof1 = Professor("P-101", "Dr. Turing")
    prof2 = Professor("P-102", "Dr. Hopper")

    cs_dept = Department("Computer Science")
    cs_dept.add_professor(prof1)
    cs_dept.add_professor(prof2)

    print(f"Faculty in {cs_dept.name}: {cs_dept.list_faculty()}")

    # Destroy the department
    del cs_dept
    print("Department destroyed.")

    # In Aggregation, professors survive outside the department
    print(f"Professors still active: {prof1}, {prof2}")
