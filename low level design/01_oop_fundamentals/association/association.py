"""Association: Peer-to-peer relationship where objects have independent lifecycles."""

from typing import List


class Patient:
    def __init__(self, patient_id: str, name: str) -> None:
        self.patient_id = patient_id
        self.name = name

    def __repr__(self) -> str:
        return f"Patient({self.name})"


class Doctor:
    def __init__(self, doctor_id: str, name: str, specialty: str) -> None:
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.patients: List[Patient] = []

    def consult(self, patient: Patient) -> None:
        self.patients.append(patient)
        print(f"Dr. {self.name} ({self.specialty}) conducted consultation with {patient.name}.")

    def __repr__(self) -> str:
        return f"Doctor(Dr. {self.name})"


if __name__ == "__main__":
    doc = Doctor("DOC-01", "Gregory House", "Diagnostics")
    p1 = Patient("PAT-01", "John Doe")
    p2 = Patient("PAT-02", "Jane Smith")

    doc.consult(p1)
    doc.consult(p2)

    # If the doctor leaves, the patients still exist independently in memory
    print(f"Doctor's patient log: {doc.patients}")
    del doc
    print(f"Patient 1 still exists independently: {p1}")
