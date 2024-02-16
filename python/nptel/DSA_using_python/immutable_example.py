def update(l, i, v):
    if i <= 0 and i < len(l):
        l[i] = v
        print("True")
    else:
        v = v + 1
        print(v)
        print("False")


ns = [3, 11, 12]
z = 8
update(ns, 2, z)
x = ["slithy",[7,10,12],2,"tove",1]
y = x[0:50]
print(y)
print(y[2])
x[1][0] = 5555
print(x[1][0])
# a = (x[4][1] == 1)
b = [23,44,87,100]
a = b[1:]
d = b[2:]
c = b
d[0] = 97
c[2] = 77
print(a[1], b[2], c[2], d[0])


def mystery(l):
  l = l[1:]
  return ()

mylist = [7,11,13]
mystery(mylist)
print(mylist)


def isprime(num):
    f = []
    for j in range(1, num + 1):
        if num % j == 0:
            f.append(j)
    if f == [1, num]:
        return True
    else:
        return False


def primeproduct(m):
    factors = []
    value = False
    for i in range(1, m+1):
        if m % i == 0:
            factors.append(i)
            for k in range(0, len(factors)):
                for l in range(0, len(factors)):
                    if factors[l] * factors[k] == m:
                        if isprime(factors[l]) == True and isprime(factors[k]) == True:
                            value = True
                            return value
                            
    return value



print(primeproduct(6))

def delchar(s, c):
    if len(c) > 1:
        return s
    s = s.replace(c, "")
    return s


def isprime(num):
    f = []
    for j in range(1, num + 1):
        if num % j == 0:
            f.append(j)
    if f == [1, num]:
        return True
    else:
        return False


def primeproduct(m):
    factors = []
    for i in range(1, m):
        if m % i == 0:
            factors.append(i)
            for k in range(0, len(factors)):
                for l in range(0, len(factors)):
                    if factors[l] * factors[k] == m:
                        if isprime(factors[l]) and isprime(factors[k]):
                            return True
                            break

    return False


def delchar(s, c):
    if len(c) > 1:
        return s
    s = s.replace(c, "")
    return s


def shuffle(l1, l2):
    new_list = []
    min_len = min(len(l1), len(l2))
    for i in range(min_len):
        new_list.append(l1[i])
        new_list.append(l2[i])
    if len(l1) > len(l2):
        new_list.extend(l1[min_len:])
    else:
        new_list.extend(l2[min_len:])
    return new_list

startmsg = "python"
endmsg = ""
for i in range(1,1+len(startmsg)):
    endmsg = startmsg[-i] + endmsg
print(endmsg)