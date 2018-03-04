#basic string compression O(N)
def compress(string):
    ans = []
    cnt = 0
    prev = string[0]
    for char in string:
        if char == prev:
            cnt = cnt + 1;
        else:
            ans.append(prev+str(cnt))
            cnt = 1
            prev = char
    ans.append(prev+str(cnt))
    return ''.join(ans) if len(string) > len(ans) else string
print(compress("abcdeeeeeeef"))
