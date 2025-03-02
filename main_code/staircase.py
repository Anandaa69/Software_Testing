def staircase(n, dp):
    result = ""
    for i in range(1,n+1):
        result += ((' '*(n-i))+(dp*i)+'\n')
    return result
