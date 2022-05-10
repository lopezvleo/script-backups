"""
* Made by: Leonel López
* Email: lalopez@cultura.gob.sv
* Date: 5/10/2022
* Description: Credentials of all the databases to be backed up.
"""

# Databases to be backed up
credentials = {
    "database_name": {
        "database": "database_name",
        "host": "127.0.0.1",
        "driver": "mysql",
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
remove_local_copy = False
