# 字符串的操作

str1 = "1234567890"
str2 = "您好地球！"
str3 = "select name from employees where name like \"%eric%\""  # 反斜杠为转义符
str4 = "hello world\nmy love"  # 换行
str5 = """This is a fantastic program to improve your life:
[1] get more money
[2] get a family
[3] make the world peace
please input your option:"""  # 三个"""前后括起大段的文字
str6 = str5 + "here"  # 连接字符串
str7 = "- - " * 10 + "\n" + str5 + str(3)  # 字符串重复次数，将数字转化为字符串
str8 = u"你好\u0020世界"  #unicode 字符串

print(str1[4:7])  # 从第5个字符开始，到第7个字符结束的子串
print(str2[:5])  # 从0开始的5个字符
print(str1[-5])  # 从右边开始的第5个字符，最后一个字符为-1
print(str1[-5:])  # 右边最后5个字符
print(len(str5)) #取长度
print(str7)
print(str8 + ":"+str(len(str8)))  #unicode类型字符串仍按平常理解文字长度计算, 而不是字节数
str8.encode('utf-16') #转换编码方式
print(str8[1] + ":"+str(len(str8)))

