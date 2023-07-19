# A=list(map(int,input().split()))
A=[6,8,9]

dic = {}
for i in A:
    dic[i] = 0

for i in A:
    count=2
    for j in range(2,i):
        if i%j==0:
            count+=1
    dic[i] = count

print(dic)
    