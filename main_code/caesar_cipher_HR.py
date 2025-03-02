import string

def caesarCipher(s, k):
    char_b = string.ascii_lowercase
    char_a = "".join([char_b[(i+k) % 26] for i in range(len(char_b))])
    result = ""
    for i in s:
        if i.isupper():
            result += (char_a[char_b.index(i.lower())]).upper()
        elif i.islower():
            result += char_a[char_b.index(i.lower())]
        else:
            result += i
    return result