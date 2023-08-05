import os
from git.repo.base import Repo

directory_to_project = dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\root"
def create():
    if not os.path.exists(dir_path):
        Repo.clone_from("https://github.com/SriBalaji2112/voiceprint_recognition", dir_path)
    else:
        print("hii")