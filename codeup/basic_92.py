# codeup basic 1094

n = int(input())
l = list(map(int, input().split()))

for i in range(len(l)-1, -1, -1):
    print(l[i], end= ' ')