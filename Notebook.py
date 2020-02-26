import time

try:
    notebookfile = open("notebook.txt", "r")
    notebookfile.close()

except IOError:
    print("\nDefault notebook not found, let's create it.")
    notebookfile = open("notebook.txt", "w")
    notebookfile.close()

timestamp = time.strftime("%X %x")

fileName = notebookfile.name

while True:

    print("\nUsing notebook: ", fileName)
    print("\n(1) Read notebook")
    print("(2) Add note")
    print("(3) Empty notebook")
    print("(4) Quit\n")

    action = int(input("What do you want to do?: "))

    if(action == 1):
        notebookfile = open(fileName, "r")
        text = notebookfile.read()
        print("\n", text)
        notebookfile.close()

    elif(action == 2):
        note = input("Write new note: ")
        notebookfile = open(fileName, "a")
        notebookfile.write(note+":::"+timestamp)
        notebookfile.write("\n")
        notebookfile.close()

    elif(action == 3):
        notebookfile = open("notebook.txt", "w")
        notebookfile.close()
        print("\nNotebook emptied.")

    elif(action == 4):
        print("\nQuit.")
        break

    else:
        print("\nUnknown action")
