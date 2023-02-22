import datetime
from dateutil.relativedelta import relativedelta
from src.utils.constants import DATE_FORMAT, RENEWAL_REMINDER_BEFORE_SUBSCRIPTION_EXPIRED_IN_DAYS


def validate_date(date) -> bool:
    date_string = date
    try:
        datetime.datetime.strptime(date_string, DATE_FORMAT)
        return True
    except ValueError:
        return False


def get_renewal_reminder_date(date, timedelta_in_months) -> str:
    try:
        date_object = datetime.datetime.strptime(date, DATE_FORMAT).date()
        new_date = date_object + relativedelta(months=timedelta_in_months) - relativedelta(
            days=RENEWAL_REMINDER_BEFORE_SUBSCRIPTION_EXPIRED_IN_DAYS)
        return new_date.strftime(DATE_FORMAT)
        # return str(new_date)
    except ValueError:
        return ""


if __name__ == '__main__':
    print(get_renewal_reminder_date("05-02-2022", 5))