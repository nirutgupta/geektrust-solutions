from datetime import datetime
from src.utils.constants import TIME_FORMAT, HOUR_TO_SECONDS, MINUTE_TO_SECONDS


def get_datetime(inp, format=TIME_FORMAT) -> datetime:
    return datetime.strptime(inp, format)


def get_datetime_str(date, format=TIME_FORMAT) -> str:
    return datetime.strftime(date, format)


def convert_seconds_to_minutes(seconds) -> float:
    return seconds/MINUTE_TO_SECONDS


def convert_seconds_to_hours(seconds) -> float:
    return seconds/HOUR_TO_SECONDS
