import json
import os
def create_folder(folder, recreate = True):
    path=folder
    try:
        os.mkdir(path)
    except FileExistsError:
        if recreate == True:
            print("Folder " + folder + " already exists, Directory recreated")
            os.system("rm -rf "+folder)
            os.mkdir(path)
    return path

def execute(command):
    os.system(command)


def readJson(jsonFile):
    with open(jsonFile) as f:
        load=json.load(f)
    return load