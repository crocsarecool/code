# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

def main():
    answer = input("What is the asnwer to the great question of life, the universe and everything?").strip().lower()
    if answer in ["42","forty-two", "forty two"]: print ("Yes")
    else: print("No")

main()
