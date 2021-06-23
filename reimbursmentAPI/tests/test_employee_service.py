from daos.employee_dao import EmployeeDAO
from daos.employee_dao_postgres import EmployeeDAOPostgres
from entities.employee import Employee
from services.employee_service import EmployeeService
from services.employee_service_impl import EmployeeServiceImpl

employee_dao: EmployeeDAO = EmployeeDAOPostgres()
employee_service: EmployeeService = EmployeeServiceImpl(employee_dao)

def test_login_as_employee():
    employee = employee_service.login_as_employee("jimmyjim", "1234")
    assert employee.first_name == "Jim"