from datetime import datetime


def get_days_from_today(date):
    today = datetime.today()
    try:
        datetime_data = datetime.strptime(date, "%Y-%m-%d")
        return (today - datetime_data).days
    except ValueError:
        return "Wrong format of string_date"


print(get_days_from_today("2004-10-15"))
print(get_days_from_today("2024-11-16"))
