# while控制逻辑，生成一个菲波那契序列
a,b = 0,1
while b<1000:
    print(a)
    c=a+b;a=b;b=c

b=701
# if
if b >= 500:
    print("LARGE")
elif b >= 700:
    print("Very LARGE")
else:
    print("small")

