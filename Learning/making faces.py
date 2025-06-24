# converts :-) to 🙂 and :-( to 🙁 and a main function which accepts user input string

def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text

def main():
    user_input = input("Give me an emoji ")
    emoji = convert(user_input)
    print(emoji)
main()