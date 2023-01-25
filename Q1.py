str = input()
lenth = len(str)
l = len(str)-1
Remove_last = str[:l - 2]
Remove_last = Remove_last+str[lenth-1]
print(Remove_last[::-1])
num1, num2 = int(input()), int(input())
print('sum of num1 and num2 =')
print(num1+num2)
print('sub of num1 and num2 =')
print(num1-num2)
print('mul of num1 and num2 =')
print(num1*num2)
print('div of num1 and num2 =')
print(num1/num2)
