from DataLoader import DataLoader
from Report import Report
from Validator import Validator


def main():
    filename = '2023_07.csv'
    data_loader = DataLoader(filename)
    validator = Validator(data_loader.month_schedule)

    norm = validator.check_if_sum_of_hours_higher_then_norm()
    sunday = validator.check_if_work_on_sunday()
    overtime = validator.count_sum_of_overtime()
    breaks = validator.check_if_too_short_break_between_days()

    attr = {'norm': norm, 'sunday': sunday,
            'overtime': overtime, 'breaks': breaks, 'norm_limit': validator.count_working_norm()}
    report_generator = Report(attr)
    report_generator.print_report()


if __name__ == '__main__':
    main()



