import datetime

#creates the headline for the app
def headline():
    print('------------------------')
    print('     BIRTHDAY APP')
    print('------------------------')


#date input
def gather_data():
    year = int(input('What year were you born [YYYY]? '))
    month = int(input('What month were you born [MM]? '))
    day = int(input('What day were you born [DD]? '))
    
    bday = datetime.date(year, month, day)
    return bday

#date difference
def date_difference(date1, date2):
    current_year = datetime.date(date2.year, date1.month, date1.day)
    dt = current_year - date2
    return dt.days

def birthday_message(days):
    if days < 0:
        print('You had your birthday {} days ago.'.format(-days))
    elif days > 0:
        print('Your birthday is in {} days!'.format(days))
    else:
        print('Happy Birthday!!!')

#main function
def main():
    headline()
    birthday = gather_data()
    today = datetime.date.today()
    days = date_difference(birthday, today)
    birthday_message(days)
    
main()