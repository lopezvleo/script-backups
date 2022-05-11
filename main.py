#!/usr/bin/env bash

"""
* Made by: Leonel López
* Email: lalopez@cultura.gob.sv
* Date: 5/10/2022
* Description: Function to create backups for: MySql, PostgreSQL and MongoDB.
"""

from datetime import datetime
from libs.backup import mysql, postgresql, mongodb
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
            insert_log("MySQL database selected ["+db_selected['database']+"]", True)
            mysql(db_selected)
        
        if db_selected['driver'] == "postgresql":
            insert_log("PostgreSQL database selected ["+db_selected['database']+"]", True)
            postgresql(db_selected)

        if db_selected['driver'] == "mongodb":
            insert_log("MongoDB database selected ["+db_selected['database']+"]", True)
            mongodb(db_selected)


__init__()
