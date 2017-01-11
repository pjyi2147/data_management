import math
def cal(n,p):
    lst = []
    for x in range(n+1):
        k = math.factorial
        com = k(n)/k(x)/k(n-x)
        r = com * (p ** x) * ((1-p)**(n-x))
        lst.append(r)
    
    return lst

def _value(k,n,p):           #k = # of success n = trial, p = possibility of success
    lst = cal(n,p)
    return lst[k]

def culm(k,n,p,start = 0):
    lst = cal(n,p)
    return sum(lst[start:k+1])

def main():
    order = input().split()
    while order[0] != 'q':
        if order[0] is 'v':
            order = order[1:]
            x, n, p = int(order[0]), int(order[1]), float(order[2])
            if len(order) == 3:
                print(_value(x,n,p))
            else:
                print('Error : not enough attributes')

        elif order[0] is 's':
            order = order[1:]
            if len(order) == 4: 
                x, n, p, start = int(order[0]), int(order[1]), float(order[2]), int(order[3])
                print(culm(x,n,p,start))
            elif len(order) == 3:
                x, n, p = int(order[0]), int(order[1]), float(order[2])
                print(culm(x,n,p))
            else: 
                print('Error: not enough attributes')

        elif order[0] is 'k':
            order = order[1:]
            if len(order) == 4:
                x, n, p, start = int(order[0]), int(order[1]), float(order[2]), int(order[3])
                print(1 - culm(x,n,p,start))
            elif len(order) == 3:
                x, n, p = int(order[0]), int(order[1]), float(order[2])
                print(1 - culm(x,n,p))
            else: 
                print('Error: not enough attributes')

        order = input().split()
main()
