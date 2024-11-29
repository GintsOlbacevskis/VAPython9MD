#import nesesery modules
import os
import time

#Recursively traverses a directory and prints its structure is a hierarchical format
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
            elif os.path.isfile(item_path):
                get_file_stats(item_path, level + 1)

    except PermissionError:
        print("   " * level + "|-- [Nav tiesību iegūt info]")

#Retrieve and print stats for a given file
def get_file_stats(file_path, level=0):
    try:
        stats = os.stat(file_path)
        print("   " * (level + 1) + f"   [Izmērs: {stats.st_size} bytes, Modificēts: {time.ctime(stats.st_mtime)}]")
    except Exception as e:
        print("   " * (level + 1) + f"   [Kļūda: {str(e)}]")

#Main
if __name__ == "__main__":
    directory = input("Ievadi direktoriju, kuru parādīt: ")
    print("\nDirektorjas struktūra:")
    traverse_dir(directory)