def prime_factor(number):
    prime = []
    while(number != 1):
      for i in range(2,number):
        if(number%i == 0):
         number = number//i
         list=prime.append(i)
         print(list)
         break
        
      
prime_factor(40)     