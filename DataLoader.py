import pandas
import datetime as dt
import calendar


class DataLoader:

    def __init__(self, fname):
        self.filename = fname
        self.year, self.month = self.extract_month_year_from_filename()
        self.month_schedule = self.load_working_hours_data()

    def load_working_hours_data(self):
        df = self.load_csv()
        weekdays = self.month_days_to_week_days(df["Day"].tolist())
        df["Weekday"] = weekdays

        return df

    def load_csv(self):
        try:
            df = pandas.read_csv('./data/'+self.filename, header=0).fillna(0)
        except FileNotFoundError:
            print("File not found.")
        except Exception:
            print("Exception occured while reading CSV file with data.")

        self.check_validity_of_number_of_days_in_month(df)

        return df

    def extract_month_year_from_filename(self):
        filename = self.filename.replace('.csv', '')
        year, month = filename.split('_')

        return int(year), int(month)

    def check_validity_of_number_of_days_in_month(self, df):
        num_of_days_in_month = calendar.monthrange(self.year, self.month)[1]
        if len(df.index) != num_of_days_in_month:
            raise Exception("Number of days in file is invalid for chosen month and year.")

    def month_days_to_week_days(self, month_days):

        return [dt.date(self.year, self.month, int(day)).isoweekday() for day in month_days]
