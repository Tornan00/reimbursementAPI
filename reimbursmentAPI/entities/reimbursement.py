class Reimbursement:

    def __init__(self, r_id: int, credits: int, category: int, description: str, approved: bool, reason: str, m_id: int, e_id: int):
        self.r_id = r_id
        self.credits = credits
        self.category = category
        self.description = description
        self.approved = approved
        self.reason = reason
        self.m_id = m_id
        self.e_id = e_id

    def __str__(self):
        return f"r_id: {self.r_id}, credits: {self.credits}, category = {self.category}, description: {self.description}, approved: {self.approved}, reason: {self.reason}, m_id: {self.m_id}, e_id: {self.e_id}"

    def as_json_dict(self):
        return {
            "rId":self.r_id,
            "credits":self.credits,
            "category":self.category,
            "description":self.description,
            "approved":self.approved,
            "reason":self.reason,
            "mId":self.m_id,
            "eId":self.e_id
        }