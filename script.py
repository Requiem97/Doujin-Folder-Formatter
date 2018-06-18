import os
import rename

#pylint: disable=unused-variable
def remove_json(path):
    for parent, sub, filenames in os.walk(path):
        for fn in filenames:
            if fn == "contentV2.json":
                os.remove(os.path.join(parent, fn))

def rename_thumb(path):
    for parent, sub, filenames in os.walk(path):
        for fn in filenames:
            if fn.lower() == "thumb.jpg" or fn.lower() == "thumb.png":
                os.rename(os.path.join(parent, fn), os.path.join(parent, "folder.jpg"))

def del_duplicate_thumb(path):
    for parent, sub, filenames in os.walk(path):
        for fn in filenames:
            if fn == "thumb.jpg" or fn == "thumb.png":
                os.remove(os.path.join(parent, fn))

if __name__ == "__main__":
    while True:
        inp = input("Choose 0 to delete .json, 1 to rename thumb.jpg, 2 delete duplicate thumb, 3 to rename folder, or 4 to exit: ")
        if inp == '0':
            remove_json(os.getcwd())
        elif inp == '1':
            rename_thumb(os.getcwd())
            print("success")
        elif inp == '2':
            del_duplicate_thumb(os.getcwd())
        elif inp == '3':
            rename.rename_folders()
        elif inp == '4':
            break
        else:
            print("invalid input")