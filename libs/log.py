"""
* Made by: Leonel López
* Email: lalopez@cultura.gob.sv
* Date: 5/10/2022
* Description: Function to create backups for: MySql, PostgreSQL and MongoDB.
"""

from datetime import datetime


def insert_log(log_string="", header=False):
    log_file = open('logs/logs_backup.log', 'a')

    # if it's the first string to be inserted, will create the header in the file
    if(header):
        now = datetime.now()
        log_file.write("\n"+str(now) + " - " + log_string + "\n")
        return

    log_file.write(log_string + "\n")
