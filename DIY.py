def digitCounts( k, n):
# write your code here
    return ''.join(map(str,range(n+1))).count(str(k))


print(digitCounts(1,15))
