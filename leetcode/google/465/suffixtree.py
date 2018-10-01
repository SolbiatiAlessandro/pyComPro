from collections import defaultdict
def sort_bucket(s, bucket, order):
    d = defaultdict(list) 
    for i in bucket: 
        key = s[i:i+order] 
        d[key].append(i) 
    result = [] 
    for k,v in sorted(d.iteritems()): 
        if len(v) > 1: 
            result += sort_bucket(s, v, order*2) 
        else: 
            result.append(v[0]) 
    return result 

def suffix_array_ManberMyers(s): 
    return sort_bucket(s, (i for i in range(len(s))), 1)
    
def lcp_array(s, sa):
    # http://codeforces.com/blog/entry/12796
    n = len(s)
    k = 0
    lcp = [0] * n
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
        
    for i in range(n):
        if rank[i] == n-1:
            k = 0
            continue
        j = sa[rank[i] + 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k;
        if k:
            k -= 1
            
    return lcp
