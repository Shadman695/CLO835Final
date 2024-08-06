# Example changes to app.py

from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

# Remove or comment out MySQL related code
# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/db_name'
# db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Welcome to the Employee Management System"

@app.route('/addemp', methods=['POST'])
def add_employee():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    primary_skill = request.form['primary_skill']
    location = request.form['location']
    # Comment out database insertion code
    # new_employee = Employee(emp_id=emp_id, first_name=first_name, last_name=last_name, primary_skill=primary_skill, location=location)
    # db.session.add(new_employee)
    # db.session.commit()
    return "Employee successfully added."

@app.route('/getemp', methods=['POST'])
def get_employee():
    emp_id = request.form['emp_id']
    # Comment out database query code
    # employee = Employee.query.filter_by(emp_id=emp_id).first()
    # if employee:
    #     return f"Employee ID:<br>{employee.emp_id}<br>First Name:<br>{employee.first_name}<br>Last Name:<br>{employee.last_name}<br>Primary Skill:<br>{employee.primary_skill}<br>Location:<br>{employee.location}"
    # else:
    #     return "Employee not found."
    return "Employee details fetched (dummy response)."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
