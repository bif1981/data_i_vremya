from datetime import datetime


class SuperDate(datetime):
    Seasons = {
        1: 'Winter',
        2: 'Winter',
        3: 'Spring',
        4: 'Spring',
        5: 'Spring',
        6: 'Summer',
        7: 'Summer',
        8: 'Summer',
        9: 'Autumn',
        10: 'Autumn',
        11: 'Autumn',
        12: 'Winter',
    }

    def get_season(self):
        return self.Seasons[self.month]

    def get_time_of_day(self):
        hour = self.hour
        if 6 <= hour < 12:
            return 'Morning'
        if 12 <= hour < 18:
            return 'Day'
        if 18 <= hour < 0:
            return 'Evening'
        else:
            return 'Night'


print('-------------------')
a = SuperDate(2024, 3, 19, 23)
print(a)
print(a.get_season())
print(a.get_time_of_day())

print('-------------------')

b = SuperDate(2023, 12, 3, 6)
print(b)
print(b.get_season())
print(b.get_time_of_day())
print('-------------------')