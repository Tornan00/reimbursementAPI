from unittest.mock import MagicMock
from daos.employee_dao import EmployeeDAO
from daos.employee_dao_postgres import EmployeeDAOPostgres
from daos.reimbersement_dao import ReimbursementDAO
from daos.reimbersement_dao_postgres import ReimbursementDAOPostgres
from entities.reimbursement import Reimbursement
from entities.employee import Employee
from services.reimbursement_service_impl import ReimbursementServiceImpl

employees = [Employee(1, "James", "Peterson", "", "", False),
             Employee(2, "Shane", "Lawson", "", "", False)]

reimbursements = [Reimbursement(1, 1000, 2, "", False, "", 0, 1),
                  Reimbursement(2, 500, 2, "", False, "", 0, 1),
                  Reimbursement(3, 600, 2, "", False, "", 0, 2),
                  Reimbursement(4, 3000, 3, "", False, "", 0, 2)]

mock_employee_dao = EmployeeDAOPostgres()
mock_reimbursement_dao = ReimbursementDAOPostgres()

mock_employee_dao.get_all_employees = MagicMock(return_value = employees)
mock_reimbursement_dao.get_all_reimbursements = MagicMock(return_value = reimbursements)

reimbursement_service = ReimbursementServiceImpl(mock_reimbursement_dao, mock_employee_dao)

def test_create_stats_table():
    result = reimbursement_service.create_stats_table()
    assert result[0]['2'] == 1500
    assert result[2]['2'] == 700