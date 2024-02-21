def compress(chars):
    n=len(chars)
    s=[chars[0]]
    count=1
    for i in range(1,n):
        if chars[i]!=chars[i-1]:
            if count>1:
                s.append(str(count))
            s.append(chars[i])
            count=1
        else:
            count+=1
    if count>1:
        s.append(str(count))
    result=list(''.join(s))
    chars=result
    print(chars)
    print(len(chars))
    return result








print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))