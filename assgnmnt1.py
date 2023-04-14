#1

#test_str = "python is a interpreted language"
 
#all_freq={}
#for i in test_str:
 #   if i in all_freq:
 #       all_freq[i]+=1
  #     all_freq[i]=1

#print(str(all_freq))

#2

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

#3

#x=int(input("Enter the base value:"))
#y=int(input("Enter the exponent value:"))

#def power(x,y):
 #   if y == 0:
  #      return 1
   # return (x*power(x,y-1))
#print(power(x,y))

#4

#n=int(input("Enter the positive integer:"))
#s=0

#for i in range(1,n):
#    s=s+pow(i,3)
#print(s)

#5

#list=[1,2,3,4,5,6,7,8,9,10]
#for i in list:
#      if (i % 2 == 0 and i % 5 == 0):
#           print("FizzBuzz")
#            continue
#      elif i % 2 == 0:
#          print("Fizz")
#          continue      
#      elif i % 5 ==0:
#           print("Buzz")
#           continue
      
 #     else:
#      print(i)

#6

#list = [22,33,24,22,55,22,65,22,30,22,47,22]
#print("Given List:\n",list)
#freq = max(set(list),key=list.count)
#print("Element with highest frequency:\n",freq)

#7

#n=[2,1,3,1]
#sum_list=0

#for i in n:
 #   sum_list +=i*i;
#print(sum_list)

#8

#n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#for i in n:
 #   if (i % 2 == 0) :
  #      print(i,"is even")
   # else:
    #    print(i,"is odd")

#9

#degree =float(input("Enter the value to be converted:"))
#Fahrenheit=degree*(9/5)+32
#Celsius =(5/9)*(Fahrenheit-32)

#print("Temperature in Fahrenheit is:",Fahrenheit)
#print("Temperature in Celsius is:",Celsius)
           
#10

#def factorial(n):
    
#    return 1 if (n==1 or n==0) else n* factorial(n-1)
#num=int(input("Enter the value:"))
#print("Factorial of ",num,"is" ,factorial(num))
