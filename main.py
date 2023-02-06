#Поисках на pypi интересные библиотеки и нашёл полезную ytr установил и опробовал) очень полезно при работе в пайчарме
#когда требуется перевод просто зайти в терминал запустить ytr и переводить необходимые тексты и проверять написание)
#https://pypi.org/project/ytr/

import datetime
from application import salary as salary
from application.db import people as people


if __name__ == '__main__':
    date = datetime.date.today()
    print(date)
    salary.calculate_salary("Test")
    people.get_employees("Test 2")
