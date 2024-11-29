#import nesesery module
import os

def traverse_dir(path, level=0):
    try:
        #List of all items in the "directory"
        items = os.listdir(path)
        for item in items:
            item_path = os.path.join(path, item)

            #Print item with indentation based on this level
            print("   " * level + f"|-- {item}")

            #If item is a "directory", traverse it recursively
            if os.path.isdir(item_path):
                traverse_dir(item_path, level + 1)
    except PermissionError:
        print("   " * level + "|-- [Nav tiesību]")

#Main
if __name__ == "__main__":
    directory = input("Ievadi direktoriju, kuru parādīt: ")
    print("\nDirektorjas struktūra:")
    traverse_dir(directory)