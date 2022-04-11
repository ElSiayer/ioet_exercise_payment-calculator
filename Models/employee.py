from Models.wage import Wage
from utilities import parse_to_minutes,weekend_rate,weekly_rate,weekend_days


class Employee:
    def __init__(self, name, days_worked):
        self.name = name        
        self.days_worked = days_worked    

    def get_daily_payment(self, wages, day):
        start_aux = day.start
        end_aux = day.end
        pay = 0
        wage_start=0
        for wage in wages:
            if wage.start <= day.start:
                wage_start=wage.start
            if wage_start <= day.start and day.start < wage.end:
                while start_aux < wage.end:
                    if (end_aux - start_aux) >= 59:
                        pay += wage.rate
                    start_aux = start_aux+60            
        return pay

    def get_employee_payment(self):
        payment=0
        for day_worked in self.days_worked:
            wage = parse_wage(weekend_rate if day_worked.day in weekend_days else weekly_rate)
            payment+= self.get_daily_payment(wage,day_worked)
        return payment
    
def parse_wage(raw_wage):
    try:
        hourly_wages = []
        for wage_data in raw_wage:
            start_hour = parse_to_minutes(wage_data[0:2],wage_data[3:5])
            end_hour = parse_to_minutes(wage_data[6:8],wage_data[9:11])
            payment = raw_wage[wage_data]
            wage_aux = Wage(start_hour, end_hour, payment)
            hourly_wages.append(wage_aux)
        return hourly_wages
    except:
        raise ValueError