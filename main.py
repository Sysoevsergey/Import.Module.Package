from datetime import datetime
from colorama import init

from application.db.people import get_employees
from application.salary import calculate_salary


def main():
    init(autoreset=True)
    date = datetime.today()
    calculate_salary()
    print(date)
    get_employees()
    print(date)


if __name__ == '__main__':
    main()