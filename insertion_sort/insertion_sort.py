hej = [2,3,3,3,3,3,2,2,2,1,1,1,0,4,5,6,7]
print(hej)

for i in range(len(hej)):
    minsta = hej[i]
    index_tmp = i
    for j in range(i, len(hej)):
        if minsta > hej[j]:
            minsta = hej[j]
            index_tmp = j

    if index_tmp != i:
        tmp = hej[i]
        tmp1 = hej[index_tmp]
        hej[i] = tmp1
        hej[index_tmp] = tmp

print(hej)
