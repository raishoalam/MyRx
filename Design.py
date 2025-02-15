from dataclasses import dataclass
from typing import List
from datetime import date

@dataclass(frozen=True)
class Address:
    street: str
    city: str

@dataclass(frozen=True)
class Employee:
    name: str
    id: str
    dateOfJoining: date
    addresses: List[Address]

# Example usage
addresses = [Address("123 Street", "City"), Address("456 Avenue", "Town")]
employee = Employee("John Doe", "E123", date(2020, 1, 1), addresses)
print(employee)
