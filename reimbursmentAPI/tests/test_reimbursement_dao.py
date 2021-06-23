from daos.employee_dao import EmployeeDAO
from daos.employee_dao_postgres import EmployeeDAOPostgres
from daos.reimbersement_dao import ReimbursementDAO
from daos.reimbersement_dao_postgres import ReimbursementDAOPostgres
from entities.reimbursement import Reimbursement

employee_dao: EmployeeDAO = EmployeeDAOPostgres()
reimbursement_dao: ReimbursementDAO = ReimbursementDAOPostgres()

test_reimbursement = Reimbursement(0, 1000, 1, "Fuel for travel to Terminus System", False, None, None, 4)
test_approved = Reimbursement(0, 10, 2, "Ramen Noodles on the Citadel", True, "", 1, 4)

def test_create_reimbursement():
    reimbursement_dao.create_reimbursement(test_reimbursement)
    assert test_reimbursement.r_id != 0

def test_get_reimbursement_by_id():
    reimbursement = reimbursement_dao.get_reimbursement_by_id(test_reimbursement.r_id)
    assert reimbursement.reason == test_reimbursement.reason

def test_get_all_reimbursements():
    reimbursement_dao.create_reimbursement(test_approved)
    reimbursements = reimbursement_dao.get_all_reimbursements()
    assert len(reimbursements) >= 2

def test_get_all_reimbursements_by_employee_id():
    reimbursements = reimbursement_dao.get_all_reimbursements_by_employee_id(4)
    assert reimbursements[0].e_id == 4

def test_get_all_pending_reimbursements():
    reimbursements = reimbursement_dao.get_all_pending_reimbursements()
    assert reimbursements[0].m_id is None

def test_get_all_past_reimbursements():
    reimbursements = reimbursement_dao.get_all_past_reimbursements()
    assert reimbursements[0].m_id is not None

def test_update_reimbursement():
    test_reimbursement.credits = 2000
    updated_reimbursement = reimbursement_dao.update_reimbursement(test_reimbursement)
    assert updated_reimbursement.credits == test_reimbursement.credits

def delete_reimbursement():
    result = reimbursement_dao.delete_reimbursement(test_approved.r_id)
    assert result