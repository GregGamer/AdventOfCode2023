import os

def create_folder(foldername):
    root_folder = os.getcwd()
    path = os.path.join(root_folder, foldername)
    os.mkdir(path)