from __future__ import division, print_function

import sys
from atexit import register

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream


sys.stdin = stream(sys.stdin.read())
input = lambda: sys.stdin.readline().rstrip('\r\n')

sys.stdout = stream()
register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
