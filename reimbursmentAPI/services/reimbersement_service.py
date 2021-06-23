from abc import ABC, abstractmethod
from typing import List

from entities.reimbursement import Reimbursement

class ReimbursementService(ABC):

    @abstractmethod
    def add_reimbursement(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def retrieve_reimbursement_by_id(self, r_id: int):
        pass

    @abstractmethod
    def retrieve_all_reimbursements(self):
        pass

    @abstractmethod
    def retrieve_all_reimbursements_by_employee_id(self, employee_id: int):
        pass

    @abstractmethod
    def retrieve_all_pending_reimbursements(self):
        pass

    @abstractmethod
    def retrieve_all_past_reimbursements(self):
        pass

    @abstractmethod
    def update_reimbursement(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def delete_reimbursement(self, r_id: int):
        pass

    @abstractmethod
    def create_stats_table(self) -> List[dict]:
        pass