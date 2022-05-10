"""
* Made by: Leonel López
* Email: lalopez@cultura.gob.sv
* Date: 5/10/2022
* Description: Function to create backups for: MySql, PostgreSQL and MongoDB.
"""

from datetime import datetime
from libs.backup import mysql
from libs.log import insert_log
from credentials import credentials


def __init__():
    insert_log("Starting the backup script", True)
    # Creating the backup file
    create_backup()


def create_backup():
    for db in credentials:
        db_selected = credentials[db]

        if db_selected['driver'] == "mysql":
            insert_log("MySql Database selected ["+db_selected['database']+"]")
            mysql(db_selected)


__init__()
