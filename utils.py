import datetime


def compare_dates(iso_string1,iso_string2):
    datetime1 = datetime.datetime.fromisoformat(iso_string1)
    datetime2 = datetime.datetime.fromisoformat(iso_string2)
    return datetime1 > datetime2
