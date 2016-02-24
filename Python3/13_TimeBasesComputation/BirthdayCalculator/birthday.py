import logging
from datetime import datetime
from optparse import OptionParser


logging.basicConfig(filename='birthday.log', level=logging.DEBUG)


class InvalidDateFormat(Exception):
    pass


def string_to_date(date):
    """
    Converts 'MM-DD-YYYY' to a date object or throws an InvalidDateFormat
    :param date: a string date
    """
    try:
        # create a datetime object from the date value
        formatter_string = "%m-%d-%Y"
        birthday = datetime.strptime(date, formatter_string)

    except ValueError as e:
        # log the format error then raise it, so it can be handled gracefully
        logging.error(e)
        raise InvalidDateFormat(e)
    return birthday


def birthday_counter(birthday):
    """
    Returns the number of days until your birthday.
    """
    now = datetime.now()
    birthday = string_to_date(birthday)
    # construct the upcoming birthday from this year, your birthday month, and
    # birthday day
    upcoming  = datetime(now.year, birthday.month, birthday.day)



if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-b',
                      '--birthday',
                      dest="birthday",
                      action="store",
                      help="Your birthday in MM-DD-YYYY format")

    (options, args) = parser.parse_args()

    if not options.birthday:
        parser.error("birthday.py requires a date in MM-DD-YYYY format")

    try:
        print(birthday_counter(options.birthday))
    except InvalidDateFormat:
        parser.error("birthday.py requires a date in MM-DD-YYYY format")
