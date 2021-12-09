import time, os, sys
# Our aim is to improve the display of text on the screen by adding a typing effect/delay.
# To do so we will need to import two libraries: time and sys. 
# We will then create two new functions called typingPrint() and typingInput() as follows:

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value

def clearScreen():
    os.system("clear")