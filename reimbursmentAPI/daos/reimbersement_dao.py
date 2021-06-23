from abc import ABC, abstractmethod
from typing import List
from entities.reimbursement import Reimbursement

class ReimbursementDAO(ABC):

    @abstractmethod
    def create_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def get_reimbursement_by_id(self, r_id: int) -> Reimbursement:
        pass

    @abstractmethod
    def get_all_reimbursements(self) -> List[Reimbursement]:
        pass

    @abstractmethod
    def get_all_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def get_all_pending_reimbursements(self) -> List[Reimbursement]:
        pass

    @abstractmethod
    def get_all_past_reimbursements(self) -> List[Reimbursement]:
        pass

    @abstractmethod
    def update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def delete_reimbursement(self, r_id: int) -> bool:
        pass