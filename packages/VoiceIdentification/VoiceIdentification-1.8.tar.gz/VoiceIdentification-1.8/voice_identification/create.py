import os
from git.repo.base import Repo
import requests

directory_to_project = dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\VI"
def create():
    if not os.path.exists(dir_path):

        def download_file_from_google_drive(id, destination):
            URL = "https://docs.google.com/uc?export=download"

            session = requests.Session()

            response = session.get(URL, params={'id': id}, stream=True)
            token = get_confirm_token(response)

            if token:
                params = {'id': id, 'confirm': token}
                response = session.get(URL, params=params, stream=True)

            save_response_content(response, destination)

        def get_confirm_token(response):
            for key, value in response.cookies.items():
                if key.startswith('download_warning'):
                    return value

            return None

        def save_response_content(response, destination):
            CHUNK_SIZE = 32768

            with open(destination, "wb") as f:
                for chunk in response.iter_content(CHUNK_SIZE):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
        print("VI Module has Downloading")
        Repo.clone_from("https://github.com/SriBalaji2112/pypi_voice_identification_downloader", dir_path)
        file_id = '1LH2wmN5E_qTQrxzdVvGgBK9W_XBSJzV4'
        destination = dir_path + '\\model\\saved_model\\variables\\variables.data-00000-of-00001'
        download_file_from_google_drive(file_id, destination)
        print("Download Finished please Remove create() function")

    else:
        print("VI was already downloaded")
        print("Please Remove create() function")

create()