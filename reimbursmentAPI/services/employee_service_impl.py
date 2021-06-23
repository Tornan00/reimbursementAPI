from daos.employee_dao import EmployeeDAO
from entities.employee import Employee
from services.employee_service import EmployeeService

class EmployeeServiceImpl(EmployeeService):

    def __init__(self, employee_dao: EmployeeDAO):
        self.employee_dao = employee_dao

    def retrieve_all_employees(self):
        return self.employee_dao.get_all_employees()

    def retrieve_employee_by_id(self, employee_id):
        return self.employee_dao.get_employee_by_id(employee_id)

    def login_as_employee(self, username: str, password: str):
        employees = self.employee_dao.get_all_employees()
        logged = None
        for employee in employees:
            if employee.username == username:
                if employee.password == password:
                    logged = employee
        return logged