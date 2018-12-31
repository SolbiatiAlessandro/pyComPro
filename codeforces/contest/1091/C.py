"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


import functools
import itertools
import operator


def prime_generator(n):
    """
    Sieve of Eratosthenes
    Create a candidate list within which non-primes will be
    marked as None.
    """    
    cand = [i for i in range(3, n + 1, 2)]
    end = int(n ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * (
                (n // cand[i]) - (n // (2 * cand[i])) - 1)

    # Filter out non-primes and return the list.
    return [2] + [i for i in cand if i]


primes_list = prime_generator(100007)


def factorize(n):
    prime_multiples = []
    for item in primes_list:
        if item > n:
            break
        else:
            while n > 1:
                if n % item == 0:
                    n //= item
                    prime_multiples.append(item)
                else:
                    break
    return prime_multiples


def calculate_divisors(n):
    prime_multiples_list = factorize(n)

    """
    construct unique combinations
    A, B, B, C --> A, B, C, AB, AC, BB, BC, ABC, ABB, BBC
    """
    unique_combinations = set()
    for i in range(1, len(prime_multiples_list)):
        unique_combinations.update(
            set(itertools.combinations(prime_multiples_list, i)))

    # multiply elements of each unique combination
    combination_product = list(functools.reduce(operator.mul, i)
                               for i in unique_combinations)
    combination_product.sort()

    return combination_product

def solve(n):
    divisors = calculate_divisors(n)[::-1]
    def compute(n, k):
        increase = n / k
        return k * (increase - 1) * increase / 2 + increase
    return [1] + [compute(n, divisor) for divisor in divisors] + [compute(n, 1)]

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = int(raw_input())
    res = solve(n)
    for r in res: print r,
