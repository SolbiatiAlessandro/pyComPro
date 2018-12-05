"""
this is a collections of some interesting templates 
for competitive programming in python(2.x)
"""

"""
- stdin(type_ = "int", sep = " ")
reads from input a string and returns a list of (type_)

e.g.
>>> stdin()
1 2 3 4
>>>[1, 2, 3, 4]
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))

"""
- joint(" ", list(int), list(int), ...,  int, int, ...)
join a generic tuple of list(int) and int together in a string

e.g
>>> joint(" ", [1, 2])
'1 2'
>>> joint(" ", [1, 2], [2, 3])
'1 2 2 3'
"""
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
