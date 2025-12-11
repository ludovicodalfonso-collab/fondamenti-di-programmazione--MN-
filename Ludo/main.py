def f(n):
    if n <= 1: return n
    if n % 2 == 0: return f(n//2)
    return 1 + f(n-1)
vals = [15, 10, 5, 8]
out = []
s = 0
for v in vals:
    r = f(v)
    out.append((v, r))
    s += r
print(out)
print(s)