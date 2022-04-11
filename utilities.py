from Models.weekdays import Weekday

days = {
    "SU": Weekday.SUNDAY,
    "MO": Weekday.MONDAY,
    "TU": Weekday.TUESDAY,
    "WE": Weekday.WEDNESDAY,
    "TH": Weekday.THURSDAY,
    "FR": Weekday.FRIDAY,
    "SA": Weekday.SATURDAY    
}

weekend_days = (Weekday.SATURDAY, Weekday.SUNDAY)

weekly_rate = {
    "00:01-09:00": 25,
    "09:01-18:00": 15,
    "18:01-00:00": 20
}

weekend_rate = {
    "00:01-09:00": 30,
    "09:01-18:00": 20,
    "18:01-00:00": 25
}
    
def parse_to_minutes(hour,minute):
    hour_parse=int(hour)*60 + int(minute)
    return 24*60 if hour_parse == 0 else hour_parse
    