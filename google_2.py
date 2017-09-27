# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    as_array = S.split(":")
    hour = as_array[0]
    minute = increment_with_cap(as_array[1], 60)
    if minute == "00":
        hour = increment_with_cap(hour, 24)
    while not is_valid(S, hour + minute):
        minute = increment_with_cap(minute, 60)
        if minute == "00":
            hour = increment_with_cap(hour, 24)
    return hour + ":" + minute


def increment_with_cap(value, cap):
    value = int(value)
    value += 1
    value = str(value % cap)
    if len(value) < 2:
        value = "0" + value
    return value

def is_valid(original, time):
    for num in time:
        if num not in original:
            return False
    return True