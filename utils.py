import datetime


def compare_dates(file_input1, file_input2):
    iso_string1 = file_input1.split(b' ')[0].decode('utf-8')
    iso_string2 = file_input2.split(b' ')[0].decode('utf-8')
    datetime1 = datetime.datetime.fromisoformat(iso_string1)
    datetime2 = datetime.datetime.fromisoformat(iso_string2)
    return datetime1 > datetime2


def is_sorted(file_input):
    length = len(file_input)
    index = 0
    while index and index-1 < length:
        if compare_dates(file_input[index], file_input[index+1]):
            return False
        index += 1
    return True
