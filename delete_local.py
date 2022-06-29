from datetime import datetime
import pathlib
import os
from libs.log import insert_log

absolute_path = str(pathlib.Path(__file__).parent.parent.resolve())
directory = os.path.join(str(absolute_path), "backups-local")
directory_log = os.path.join(str(absolute_path), "logs")


def __init__():
    delete_local()


# Function will delete all the local copies of the DBs
def delete_local():
    os.remove(os.path.join(directory_log, "logs_backup.log"))
    insert_log("Deleting backups", True)
    insert_log("Deleting log file")

    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if(file_name != '.gitignore'):
                insert_log(
                    "Deleting DB file: {}/{}".format(directory, file_name))
                os.remove(os.path.join(directory, file_name))
                insert_log(f"DB backup {file_name} deleted successfully.")

    insert_log("Backups succesfully deleted")


__init__()
