def funnyString(s):
    rv_str = s[::-1]
    diff_list_b = list()
    diff_list_a = list()
    for i in range(len(s)):
        if i+1 < len(s):
            diff_list_b.append(abs(ord(s[i])-ord(s[i+1])))        
            diff_list_a.append(abs(ord(rv_str[i])-ord(rv_str[i+1])))

    if diff_list_a == diff_list_b:
        return "Funny"
    elif diff_list_a != diff_list_b:
        return "Not Funny"