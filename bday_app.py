import datetime


def print_header():
    print('----------------------')
    print('  Birthday App')
    print('----------------------')


# function for getting user bday
def get_birthday_from_user():
    print('When were you born?')
    year = int(input('YEAR [YYYY]: '))
    month = int(input('MONTH [MM]: '))
    day = int(input('DAY [DD]: '))
    # date time convert it to year, month, day format
    birthday = datetime.date(year, month, day)
    return birthday  # this will be sent back to main function and will be assigned to 'bday'


# function for subtracting your bday and current day
# original_date = bday ; target_date = Today
def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date  # This is to get the number of days
    return (dt.days) # This will only shows the days not the decimal part


# Function for showing how many days before, after or if its your birthday
# days = number_of_days
def print_birthday_information(days):
    if days < 0:
        print('You had your Birthday {} days ago this year'.format(-days))
    elif days > 0:
        print('Your Birthday is in {} days!'.format(days))
    else:
        print('Happy Birthday')


def main():
    # This is to call 'def print_header' function
    print_header()
    # After 'def get_birthday_from_user' function executed and assign return value to 'bday'
    bday = get_birthday_from_user()
    # Today is the target_date
    Today = datetime.date.today()
    # Bday and Today variable will be sent to function 'compute_days_dates'
    number_of_days = compute_days_between_dates(bday, Today)
    # Send number_of_days to function 'print_birthday_of_days'
    print_birthday_information(number_of_days)


main()
