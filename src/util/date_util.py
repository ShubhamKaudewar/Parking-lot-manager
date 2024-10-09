import time
from datetime import datetime, date, timedelta


def current_time_in_millis():
    current_milli_time = int(round(time.time() * 1000))
    return current_milli_time


def get_date_in_string_from_millis(date_in_millis):
    date_in_seconds = date_in_millis/1000.0
    return datetime.fromtimestamp(date_in_seconds).strftime('%Y-%m-%d, %H:%M:%S')


def todayEOD():
    d = datetime.now()
    totalSeconds = (datetime(d.year, d.month, d.day, 10, 0, 0) - datetime(1970, 1, 1)).total_seconds()
    return totalSeconds * 1000