# Counts the number of spaces
def main():
    userInput=input("How are you feeling:")
    print("The number of spaces used:",count_spaces(userInput))
def count_spaces(string):
    spaces = 0
    for char in string:
        if char == " " :
            spaces = spaces + 1

    return spaces
main()
