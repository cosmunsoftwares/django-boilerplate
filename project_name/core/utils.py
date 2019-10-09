class CPF(object):

    INVALID_CPFS = ['00000000000', '11111111111', '22222222222', '33333333333', '44444444444',
                    '55555555555', '66666666666', '77777777777', '88888888888', '99999999999']

    def __init__(self, cpf):
        self.cpf = cpf

    def validate_size(self):
        cpf = self.cleaning()

        if bool(cpf and (len(cpf) > 11 or len(cpf) < 11)):
            return False

        return True

    def validate(self):
        cpf = self.cleaning()

        if self.validate_size() and cpf not in self.INVALID_CPFS:
            digit_1 = 0
            digit_2 = 0
            i = 0

            while i < 10:
                digit_1 = (digit_1 + (int(cpf[i]) * (11-i-1))) % 11 if i < 9 else digit_1
                digit_2 = (digit_2 + (int(cpf[i]) * (11-i))) % 11
                i += 1

            return ((int(cpf[9]) == (11 - digit_1 if digit_1 > 1 else 0)) and
                    (int(cpf[10]) == (11 - digit_2 if digit_2 > 1 else 0)))

        return False

    def cleaning(self):
        return self.cpf.replace('.', '').replace('-', '') if self.cpf else ''

    def format(self):
        return '%s.%s.%s-%s' % (self.cpf[0:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:11]) if self.cpf else ''


class ZipCode(object):

    def __init__(self, zip_code):
        """
        Class to interact with zip_code brazilian numbers
        """
        self.zip_code = zip_code

    def format(self):
        return '%s-%s' % (self.zip_code[0:5], self.zip_code[5:8]) if self.zip_code else ''

    def cleaning(self):
        return self.zip_code.replace('-', '') if self.zip_code else ''


class Phone(object):

    def __init__(self, phone):
        self.phone = phone

    def cleaning(self):
        if self.phone:
            phone = self.phone.replace('(', '')
            phone = phone.replace(')', '')
            phone = phone.replace('-', '')
            phone = phone.replace(' ', '')
            phone = phone.replace('.', '')
            phone = phone.replace('+', '')

            return phone

        return ''

    def format(self):
        if self.phone:
            if len(self.phone) == 8:
                return '%s.%s' % (self.phone[0:4], self.phone[4:8])
            if len(self.phone) == 9:
                return '%s %s.%s' % (self.phone[0:1], self.phone[1:5], self.phone[5:9])
            if len(self.phone) == 10:
                return '%s %s.%s' % (self.phone[0:2], self.phone[2:6], self.phone[6:10])
            if len(self.phone) == 11:
                return '%s %s%s.%s' % (self.phone[0:2], self.phone[2:3], self.phone[3:7], self.phone[7:11])
            if len(self.phone) == 13:
                return '+%s (%s) %s %s.%s' % (
                    self.phone[0:2],
                    self.phone[2:4],
                    self.phone[4:5],
                    self.phone[5:9],
                    self.phone[9:13]
                )

        return ''


class CNPJ(object):

    def __init__(self, cnpj):
        """
        Class to interact with cnpj brazilian numbers
        """
        self.cnpj = cnpj

    def calculating_digit(self, result):
        result = result % 11
        if result < 2:
            digit = 0
        else:
            digit = 11 - result
        return str(digit)

    def calculating_first_digit(self):
        one_validation_list = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        result = 0
        pos = 0
        for number in self.cnpj:
            try:
                one_validation_list[pos]
            except IndexError:
                break
            result += int(number) * int(one_validation_list[pos])
            pos += 1
        return self.calculating_digit(result)

    def calculating_second_digit(self):
        two_validation_list = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        result = 0
        pos = 0
        for number in self.cnpj:
            try:
                two_validation_list[pos]
            except IndexError:
                break
            result += int(number) * int(two_validation_list[pos])
            pos += 1
        return self.calculating_digit(result)

    def validate(self):
        """
        Method to validate brazilian cnpjs
        """
        self.cnpj = self.cleaning()

        if len(self.cnpj) != 14:
            return False

        checkers = self.cnpj[-2:]

        digit_one = self.calculating_first_digit()
        digit_two = self.calculating_second_digit()

        return bool(checkers == digit_one + digit_two)

    def cleaning(self):
        if self.cnpj:
            return self.cnpj.replace('-', '').replace('.', '').replace('/', '')
        return ''

    def format(self):
        """
        Method to format cnpj numbers.
        """
        if self.cnpj:
            return '%s.%s.%s/%s-%s' % (self.cnpj[0:2], self.cnpj[2:5], self.cnpj[5:8], self.cnpj[8:12],
                                       self.cnpj[12:14])
        return ''
