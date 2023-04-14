### 1

#r=float(input('Enter the radius of circle'))
#area=3.14*r**2
#print(area)

### 2

#name=input("Enter the name:")
#roll_no=int(input("Enter the roll number:"))
#mark=int(input("Enter the mark:"))
#print("Name:",name)
#print("Roll number:",roll_no)
#print("Mark",mark)

###3

#l=[12,3,47,10]
#print(l)
#print("Largest number is ",max(l))

### 4

#num = list(range(10))
#previous_num = 0
#for i in num:
 #   sum = previous_num + i
  #  print('Current Number '+ str(i) + ' Previous Number ' + str(previous_num) + ' is ' + str(sum))
   # previous_num=i

###5

#list=[10,20,33,46,55]
#for i in list:
 #     if i % 5 == 0:
  #         print(i)

### 6

#num=int(input("Enter the number:"))
#if num > 1: 
 #  for i in range(2,num):
  #     if (num % i) == 0:
   #        print(num,"is not a prime number")
    #       break
   #else:
    #   print(num,"is a prime number")
#else:
 #  print(num,"is not a prime number")

### 7

#num=(10,40,33,70)
#print(str(num[::-1]))

### 8

#num1=34
#num2=12
#num3=7

#if(num1>=num2) and (num1>=num3):
#  max  = num1
#elif (num2>=num1) and (num2>=num3):
#  max = num2
#else:
#  max=num3
#print("The maximum is:",max)

###9

#n=int(input("Enter the number of rows:"))
#for i in range(0,n):
 #   for j in range(0,i+1):
  #      print("*",end="")
   # print()


### 10

#n=int(input("Enter the number of rows:"))
#for i in range(0,n):
 #   for j in range(0,i+1):
  #     print("*",end="")
   # print()
#for i in range(n,0,-1):
 #       for j in range(i):
  #          print("*",end="")
   #     print()
    