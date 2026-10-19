"""Inheritance, super(), Multiple Inheritance, and Method Resolution Order (MRO)."""


class Employee:
    def __init__(self, emp_id: str, name: str, base_salary: float) -> None:
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def calculate_pay(self) -> float:
        return self.base_salary


class FullTimeEmployee(Employee):
    def __init__(self, emp_id: str, name: str, base_salary: float, annual_bonus: float) -> None:
        super().__init__(emp_id, name, base_salary)
        self.annual_bonus = annual_bonus

    def calculate_pay(self) -> float:
        # Extends base salary with monthly portion of bonus
        return self.base_salary + (self.annual_bonus / 12)


# Demonstrating Multiple Inheritance & Mixins (Common in Django / Flask)
class AuditLogMixin:
    def log_event(self, action: str) -> None:
        print(f"[AUDIT LOG] Action '{action}' triggered for entity.")


class MetricsMixin:
    def record_metric(self, metric_name: str, value: float) -> None:
        print(f"[METRICS] Recorded {metric_name} = {value}")


class AuditedPayrollProcessor(AuditLogMixin, MetricsMixin):
    def process_payroll(self, employee: Employee) -> float:
        payout = employee.calculate_pay()
        self.log_event(f"Payout for {employee.name} ({employee.emp_id})")
        self.record_metric("payroll_payout_amount", payout)
        return payout


if __name__ == "__main__":
    fte = FullTimeEmployee("EMP-001", "Sarah Connor", base_salary=8000.0, annual_bonus=24000.0)
    print(f"Employee {fte.name} monthly pay: ${fte.calculate_pay():.2f}")

    processor = AuditedPayrollProcessor()
    total = processor.process_payroll(fte)
    print(f"Processed total: ${total:.2f}")

    print("\nMethod Resolution Order (MRO) for AuditedPayrollProcessor:")
    for cls in AuditedPayrollProcessor.__mro__:
        print(f" -> {cls.__name__}")
