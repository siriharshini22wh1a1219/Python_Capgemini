import logging
logging.basicConfig(
    filename="payroll.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Employee:

    hra_percentage = 20   

    def __init__(self, emp_name, emp_id, basic_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.basic_salary = basic_salary
        self.leaves_taken = 0
        self.net_salary = 0

    def calculate_salary(self):
        hra = (self.basic_salary * Employee.hra_percentage) / 100
        self.net_salary = self.basic_salary + hra
        logging.info("Salary calculated successfully.")

    def apply_leave_deduction(self, leaves):
        self.leaves_taken = leaves
        per_day_salary = self.basic_salary / 30
        deduction = per_day_salary * leaves
        self.net_salary -= deduction
        logging.info("Leave deduction applied.")


    def display_payslip(self):
        logging.info("Employee Name:%s", self.emp_name)
        logging.info("Employee ID:%s", self.emp_id)
        logging.info("Basic Salary:%d", self.basic_salary)
        logging.info("HRA %:%d", Employee.hra_percentage)
        logging.info("Leaves Taken:%d", self.leaves_taken)       
        logging.info("Net Salary:%d", self.net_salary)

    @classmethod
    def update_hra_percentage(cls, new_percentage):
        cls.hra_percentage = new_percentage
        logging.info("HRA percentage updated to:", cls.hra_percentage)

e1 = Employee("Harshini", 101, 50000)

e1.calculate_salary()
e1.apply_leave_deduction(2)
e1.display_payslip()

Employee.update_hra_percentage(25)
