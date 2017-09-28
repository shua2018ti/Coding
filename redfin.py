"""
Given a list of meetings represented as tuples (<START_TIME>, <END_TIME>), schedule the meeting in the minimum number
of rooms.
"""

def schedule_meetings(meetings):
    meetings_sorted = sorted(meetings, lambda x: (x[0], x[1]))