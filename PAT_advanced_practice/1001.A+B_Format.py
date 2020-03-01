a, b = -1000000, 9

# a, b = map(int, input().split())
ls = []
s = str(abs(a+b))
for i in range(len(s) // 3):
    ls.append(s[-3*i-1:-3*i-4:-1])
if s[-3*(len(s)//3) - 1::-1] != '':
    ls.append(s[-3*(len(s)//3) - 1::-1])
if a+b < 0:
    print('-'+','.join(ls)[::-1])
else:
    print(','.join(ls)[::-1])
