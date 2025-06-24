# first I'm giving it a default emotional state

emoticon = ":-("

# Then I am going to define 2 new functions to show how I update the emoticon

# this is the Say function. It takes the phrase adds a space followed by the emoji
def say(phrase):
    print(phrase + " " + emoticon)

# this is the main function, which updates the emotional state
def main():
    global emoticon

    say("Is anyone there")
    emoticon = ":-)"
    say ("oh Hi") 
# So it's saying that is anyone there with the old emoticon then it's asserting there's a new emoticon.
# Then it's using the say function which uses the new global emoticon.

main()


