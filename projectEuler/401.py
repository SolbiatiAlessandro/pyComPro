def sumsquares(n):
    return (n * (n + 1) * (2*n + 1)) // 6

def main():
    from time import time
    from math import sqrt
    t1 = time()
    N = pow(10, 15)
    chaos_border = int((N**.5) - .00001)
    print(chaos_border)
    chaos_sum = 0
    non_chaos_sum = 0
    for i in range(1, 1 + chaos_border):
        chaos_sum += (N//i)*pow(i, 2) 
    for f in range(int((N**.5) + .00001), 0, -1):
        lo = N//(f+1)
        hi = N//(f)
        local_contribution = f*sumsquares(hi) - f*sumsquares(lo)
        non_chaos_sum += (local_contribution)

    print(non_chaos_sum + chaos_sum)
    print(time() - t1)
main()


def brute(N):
    for d in range(1, N+1):
        print('divisor: ',d,' freq:',N//d,' contribution:',(N//d)*pow(d,2))
