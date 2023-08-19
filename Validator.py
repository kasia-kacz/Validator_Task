

class Validator:

    def __init__(self, month_schedule):
        self.data_to_validate = month_schedule

    def check_if_sum_of_hours_higher_then_norm(self):
        total_sum = self.data_to_validate['Hours'].sum()
        norm = self.count_working_norm()

        if total_sum > norm:
            return True
        else:
            return False

    def check_if_work_on_sunday(self):
        sunday_hours = self.data_to_validate.loc[self.data_to_validate['Weekday'] == 7, 'Hours'].sum()
        if sunday_hours != 0:
            return True
        else:
            return False

    def count_sum_of_overtime(self):
        overtime = 0
        for index, row in self.data_to_validate.iterrows():
            if row.Weekday == 7:
                overtime = overtime + row.Hours
            elif row.Hours > 8:
                overtime = overtime + row.Hours - 8

        return overtime

    def check_if_too_short_break_between_days(self):
        max_work_hours_if_next_day_is_work = 24 - 11
        data = self.data_to_validate[['Day', 'Hours']].copy()
        data['Next'] = data['Hours'].shift(-1).fillna(0)
        data['TooShortBreak'] = data.apply(
            lambda row: row['Hours'] > max_work_hours_if_next_day_is_work and row['Next'] != 0, axis=1)

        return data['TooShortBreak'].any()

    def count_working_norm(self):
        days_number = len(self.data_to_validate[self.data_to_validate["Weekday"] != 7])
        hours_number = 8

        return days_number*hours_number
