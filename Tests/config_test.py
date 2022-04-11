from  Models.weekdays import Weekday
from Models.wage import Wage

#Using in test_employee.py

day_worked = {
    "day": Weekday.MONDAY,
    "start": '01:00',
    "end": '02:00',
    "pay_amount": 25
}

employee_test = {
    "raw": "test=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00",
    "name": 'test',
    "payment": 215
}

#Using in test_parse.py

time_test = {
    "hour_test": "10:20",
    "in_minutes": 620
}

wage_test = {
    
    "wage_rate": {
        "00:01-09:00": 25,
    },
    "wages_output": [str(Wage(1,540,25))]
}
