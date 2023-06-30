# Program to convert celsius to fehrenhiet
def convert_fehrenhiet(celsius):
    f = (celsius*9/5)+32
    print("Convert to celsius to fehrenhiet: ",f,"fehrenhiet")

convert_fehrenhiet(30)   

# Program to convert fehrenhiet to celsius
def convert_celsius(fehrenhiet):
    c = (fehrenhiet-32)*(5/9)
    print("Convert to fehrenhiet to celsius: ",c,"celsius")

convert_celsius(86)   