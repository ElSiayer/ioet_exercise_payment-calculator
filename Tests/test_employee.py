import unittest
import utilities as utility
import config_test as test
from Models.employee import Employee,parse_wage
from Models.day_worked import DayWorked
from app import parse_employee


class TestEmployee(unittest.TestCase):
    def test_get_pay(self):        
        employee_test = Employee("test",[])
        day_test=test.day_worked['day']
        rate = utility.weekend_rate  if day_test in utility.weekend_days else utility.weekly_rate
        start_hour_test=utility.parse_to_minutes(test.day_worked['start'][0:2],test.day_worked['start'][3:5])
        end_hour_test=utility.parse_to_minutes(test.day_worked['end'][0:2],test.day_worked['end'][3:5])
        day_worked_test = DayWorked(day=day_test, start=start_hour_test, end=end_hour_test)       
        wage_test = parse_wage(rate)
        pay = employee_test.get_daily_payment(wages=wage_test, day=day_worked_test)
        self.assertEqual(pay, test.day_worked["pay_amount"], f"Should be {test.day_worked['pay_amount']}")
    

    def test_employee(self):
        testEmployee =parse_employee(test.employee_test["raw"])
        pay = testEmployee.get_employee_payment()
        test_result=f'The amount to pay {testEmployee.name} is: {pay} USD' 
        self.assertEqual(test_result, f'The amount to pay {test.employee_test["name"]} is: {test.employee_test["payment"]} USD',
                         f"Should be 'The amount to pay {test.employee_test['name']} is: {test.employee_test['payment']} USD'")


if __name__ == '__main__':
    unittest.main()
