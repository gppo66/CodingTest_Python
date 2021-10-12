a = int(input())
b = (input())

s = b.split(" ")
if a == len(s):
    s = [int (i) for i in s]
    s.sort()
    answer = str(s[0]) + " " + str(s[len(s)-1])
    print(answer)


