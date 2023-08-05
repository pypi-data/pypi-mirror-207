import os
from git.repo.base import Repo

directory_to_project = dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\VI"
def create():
    if not os.path.exists(dir_path):
        print("VI Module has Downloading")
        Repo.clone_from("https://github.com/SriBalaji2112/pypi_voice_identification_downloader", dir_path)
        print("Download Finished please Remove create() function")
    else:
        print("VI was already downloaded")
        print("Please Remove create() function")