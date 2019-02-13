"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(start_values, neighbs):
    answers = [-1 for _ in xrange(len(start_values))]
    def construct(node, parent):
        local_neighbs = neighbs[node]
        if len(local_neighbs) == 1:
            answers[node] = start_values[node]
        else:
            top1, top2 = 0, 0
            for child in local_neighbs:
                if child[0] != parent:
                    construct(child[0], node)
                    value = start_values[child[0]] - child[1]
                    if value > top1:
                        top2 = top1
                        top1 = value
                    elif value > top2:
                        top2 = value
            answers[node] = top1 + top2 + start_values[node]
            start_values[node] += top1
    construct(0, -1)
    return max(answers)


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = int(raw_input())
    start_values = stdin()
    neighbs = [[] for _ in xrange(n)]
    for _ in xrange(len(start_values) - 1):
        u, v, c = stdin()
        neighbs[u-1].append((v-1, c))
        neighbs[v-1].append((u-1, c))
    print solve(start_values, neighbs)
