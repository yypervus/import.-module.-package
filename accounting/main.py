from datetime import datetime
from accounting.application.salary import calculate_salary
from application.people import get_employees


def main():
    print(datetime.now().strftime('%d.%m.%Y'))
    calculate_salary()
    get_employees()

if __name__ == '__main__':
    main()