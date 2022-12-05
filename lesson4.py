# a = int(input())
# b = int(input())
# for i in range(a, b+1):
#     print(i)

# a = int(input())
# b = int(input())
# if a<b:
#     for i in range(a,b+1):
#         print(i)
# else:
#     for i in range(a,b-1,-1):
#         print(i)


# a=int(input())
# b=int(input())
# for i in range (a-1+ a%2,b,-2):
#     print(i)


# a=[0,1,2,3,4,5,6,7,8,9]
# sum=0
# for i in a:
#     sum+=i
# print(sum)


# a=[1,1,1,1,1,1,1,1,1,1]
# sum=0
# for i in a:
#     sum+=i
# print(sum)




# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum += i**3
# print(sum)


# n=int(input())
# nfaktor=1
# for i in range(2,n+1):
#     nfaktor=nfaktor*i
# print(f"n!={nfaktor}")


# age= int(input("сколько васе лет?"))
# sum=0
# for i in range(1,age+1):
#     sum+=i*10
# print(f"вася получил {sum} рублей")


# bank1=int(input("введите первый счет"))
# bank2=0.01
# days=int(input("сколько дней у вас есть"))
# for i in range(1,days+1):
#     bank2=bank2*2
# if bank1>bank2:
#     print("первое предложение выгоднее")
# else:
#     print("второе предложение выгоднее")


amount=int(input("сколько чисел хотите ввести"))
nulls=0
for i in range(1,amount+1):
    number=int(input("введите число"))
    if number==0:
        nulls+=1
print(f"среди этих чисел {nulls} нулей")