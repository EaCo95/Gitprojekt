from time import time, ctime

class MyLogger:
    def __init__(self, log_file):
        with open(log_file, "a") as file:
            file.write("log Start")
            ts=time.time()
            timeStamp=(ts)
            file.write("\n")
            file.write(timeStamp)
            file.write("\n")
            

log_file_name = "MobilePhoneBrands.txt"
logger = MyLogger(log_file_name)