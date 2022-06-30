"""
* Made by: Leonel López
* Email: lalopez@cultura.gob.sv
* Date: 5/10/2022
* Description: Credentials of all the databases to be backed up.
"""

# Databases to be backed up
credentials = {
    "mysql_db": {
        "database": "database_name",
        "host": "127.0.0.1",
        "driver": "mysql",
        "user": "user",
        "password": "password"
    },
    "postgres_db": {
        "database": "postgres_db",
        "host": "127.0.0.1",
        "port": "5432",
        "driver": "postgresql",
        "user": "user",
        "password": "password"
    },
    "mongo_db": {
        "database": "mongo_db",
        "host": "127.0.0.1",
        "port": "27017",
        "driver": "mongodb",
        "user": "user",
        "password": "password"
    },
}

# OneDrive credentials
onedrive = {
    'resource': "https://graph.microsoft.com",
    'client_id': 'client_id',
    'client_secret': 'client_secret',
    'grant_type': 'password',
    'username': 'email',
    'password': 'email_password',
}

# ID of the institution
onedrive_tenant_id = 'tenant_id'

# If remove_local_copy enabled, the backups directory will be deleted after upload
remove_local_copy = True

# File date format to be generated, for ex: db_name_30_06.sql
date_format = '%d_%m'
