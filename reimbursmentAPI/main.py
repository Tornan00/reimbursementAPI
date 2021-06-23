from flask import Flask, request, jsonify
import logging
from flask_cors import CORS
from daos.employee_dao_postgres import EmployeeDAOPostgres
from daos.reimbersement_dao_postgres import ReimbursementDAOPostgres
from entities.reimbursement import Reimbursement
from services.employee_service_impl import EmployeeServiceImpl
from services.reimbursement_service_impl import ReimbursementServiceImpl

app: Flask = Flask(__name__)
CORS(app)
logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(message)s')

employee_dao = EmployeeDAOPostgres()
reimbursement_dao = ReimbursementDAOPostgres()
employee_service = EmployeeServiceImpl(employee_dao)
reimbursement_service = ReimbursementServiceImpl(reimbursement_dao, employee_dao)

@app.route("/employees", methods = ["GET"])
def get_all_employees():
    employees = employee_service.retrieve_all_employees()
    json_employees = [e.as_json_dict() for e in employees]
    return jsonify(json_employees)

@app.route("/employees/<employee_id>", methods = ["GET"])
def get_employee_by_id(employee_id: str):
    employee = employee_service.retrieve_employee_by_id(int(employee_id))
    if employee is None:
        return "An employee with the given id could not be found", 404
    return jsonify(employee.as_json_dict())

@app.route("/employees/login", methods = ["GET"])
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    employee = employee_service.login_as_employee(username, password)
    if employee is None:
        return "An employee with the given id could not be found", 404
    return jsonify(employee.as_json_dict())

@app.route("/employees/<employee_id>/reimbursements", methods = ["POST"])
def create_reimbursement(employee_id: str):
    employee = employee_service.retrieve_employee_by_id(int(employee_id))
    if employee is None:
        return "An employee with the given id could not be found", 404

    body = request.get_json()
    reimbursement = Reimbursement(body["rId"], body["credits"], body["category"], body["description"], body["approved"], body["reason"], body["mId"], body["eId"])
    reimbursement_service.add_reimbursement(reimbursement)
    return f"Created reimbursement with id {reimbursement.r_id}", 201

@app.route("/employees/<employee_id>/reimbursements", methods = ["GET"])
def get_all_reimbursements(employee_id: str):
    employee = employee_service.retrieve_employee_by_id(int(employee_id))
    if employee is None:
        return "An employee with the given id could not be found", 404

    reimbursements = reimbursement_service.retrieve_all_reimbursements()
    json_reimbursements = [r.as_json_dict() for r in reimbursements]
    return jsonify(json_reimbursements)

@app.route("/employees/<employee_id>/reimbursements/past", methods = ["GET"])
def get_all_past_reimbursements(employee_id: str):
    employee = employee_service.retrieve_employee_by_id(int(employee_id))
    if employee is None:
        return "An employee with the given id could not be found", 404

    reimbursements = reimbursement_service.retrieve_all_past_reimbursements()
    json_reimbursements = [r.as_json_dict() for r in reimbursements]
    return jsonify(json_reimbursements)

@app.route("/employees/<employee_id>/reimbursements/pending", methods = ["GET"])
def get_all_pending_reimbursements(employee_id: str):
    employee = employee_service.retrieve_employee_by_id(int(employee_id))
    if employee is None:
        return "An employee with the given id could not be found", 404

    reimbursements = reimbursement_service.retrieve_all_pending_reimbursements()
    json_reimbursements = [r.as_json_dict() for r in reimbursements]
    return jsonify(json_reimbursements)

@app.route("/employees/<employee_id>/reimbursements/<r_id>", methods = ["GET"])
def get_reimbursement_by_id(employee_id: str, r_id: str):
    employee = employee_service.retrieve_employee_by_id(int(employee_id))
    if employee is None:
        return "An employee with the given id could not be found", 404

    reimbursement = reimbursement_service.retrieve_reimbursement_by_id(int(r_id))
    if reimbursement is None:
        return "A reimbursement with the given id could not be found", 404
    return jsonify(reimbursement.as_json_dict())

@app.route("/employees/<employee_id>/reimbursements/employee", methods = ["GET"])
def get_all_reimbursements_by_employee_id(employee_id: str):
    employee = employee_service.retrieve_employee_by_id(int(employee_id))
    if employee is None:
        return "An employee with the given id could not be found", 404

    reimbursements = reimbursement_service.retrieve_all_reimbursements_by_employee_id(employee_id)
    json_reimbursements = [r.as_json_dict() for r in reimbursements]
    return jsonify(json_reimbursements)

@app.route("/employees/<employee_id>/reimbursements/<r_id>", methods = ["PUT"])
def update_reimbursement(employee_id: str, r_id: str):
    employee = employee_service.retrieve_employee_by_id(int(employee_id))
    if employee is None:
        return "An employee with the given id could not be found", 404

    reimbursement = reimbursement_service.retrieve_reimbursement_by_id(int(r_id))
    if reimbursement is None:
        return "A reimbursement with the given id could not be found", 404

    body = request.get_json()
    result = Reimbursement(int(r_id), body["credits"], body["category"], body["description"], body["approved"], body["reason"], body["mId"], body["eId"])
    reimbursement_service.update_reimbursement(result)
    return f"Reimbursement with id {r_id} updated successfully", 201

@app.route("/employees/<employee_id>/reimbursements/<r_id>", methods = ["DELETE"])
def delete_reimbursement(employee_id: str, r_id: str):
    employee = employee_service.retrieve_employee_by_id(int(employee_id))
    if employee is None:
        return "An employee with the given id could not be found", 404

    reimbursement = reimbursement_service.retrieve_reimbursement_by_id(int(r_id))
    if reimbursement is None:
        return "A reimbursement with the given id could not be found", 404

    reimbursement_service.delete_reimbursement(int(r_id))
    return "Deleted Successfully", 205

@app.route("/employees/<employee_id>/reimbursements/stats", methods = ["GET"])
def get_stats(employee_id: str):
    employee = employee_service.retrieve_employee_by_id(int(employee_id))
    if employee is None:
        return "An employee with the given id could not be found", 404

    stats = reimbursement_service.create_stats_table()
    return jsonify(stats)

if __name__ == '__main__':
    app.run()
