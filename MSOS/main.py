import os
import readline  # for readline support

# Function to provide autocomplete suggestions
def complete(text, state):
    options = [i for i in os.listdir('.') if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

# Register autocomplete function with readline
readline.set_completer(complete)
readline.parse_and_bind('tab: complete')

# ASCII art for "MSOS" in big font
ascii_art = """

"""

# Print the ASCII art
print(ascii_art)

# Main loop
while True:
    user_input = input("$ ")
    command, *args = user_input.split()

    if command == "exit":
        break
    elif command == "ls":
        print("\n".join(os.listdir('.')))
    elif command == "mkdir":
        if args:
            os.mkdir(args[0])
        else:
            print("Usage: mkdir [directory_name]")
    elif command == "cd":
        if args:
            try:
                os.chdir(args[0])
            except FileNotFoundError:
                print("Directory not found")
        else:
            print("Usage: cd [directory_name]")
    else:
        print("Command not found")
