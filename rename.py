import os
import re


def rename_folders():
    base_dir = os.getcwd()
    dj = os.listdir(base_dir)
    new_dj = None
    exclude_files = ["__pycache__", "backup.txt", "rename.py",
                     "script.py", ".git", ".gitattributes", ".gitignore", "README.md"]
    error_folders = []
    for file_name in exclude_files:
        try:
            dj.remove(file_name)
        except Exception:
            continue

    backup = open("backup.txt", "w")
    for d in dj:
        try:
            new_dj = (d.split(" - "))
            backup.write(d + "\n")
            if len(new_dj) < 3:
                if len(new_dj) == 1:
                    author = new_dj[0].replace("[", '').split("]")
                    folder_name = "["+author[0]+"]"+" " + \
                        author[-1].replace(author[0], '').strip()
                    print(folder_name)
                    os.rename(os.path.join(base_dir, d),
                              os.path.join(base_dir, folder_name))
                    continue
                else:
                    continue
            else:
                author = "[" + new_dj[0].replace("_", " ").title() + "]"
                title = new_dj[1].strip()
                title = title.replace("_s_", "'s_").replace(
                    "'t_", "'t ").replace("_ve_", "'ve ")
                title = title.replace("_", " ")
                title = title.title().replace(
                    "Fakku", '').replace(new_dj[0], '')
                title = title.replace("'S", "'s").replace(
                    "'T", "'t").replace("'Ve", "'ve")
                folder_name = re.sub(' +', ' ', author + " " + title)
                os.rename(os.path.join(base_dir, d),
                          os.path.join(base_dir, folder_name))
                continue
        except FileExistsError:
            error_folders.append("\nCan't rename "+d+" into " +
                                 folder_name + "\n" + folder_name + "already exists")
            continue
    for string in error_folders:
        print(string)
    print("success")


if __name__ == "__main__":
    rename_folders()
