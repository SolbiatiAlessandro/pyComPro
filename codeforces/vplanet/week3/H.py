"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(n, W, B, X, quantities, costs):
    prev = [[W, W]]
    for i in xrange(n):
        prev = map(lambda pc: [min(pc[0]+X, pc[1]), pc[1]], prev)
        prev_height, curr_height = 0, 0
        curr_subtract = [-costs[i] * level for level in xrange(quantities[i] + 1)]
        curr = [[W, W]]

        for _ in xrange(len(prev) - 1 + quantities[i]):
            if prev_height + 1 == len(prev):
                curr_height += 1
            elif curr_height == quantities[i]:
                prev_height += 1
            else:
                increase_prev_val = prev[prev_height + 1][0] + curr_subtract[curr_height]
                increase_curr_val = prev[prev_height][0] + curr_subtract[curr_height + 1]
                if increase_curr_val > increase_prev_val:
                    curr_height += 1
                else:
                    prev_height += 1

            points = prev[prev_height][0] + curr_subtract[curr_height]
            capacity = prev[prev_height][1] + B
            if points >= 0:
                curr.append([points, capacity])
            else:
                break

        prev = curr

    return len(prev) - 1
            

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, W, B, X = stdin()
    quantities = stdin()
    costs = stdin()
    print solve(n, W, B, X,quantities,costs)
