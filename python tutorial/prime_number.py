#program to find prime number or not
# To take input from the user
# num = int(input("Enter a number: "))
# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#    # check for factors
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            break
#    else:
#         print(num,"is a prime number")
       
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#    print(num,"is not a prime number")


# Program to check prime numbers in a certain interval

def prime_number(num1,num2):

    for num in range(num1, num2):
        if num > 1:
           for i in range(2,num):
             if (num % i) == 0:
              break
           
           else:
            print(num)
       

prime_number(100,150)
