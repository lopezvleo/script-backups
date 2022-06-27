from datetime import datetime
import os
import pathlib
from libs.backup import mysql, postgresql, mongodb
from libs.log import insert_log
from credentials import credentials
from libs.onedrive import upload_file

absolute_path = str(pathlib.Path(__file__).parent.parent.resolve())
directory = os.path.join(str(absolute_path), "backups")


def __init__():
    insert_log("Starting the backup script", True)
    # Creating the backup file
    create_backup()
    # print(directory)
    upload_file(directory)


def create_backup():
    for db in credentials:
        db_selected = credentials[db]

        if db_selected['driver'] == "mysql":
            insert_log(
                "MySQL database selected ["+db_selected['database']+"]", True)
            mysql(db_selected)

        if db_selected['driver'] == "postgresql":
            insert_log(
                "PostgreSQL database selected ["+db_selected['database']+"]", True)
            postgresql(db_selected)

        if db_selected['driver'] == "mongodb":
            insert_log(
                "MongoDB database selected ["+db_selected['database']+"]", True)
            mongodb(db_selected)


__init__()
