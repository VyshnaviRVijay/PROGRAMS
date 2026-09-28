# write a program to check whether a number is prime or not
# a=int(input("Enter a number:"))
# count=0
# for i in range(1,a+1):
#     if a%i==0:
#         count+=1
# if count==2:
#     print(a,"is a prime number")
# else:
#     print(a,"is not a prime number")

#
# num=int(input("Enter a number:"))
# is_prime=True
# if num==1:
#     is_prime=False
# else:
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
# if is_prime:
#     print("Prime")
# else:
#     print("not prime")


num=int(input("Enter a number:"))
if num==1:
    print("not a prime")
for i in range(2,num):
    if num%i==0:
        print("not a prime")
        break
else:
    print("prime")