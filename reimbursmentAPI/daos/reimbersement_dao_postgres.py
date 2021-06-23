from typing import List
from daos.reimbersement_dao import ReimbursementDAO
from entities.reimbursement import Reimbursement
from utils.connection_util import connection

class ReimbursementDAOPostgres(ReimbursementDAO):
    def create_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = """insert into reimbursement values (default, %s, %s, %s, %s, %s, %s, %s) returning r_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.credits, reimbursement.category, reimbursement.description, reimbursement.approved, reimbursement.reason, reimbursement.m_id, reimbursement.e_id))
        connection.commit()
        r_id = cursor.fetchone()[0]
        reimbursement.r_id = r_id
        return reimbursement

    def get_reimbursement_by_id(self, r_id: int) -> Reimbursement:
        sql = """select * from reimbursement where r_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [r_id])
        record = cursor.fetchone()
        if record is None:
            return None
        else:
            return Reimbursement(*record)

    def get_all_reimbursements(self) -> List[Reimbursement]:
        sql = """select * from reimbursement"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        return [Reimbursement(*record) for record in records]

    def get_all_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursement]:
        sql = """select * from reimbursement where e_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        records = cursor.fetchall()
        return [Reimbursement(*record) for record in records ]

    def get_all_pending_reimbursements(self) -> List[Reimbursement]:
        sql = """select * from reimbursement where m_id IS NULL"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        return [Reimbursement(*record) for record in records]

    def get_all_past_reimbursements(self) -> List[Reimbursement]:
        sql = """select * from reimbursement where m_id IS NOT NULL"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        return [Reimbursement(*record) for record in records]

    def update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = """update reimbursement set credits = %s, category = %s, description = %s, approved = %s, reason = %s, m_id = %s, e_id = %s where r_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.credits, reimbursement.category, reimbursement.description, reimbursement.approved, reimbursement.reason, reimbursement.m_id, reimbursement.e_id, reimbursement.r_id))
        connection.commit()
        return reimbursement

    def delete_reimbursement(self, r_id: int) -> bool:
        sql = """delete from reimbursement where r_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [r_id])
        connection.commit()
        return True