dic_num =[]
x =1
for i in range(10):
    dic_num = int(input())
    x = x*dic_num
x= str(x)
for i in range(0, 10):
    print(x.count(str(i)))


