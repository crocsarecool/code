# program that does math for the user

user_expression = input("What's the expression ").strip()

x, y, z = user_expression.split()

x = int(x)
z = int(z)

if y == "+": 
    result = x + z
elif y == "-": 
    result = x - z
elif y == "*": 
    result = x * z
elif y == "/": 
    result = x / z
else: 
    print("Invalid operator. Please use +, -, *, or /")
    exit()

print(f"{result:.1f}")



