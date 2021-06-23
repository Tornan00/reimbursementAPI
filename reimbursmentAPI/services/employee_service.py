from abc import ABC, abstractmethod
from entities.employee import Employee

class EmployeeService(ABC):

    @abstractmethod
    def retrieve_all_employees(self):
        pass

    @abstractmethod
    def retrieve_employee_by_id(self, employee_id):
        pass

    @abstractmethod
    def login_as_employee(self, username: str, password: str):
        pass