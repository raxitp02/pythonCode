def isvowel(a):
    """
    Returns True if input character is a vowel, False otherwise
    :param a:
    :return Bool:
    """
    if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
        return True
    elif a == "A" or a == "E" or a == "I" or a == "O" or a == "U":
        return True
    return False

def v_or_c(s):
    """
    checks if vowels or consonants are greater in number in s
    :param s:
    :return:
    """
    if len(s) <= 0:
        return 0
    if len(s) == 1:
        if isvowel(s[0]):
            return 1
        return 0
    else:
        if isvowel(s[0]):
            return 1 + v_or_c(s[1:])
        else:
            return 0 + v_or_c(s[1:])

s = input()
vowels = v_or_c(s)
if vowels > len(s) - vowels:
    print("Vowels")
elif vowels == len(s) - vowels:
    print("Equal")
else:
    print("Consonants")