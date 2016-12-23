import math
def cal(n,p):
    lst = []
    for x in range(n+1):
        k = math.factorial
        com = k(n)/k(x)/k(n-x)
        r = com * (p ** x) * ((1-p)**(n-x))
        lst.append(r)
    
    return lst

def value(k,n,p):           #k = # of success n = trial, p = possibility of success
    lst = cal(n,p)
    return lst[k]

def culm(k,n,p):
    lst = cal(n,p)
    return sum(lst[:k+1])

print(value(3,3,1/3))
print(1-culm(1,7,1/4))

