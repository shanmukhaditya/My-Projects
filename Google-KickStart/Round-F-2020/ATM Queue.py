
T = int(input())

for x in range(1,T+1):
    N1, N2 = map(int,input().split())
    arr = list(map(int,input().split()))
    temp = []
    for i,v in enumerate(arr):
        r = v//N2
        if N2*r == v:
            r -= 1
        temp.append((r,i+1))
        print(temp, v)
    temp.sort()
    print(temp)
    ans = [b for _,b in temp]
    print("Case #{}: ".format(x) + " ".join(list(map(str,ans))))
