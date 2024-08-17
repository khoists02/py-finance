from datetime import datetime

# '%d-%m-%Y'
def format_date_from_timestamp(timestamp: str, date_format: str):
    date = datetime.fromtimestamp(int(timestamp) / 1e3)
    return date.strftime(date_format)