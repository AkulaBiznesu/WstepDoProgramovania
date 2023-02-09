#2.1
s = ["hello", "my", "friend"]
d = {s.index(i) : len(i) for i in s}

for i in reversed(d):
    print(i)

n = len(s)
for i in range(n):
    for j in range(i+1,n):
        if len(s[i]) < len(s[j]):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

print(d, s)