import math
#x=how many successes we want
#k = The number of successes
#n = the number of choice
#N = the number of the whole thing
def C(n,r):
    f = math.factorial
    return f(n)/f(r)/f(n-r)

def value_hyper(x,k,n,N):
    return C(k,x) * C(N-k,n-x) / C(N,n) 

def sum_hyper(x,k,n,N,start=0):
    total = 0
    for p in range(start, x+1):
        total = total + value_hyper(p,k,n,N)
    return total

def main():
    order = input().split()
    while order[0] != 'q':
        if order[0] is 's':
            order = list(map(int, order[1:]))
            if len(order) is 5:
                print(sum_hyper(order[0], order[1], order[2], order[3], order[4]))
            elif len(order) < 4:
                print("Error: not enough attributes")
            else:
                print(sum_hyper(order[0], order[1], order[2], order[3]))

        elif order[0] is 'v':
            order = list(map(int, order[1:]))
            if len(order) < 4:
                print("Error: not enough attributes")
            else:
                print(value_hyper(order[0], order[1], order[2], order[3]))

        elif order[0] is 'k':
            order = list(map(int, order[1:]))
            if len(order) is 5:
                print(1 - sum_hyper(order[0], order[1], order[2], order[3], order[4]))
            elif len(order) < 4:
                print("Error: not enough attributes")
            else:
                print(1 - sum_hyper(order[0], order[1], order[2], order[3]))
                
        order = input().split()

main()
