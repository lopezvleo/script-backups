import os
import requests
import json
from credentials import onedrive, onedrive_tenant_id, remove_local_copy
from libs.log import insert_log

# Function will upload the files in the backup directory


def upload_file(directory):
    # Retrieving credentials
    data = onedrive

    # Login in the user
    URL = "https://login.windows.net/" + \
        onedrive_tenant_id + "/oauth2/token?api-version=1.0"

    response = requests.post(url=URL, data=data)
    json_data = json.loads(response.text)

    # Getting the access token
    TOKEN = json_data["access_token"]

    URL = "https://graph.microsoft.com/v1.0/users/" + \
        onedrive['username'] + "/drive/root:/backups"

    headers = {
        'Authorization': "Bearer " + TOKEN
    }
    response = requests.get(URL, headers=headers)
    json_data = json.loads(response.text)

    # insert_log("Uploading file(s) to "+URL)

    for root, dirs, files in os.walk(directory):
        for file_name in files:
            # if(file_name == '.gitignore'):
            #     print(file_name)
            if(file_name != '.gitignore'):
                file_path = os.path.join(root, file_name)
                insert_log("Uploading "+file_name+" to OneDrive...")

                fileHandle = open(file_path, 'rb')
                response = requests.put(URL+"/"+file_name+":/content",
                                        data=fileHandle, headers=headers)
                fileHandle.close()

                # If remove_local_copy enabled, the backups directory will be deleted after upload
                if remove_local_copy and response.status_code == 200 or response.status_code == 201:
                    # remove folder contents
                    insert_log("Succeeded, removing original file...")
                    os.remove(os.path.join(root, file_name))

    insert_log("File succesfully uploaded")
