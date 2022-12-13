def median(A, B, n):
    m1, m2 = 0, 0
    if(n == 0):
        return 0
    if(n == 2):
        for item in B:
            A.append(item)
        A.sort()
        return A[1]
        # else:
        #     return (A[0] + B[0]) // 2
            
    
    m1 = getMedian(A, n)
    m2 = getMedian(B, n)

    if (m1 == m2):
        return m1
    if (m1 < m2):
        return median(A[n//2 : n], B[0 : n//2 + 1], n - n//2)
    else:
        return median(A[0 : n//2 + 1], B[n//2 : n], n - n//2)


def getMedian(C, n):
    if (n % 2 == 0):
        return (C[n//2 - 1] + C[n//2])//2
    else:
        return C[n//2]

problemas = int(input())
print(problemas)
for i in range(problemas):
    n = int(input())
    A, B = "" , ""
    A = input()
    B = input()
    A = [int(x) for x in A.split()]
    B = [int(x) for x in B.split()]
    print(median(A, B, n))
