import sys

n = int(input())
T, C = map(int, sys.stdin.readline().strip().split())

Ts = []
Cs = []
for _ in range(n):
    _T, _C = map(int, sys.stdin.readline().strip().split())
    Ts.append(_T)
    Cs.append(_C)

result = None
if all(map(lambda t: t == T, Ts)):
    result = T
elif min(Ts) > T:
    t = min(Ts)
    if C >= sum([_c * (t - _t) / (T - t) for _t, _c in zip(Ts, Cs)]):
        result = t
elif max(Ts) < T:
    t = max(Ts)
    if C >= sum([_c * (t - _t) / (T - t) for _t, _c in zip(Ts, Cs)]):
        total_t, total_c = T*C, C
        for _t, _c in zip(Ts, Cs):
            total_t += _t * _c
            total_c += _c
        result = (total_t) / total_c
if result:
    print("Possible\n%.4f" % (result))
else:
    print("Impossible")