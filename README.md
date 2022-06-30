# Backups for MySQL, PostgreSQL and MongoDB

Script to create backups for MySQL, PostgreSQL, MongoDB and automatically upload the files to OneDrive for Linux.

## Requeriments

    - Python 3.6 or above

## Install the project

    git clone https://github.com/lopezvleo/script-backups

## Create credentials file

Copy the `.example.credentials.py` and paste like `credentials.py`

    cp .example.credentials.py credentials.py

## Set up your credentials of the databases and OneDrive account

## Permissions

Give all the permissions to the folder

    chmod -R 777 script-backups

## Create the cron

Sh to backup the DBs

    0 1 * * * sh /home/user_local/script-backups/scripts/backup.bash

Sh to delete the local copy of the DB every month

    0 0 1 * * sh /home/user_local/script-backups/scripts/delete.bash