A = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

#No. 6
def binSe(target):
    low = 0
    high = len(A)

    while low < high:
        mid = (high + low) // 2
        if A[mid] == target:
            return "Target pada indeks " + str(mid)
        elif target < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

#No. 7
B = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
def binSe2(target):
    low = 0
    high = len(B)
    x = []

    while low < high:
        if B[low] == target:
            x.append(low)
            low+=1
        else:
            low+=1
    return x

