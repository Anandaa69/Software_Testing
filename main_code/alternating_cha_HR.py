def alternatingCharacters(s):
    result = 0
    for i in range(len(s)):
        if i+1 < len(s) and s[i] == s[i+1]:
            result += 1
    return result