from collections import defaultdict
from datetime import datetime, date, timedelta


def get_day_today():
    date = datetime.today().date()
    return date.strftime("%A")


def get_day_of_week_from_date(input_date):
    return input_date.strftime("%A")


def get_datetime_from_input(year, month, day):
    return datetime(year=int(year), month=int(month), day=int(day))


def delta_days(month, day):
    diff = (datetime(year=datetime.today().year, month=month, day=day) - datetime.today()).days+1
    return diff


def print_join_defaultdict_by_comma_space(defdict):
    for x, y in defdict.items():
        print(f"{x}: {', '.join(y)}")


data = [
    {
        "name": "Bill Gates",
        "birthday": datetime(1955, 12, 9)
    },
    {
        "name": "Volodymyr Zelensky",
        "birthday": datetime(1975, 12, 8)
    },
    {
        "name": "Jeff Bezos",
        "birthday": datetime(1955, 12, 5)
    },
    {
        "name": "Olha Tomilina",
        "birthday": datetime(1955, 12, 5)
    },
    {
        "name": "Yeva Kitun",
        "birthday": datetime(2013, 10, 28)
    }
]


def get_birthdays_per_week(users):
    this_week_birthdays = defaultdict(list)
    for user in users:
        current_user_birthday = user["birthday"]
        current_user_name = user["name"]
        current_user_birthday_month = current_user_birthday.month
        current_user_birthday_day = current_user_birthday.day

        user_delta = delta_days(current_user_birthday_month, current_user_birthday_day)
        if 7 > user_delta >= 0:
            if get_day_of_week_from_date(get_datetime_from_input(datetime.today().year, datetime.today().month, datetime.today().day + user_delta)) == 'Saturday':
                user_delta += 2
            elif get_day_of_week_from_date(get_datetime_from_input(datetime.today().year, datetime.today().month, datetime.today().day + user_delta)) == 'Sunday':
                user_delta += 1
            next_birthday = get_day_of_week_from_date(get_datetime_from_input(datetime.today().year, datetime.today().month, datetime.today().day + user_delta))
            this_week_birthdays[next_birthday].append(current_user_name)

    return this_week_birthdays


if __name__ == '__main__':
    congratulate_these = get_birthdays_per_week(data)
    print_join_defaultdict_by_comma_space(congratulate_these)
