import unittest
import utilities as utility
from Models.employee import parse_wage
import config_test as test

class TestParse(unittest.TestCase):
    def test_parse_to_minutes(self):
        hour_test=test.time_test["hour_test"]
        minutes_test=utility.parse_to_minutes(hour_test[0:2],hour_test[3:5])
        self.assertEqual(minutes_test, test.time_test["in_minutes"], f"Should be {test.time_test['in_minutes']}")
    
    def test_parse_wage(self):
        wage_test=[]
        for wage in parse_wage(test.wage_test["wage_rate"]):
            wage_test.append(str(wage))
        self.assertEqual(wage_test, test.wage_test["wages_output"], f"Should be {test.wage_test['wages_output']}")

if __name__ == '__main__':
    unittest.main()
