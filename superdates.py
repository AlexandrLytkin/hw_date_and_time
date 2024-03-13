import random
from datetime import datetime


class SuperDate(datetime):
    list_season = {(12, 1, 2): 'Winter', range(3, 6): 'Spring', range(6, 10): 'Summer', range(10, 12): 'Autumn'}
    dict_time = {range(6, 12): 'Morning', range(12, 18): 'Day', range(18, 24): 'Evening', range(0, 6): 'Night'}

    def __init__(self, year, month, day, hour):
        self.date = datetime(year, month, day, hour)

    def __check_leap_year(self):
        pass

    def get_season(self):
        for current in self.list_season:
            if self.date.month in current:
                return self.list_season[current]

    def get_time_of_day(self):
        for current in self.dict_time:
            if self.date.hour in current:
                return self.dict_time[current]


if __name__ == '__main__':

    a = SuperDate(2024, 2, 22, 12)

    print(a.get_season())
    print(a.get_time_of_day())
    print(30 * '-')

    try:
        for i in range(1_000):
            n_y = random.randint(1, 2024)
            n_m = random.randint(1, 12)
            n_d = random.randint(1, 28)
            n_h = random.randint(0, 23)
            a = SuperDate(year=n_y, month=n_m, day=n_d, hour=n_h)
            print(a.date)
            print(a.get_season())
            print(a.get_time_of_day())
            print(30 * '-')
    except ValueError as er:
        print(f'Введено не верное число {a.date.day} - {er}')
