def selection_sort(l):
    for start in range(len(l)):
        min_pos = start
        for i in range(start, len(l)):
            if l[i] < l[min_pos]:
                min_pos = i
        (l[start], l[min_pos]) = (l[min_pos], l[start])


l1 = [1, 6, 5, 9, 12, 4, 33, 29]

selection_sort(l1)
print("Sorted list is:", l1)


def insertion_sort(seq):
    for end in range(len(seq)):
        pos = end
        while pos > 0 and seq[pos-1] > seq[pos]:
            (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
            pos = pos - 1


seq = [4, 8, 5, 7, 2, 6]
insertion_sort(seq)
print("After Insertion Sort:", seq)

