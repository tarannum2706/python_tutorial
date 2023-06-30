
# program to write the tables
def tables(table,n):
     multiply=1
     for i in range(1,table+1):
          for j in range(1,n+1):
               multiply = i*j
               print(multiply)
          print()         

tables(5,10) 

num= int(input("Enter the number to display the table of : "))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)