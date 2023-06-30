# Python program to check if the number is an Armstrong number or not

# take input from the user
# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#    digit = temp % 10
#    print(digit)
#    sum += digit ** 3
#    print(sum)
#    temp //= 10
#    print(temp)

# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")



# Program to check Armstrong numbers in a certain interval

lower = 100
upper = 3000

for num in range(lower, upper + 1):
   order = len(str(num))
    
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
       
   if num == sum:
       print(num)