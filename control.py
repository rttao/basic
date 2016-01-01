# while控制逻辑，生成一个菲波那契序列
a,b = 0,1
while b<1000:
    print(a)
    c=a+b;a=b;b=c

# if, python没有switch case
if b <= 500:
    print("small")
elif b <= 700:
    print("LARGE")
else:
    print("Very large")

if a<=500:
    if b<=500:
        b += a
    elif b <= 700:
        b = b-a
else:
    b = a*b
print(a,b)

# for 循环
count = range(100)
x = 0
for i in count:
  x += i

print(x)