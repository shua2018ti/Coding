"""
Given a list of meetings represented as tuples (<START_TIME>, <END_TIME>), schedule the meeting in the minimum number
of rooms.
"""

def schedule_meetings(meetings):
    meetings_sorted = sorted(meetings, key=lambda x: (x[0], x[1]))
    rooms = []
    for meeting in meetings_sorted:
        added = False
        for room in rooms:
            if meeting[0] >= room[-1][1]:
                room.append(meeting)
                added = True
        if not added:
            rooms.append([meeting])
    return (len(rooms), rooms)

print(schedule_meetings([(9, 14), (9, 10), (11, 14), (7, 9), (13, 15)]))