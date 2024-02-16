from random import *
import csv


class fake:
    """ this class developed by pankaj for creating duplicate employee data .
        employee_name, employee_number, employee_salary, employee_city, employee_phone_number.
        also give a option to save data in txt file...[or]...csv file.....
        thanks for visit........................................................................"""

    def __init__(self):
        self.n = int(input('How many fake employee data you need....'))

    @staticmethod
    def ename():
        op = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        name = ''
        for x in range(randrange(3, 10)):
            name += choice(op)
        return name.capitalize()

    @staticmethod
    def eno():
        en = 'e-'
        e = randrange(1000, 9999)
        return en + str(e)

    @staticmethod
    def esalarry():
        es = float(randrange(10000, 50000))
        return es

    @staticmethod
    def ecity():
        c = ['jaipur', 'Bangalore', 'Hyderabad', 'delhi', 'Chennai']
        return choice(c)

    @staticmethod
    def ephn():
        f = randint(6, 9)
        ph = ''
        for x in range(9):
            ph += str(randint(1, 9))
        a = f'+91 {f}{ph} '
        return a

    def data(self):
        for x in range(self.n):
            print('______________________________________________________________________')
            print(f'employee name : {self.ename()}')
            print(f'employee no : {self.eno()}')
            print(f'employee salary : {self.esalarry()}')
            print(f'employee city : {self.ecity()}')
            print(f'employee mobile no : {self.ephn()}')
            print('______________________________________________________________________')

    def file(self):
        op = input('Do you want to save data in file [yes||no]...').lower()
        while True:
            if op not in ['yes', 'no']:
                while op not in ['yes', 'no']:
                    op = input('choose valid option....')
            if op == 'no':
                print('data only for display...')
                self.data()
                break
            fname = input('In which file you store data [txt || csv]... ')
            if fname == 'csv':
                name = input('enter file name with extension(.csv) in which you store data...')
                with open(name, 'a', newline='') as f:
                    b = csv.writer(f)
                    b.writerow(['employee name :', 'employee no. :', 'employee salary :', 'employee city :',
                                'employee mobile no :'])
                    for x in range(self.n):
                        b.writerow(
                            (self.ename(), self.eno(), self.esalarry(),
                             self.ecity(), self.ephn()))
                    print('Data save successfully check file....')
            if fname == 'txt':
                name = input('enter file name with extension(.txt) in which you store data...')
                with open(name, 'a', ) as f:
                    a = '_'
                    for x in range(self.n):
                        f.write(
                            f'{a * 50}\n employee name :{self.ename()}\n employee no :{self.eno()}\n employee salary :{self.esalarry()}\n'
                            f'employee city : {self.ecity()}\n employee mobile no :{self.ephn()}\n{a * 50}\n')
                    print('Data save successfully check file....')
            p = input('enter y to close file...')
            if p == 'y':
                print('thanks for visit.....')
                break


s = fake()
s.file()

