"""
Given an dictionary containing students as keys and an array of students that should come before the
key, flatten this data structure

{
    'A':['B', 'C', 'D'],
    'B':['C', 'D'],
    'C':['D', 'F'],
}

[D, F, C, B, A] <-- front of line
"""

students = {
    'A':set(['B', 'C', 'D']),
    'B':set(['C', 'D']),
    'C':set(['D', 'F']),
}


def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        return 0
    return compare

def compare_students(student_1, student_2):
    if students.get(student_1) is not None and student_2 in students[student_1]:
        return True
    return False

def arrange_students(students):
    uniques = set()
    for key, value in students.items():
        uniques.add(key)
        for item in value:
            uniques.add(item)
    return sorted(list(uniques), cmp=make_comparator(compare_students))

print(arrange_students(students))
