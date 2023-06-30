# Program to check a number is odd and even
def check_number(num):
    if num%2==0:
        print("Number is even")
    else:
        print("Number is odd")

check_number(36)   

# Program to find the largest number
def largest_number(a,b,c):
  if a>=b and a>=c:
    print("Largest number is: ",a)
  elif b>=a and b>=c:
    print("Largest number is: ",b)
  else:
    print("Largest number is: ",c)
    
largest_number(30,60,70) 

#program to find the sum of natural number
def natural_num(n):
    sum=0
    if n<0:
        print("enter the positive number")
    else:
     for i in range(1,n+1):
        sum=sum+i

     print(sum)
     
natural_num(16)        
