class Logger:
    def log(self, message):
        print("Log:", message)

class FileLogger(Logger):
    def log(self, message):
        super().log(message)
        print("Writing log to file:", message)

logger = FileLogger()
logger.log("System started")