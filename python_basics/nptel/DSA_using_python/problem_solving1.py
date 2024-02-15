def matched(str):
    counter = 0
    for char in str:
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1
            if counter < 0:
                return False
    if counter == 0:
        return True
    else:
        return False


print(matched("(7)(a"))
print(matched("a)*(?"))


def rotatelist(l, k):
    new_list = l[:]
    if k < 1:
        return new_list
    for __ in range(k): # __ means looping but need no variable
        new_list.append(new_list[0])
        new_list.pop(0)
    return new_list


l = [1, 2, 3, 4, 5]
print(l)
print(rotatelist(l, 3))


def splitsum(l):
    square = 0
    cube = 0
    for i in range(len(l)):
        if l[i] > 0:
            square += pow((l[i]), 2)
        else:
            cube += pow((l[i]), 3)
    hehe = [square, cube]
    return hehe


print(splitsum([1, 3, -5]))
