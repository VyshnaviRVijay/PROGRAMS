##LIST PROGRAMS
from token import NUMBER

#PRINT ALL ELEMENTS IN A LIST
numbers=[10,20,30,40,50]
for i in numbers:
    print(i)

#FIND THE SUM OF LIST ELEMENTS
sum=0
numbers=[10,20,30,40]
for i in numbers:
    sum=sum+i
print(sum)

#FIND THE LARGEST ELEMENT
numbers=[10,20,30,40]
largest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
print(largest)

#COUNT EVEN NUMBERS
numbers=[1,2,3,4,5,6,7]
count=0
for i in numbers:
    if (i%2==0):
        count=count+1
print(count)

#PRINT LIST IN REVERSE
numbers=[10,20,30,40]
# ##print(numbers[::-1])
reversed=[]
for i in numbers:
    reversed=[i]+reversed
print(reversed)  ##printing reversed list
for i in reversed:
    print(i)     ##printing elements in reversed list




###TUPLE PROGRAMS

#PRINT TUPLE ELEMENTS
fruits=("Apple","Banana","Orange")
for fruit in fruits:
    print(fruit)

##COUNT TOTAL ELEMENTS
count=0
t=(10,20,30,40,50)
for num in t:
    count+=1
print(count)

##FIND MAXIMUM ELEMENT
t=(12,45,23,67,34)
large=t[1]
for num in t:
    if num>large:
        large=num
print(large,"is the largest element")

#another method
# large=t[0]
# for i in range(1,len(t)):
#     if t[i]>large
#         large=t[i]
# print(large,"is the largest element")

##SUM OF TUPLE ELEMENTS
t=(5,10,15,20)
sum=0
for num in t:
    sum+=num
print(sum)


##SEARCH AN ELEMENT
t=(10,20,30,40)
x=30
for i in t:
    if i==x:
        print("element is present")
        break
else:
    print("element is not present")


##PASS= placeholder used when no codes to be executed.
B=["ORANGE",'APPLE',"GRAPES"]
for i,j in enumerate(B):
    print(i,j)
##enumerate() = function will return both the index and corresponding values


#HOMEWORK PROGRAMS

1. ADD DIGITS OF A NUMBER
num=12345
sum=0
while num>0:
     digit=num%10
     sum=sum+digit
     num=num//10
print(sum)

2. REVERSE A NUMBER
num=int(input("Enter a number: "))
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
print(rev)

# 3. FACTORIAL OF A NUMBER
fact=1
n=int(input("Enter a number:"))
for i in range(1,n+1):
    fact=fact*i
print(fact)


#5.CHECK WHETHER THE NUMBER IS PRIME OR NOT
num=int(input("Enter a number: "))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print(num,"is a prime number")

else:
    print(num,"is not a prime number")


#04/09/2026


student={"name":"Ali","age":22,"course":"Python"}
#1.PRINT ALL KEYS
# print(student.keys())

for key in student:
    print(key)
#2.PRINT ALL VALUES
# print(student.values())

for key in student:
    print(student[key])
#3.PRINT ALL KEY VALUE PAIRS
for key in student:
    print(key,":",student[key])


4.SUM OF DICT VALUES
marks={"Math":80,"Science":75,"English":90}
# mark=marks.values()
# print(sum(mark))
total=0
for key in marks:
    total=total+marks[key]
print("Total marks:",total)

#5.COUNT DICT ITEMS

student={"name":"Ali","age":22,"course":"Python"}
count=0
for key in student:
    count+=1
print(count)

#6.FIND HIGHEST VALUE
marks={"Math":80,"Science":95,"English":88}
highest=0
for key in marks:
    if marks[key]>highest:
        highest=marks[key]
print(highest,"is highest")

