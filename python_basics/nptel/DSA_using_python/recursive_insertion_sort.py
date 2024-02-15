import sys
sys.setrecursionlimit(10000)


def insertionSort(seq):
    isort(seq, len(seq))


def isort(seq, k):
    if k > 1:
        isort(seq, k-1)
        insert(seq, k-1)


def insert(seq, k):
    pos = k
    while pos > 0 and seq[pos-1] > seq[pos]:
        (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
        pos = pos - 1


seq = [74, 32, 89, 55, 21, 64]
insertionSort(seq)
print("After Recursive Insertion Sort:", seq)
# because default depth of recursion is less than 1000
l = list(range(1000, 0, -1))
insertionSort(l)
print(l)
