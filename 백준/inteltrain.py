p = 0
a = []
for i in range(0,10):
    b = (input())
    t = b.split(" ")
    p += int(t[1]) - int(t[0])
    a.append(p)
print(max(a))
