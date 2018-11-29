_, string = raw_input(), raw_input()
start, end, res = 0, 0, 0
for char in string:
    if char == "G": start += 1
    else: end, start = start, 0
    res = max(res, start + end + 1)
print min(res, string.count("G"))
