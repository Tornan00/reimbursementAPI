
class Employee:

    def __init__(self, employee_id: int, first_name: str, last_name: str, username: str, password: str, manager: bool):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.manager = manager

    def __str__(self):
        return f"id: {self.employee_id}, name: {self.first_name} {self.last_name}, username: {self.username}, password: {self.password}, manager: {self.manager}"

    def as_json_dict(self):
        return {
            "employeeId":self.employee_id,
            "firstName":self.first_name,
            "lastName":self.last_name,
            "username":self.username,
            "password":self.password,
            "manager":self.manager
        }