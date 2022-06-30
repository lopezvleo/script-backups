import os
from datetime import datetime
import pathlib
from libs.log import insert_log
from libs.onedrive import upload_single_file
from credentials import date_format

# Getting the path of the current folder
absolute_path = str(pathlib.Path(__file__).parent.parent.resolve())
date = datetime.today().strftime(date_format)


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
    file_name = db_selected['database'] + "_" + str(date)+".sql"
    path_backup = directory + file_name

    os.system("bash " + absolute_path + "/scripts/mysql.bash " + db_selected['user'] + " '" + db_selected['password'] +
              "' " + db_selected['host'] + " " + db_selected['database'] + " " + path_backup)

    insert_log("Backup successfully created in " + directory)


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
    file_name = db_selected['database'] + "_" + str(date)+".sql"
    path_backup = directory + file_name

    os.system("bash " + absolute_path + "/scripts/postgresql.bash " +
              db_selected['password'] + " " + db_selected['user'] + " " + db_selected['host'] + " " + db_selected['database'] + " " + path_backup)

    insert_log("Backup successfully created in " + directory)


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
    file_name = db_selected['database'] + "_" + str(date)+".gz"
    path_backup = directory + file_name

    os.system("bash " + absolute_path + "/scripts/mongodb.bash " + db_selected['host'] + " " + db_selected['port'] +
              " " + db_selected['database'] + " " + db_selected['user'] + " " + " " + db_selected['password'] + " " + path_backup)

    upload_single_file(directory, file_name)
