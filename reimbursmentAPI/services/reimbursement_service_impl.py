from typing import List
from daos.employee_dao import EmployeeDAO
from daos.reimbersement_dao import ReimbursementDAO
from entities.reimbursement import Reimbursement
from services.reimbersement_service import ReimbursementService

class ReimbursementServiceImpl(ReimbursementService):

    def __init__(self, reimbursement_dao: ReimbursementDAO, employee_dao: EmployeeDAO):
        self.reimbursement_dao = reimbursement_dao
        self.employee_dao = employee_dao

    def add_reimbursement(self, reimbursement: Reimbursement):
        return self.reimbursement_dao.create_reimbursement(reimbursement)

    def retrieve_reimbursement_by_id(self, r_id: int):
        return self.reimbursement_dao.get_reimbursement_by_id(r_id)

    def retrieve_all_reimbursements(self):
        return self.reimbursement_dao.get_all_reimbursements()

    def retrieve_all_reimbursements_by_employee_id(self, employee_id: int):
        return self.reimbursement_dao.get_all_reimbursements_by_employee_id(employee_id)

    def retrieve_all_pending_reimbursements(self):
        return self.reimbursement_dao.get_all_pending_reimbursements()

    def retrieve_all_past_reimbursements(self):
        return self.reimbursement_dao.get_all_past_reimbursements()

    def update_reimbursement(self, reimbursement: Reimbursement):
        return self.reimbursement_dao.update_reimbursement(reimbursement)

    def delete_reimbursement(self, r_id: int):
        return self.reimbursement_dao.delete_reimbursement(r_id)

    def create_stats_table(self) -> List[dict]:
        stats = []
        ids = []

        reimbursements = self.reimbursement_dao.get_all_reimbursements()
        employees = self.employee_dao.get_all_employees()
        for employee in employees:
            ids.append((employee.employee_id, str(employee.first_name + " " + employee.last_name), employee.manager))

        for i in ids:
            if not i[2]:
                d = {"name":i[1], '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}
                for reimbursement in reimbursements:
                    if i[0] == reimbursement.e_id:
                        d[str(reimbursement.category)] += reimbursement.credits
                stats.append(d)

        avg = {"name":"Average", '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}
        for x in range(1,9):
            count = 0
            for reimbursement in reimbursements:
                if reimbursement.category == x:
                    avg[str(x)] += reimbursement.credits
                    count += 1
            if count != 0:
                avg[str(x)] = avg[str(x)]/count
            else:
                avg[str(x)] = 0
        stats.append(avg)

        return stats