from Models.day_worked import DayWorked
from Models.employee import Employee
from utilities import parse_to_minutes,days

def parse_employee(info):
    try:
        employee_name, date_raw = info.split("=")
        days_worked = []
        for day_raw in date_raw.split(","):
            day = day_raw[0:2]
            start_hour = parse_to_minutes(day_raw[2:4],day_raw[5:7])
            end_hour = parse_to_minutes(day_raw[8:10],day_raw[11:13])
            days_worked.append(DayWorked(days[day], start_hour, end_hour))
        return Employee(employee_name, days_worked)
    except:
        raise ValueError

def main():
    employees = []
    # Read the file with the employees with their work schedule
    with open("employees.txt", "r") as data:
        for line_num, info in enumerate(data):
            try:
                employee_parse = parse_employee(info.strip())                
            except ValueError:
                print(f"\nLine #{line_num + 1} is not valid. Correct syntax is: EMPLOYEE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n")
                raise
            employees.append(employee_parse)
    if len(employees) < 5:
        raise ValueError("At least 5 records are needed in the employees.txt file")
    for employee in employees:
        pay = employee.get_employee_payment()
        print(f"The amount to pay {employee.name} is: {pay} USD")



if __name__ == '__main__':
    main()
