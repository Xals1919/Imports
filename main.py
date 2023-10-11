from datetime import date

from emoji import emojize

from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    pass
    calculate_salary()
    get_employees()
    print(date.today())
    print(emojize('Python is :grinning_face:'))
