import sys
def merge(A, B):
    (C, m, n) = ([], len(A), len(B))
    (i, j) = (0, 0)
    while i + j < m + n:
        if i == m:
            C.append(B[j])
            j = j + 1
        elif j == n:
            C.append(A[i])
            i = i + 1
        elif A[i] <= B[j]:
            C.append(A[i])
            i = i + 1
        elif A[i] > B[j]:
            C.append(B[j])
            j = j + 1
    return C


def mergesort(A, left, right):
    if right - left <= 1:
        return A[left:right]
    if right - left > 1:
        mid = (left + right) // 2
        L = mergesort(A, left, mid)
        R = mergesort(A, mid, right)
        return merge(L, R)


list1 = [43, 32, 22, 78, 63, 57, 91, 13]
print(mergesort(list1, 0, len(list1)))


def quick_sort(A, l, r):
    if r - l <= 1:
        return ()
    yellow = l + 1
    for green in range(l+1, r):
        if A[green] <= A[l]:
            (A[yellow], A[green]) = (A[green], A[yellow])
            yellow = yellow + 1
    (A[l], A[yellow-1]) = (A[yellow-1], A[l])

    quick_sort(A, l, yellow - 1)
    quick_sort(A, yellow, r)


l = list(range(20, 0, -1))
print(l)
sys.setrecursionlimit(10000)
quick_sort(l, 0, len(l))
print(l)
