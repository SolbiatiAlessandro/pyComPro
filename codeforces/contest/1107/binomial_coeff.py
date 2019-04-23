def binomial(n, k):
    if k > n: raise Exception
    if k == 0: return 1
    if k > n/2:
        return binomial(n, n-k)
    return n * binomial(n-1,k-1) / k
if __name__ == "__main__":
    assert binomial(5, 4) == 5
    assert binomial(5, 3) == 10
    assert binomial(5, 1) == 5
    assert binomial(5, 5) == 1
    assert binomial(5, 0) == 1
    from time import time
    t = time()
    assert binomial(123, 56) == 468410292423894497225305443312892167
    print(time()-t)
    print("ok")
