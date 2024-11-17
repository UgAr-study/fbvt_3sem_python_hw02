import argparse
from dll import DoublyLinkedList
from enum import Enum

class Action(str, Enum):
    PUSH="push"
    POP="pop"
    SORT="sort"
    PRINT="print"

def sort_cmd(dll: DoublyLinkedList) -> DoublyLinkedList:
    values = [dll._at(i).data for i in range(len(dll))]
    return DoublyLinkedList(sorted(values))

def print_cmd(dll: DoublyLinkedList):
    values = [dll._at(i).data for i in range(len(dll))]
    print(values)
    return

def main():
    parser = argparse.ArgumentParser(
        description="Doubly linked list CLI - A command line interface to manage a doubly linked list.\n\n"
                    "Available Commands:\n"
                    "  push <values>      Add one or more values to the end of the list.\n"
                    "  pop [count]        Remove one or more values from the beginning of the list. Default is 1.\n"
                    "  sort               Sort the list in ascending order.\n"
                    "  print              Display the current state of the list.\n\n"
                    "Examples:\n"
                    "  dll-cli push 1 2 3 pop 2 sort print\n"
                    "    - Pushes values 1, 2, and 3 into the list, pops 2 values, sorts the list, and prints it.")
    parser.add_argument("commands", nargs="*", help="Commands to execute sequentially (e.g., push 1 2 3 pop 2 sort print)")
    parser.add_argument("--help", help="Commands to execute sequentially (e.g., push 1 2 3 pop 2 sort print)")
    args = parser.parse_args()

    my_dll = DoublyLinkedList[float]()
    commands = args.commands
    i = 0
    # iterate over each cmd
    while i < len(commands):
        command = Action(commands[i].lower())

        if command == Action.PUSH:
            i += 1
            while i < len(commands):
                try:
                    value = float(commands[i])
                    my_dll.push(value)
                    print(f"Pushed {value} to the list.")
                    i += 1
                except ValueError:
                    break
            continue

        elif command == Action.POP:
            i += 1
            try:
                count = int(commands[i])
                i += 1
            except (IndexError, ValueError):
                count = 1
            for _ in range(count):
                try:
                    value = my_dll.pop()
                    print(f"Popped {value} from the list.")
                except ValueError as e:
                    print(e)
            continue

        elif command == Action.SORT:
            my_dll = sort_cmd(my_dll)
            print("List sorted.")

        elif command == Action.PRINT:
            print_cmd(my_dll)

        i += 1
    return

if __name__ == "__main__":
    main()