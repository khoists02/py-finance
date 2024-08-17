from datetime import datetime


def reverse(lst):
    new_lst = lst[::-1]
    return new_lst


# '%d-%m-%Y'
def format_date_from_timestamp(timestamp: str, date_format: str):
    date = datetime.fromtimestamp(int(timestamp) / 1e3)
    return date.strftime(date_format)
