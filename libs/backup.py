import os

from libs.log import insert_log

"""
* Made by: Leonel López
* Email: lalopez@cultura.gob.sv
* Date: 5/10/2022
* Description: Scripts to create the backups of the databases.
"""

from datetime import datetime
import pathlib
from libs.onedrive import upload_file

# Getting the path of the current folder
absolute_path = pathlib.Path(__file__).parent.parent.resolve()
date = datetime.today().strftime('%d_%m_%Y')


def mysql(db_selected):
    """
    Arguments to be passed: 

    1st - Username
    2nd - Password
    3rd - Host
    4th - Database
    5th - Path of the backup
    """

    insert_log("Creating backup...")
    directory = str(absolute_path) + "/backups/"
    path_backup = directory + \
        db_selected['database'] + "_" + str(date)+".sql"

    os.system("./scripts/mysql.bash " + db_selected['user'] + " '" + db_selected['password'] +
              "' " + db_selected['host'] + " " + db_selected['database'] + " " + path_backup)

    insert_log("Backup successfully created in " + directory)
    upload_file(directory)
