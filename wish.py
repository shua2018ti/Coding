def is_palindrome(s):
    return s == s[::-1]

def count_palindromic_substrings(s):
    palindromes = 0
    for idx1 in range(len(s) + 1):
        for idx2 in range(idx1):
            if is_palindrome(s[idx2:idx1]):
                palindromes += 1
    return palindromes