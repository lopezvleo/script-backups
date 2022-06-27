from datetime import datetime
import pathlib
import webbrowser
import os
import requests
import json
from credentials import onedrive, onedrive_tenant_id, remove_local_copy
from libs.log import insert_log
import msal

date = datetime.today().strftime('%d_%m_%Y')
RESOURCE_URL = 'https://graph.microsoft.com/'
API_VERSION = 'v1.0'
onedrive_destination = '{}/{}/me/drive/root:/backups/{}'.format(
    RESOURCE_URL, API_VERSION, date)
absolute_path = str(pathlib.Path(__file__).parent.parent.resolve())


# Function will upload the files in the backup directory
def upload_file(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if(file_name != '.gitignore'):
                upload_single_file(root, file_name)

    insert_log("Files succesfully uploaded")


def upload_single_file(directory, file_name):

    TOKEN = authenticate()

    file_path = os.path.join(directory, file_name)
    file_size = os.stat(file_path).st_size
    file_data = open(file_path, 'rb')

    headers = {
        'Authorization': 'Bearer ' + TOKEN,
    }

    if file_size < 4100000:
        # Perform is simple upload to the API

        response = requests.put(onedrive_destination+"/"+file_name +
                                ":/content", data=file_data, headers=headers)
    else:
        # Creating an upload session
        upload_session = requests.post(
            onedrive_destination+"/"+file_name+":/createUploadSession", headers=headers).json()

        with open(file_path, 'rb') as f:
            total_file_size = os.path.getsize(file_path)
            chunk_size = 327680
            chunk_number = total_file_size//chunk_size
            chunk_leftover = total_file_size - chunk_size * chunk_number
            i = 0

            while True:
                chunk_data = f.read(chunk_size)
                start_index = i*chunk_size
                end_index = start_index + chunk_size

                # If end of file, break
                if not chunk_data:
                    break
                if i == chunk_number:
                    end_index = start_index + chunk_leftover

                # Setting the header with the appropriate chunk data location in the file
                headers = {
                    'Authorization': 'Bearer ' + TOKEN,
                    'Content-Length': '{}'.format(chunk_size),
                    'Content-Range': 'bytes {}-{}/{}'.format(
                        start_index, end_index-1, total_file_size)
                }

                # Upload one chunk at a time
                response = requests.put(
                    upload_session['uploadUrl'], data=chunk_data, headers=headers)

                print(response)
                print(response.json())

                i = i + 1

            file_data.close()

        file_data.close()

    backup_local = os.path.join(absolute_path, "backups-local")

    # If remove_local_copy enabled, the backups directory will be deleted after upload
    if remove_local_copy and response.status_code == 200 or response.status_code == 201:
        # remove folder contents
        insert_log("Succeeded, not removing original file...")
        # os.remove(os.path.join(directory, file_name))
    else:
        insert_log("Succeeded, moving original file...")
        # if file exists replace else move
        if os.path.exists(os.path.join(backup_local, file_name)):
            os.replace(os.path.join(directory, file_name),
                       os.path.join(backup_local, file_name))
            print("Replacing file")
        else:
            os.rename(os.path.join(directory, file_name),
                      os.path.join(backup_local, file_name))
            print("Moving file")


def authenticate():
    # Retrieving credentials
    data = onedrive

    # Login in the user
    URL = "https://login.windows.net/" + \
        onedrive_tenant_id + "/oauth2/token?api-version=1.0"

    response = requests.post(url=URL, data=data)
    json_data = json.loads(response.text)

    # Getting the access token
    TOKEN = json_data["access_token"]

    return TOKEN
