from src.constants import TIME_FORMAT
from datetime import datetime


def str_to_datetime(date_str, format=TIME_FORMAT):
    date = datetime.strptime(date_str, format)
    return date
