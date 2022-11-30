# a=int(input('введите первое число'))#номер 1
# b=int(input('введите второе число'))
# if a>b:
#     print(b)
# else:
#     print(a)



# a=int(input('введите первое число'))#номер 2
# b= int(input('введите второе число'))
# c=int(input('введите третье число'))
# if a<b and a<c:
#     print(a)
# elif b<a and b<c:
#     print(b)
# else:
#     print(c)


# a=int(input('введите число'))#номер 3
# if a<0:
#     print(-1)
# elif a>0:
#     print(1)
# else:
#     print(0)


# x1= int(input('введите x1'))#номер 4
# y1= int(input('введите y1'))
# x2= int(input('введите x2'))
# y2= int(input('введите y2'))
# if x1<=8 and x1>0 and x2<=8 and x2>0 and y1<=8 and y1>0 and y2<=8 and y2>0:
#     if (x1+y1)%2==(x2+y2)%2:
#         print("цвет одинаковый")
#     else:
#         print("цвет разный")


# a=int(input('введите первое число'))#номер 5
# b=int(input('введите второе число'))
# c=int(input('введите третье число'))
# if a==b==c:
#     print(3)
# elif a==b or b==c or a==c:
#     print(2)
# else:
#     print(0)


n=int(input('введите длину шоколадки'))#номер 6
m=int(input('введите ширину шоколадки'))
k=int(input('сколько долек должно получиться?'))
if (k%n==0 and k<m*n) or (k%m==0 and k<m*n):
    print("yes")
else:
    print("no")



# x1=int(input("введите x1"))#номер 7
# y1=int(input("введите y1"))
# x2=int(input("введите x2"))
# y2=int(input("введите y2"))
# if x1<=8 and x1>0 and x2<=8 and x2>0 and y1<=8 and y1>0 and y2<=8 and y2>0:
#     if x1==x2 or y1==y2:
#         print("yes")
#     else:
#         print("no")
# else:
#     print("клетка за пределами доски")


# x1=int(input("введите x1"))#номер 8
# y1=int(input("введите y1"))
# x2=int(input("введите x2"))
# y2=int(input("введите y2"))
# if x1<=8 and x1>0 and x2<=8 and x2>0 and y1<=8 and y1>0 and y2<=8 and y2>0:
#     if x1+1==x2 or x1-1==x2 or y1+1==y2 or y1-1==y2:
#         print("yes")
#     else:
#         print("no")
# else:
#     print("клетка за пределами доски")



# x1=int(input("введите x1"))#номер 9
# y1=int(input("введите y1"))
# x2=int(input("введите x2"))
# y2=int(input("введите y2"))
# if x1<=8 and x1>0 and x2<=8 and x2>0 and y1<=8 and y1>0 and y2<=8 and y2>0:
#     if abs(x1-x2)==abs(y1-y2):
#         print('может попасть')
#     else:
#         print('не может попасть')
# else:
#     print("клетка за пределами доски")



# x1=int(input("введите x1"))#номер 10
# y1=int(input("введите y1"))
# x2=int(input("введите x2"))
# y2=int(input("введите y2"))
# if x1<=8 and x1>0 and x2<=8 and x2>0 and y1<=8 and y1>0 and y2<=8 and y2>0:
#     if abs(x1-x2)==abs(y1-y2)or x1==x2 or y1==y2:
#         print('может попасть')
#     else:
#         print('не может попасть')
# else:
#     print("клетка за пределами доски")



# x1=int(input("введите x1"))#номер 11
# y1=int(input("введите y1"))
# x2=int(input("введите x2"))
# y2=int(input("введите y2"))
# if x1<=8 and x1>0 and x2<=8 and x2>0 and y1<=8 and y1>0 and y2<=8 and y2>0:
#     if (x1+2==x2 or x1-2==x2) and (y1+1==y2 or y1-1==y2):
#         print('может попасть')
#     else:
#         print('не может попасть')
# else:
#     print("клетка за пределами доски")