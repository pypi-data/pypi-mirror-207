from pytz import timezone
from datetime import datetime


def get_current_datetime_string(tz_=None):
    if not tz_:
        tz_ = "Asia/Kolkata"
    return datetime.now(timezone(tz_)).strftime("%d-%m-%Y %H:%M:%S")


def get_current_timestamp():
    curr_time = datetime.utcnow()
    return datetime.timestamp(curr_time)
