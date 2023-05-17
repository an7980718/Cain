zheng=int(input("请输入一个四位整数："))
four=zheng%10
three=zheng%100//10
two=zheng%1000//100
one=zheng//1000
he=four+three+two+one
print("各位相加和等于：" + str(he))