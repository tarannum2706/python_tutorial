
# Program to check the string is palindrome or not
def palindrome(n):
    my_str = n.lower()
    reverse = str(n)[::-1].lower()
    if my_str == reverse:
        print("Palindrome")
    else:
        print("Not palindrome")

palindrome("Racecar") 


# find the factor of a number
def factor(num):
    print("The factors are:")
    for i in range(1,num+1):
        if num%i == 0:
            print(i)

factor(20)    
