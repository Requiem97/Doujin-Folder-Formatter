import os
import rename

#pylint: disable=unused-variable


def remove_json(path):
    for parent, sub, filenames in os.walk(path):
        for fn in filenames:
            if fn == "contentV2.json":
                os.remove(os.path.join(parent, fn))
    print("success")


def rename_thumb(path):
    for parent, sub, filenames in os.walk(path):
        for fn in filenames:
            if fn.lower() == "thumb.jpg" or fn.lower() == "thumb.png":
                os.rename(os.path.join(parent, fn),
                          os.path.join(parent, "folder.jpg"))
    print("success")


def del_duplicate_thumb(path):
    for parent, sub, filenames in os.walk(path):
        for fn in filenames:
            if fn == "thumb.jpg" or fn == "thumb.png":
                os.remove(os.path.join(parent, fn))
    print("success")


if __name__ == "__main__":
    print("Deleting contentV2.json")
    remove_json(os.getcwd())
    print("Renaming thumb images to folder.jpg")
    rename_thumb(os.getcwd())
    print("Deleting duplicate thumb file")
    del_duplicate_thumb(os.getcwd())
    print("Reformatting folder names")
    rename.rename_folders()
