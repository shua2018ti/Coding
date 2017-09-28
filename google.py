# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S, K):
    final = []
    running_word = []
    for character in S[::-1]:
        if character == "-":
            continue
        running_word.insert(0, character.upper())
        if len(running_word) == K:
            final.insert(0, "".join(running_word))
            running_word = []
    if running_word:
        final.insert(0, "".join(running_word))
    return "-".join(final)
