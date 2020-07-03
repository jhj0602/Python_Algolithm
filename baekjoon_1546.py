N = int(input())
array=[]
array=list(map(int,input().split()))
maxScore =max(array)
result =0
for i in array:
    result = result+i/maxScore*100
print(result/N)