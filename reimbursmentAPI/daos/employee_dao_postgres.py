from typing import List
from daos.employee_dao import EmployeeDAO
from entities.employee import Employee
from utils.connection_util import connection

class EmployeeDAOPostgres(EmployeeDAO):
    def get_employee_by_id(self, employee_id: int) -> Employee:
        sql = """select * from employee where employee_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        record = cursor.fetchone()
        return Employee(*record)

    def get_all_employees(self) -> List[Employee]:
        sql = """select * from employee"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        return [Employee(*record) for record in records]