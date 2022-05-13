"""
* Made by: Leonel López
* Email: lalopez@cultura.gob.sv
* Date: 5/10/2022
* Description: Scripts to create the backups of the databases.
"""

import os
from datetime import datetime
import pathlib
from libs.onedrive import upload_file
from libs.log import insert_log

# Getting the path of the current folder
absolute_path = str(pathlib.Path(__file__).parent.parent.resolve())
date = datetime.today().strftime('%d_%m_%Y')


def mysql(db_selected):
    """
    Arguments to be passed: 

    - Username
    - Password
    - Host
    - Database
    - Path of the backup
    """

    insert_log("Creating backup...")
    directory = str(absolute_path) + "/backups/"
    path_backup = directory + \
        db_selected['database'] + "_" + str(date)+".sql"

    os.system("bash " + absolute_path + "/scripts/mysql.bash " + db_selected['user'] + " '" + db_selected['password'] +
              "' " + db_selected['host'] + " " + db_selected['database'] + " " + path_backup)

    insert_log("Backup successfully created in " + directory)
    upload_file(directory)


def postgresql(db_selected):
    """
    Arguments to be passed: 

    - Password
    - Username
    - Host
    - Database
    - Path of the backup
    """

    insert_log("Creating backup...")
    directory = str(absolute_path) + "/backups/"
    path_backup = directory + \
        db_selected['database'] + "_" + str(date)+".psql"

    os.system("bash " + absolute_path + "/scripts/postgresql.bash " + db_selected['password'] + " " + db_selected['user'] + " " + db_selected['host'] + " " + db_selected['database'] + " " + path_backup)

    insert_log("Backup successfully created in " + directory)
    upload_file(directory)


def mongodb(db_selected):
    """
    Arguments to be passed: 

    - Host
    - Port
    - Database
    - Username
    - Password
    - Path of the backup
    """

    insert_log("Creating backup...")
    directory = str(absolute_path) + "/backups/"
    path_backup = directory + \
        db_selected['database'] + "_" + str(date)+".gz"

    os.system("bash " + absolute_path + "/scripts/mongodb.bash " + db_selected['host'] + " " + db_selected['port'] + " " + db_selected['database'] + " " + db_selected['user'] + " " + " " + db_selected['password'] + " " + path_backup)

    insert_log("Backup successfully created in " + directory)
    upload_file(directory)
