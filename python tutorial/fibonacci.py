#fibonacci series with recursion
def fib(n):
   if(n <= 2):
      return(1)
   else:
      return(fib(n-1) + fib(n-2))
n = 9
for i in range(1,n+1): 
    print(fib(i))

#fibonacci series with iteration
# def fib(num):
#   first = 0
#   second = 1
#   nextterm = ""
#   count = 1
#   while (count <= num+1):
#       if (count <= 1):
#         nextterm = count
#       else:
#         print(nextterm)
#         nextterm = first + second
#         first = second
#         second = nextterm     
#         count += 1
# print(fib(5))



