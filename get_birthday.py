from datetime import datetime

THIS_WEEK_BIRTHDAYS = {'Monday': '', 'Tuesday': '', 'Wednesday': '',
                       'Thursday': '', 'Friday': '', 'Saturday': '', 'Sunday': ''}


def get_birthday_per_week(users):
    current_date = datetime.now().date()
    for user in users:
        user_date = user['birthday'].date()
        current_year_user_data = datetime(
            current_date.year, user_date.month, user_date.day). date()
        date_delta = (current_date - current_year_user_data).days
        day_congratulation = current_year_user_data.weekday()

        if 2 >= date_delta >= 1:
            if day_congratulation in range(5, 7):
                THIS_WEEK_BIRTHDAYS["Monday"] += (user['name']+', ')
        elif date_delta in range(-6, 1):
            THIS_WEEK_BIRTHDAYS[current_year_user_data.strftime(
                '%A')] += (user['name'] + ', ')

    for k, v in THIS_WEEK_BIRTHDAYS.items():
        if len(v) > 0:
            print(f'{k}: {v[:-2]}')


users = [{'name': 'Sasha', 'birthday': datetime(1981, 2, 11)},
         {'name': 'Serhiy', 'birthday': datetime(1990, 2, 12)},
         {'name': 'Katya', 'birthday': datetime(1990, 2, 15)},
         {'name': 'Lena', 'birthday': datetime(1995, 2, 19)},
         {'name': 'Odarka', 'birthday': datetime(1995, 2, 13)},
         {'name': 'Lida', 'birthday': datetime(1991, 3, 12)}]

if __name__ == '__main__':
    get_birthday_per_week(users)
