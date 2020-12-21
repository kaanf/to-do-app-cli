user_input = "random"
data = list()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# 1. Add an item
# 2. Mark as done
# 3. View items
# 4. Exit

def show():
    print(bcolors.HEADER + "Menu:" + bcolors.ENDC)
    print("1. Add an item")
    print("2. Mark as done")
    print("3. View items")
    print("4. Exit")


while user_input != "4":
    show()
    user_input = input("Enter your choice: ")

    if user_input == "1":
        item = input("\nWhat is to be done? ")
        data.append(item)
        print(bcolors.OKGREEN + "Item added succesfully. (", item, ")\n" + bcolors.ENDC)
    elif user_input == "2":
        item = input("\nWhat is to be marked as done? ")
        if item.capitalize() in data:
            data.remove(item.capitalize())
            print(bcolors.OKCYAN + "Removed item: ", item, "\n" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "\nItem does not exist in the to-do list." + bcolors.ENDC)
    elif user_input == "3":
        print("\nList of to-do items: ")
        count = 1
        for items in data:
            print(bcolors.OKBLUE + str(count) + ". " + items + bcolors.ENDC)
            count += 1
        print("\n")
    elif user_input == "4":
        print(bcolors.FAIL + "Goodbye.\n" + bcolors.ENDC)
