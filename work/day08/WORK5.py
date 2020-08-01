s = input().lower()
w = input().lower()
q = w.split()
t = 1
if s in q:
    k = w.index(s)
    while t:
        if (w[k - 1] == " ") & (w[k + len(s)] == " "):
            t = 0
        else:
            k = w.index(s, k + 1)
    print(str(q.count(s)) + " " + str(k))
else:
    print(-1)
