import sys

def is_word(string):
    return string in {"a", "bcd", "e", "f", "ef"}

def find_words(parent, child):
    if len(child) == 0:
        return [[parent + child]]
    right_words = []
    for i in range(len(child)):
        left = child[:i + 1]
        right = []
        if is_word(left):
            right = find_words(left, child[i + 1:])
        for item in right:
            right_words.append(item)
    if parent is not "":
        for items in right_words:
            items.insert(0, parent)
    return right_words

def drop_spaces():
    string = sys.argv[1]
    if string == "" or len(string) == 1:
        return string
    return find_words("", string)

print(drop_spaces())
