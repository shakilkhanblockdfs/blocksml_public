def getMinDiff(arr, n, k):
    
    result=[]
    for i in arr:
        if k>=i:
            result.append(i+k)
        else:
            result.append(i-k)
    # max = max(result)
    # min - min(result)
    result.sort()
    print(result)
    return result[-1]-result[0]

k = 1
n = 4
arr = [7, 7, 3, 5]
print(getMinDiff(arr, n, k))
