from datetime import datetime
import pathlib

absolute_path = pathlib.Path(__file__).parent.parent.resolve()


def insert_log(log_string="", header=False):
    # print(str(absolute_path)+"/logs/logs_backup.log")
    log_file = open(str(absolute_path)+"/logs/logs_backup.log", 'a')

    # if it's the first string to be inserted, will create the header in the file
    if(header):
        now = datetime.now()
        log = "\n"+str(now) + " - " + log_string + "\n"
        print(log)
        log_file.write(log)
        return

    log = log_string + "\n"
    print(log)
    log_file.write(log)
