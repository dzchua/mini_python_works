from pathlib import Path
from os import system
import os, shutil


def option1():
    print("Welcome! Which recipes would you like to have?")
    file_path = Path(Path.home(), "documents", "da", "python-script", "recipes")
    for file in Path(file_path).glob("*"):
        print(file.stem)

    cat = input(f"""\nSelect one of the list: """)
    system("cls")

    recipes_path = Path(Path.home(), "documents", "da", "python-script", "recipes", cat)
    for txt in Path(recipes_path).glob("*.txt"):
        print(txt.stem)

    recipe = input("\nWhich recipe do you want to read from the list above? \n")
    destination = Path(recipes_path, f"{recipe}.txt")
    print(destination.read_text())


# ----------------------------
def option2():
    print("Welcome! Which recipes would you like to add?")
    file_path = Path(Path.home(), "documents", "da", "python-script", "recipes")
    for file in Path(file_path).glob("*"):
        print(file.stem)

    cat2 = input(f"""\nSelect one of the list: """)
    system("cls")

    recipes_path = Path(
        Path.home(), "documents", "da", "python-script", "recipes", cat2
    )
    new_rep = input("Write a name for your new recipe! \n")

    filepath = os.path.join(f"{recipes_path}", f"{new_rep}.txt")
    if not os.path.exists(f"{recipes_path}"):
        os.makedirs(f"{recipes_path}")
    f = open(filepath, "a")
    f.write(input("What do you want to write?\n"))


# -----------------------------
def option3():
    cat3 = input("Create new recipes!\n")

    newpath = Path(Path.home(), "documents", "da", "python-script", "recipes", cat3)
    if not os.path.exists(newpath):
        os.makedirs(newpath)


# ------------------------------
def option4():
    cat4 = input(
        """Select one of the list to delete
    1. Dessert 2. Meat 3. Pasta 4. Salad \n"""
    )

    delete_path = Path(Path.home(), "documents", "da", "python-script", "recipes", cat4)
    for txt in Path(delete_path).glob("*.txt"):
        print(txt.stem)

    delete_recipe = input("\nWhich recipe do you want to delete?\n")
    delete_dest = Path(delete_path, f"{delete_recipe}.txt")

    os.remove(delete_dest)


# -------------------------------
def option5():
    cat_path = Path(Path.home(), "documents", "da", "python-script", "recipes")

    system("cls")
    for txt in Path(cat_path).glob("*"):
        print(txt.stem)

    del_cat = input("\nWhich category do you want to delete?\n")
    selected_dir = Path(f"{cat_path}", f"{del_cat}")
    shutil.rmtree(selected_dir)


# -------------------------------
system("cls")
recipes_path = Path(Path.home(), "documents", "da", "python-script", "recipes")
onlyfiles = os.listdir(recipes_path)

choice = int(
    input(
        f"""
Welcome! The directory to recipes is {recipes_path}
There are currently {len(onlyfiles)} recipes.
Type: 
(1) To read recipes 
(2) To create new recipe 
(3) For new category 
(4) To delete recipes 
(5) To delete category
"""
    )
)

options = [option1, option2, option3, option4, option5]
output = options[choice - 1]()
