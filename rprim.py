ai,bi=map(int,input().split())
h=[]
for i in range(ai,bi+1):
    for j in range(2,i):
        if i%j==0:
            break;
    else:
        h.append(i)
print(len(h))
