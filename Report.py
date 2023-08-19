

class Report:

    def __init__(self, attr):
        self.is_sum_higher_then_norm = attr['norm']
        self.is_work_on_sunday = attr['sunday']
        self.overtime = attr['overtime']
        self.is_too_short_break = attr['breaks']
        self.norm_limit = attr['norm_limit']

    def print_report(self):
        print('------------------------------------------------------------')
        print('Raport z przebiegu walidacji:')
        print('------------------------------------------------------------')

        # First requirement
        if self.is_sum_higher_then_norm:
            print('1. Suma przepracowanych godzin w miesiącu przekracza normę (ponad ' + str(self.norm_limit) + 'h).')
        else:
            print('1. Suma przepracowanych godzin w miesiącu nie przekracza normy (mniej niż ' + str(self.norm_limit) + 'h).')

        # Second requirement
        if self.is_work_on_sunday:
            print('2. Została zaplanowana praca na niedziele.')
        else:
            print('2. Nie została zaplanowana praca na niedziele.')

        # Third requirement
        print('3. Liczba nadgodzin w miesiącu: ' + str(self.overtime))

        # Fourth requirement
        if self.is_too_short_break:
            print('4. W ciągu miesiąca zaplanowano zbyt krótkie przerwy między dniami pracy (krótsze niż 11h).')
        else:
            print('4. W ciągu miesiąca zaplanowano odpowiednie przerwy między dniami pracy (dłuższe bądź równe 11h).')
