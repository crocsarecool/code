#implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

def three():
    user_input = input("Say Something")
    newinput = user_input.replace(" ", "...")
    print(newinput)
three()


