from daos.employee_dao import EmployeeDAO
from daos.employee_dao_postgres import EmployeeDAOPostgres
from entities.employee import Employee

employee_dao: EmployeeDAO = EmployeeDAOPostgres()

def test_get_employee_by_id():
    employee = employee_dao.get_employee_by_id(3)
    assert employee.first_name == "Sasha"

def test_get_all_employees():
    employees = employee_dao.get_all_employees()
    assert len(employees) == 4