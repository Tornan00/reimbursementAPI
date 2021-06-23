from abc import ABC, abstractmethod
from typing import List
from entities.employee import Employee

class EmployeeDAO(ABC):

    @abstractmethod
    def get_employee_by_id(self, employee_id: int) -> Employee:
        pass

    @abstractmethod
    def get_all_employees(self) -> List[Employee]:
        pass