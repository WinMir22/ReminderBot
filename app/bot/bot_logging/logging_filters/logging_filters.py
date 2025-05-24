import logging


class LoggingErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR


class LoggingWarningFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.WARNING
